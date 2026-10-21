#!/usr/bin/env python3
"""由单一元数据源生成插件清单、插件级 LICENSE 与市场目录。

产出: plugins/<p>/.zcode-plugin/plugin.json、plugins/<p>/LICENSE、.claude-plugin/marketplace.json。
改版本号/描述/关键词只改这里的 PLUGINS,然后重跑;市场目录项与插件清单保持一致。
用法: python3 tools/build_manifests.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKET_NAME = 'ai-era-software-engineering-skills'
MARKET_VERSION = '1.2.0'
REPO_URL = 'https://github.com/Fen9pi-Max/ai-era-software-engineering-skills'
OWNER = {'name': 'Fen9pi-Max', 'url': 'https://github.com/Fen9pi-Max'}
APACHE_SRC = ROOT / 'plugins' / 'agent-engineering' / 'skills' / 'ai-agent-infra' / 'LICENSE'

MIT_TEXT = '''MIT License

Copyright (c) 2026 Fen9pi-Max

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

PLUGINS = [
    {
        'name': 'testing-methodology', 'version': '1.2.0', 'license': 'MIT', 'category': 'developer-tools',
        'displayName': 'Testing Methodology', 'displayName_zh': '测试方法论',
        'keywords': ['testing', 'exploratory-testing', 'test-design', 'test-automation', 'mutation-testing', '测试', '探索式测试', '自动化测试'],
        'description': 'Testing methodology skills distilled from six classics: Explore It!, Beautiful Testing, Effective Software Testing, How Google Tests Software, MFQ&PPDCS test analysis and design, and automation testing best practices.',
        'description_zh': '六本测试经典蒸馏的测试方法论 skill:探索式测试(Explore It!)、Beautiful Testing、Effective Software Testing、Google 软件测试之道、MFQ&PPDCS 测试分析设计、自动化测试最佳实践。',
    },
    {
        'name': 'legacy-code-craft', 'version': '1.1.0', 'license': 'MIT', 'category': 'developer-tools',
        'displayName': 'Legacy Code Craft', 'displayName_zh': '遗留代码与代码质量',
        'keywords': ['legacy-code', 'refactoring', 'tdd', 'technical-debt', 'ai-coding', '遗留代码', '重构', '技术债'],
        'description': 'Ten capability cards distilled from the nine practices of Beyond Legacy Code, adapted for AI-agent programming (agents write, humans review): small batches, TDD rhythm, refactoring safety nets, technical debt.',
        'description_zh': '《修改软件的艺术》9 条最佳实践蒸馏的 10 张能力卡,已做 AI agent 编程适配(agent 写码、人审码):小批次、TDD 节奏、重构安全网、技术债偿还。',
    },
    {
        'name': 'agent-engineering', 'version': '1.1.0', 'license': 'Apache-2.0', 'category': 'developer-tools',
        'displayName': 'Agent Engineering', 'displayName_zh': 'Agent 工程',
        'keywords': ['ai-agent', 'agent-infra', 'llm', 'context-engineering', 'observability', 'agent 工程', '智能体'],
        'description': '22 atomic capabilities for enterprise AI agent engineering, distilled from an Alibaba Cloud AI Agent handbook.',
        'description_zh': '企业级 AI agent 工程的 22 项原子能力(阿里云 AI Agent 手册蒸馏)。',
    },
    {
        'name': 'engineering-management', 'version': '1.2.0', 'license': 'MIT', 'category': 'productivity',
        'displayName': 'Engineering Management', 'displayName_zh': '工程管理',
        'keywords': ['engineering-management', 'project-management', 'team-leadership', 'cybernetics', '工程管理', '项目管理', '团队管理'],
        'description': 'Engineering management skills: cybernetic project management (Qian Xuesen), managing small teams of under ten (Google high-performance practices), and the P9 Work Method (technical depth, architecture and leadership).',
        'description_zh': '工程管理三书蒸馏:钱学森《工程控制论》控制论项目管理、《如何管理10人以下小团队》谷歌高绩效团队法、《P9 工作法》技术硬实力/架构力/领导力。',
    },
    {
        'name': 'security-testing', 'version': '1.1.0', 'license': 'MIT', 'category': 'developer-tools',
        'displayName': 'Security Testing', 'displayName_zh': '安全测试',
        'keywords': ['penetration-testing', 'security', 'authorized-testing', '渗透测试', '安全测试'],
        'description': 'Authorized penetration-testing methodology in five phases, covering web and system targets.',
        'description_zh': '授权渗透测试五阶段方法论(Web 与系统目标)。',
    },
    {
        'name': 'product-thinking', 'version': '1.1.0', 'license': 'MIT', 'category': 'productivity',
        'displayName': 'Product Thinking', 'displayName_zh': '产品思维',
        'keywords': ['product-management', 'user-value', 'product-strategy', 'ai-product', '产品方法论', '用户价值', 'AI 产品'],
        'description': '18 capability cards from Yu Jun\'s Product Methodology, adapted for AI-era productization: AI feature value, hallucination liability, token-cost pricing, AI trust.',
        'description_zh': '《俞军产品方法论》18 张能力卡,已做 AI 产品化适配:AI 功能价值评估、幻觉致损判责、token 成本定价、AI 信任机制。',
    },
]


def write_license(plugin_dir: Path, license_id: str) -> None:
    if license_id == 'Apache-2.0':
        text = APACHE_SRC.read_text(encoding='utf-8')
    else:
        text = MIT_TEXT
    (plugin_dir / 'LICENSE').write_text(text, encoding='utf-8')


def main() -> int:
    entries = []
    for p in PLUGINS:
        plugin_dir = ROOT / 'plugins' / p['name']
        manifest = {
            'name': p['name'],
            'version': p['version'],
            'description': p['description_zh'],
            'author': OWNER,
            'license': p['license'],
            'homepage': REPO_URL,
            'repository': REPO_URL,
            'keywords': p['keywords'],
            'skills': 'skills',
        }
        (plugin_dir / '.zcode-plugin').mkdir(parents=True, exist_ok=True)
        (plugin_dir / '.zcode-plugin' / 'plugin.json').write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        write_license(plugin_dir, p['license'])
        entries.append({
            'name': p['name'],
            'source': f"./plugins/{p['name']}",
            'version': p['version'],
            'description': p['description'],
            'description_i18n': {'en': p['description'], 'zh-CN': p['description_zh']},
            'displayName': p['displayName'],
            'displayName_i18n': {'en': p['displayName'], 'zh-CN': p['displayName_zh']},
            'category': p['category'],
            'keywords': p['keywords'],
        })
    catalog = {
        'name': MARKET_NAME,
        'version': MARKET_VERSION,
        'description': 'Software-engineering skills for the AI-agent era: testing, legacy code, agent engineering, engineering management, security testing and product thinking, distilled from classic books via cangjie-skill.',
        'description_i18n': {
            'en': 'Software-engineering skills for the AI-agent era: testing, legacy code, agent engineering, engineering management, security testing and product thinking, distilled from classic books via cangjie-skill.',
            'zh-CN': 'AI 时代的软件工程 skill 合集:测试、遗留代码、Agent 工程、工程管理、安全测试与产品思维,均由经典书籍经 cangjie-skill 蒸馏而来。',
        },
        'owner': OWNER,
        'plugins': entries,
    }
    (ROOT / '.claude-plugin').mkdir(exist_ok=True)
    (ROOT / '.claude-plugin' / 'marketplace.json').write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'生成 {len(PLUGINS)} 份 plugin.json + LICENSE + .claude-plugin/marketplace.json(市场 v{MARKET_VERSION})')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
