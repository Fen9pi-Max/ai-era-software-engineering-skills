#!/usr/bin/env python3
"""从公开 GitHub 源仓库聚合 skill 包到本市场的 plugins/ 目录(可复现、可校验)。

三种模式:
  默认          按 sources.lock.json 钉住的 commit 检出各源仓库并落盘(可复现构建)
  --update      抓取各源仓库最新默认分支,推进锁文件里的 commit(有意升级时用)
  --check       只校验:按锁文件在临时目录重新落盘,与 plugins/ 逐字节比对,有漂移则退出码 1(CI 用)

布局: single = 仓库根 SKILL.md 即一个 skill;pack = 每个含 SKILL.md 的一级子目录是一个 skill。
skill 目录名取 SKILL.md frontmatter 的 name(加载器要求目录名 == name)。
随安装进入用户机器的只保留运行所需内容:蒸馏过程产物(distillation/、candidates/、测试记录等)不分发;
pack 布局会把源仓库根的 LICENSE 复制进每个 skill 目录,保证许可随 skill 走。
"""
import filecmp
import json
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Optional
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / '.cache' / 'sources'
LOCK = ROOT / 'sources.lock.json'
EXCLUDE_NAMES = {
    '.git', '.github', '.gitignore', 'README.md', 'README_en.md', 'install.sh',
    'BUILD_MANIFEST.json', '.DS_Store',
    'distillation', 'candidates', 'rejected', 'test-prompts.json', 'test-results.md', 'DIGEST.md',
}
FM_RE = re.compile(r'\A---\s*\n(.*?)\n---\s*\n', re.S)

# 插件 -> [(GitHub 仓库, 布局)]
SOURCES: dict[str, list[tuple[str, str]]] = {
    'testing-methodology': [
        ('Fen9pi-Max/beautiful-testing-skill', 'pack'),
        ('Fen9pi-Max/exploratory-testing-skill', 'pack'),
        ('Fen9pi-Max/effective-software-testing-skill', 'single'),
        ('Fen9pi-Max/pirate-testing-mfqppdcs-skill', 'pack'),
        ('Fen9pi-Max/automation-testing-best-practices-skill', 'pack'),
        ('Fen9pi-Max/how-google-tests-software-skill', 'single'),
    ],
    'legacy-code-craft': [('Fen9pi-Max/beyond-legacy-code-skill', 'single')],
    'agent-engineering': [('Fen9pi-Max/ai-agent-infra', 'single')],
    'engineering-management': [
        ('Fen9pi-Max/cybernetic-project-management', 'single'),
        ('Fen9pi-Max/small-team-management-skill', 'single'),
        ('Fen9pi-Max/p9-work-methods-skill', 'single'),
    ],
    'security-testing': [('Fen9pi-Max/pentest-skill', 'single')],
    'product-thinking': [('Fen9pi-Max/yujun-product-methodology-skill', 'single')],
}


def git(repo_dir: Path, *args: str) -> str:
    r = subprocess.run(['git', '-C', str(repo_dir), *args], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f'git {" ".join(args)} 失败({repo_dir.name}): {r.stderr.strip()}')
    return r.stdout.strip()


def load_lock() -> dict:
    return json.loads(LOCK.read_text(encoding='utf-8')) if LOCK.exists() else {}


def pinned_commits(lock: dict) -> dict[str, str]:
    """repo -> 锁文件记录的 commit(同一仓库的所有 skill 共享一个 commit)。"""
    pins: dict[str, str] = {}
    for skills in lock.values():
        for info in skills.values():
            repo = info['repo'].replace('https://github.com/', '')
            pins.setdefault(repo, info['commit'])
    return pins


def checkout(repo: str, pin: Optional[str], update: bool) -> tuple[Path, str]:
    dest = CACHE / repo.split('/')[-1]
    url = f'https://github.com/{repo}.git'
    if not dest.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(['git', 'clone', '-q', url, str(dest)], capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f'clone 失败 {repo}: {r.stderr.strip()}')
    if update or pin is None:
        git(dest, 'fetch', '-q', 'origin')
        default = git(dest, 'symbolic-ref', 'refs/remotes/origin/HEAD').rsplit('/', 1)[-1]
        git(dest, 'checkout', '-q', '--detach', f'origin/{default}')
    else:
        if subprocess.run(['git', '-C', str(dest), 'cat-file', '-e', f'{pin}^{{commit}}'],
                          capture_output=True).returncode != 0:
            git(dest, 'fetch', '-q', 'origin')
        git(dest, 'checkout', '-q', '--detach', pin)
    return dest, git(dest, 'rev-parse', 'HEAD')


