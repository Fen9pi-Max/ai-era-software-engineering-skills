---
name: pirate-testing-mfqppdcs
description: |
  《海盗派测试分析MFQ&PPDCS》来源路由入口：访问本书全部 9 个能力（6 个晋级 + 3 个路由），含测试执行反馈环、海盗派原则、术语表与收银机/大富翁完整案例。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: router
  cangjie.bundle-id: bundle.pirate-testing-mfqppdcs
  cangjie.capability-count: 8
  cangjie.entrypoint-count: 7
---
# 海盗派测试分析MFQ&PPDCS — 来源路由入口（compact pack）

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 自动化测试框架与脚本工程（见 automation-testing-best-practices 技能包）
- 单元测试/TDD 编码实践
- 具体测试管理工具（TestRail/Jira）操作
- 性能/安全等专项测试的执行技术

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 先 Why 后 How：KYM 了解任务、把握主干忽略细节
2. 测试域无穷、资源有限：基于风险（L×I）做明智选择，变无限为有限
3. MFQ 三维拆分：单功能 M 建模深挖、功能交互 F 探索、质量属性 Q 专项
4. 画 Model 的过程就是澄清需求的过程——测试分析越早越好（预防性测试）
5. 测试数据必须具体且多样化，禁用"有效的"类模糊字眼
6. Tests ≠ Testing：设计出的用例不等于测试，执行中持续收集信息调整策略
7. Apply Heuristics, Not to Follow Them——一切步骤基于上下文取舍

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 接手新测试任务时调研上下文与目标；明确测试任务的风险与信息缺口 | references/capabilities/kym-cidtestd.md | 已晋级为独立 Skill `kym-cidtestd`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 从需求文档快速梳理测试范围；防遗漏的测试覆盖清单 | references/capabilities/tco-coverage-outline.md | 已晋级为独立 Skill `tco-coverage-outline`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 对被测系统做三维测试拆分；决定各维度用什么测试手段 | references/capabilities/mfq-analysis-views.md | 已晋级为独立 Skill `mfq-analysis-views`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 为单功能选择合适的测试建模技术；从需求文字中识别建模信号 | references/capabilities/ppdcs-model-selection.md | 已晋级为独立 Skill `ppdcs-model-selection`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 对单功能建模并产出测试条件；通过建模发现需求模糊与遗漏 | references/capabilities/modeling-workflow.md | 已晋级为独立 Skill `modeling-workflow`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 把测试条件细化为可执行测试实例；为变量选取具体且多样化的测试数据 | references/capabilities/test-design-4steps.md | 已晋级为独立 Skill `test-design-4steps`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 规划与复盘测试执行 Session；评估并提升测试深度 | references/capabilities/test-execution-feedback.md | references/capabilities/pirate-testing-principles.md、references/capabilities/test-design-4steps.md |
| 评审测试方案与工作方式；校准测试观念（防形式化/一次性分析） | references/capabilities/pirate-testing-principles.md | references/capabilities/kym-cidtestd.md、references/capabilities/test-execution-feedback.md |

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

- 缺少被测对象描述与任务背景时，先做 KYM 补齐上下文再分析
- 需求过于模糊无法确定单功能边界时，输出疑问清单交需求方澄清
