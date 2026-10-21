#!/usr/bin/env python3
"""由 sources.lock.json 与市场目录生成 README.md(插件/skill 清单与来源追溯)。

用法: python3 tools/build_readme.py   (先运行 sync_sources.py 与 build_manifests.py)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    lock = json.loads((ROOT / 'sources.lock.json').read_text(encoding='utf-8'))
    catalog = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    meta = {e['name']: e for e in catalog['plugins']}
    total = sum(len(v) for v in lock.values())
    lines = [
        '# AI 时代的软件工程 Skill 合集',
        '',
        f'一个 ZCode 插件市场:**{len(lock)} 个插件 / {total} 个 skill**,覆盖 agent 写码之后人类仍要守住的几道关——测什么、怎么改旧代码、怎么搭 agent、怎么管团队、怎么验安全、怎么判断产品。',
        '全部内容由经典书籍经 [cangjie-skill](https://github.com/kangarooking/cangjie-skill)(RIA-TV++)蒸馏而来,各来源仓库是事实源,本仓库负责聚合与分发。',
        '',
        '## 安装(ZCode)',
        '',
        '1. **Plugin Marketplace → Add → Add Plugin Marketplace**,粘贴 `Fen9pi-Max/ai-era-software-engineering-skills`(或本地克隆目录)并添加;',
        '2. 在 **Personal → ai-era-software-engineering-skills** 下按需 **Install** 插件(建议只装用得上的主题,避免技能列表膨胀);',
        '3. 新任务里从输入框的 skill 选择器选用,或直接描述场景由 agent 按触发条件调用。已安装插件在 **Settings → Plugins** 管理。',
        '',
        '市场目录为 `.claude-plugin/marketplace.json`,插件清单为各插件的 `.zcode-plugin/plugin.json`。',
        '',
        '## 插件与 skill',
        '',
    ]
    for plugin, skills in lock.items():
        m = meta[plugin]
        lines += [
            f"### {m['displayName_i18n']['zh-CN']} `{plugin}` v{m['version']} — {len(skills)} 个 skill",
            '', m['description_i18n']['zh-CN'], '',
            '| skill | 来源仓库 | commit |', '| --- | --- | --- |',
        ]
        for sk, src in skills.items():
            repo_short = src['repo'].replace('https://github.com/', '')
            lines.append(f"| `{sk}` | [{repo_short}]({src['repo']}) | `{src['commit']}` |")
        lines.append('')
    lines += [
        '## 更新与复现',
        '',
        '```bash',
        'python3 tools/sync_sources.py        # 从各源仓库拉取并重新落盘 plugins/,刷新 sources.lock.json',
        'python3 tools/build_manifests.py     # 由单一元数据生成插件清单与市场目录(改版本/描述只改这里)',
        'python3 tools/build_readme.py        # 重新生成本 README',
        'python3 tools/validate_marketplace.py   # 命名/版本/描述/链接校验(CI 同步执行)',
        '```',
        '',
        '`sources.lock.json` 记录每个 skill 的源仓库与 commit,任何一张卡都可以追溯到它的蒸馏来源。',
        '',
        '## 内容定性与许可',
        '',
        '各 skill 为对原书方法论的摘要蒸馏与结构化重述,**不含原书文本**;原书版权归作者与出版社所有。',
        '本仓库自身文件采用 MIT;各插件沿用其来源仓库的许可(`agent-engineering` 为 Apache-2.0,随 skill 保留原 LICENSE;其余为 MIT)。',
        '',
        '相邻合集:[国密标准 Skill 合集](https://github.com/Fen9pi-Max/gmt-crypto-standards-skill)(95 个 GM/T·GM/Y 标准 skill,领域合规,独立维护)。',
    ]
    (ROOT / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'README: {len(lock)} 插件 / {total} skill')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
