#!/usr/bin/env python3
"""从公开 GitHub 源仓库聚合 skill 包到本市场的 plugins/ 目录。

每个源仓库保持为该主题的事实源,本仓库只做聚合与分发:
  - single 布局: 仓库根 SKILL.md 即一个 skill
  - pack 布局:   每个含 SKILL.md 的一级子目录是一个 skill
skill 目录名取 SKILL.md frontmatter 的 name(加载器要求目录名 == name)。
每次同步把 源仓库/commit/路径 写入 sources.lock.json,保证可追溯、可复现。

用法: python3 tools/sync_sources.py [--offline]   (--offline 不 fetch,用已缓存源)
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / '.cache' / 'sources'
EXCLUDE = {'.git', '.github', '.gitignore', 'README.md', 'README_en.md', 'install.sh', 'BUILD_MANIFEST.json', '.DS_Store'}

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


def fetch(repo: str, offline: bool) -> Path:
    dest = CACHE / repo.split('/')[-1]
    if dest.exists():
        if not offline:
            subprocess.run(['git', '-C', str(dest), 'pull', '-q', '--ff-only'], check=False)
    else:
        if offline:
            sys.exit(f'缓存缺失且 --offline: {repo}')
        CACHE.mkdir(parents=True, exist_ok=True)
        subprocess.run(['git', 'clone', '-q', '--depth', '1', f'https://github.com/{repo}.git', str(dest)], check=True)
    return dest


def head(repo_dir: Path) -> str:
    return subprocess.run(['git', '-C', str(repo_dir), 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()


def skill_name(skill_md: Path) -> str:
    fm = yaml.safe_load(skill_md.read_text(encoding='utf-8').split('---')[1])
    name = str(fm.get('name', '')).strip()
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name):
        sys.exit(f'非法 skill name {name!r}: {skill_md}')
    return name


def copy_skill(src_dir: Path, dst_dir: Path) -> None:
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    dst_dir.mkdir(parents=True)
    for item in src_dir.iterdir():
        if item.name in EXCLUDE:
            continue
        if item.is_dir():
            shutil.copytree(item, dst_dir / item.name, ignore=shutil.ignore_patterns('__pycache__', '.DS_Store'))
        else:
            shutil.copy2(item, dst_dir / item.name)


def main() -> int:
    offline = '--offline' in sys.argv
    lock: dict = {}
    total = 0
    for plugin, sources in SOURCES.items():
        skills_root = ROOT / 'plugins' / plugin / 'skills'
        if skills_root.exists():
            shutil.rmtree(skills_root)
        skills_root.mkdir(parents=True)
        lock[plugin] = {}
        for repo, layout in sources:
            repo_dir = fetch(repo, offline)
            sha = head(repo_dir)
            if layout == 'single':
                candidates = [repo_dir]
            else:
                candidates = sorted(d for d in repo_dir.iterdir() if d.is_dir() and (d / 'SKILL.md').exists())
            for cand in candidates:
                name = skill_name(cand / 'SKILL.md')
                if layout == 'pack' and cand.name != name:
                    print(f'  [note] {repo}/{cand.name}: 目录名与 name 不一致,按 name={name} 落盘')
                copy_skill(cand, skills_root / name)
                lock[plugin][name] = {
                    'repo': f'https://github.com/{repo}',
                    'commit': sha,
                    'path': '.' if cand == repo_dir else cand.name,
                }
                total += 1
        print(f'{plugin}: {len(lock[plugin])} 个 skill')
    (ROOT / 'sources.lock.json').write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'同步完成: {len(SOURCES)} 插件 / {total} skill,来源记录于 sources.lock.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
