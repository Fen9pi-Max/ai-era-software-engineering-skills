# AI 时代的软件工程 Skill 合集

一个 ZCode 插件市场:**6 个插件 / 37 个 skill**,覆盖 agent 写码之后人类仍要守住的几道关——测什么、怎么改旧代码、怎么搭 agent、怎么管团队、怎么验安全、怎么判断产品。
全部内容由经典书籍经 [cangjie-skill](https://github.com/kangarooking/cangjie-skill)(RIA-TV++)蒸馏而来,各来源仓库是事实源,本仓库负责聚合与分发。

## 安装(ZCode)

1. **Plugin Marketplace → Add → Add Plugin Marketplace**,粘贴仓库地址 `https://github.com/Fen9pi-Max/ai-era-software-engineering-skills`(或先克隆到本地,粘贴克隆目录)并添加;
2. 在 **Personal → ai-era-software-engineering-skills** 下按需 **Install** 插件(建议只装用得上的主题,避免技能列表膨胀);
3. 新任务里从输入框的 skill 选择器选用,或直接描述场景由 agent 按触发条件调用。已安装插件在 **Settings → Plugins** 管理。

市场目录为 `.claude-plugin/marketplace.json`,插件清单为各插件的 `.zcode-plugin/plugin.json`。

## 插件与 skill

### 测试方法论 `testing-methodology` v1.2.0 — 30 个 skill

六本测试经典蒸馏的测试方法论 skill:探索式测试(Explore It!)、Beautiful Testing、Effective Software Testing、Google 软件测试之道、MFQ&PPDCS 测试分析设计、自动化测试最佳实践。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `beautiful-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62ffcf909f4de7271f13794c89dc1f60245` |
| `fuzzing-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62ffcf909f4de7271f13794c89dc1f60245` |
| `mutation-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62ffcf909f4de7271f13794c89dc1f60245` |
| `performance-testing-collaboration` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62ffcf909f4de7271f13794c89dc1f60245` |
| `slime-efficient-testing` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62ffcf909f4de7271f13794c89dc1f60245` |
| `stakeholder-test-metrics` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62ffcf909f4de7271f13794c89dc1f60245` |
| `test-case-effectiveness` | [Fen9pi-Max/beautiful-testing-skill](https://github.com/Fen9pi-Max/beautiful-testing-skill) | `276bc62ffcf909f4de7271f13794c89dc1f60245` |
| `charter-session-design` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `deep-observation-testability` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `entity-crud-exploration` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `exploratory-testing` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `intermittent-bug-hunting` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `oracle-strategies` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `state-model-exploration` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `test-heuristics-cheatsheet` | [Fen9pi-Max/exploratory-testing-skill](https://github.com/Fen9pi-Max/exploratory-testing-skill) | `dc08b120fa168e57f90c7907e4b752d98123a288` |
| `effective-software-testing` | [Fen9pi-Max/effective-software-testing-skill](https://github.com/Fen9pi-Max/effective-software-testing-skill) | `fe4e8a5a23ac50bf5a3225267d9b92e825b7bc79` |
| `kym-cidtestd` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e4996c3e966ee255476820c9ccf90ccc2c` |
| `mfq-analysis-views` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e4996c3e966ee255476820c9ccf90ccc2c` |
| `modeling-workflow` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e4996c3e966ee255476820c9ccf90ccc2c` |
| `pirate-testing-mfqppdcs` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e4996c3e966ee255476820c9ccf90ccc2c` |
| `ppdcs-model-selection` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e4996c3e966ee255476820c9ccf90ccc2c` |
| `tco-coverage-outline` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e4996c3e966ee255476820c9ccf90ccc2c` |
| `test-design-4steps` | [Fen9pi-Max/pirate-testing-mfqppdcs-skill](https://github.com/Fen9pi-Max/pirate-testing-mfqppdcs-skill) | `ea0af3e4996c3e966ee255476820c9ccf90ccc2c` |
| `automation-decision-checklist` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a629783bd461e8a6cf07e5fcc6dc59864377` |
| `automation-testing-best-practices` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a629783bd461e8a6cf07e5fcc6dc59864377` |
| `pilot-project-methodology` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a629783bd461e8a6cf07e5fcc6dc59864377` |
| `results-verification-defense` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a629783bd461e8a6cf07e5fcc6dc59864377` |
| `roi-evaluation` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a629783bd461e8a6cf07e5fcc6dc59864377` |
| `testware-architecture` | [Fen9pi-Max/automation-testing-best-practices-skill](https://github.com/Fen9pi-Max/automation-testing-best-practices-skill) | `4a74a629783bd461e8a6cf07e5fcc6dc59864377` |
| `how-google-tests-software` | [Fen9pi-Max/how-google-tests-software-skill](https://github.com/Fen9pi-Max/how-google-tests-software-skill) | `b80dbd100b9af48389ed87261935d5a795fad17e` |

### 遗留代码与代码质量 `legacy-code-craft` v1.1.0 — 1 个 skill

《修改软件的艺术》9 条最佳实践蒸馏的 10 张能力卡,已做 AI agent 编程适配(agent 写码、人审码):小批次、TDD 节奏、重构安全网、技术债偿还。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `beyond-legacy-code` | [Fen9pi-Max/beyond-legacy-code-skill](https://github.com/Fen9pi-Max/beyond-legacy-code-skill) | `dd86dd4cb27e55af29f5a303b1b099ae294fa702` |

### Agent 工程 `agent-engineering` v1.1.0 — 1 个 skill

企业级 AI agent 工程的 22 项原子能力(阿里云 AI Agent 手册蒸馏)。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `ai-agent-infra` | [Fen9pi-Max/ai-agent-infra](https://github.com/Fen9pi-Max/ai-agent-infra) | `d147b324d2e85672be1d96a1ede5046060f2a2de` |

### 工程管理 `engineering-management` v1.2.0 — 3 个 skill

工程管理三书蒸馏:钱学森《工程控制论》控制论项目管理、《如何管理10人以下小团队》谷歌高绩效团队法、《P9 工作法》技术硬实力/架构力/领导力。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `cybernetic-project-management` | [Fen9pi-Max/cybernetic-project-management](https://github.com/Fen9pi-Max/cybernetic-project-management) | `3e1ccbd5662e2ee1b3c5c4537d9c8e6566fd6009` |
| `small-team-management` | [Fen9pi-Max/small-team-management-skill](https://github.com/Fen9pi-Max/small-team-management-skill) | `1a397b399900b15521541b76490713f906e675d0` |
| `p9-work-methods` | [Fen9pi-Max/p9-work-methods-skill](https://github.com/Fen9pi-Max/p9-work-methods-skill) | `fb7d97db25a994f5f2de969d9975ae4a7b59b505` |

### 安全测试 `security-testing` v1.1.0 — 1 个 skill

授权渗透测试五阶段方法论(Web 与系统目标)。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `pentest-practice` | [Fen9pi-Max/pentest-skill](https://github.com/Fen9pi-Max/pentest-skill) | `91a9f26973f6fec1d106b6733b7ec6d2cca96435` |

### 产品思维 `product-thinking` v1.1.0 — 1 个 skill

《俞军产品方法论》18 张能力卡,已做 AI 产品化适配:AI 功能价值评估、幻觉致损判责、token 成本定价、AI 信任机制。

| skill | 来源仓库 | commit |
| --- | --- | --- |
| `yujun-product-methodology` | [Fen9pi-Max/yujun-product-methodology-skill](https://github.com/Fen9pi-Max/yujun-product-methodology-skill) | `19072c5bf4bfb2aba95edb186eef7eedb1eed329` |

## 更新与复现

```bash
python3 tools/sync_sources.py        # 从各源仓库拉取并重新落盘 plugins/,刷新 sources.lock.json
python3 tools/build_manifests.py     # 由单一元数据生成插件清单与市场目录(改版本/描述只改这里)
python3 tools/build_readme.py        # 重新生成本 README
python3 tools/validate_marketplace.py   # 命名/版本/描述/链接校验(CI 同步执行)
```

`sources.lock.json` 记录每个 skill 的源仓库与 commit,任何一张卡都可以追溯到它的蒸馏来源。

## 内容定性与许可

各 skill 为对原书方法论的摘要蒸馏与结构化重述,**不含原书文本**;原书版权归作者与出版社所有。
本仓库自身文件采用 MIT;各插件沿用其来源仓库的许可(`agent-engineering` 为 Apache-2.0,随 skill 保留原 LICENSE;其余为 MIT)。

相邻合集:[国密标准 Skill 合集](https://github.com/Fen9pi-Max/gmt-crypto-standards-skill)(95 个 GM/T·GM/Y 标准 skill,领域合规,独立维护)。
