---
name: automation-testing-best-practices
description: |
  《自动化测试最佳实践》来源路由入口：访问本书全部 10 个能力（5 个晋级 + 5 个路由），含 MBT 工作流、猴子测试、失败分析日志、测试件标准、24 反模式清单等未晋级能力卡。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: router
  cangjie.bundle-id: bundle.automation-testing-best-practices
  cangjie.capability-count: 10
  cangjie.entrypoint-count: 6
---
# 自动化测试最佳实践（Experiences of Test Automation） — 来源路由入口（compact pack）

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 具体测试工具的安装与配置教程（Selenium/Pytest 等用法）
- 单元测试/TDD 编码实践
- 性能/安全测试专项方法论
- 纯手动测试设计技术（等价类/边界值细节）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 自动化测试就是软件开发：规格、评审、编码标准、严格复用一样不能少
2. 抽象、抽象、再抽象：工具与测试件分离、测试与实现分离（DSTL）
3. 区分测试目标与自动化目标：回归自动化的价值在信心与速度，不在发现 bug
4. ROI 计入维护与失败分析：零投入必得负回报
5. 从有目标的试点开始，quick wins 换取管理层持续支持
6. 警惕假通过：期望结果负责制 + 僵尸测试防御 + 对测试件本身做测试
7. 部分自动化与人机结合往往优于全自动

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 设计或重构自动化测试框架的分层架构；评估抽象层厚度是否合适 | references/capabilities/testware-architecture.md | 已晋级为独立 Skill `testware-architecture`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 筛选哪些测试用例应该自动化；划定暂不自动化的范围并管理期望 | references/capabilities/automation-decision-checklist.md | 已晋级为独立 Skill `automation-decision-checklist`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 论证自动化投资的投入产出；评估既有自动化是否仍划算 | references/capabilities/roi-evaluation.md | 已晋级为独立 Skill `roi-evaluation`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 启动自动化倡议并设计试点；决定扩大/调整/止损 | references/capabilities/pilot-project-methodology.md | 已晋级为独立 Skill `pilot-project-methodology`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 审查既有套件的真实有效性；建立结果验证与测试生命周期治理 | references/capabilities/results-verification-defense.md | 已晋级为独立 Skill `results-verification-defense`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 设计自动化失败的日志与报告；建立故障签名自动分类 | references/capabilities/failure-analysis-logging.md | references/capabilities/results-verification-defense.md、references/capabilities/monkey-reliability-testing.md |
| 对状态丰富的系统做基于模型的测试；用两两组合压缩测试数据组合爆炸 | references/capabilities/mbt-workflow.md | references/capabilities/monkey-reliability-testing.md、references/capabilities/roi-evaluation.md、references/capabilities/testware-architecture.md |
| 用随机测试评估系统稳定性；建立可靠性度量门槛 | references/capabilities/monkey-reliability-testing.md | references/capabilities/mbt-workflow.md、references/capabilities/failure-analysis-logging.md |
| 为测试件制定编码规约与命名标准；组织可复用模块与文档 | references/capabilities/testware-standards.md | references/capabilities/testware-architecture.md、references/capabilities/results-verification-defense.md |
| 诊断自动化项目的问题；项目启动前做风险预防检查 | references/capabilities/automation-pitfalls.md | references/capabilities/automation-decision-checklist.md、references/capabilities/testware-architecture.md、references/capabilities/pilot-project-methodology.md |

**非能力类查询**：
- 书名/作者/章节/整书概览 → references/overview.md
- 术语解释 → references/glossary.md
- 决策规则速查（不需要原文依据时） → references/cheatsheet.md
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → references/capability-index.md

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张。
- 概览/书名类问题不加载能力卡，用「核心原则」与 overview.md 回答。
- 路由表与 capability-index.md 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 边界与判停

- 用户环境缺乏明确被测系统与执行频率信息，无法做决策清单/ROI 评估时，先补齐信息
- 涉及受监管行业（医疗/航空）合规裁决时，提示需质量部门确认
