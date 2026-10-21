#!/usr/bin/env python3
"""市场仓库校验器(本地与 CI 共用)。

  1. .claude-plugin/marketplace.json 可解析,插件名唯一,source 目录存在
  2. 每个插件 .zcode-plugin/plugin.json: name == 目录名,version 为语义化版本且与目录项一致,skills 目录非空
  3. 每个 skills/<d>/SKILL.md: frontmatter name == d;description 非空、≤1024(>500 警告)
  4. skill 名跨插件不重复(警告)
  5. Markdown 相对链接可解析
用法: python3 tools/validate_marketplace.py    退出码 0=通过 1=失败
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SEMVER = re.compile(r'^\d+\.\d+\.\d+$')
LINK_RE = re.compile(r'\[[^\]]*\]\(([^)\s]+)\)')
FAILS: list[str] = []
WARNS: list[str] = []


def main() -> int:
    catalog_path = ROOT / '.claude-plugin' / 'marketplace.json'
    try:
        catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
    except Exception as exc:  # noqa: BLE001
        print(f'FAIL  [catalog] 无法解析 {catalog_path}: {exc}')
        return 1
    entries = catalog.get('plugins') or []
    names = [e.get('name') for e in entries]
    if len(names) != len(set(names)):
        FAILS.append('[catalog] 插件名重复')
    all_skills: dict[str, str] = {}
    skill_total = 0
    for e in entries:
        name = e.get('name', '?')
        src = (ROOT / str(e.get('source', ''))).resolve()
        if not src.is_dir():
            FAILS.append(f'[catalog] {name}: source 目录不存在 {e.get("source")}')
            continue
        if src.name != name:
            FAILS.append(f'[plugin] {name}: 目录名 {src.name} 与插件名不一致')
        mpath = src / '.zcode-plugin' / 'plugin.json'
        if not mpath.exists():
            FAILS.append(f'[plugin] {name}: 缺少 .zcode-plugin/plugin.json')
            continue
        m = json.loads(mpath.read_text(encoding='utf-8'))
        if m.get('name') != name:
            FAILS.append(f'[plugin] {name}: 清单 name={m.get("name")!r} 不一致')
        if not SEMVER.match(str(m.get('version', ''))):
            FAILS.append(f'[plugin] {name}: version 非语义化版本 {m.get("version")!r}')
        if m.get('version') != e.get('version'):
            FAILS.append(f'[plugin] {name}: 清单 version {m.get("version")} 与目录项 {e.get("version")} 不一致')
        skills_dir = src / str(m.get('skills', 'skills'))
        skill_dirs = sorted(d for d in skills_dir.iterdir() if d.is_dir()) if skills_dir.is_dir() else []
        if not skill_dirs:
            FAILS.append(f'[plugin] {name}: skills 目录为空或不存在')
        for d in skill_dirs:
            sm = d / 'SKILL.md'
            if not sm.exists():
                FAILS.append(f'[skill] {name}/{d.name}: 缺少 SKILL.md')
                continue
            fm = yaml.safe_load(sm.read_text(encoding='utf-8').split('---')[1]) or {}
            if fm.get('name') != d.name:
                FAILS.append(f'[skill] {name}/{d.name}: name={fm.get("name")!r} 与目录名不一致')
            desc = fm.get('description')
            if not isinstance(desc, str) or not desc.strip():
                FAILS.append(f'[skill] {name}/{d.name}: description 为空')
            elif len(desc) > 1024:
                FAILS.append(f'[skill] {name}/{d.name}: description {len(desc)} 字符超过 1024')
            elif len(desc) > 500:
                WARNS.append(f'[skill] {name}/{d.name}: description {len(desc)} 字符(>500)')
            if d.name in all_skills:
                WARNS.append(f'[skill] {d.name} 同时出现在 {all_skills[d.name]} 与 {name}')
            all_skills[d.name] = name
            skill_total += 1
    for md in ROOT.glob('plugins/**/*.md'):
        text = md.read_text(encoding='utf-8')
        for target in LINK_RE.findall(text):
            if target.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            path = target.split('#')[0]
            if path and not (md.parent / path).resolve().exists():
                FAILS.append(f'[broken-link] {md.relative_to(ROOT)}: {target}')
    print(f'plugins: {len(entries)} | skills: {skill_total}')
    for w in WARNS:
        print(f'WARN  {w}')
    for f in FAILS:
        print(f'FAIL  {f}')
    print(f'结果: {"通过" if not FAILS else "未通过"}(fail={len(FAILS)}, warn={len(WARNS)})')
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