def skill_name(skill_md: Path) -> str:
    m = FM_RE.match(skill_md.read_text(encoding='utf-8'))
    if not m:
        sys.exit(f'缺少 frontmatter: {skill_md}')
    name = str((yaml.safe_load(m.group(1)) or {}).get('name', '')).strip()
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name):
        sys.exit(f'非法 skill name {name!r}: {skill_md}')
    return name


def copy_skill(src_dir: Path, dst_dir: Path, repo_license: Optional[Path]) -> None:
    dst_dir.mkdir(parents=True)
    for item in src_dir.iterdir():
        if item.name in EXCLUDE_NAMES:
            continue
        if item.is_dir():
            shutil.copytree(item, dst_dir / item.name,
                            ignore=shutil.ignore_patterns('__pycache__', '.DS_Store', *EXCLUDE_NAMES))
        else:
            shutil.copy2(item, dst_dir / item.name)
    if repo_license and not (dst_dir / 'LICENSE').exists():
        shutil.copy2(repo_license, dst_dir / 'LICENSE')


def materialize(target_plugins: Path, lock: dict, update: bool) -> dict:
    pins = pinned_commits(lock)
    new_lock: dict = {}
    for plugin, sources in SOURCES.items():
        skills_root = target_plugins / plugin / 'skills'
        if skills_root.exists():
            shutil.rmtree(skills_root)
        skills_root.mkdir(parents=True)
        new_lock[plugin] = {}
        for repo, layout in sources:
            repo_dir, sha = checkout(repo, pins.get(repo), update)
            repo_license = repo_dir / 'LICENSE' if (repo_dir / 'LICENSE').exists() else None
            cands = [repo_dir] if layout == 'single' else sorted(
                d for d in repo_dir.iterdir() if d.is_dir() and (d / 'SKILL.md').exists())
            for cand in cands:
                name = skill_name(cand / 'SKILL.md')
                copy_skill(cand, skills_root / name, repo_license if layout == 'pack' else None)
                new_lock[plugin][name] = {
                    'repo': f'https://github.com/{repo}',
                    'commit': sha,
                    'path': '.' if cand == repo_dir else cand.name,
                }
    return new_lock


def _collect_drift(cmp: filecmp.dircmp, prefix: str) -> list[str]:
    out = [f'{prefix}/{n} 仅在仓库中' for n in cmp.left_only]
    out += [f'{prefix}/{n} 仅在源重建中' for n in cmp.right_only]
    out += [f'{prefix}/{n} 内容不同' for n in cmp.diff_files]
    for sub, subcmp in cmp.subdirs.items():
        out += _collect_drift(subcmp, f'{prefix}/{sub}')
    return out


def main() -> int:
    update, check = '--update' in sys.argv, '--check' in sys.argv
    lock = load_lock()
    if check:
        if not lock:
            sys.exit('--check 需要已有 sources.lock.json')
        with tempfile.TemporaryDirectory() as tmp:
            tmp_plugins = Path(tmp) / 'plugins'
            fresh_lock = materialize(tmp_plugins, lock, update=False)
            drift: list[str] = []
            for plugin in SOURCES:
                a, b = ROOT / 'plugins' / plugin / 'skills', tmp_plugins / plugin / 'skills'
                drift += _collect_drift(filecmp.dircmp(a, b), f'{plugin}/skills')
            if fresh_lock != lock:
                drift.append('sources.lock.json 与按锁重建的记录不一致')
            if drift:
                print('漂移:')
                for d in drift[:30]:
                    print('  ', d)
                print(f'结果: 未通过({len(drift)} 处漂移)')
                return 1
            print(f'结果: 通过(plugins/ 与锁文件一致,{sum(len(v) for v in lock.values())} skill)')
            return 0
    new_lock = materialize(ROOT / 'plugins', lock, update)
    LOCK.write_text(json.dumps(new_lock, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    total = sum(len(v) for v in new_lock.values())
    for plugin, skills in new_lock.items():
        print(f'{plugin}: {len(skills)} 个 skill')
    print(f"同步完成({'已推进锁定 commit' if update else '按锁定 commit'}): {len(SOURCES)} 插件 / {total} skill")
    return 0


if __name__ == '__main__':
    sys.exit(main())
