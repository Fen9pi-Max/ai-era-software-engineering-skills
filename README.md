# AI 时代的软件工程 Skill 合集

一个 ZCode 插件市场:**6 个插件 / 34 个 skill**,覆盖 agent 写码之后人类仍要守住的几道关——测什么、怎么改旧代码、怎么搭 agent、怎么管团队、怎么验安全、怎么判断产品。
全部内容由经典书籍经 [cangjie-skill](https://github.com/kangarooking/cangjie-skill)(RIA-TV++)蒸馏而来,各来源仓库是事实源,本仓库负责聚合与分发。

## 安装(ZCode)

1. **Plugin Marketplace → Add → Add Plugin Marketplace**,粘贴 `Fen9pi-Max/ai-era-software-engineering-skills`(或本地克隆目录)并添加;
2. 在 **Personal → ai-era-software-engineering-skills** 下按需 **Install** 插件(建议只装用得上的主题,避免技能列表膨胀);
3. 新任务里从输入框的 skill 选择器选用,或直接描述场景由 agent 按触发条件调用。已安装插件在 **Settings → Plugins** 管理。

市场目录为 `.claude-plugin/marketplace.json`,插件清单为各插件的 `.zcode-plugin/plugin.json`。

## 插件与 skill

### 测试方法论 `testing-methodology` — 29 个 skill

五本测试经典蒸馏的测试方法论 skill:探索式测试(Explore It!)、Beautiful Testing、Effective Software Testing、MFQ&PPDCS 测试分析设计、自动化测试最佳实践。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `beautiful-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62` |
| `fuzzing-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62` |
| `mutation-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62` |
| `performance-testing-collaboration` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62` |
| `slime-efficient-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62` |
| `stakeholder-test-metrics` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62` |
| `test-case-effectiveness` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62` |
| `charter-session-design` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `deep-observation-testability` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `entity-crud-exploration` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `exploratory-testing` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `intermittent-bug-hunting` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `oracle-strategies` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `state-model-exploration` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `test-heuristics-cheatsheet` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b12` |
| `effective-software-testing` | [Fen9pi-Max/effective-software-testing-skill](https://github.com/Fen9pi-Max/effective-software-testing-skill) | `0b78ead` |
| `kym-cidtestd` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e` |
| `mfq-analysis-views` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e` |
| `modeling-workflow` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e` |
| `pirate-testing-mfqppdcs` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e` |
| `ppdcs-model-selection` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e` |
| `tco-coverage-outline` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e` |
| `test-design-4steps` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e` |
| `automation-decision-checklist` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a62` |
| `automation-testing-best-practices` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a62` |
| `pilot-project-methodology` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a62` |
| `results-verification-defense` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a62` |
| `roi-evaluation` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a62` |
| `testware-architecture` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a62` |

### 遗留代码与代码质量 `legacy-code-craft` — 1 个 skill

《修改软件的艺术》9 条实践,已做 AI agent 编程适配(agent 写码、人审码):小批次、TDD 节奏、重构安全网、技术债偿还。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `beyond-legacy-code` | [Fen9pi-Max/beyond-legacy-code-skill](https://github.com/Fen9pi-Max/beyond-legacy-code-skill) | `dd86dd4` |

### Agent 工程 `agent-engineering` — 1 个 skill

企业级 AI agent 工程的 22 项原子能力(阿里云 AI Agent 手册蒸馏)。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `ai-agent-infra` | [Fen9pi-Max/ai-agent-infra](https://github.com/Fen9pi-Max/ai-agent-infra) | `d147b32` |

### 工程管理 `engineering-management` — 1 个 skill

钱学森《工程控制论》蒸馏出的 13 项控制论项目管理能力。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `cybernetic-project-management` | [Fen9pi-Max/cybernetic-project-management](https://github.com/Fen9pi-Max/cybernetic-project-management) | `f7a14b9` |

### 安全测试 `security-testing` — 1 个 skill

授权渗透测试五阶段方法论(Web 与系统目标)。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `pentest-practice` | [Fen9pi-Max/pentest-skill](https://github.com/Fen9pi-Max/pentest-skill) | `91a9f26` |

### 产品思维 `product-thinking` — 1 个 skill

《俞军产品方法论》18 张能力卡,已做 AI 产品化适配:AI 功能价值评估、幻觉致损判责、token 成本定价、AI 信任机制。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `yujun-product-methodology` | [Fen9pi-Max/yujun-product-methodology-skill](https://github.com/Fen9pi-Max/yujun-product-methodology-skill) | `b25936c` |

## 更新与复现

```bash
python3 tools/sync_sources.py      # 从各源仓库拉取并重新落盘 plugins/,刷新 sources.lock.json
python3 tools/build_manifests.py   # 由 tools/ 内单一元数据重新生成插件清单与市场目录
python3 tools/validate_marketplace.py   # 命名/版本/描述/链接校验(CI 同步执行)
```

`sources.lock.json` 记录每个 skill 的源仓库与 commit,任何一张卡都可以追溯到它的蒸馏来源。

## 内容定性与许可

各 skill 为对原书方法论的摘要蒸馏与结构化重述,**不含原书文本**;原书版权归作者与出版社所有。
本仓库自身文件采用 MIT;各插件沿用其来源仓库的许可(`agent-engineering` 为 Apache-2.0,随 skill 保留原 LICENSE;其余为 MIT)。

相邻合集:[国密标准 Skill 合集](https://github.com/Fen9pi-Max/gmt-crypto-standards-skill)(95 个 GM/T·GM/Y 标准 skill,领域合规,独立维护)。
