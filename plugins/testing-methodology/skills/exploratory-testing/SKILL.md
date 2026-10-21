---
name: exploratory-testing
description: |
  《探索吧！深入理解探索式软件测试》来源路由入口：访问本书全部 13 个能力（7 个晋级 + 6 个路由），含生态系统信任边界、顺序交互变化、需求探索、噩梦头条工作坊、遗留系统侦察、干系人汇报等未晋级能力卡。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: router
  cangjie.bundle-id: bundle.exploratory-testing
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 8
---
# 探索吧！深入理解探索式软件测试（Explore It!） — 来源路由入口（compact pack）

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 脚本化/自动化回归测试的设计与实现（检查侧）
- 性能、安全专项测试方法论
- 测试团队管理、招聘流程（附录1 仅作参考保留）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 已测试 = 已检查 + 已探索；预设计用例是绊线网，探索侦察网外区域
2. 探索 = 同时设计并执行测试以学习系统，根据前一个试验的洞察选择下一个试验
3. 探测章程给方向不规定步骤；过细是用例，过宽永远做不完
4. 变量是变化的原子单元：找到变量（明显/微妙/可间接访问）再用启发法改变它
5. 可测试性 = 可视性 + 控制；日志、控制台、监控让不可见变可见
6. 无需求时仍有神谕：绝不/始终规则、内在一致性、标准、对比、近似
7. 任何缺陷 100% 可重现，只要发现并控制影响它的所有变量
8. 早探索多探索；探索发现大量惊喜说明流程之网有大洞

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 为某特性/模块起草探测章程；组织和执行限时探测会话并汇报结果 | references/capabilities/charter-session-design.md | 已晋级为独立 Skill `charter-session-design`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 对某系统头脑风暴可变化的变量；用启发法（0/1/多、金发女孩、干扰等）生成试验清单 | references/capabilities/test-heuristics-cheatsheet.md | 已晋级为独立 Skill `test-heuristics-cheatsheet`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 提高对被测系统的观察深度；为难测系统布置可测试性监控 | references/capabilities/deep-observation-testability.md | 已晋级为独立 Skill `deep-observation-testability`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 无明确需求时判定观察到的行为是否正确；为系统建立"绝不/始终"规则清单 | references/capabilities/oracle-strategies.md | 已晋级为独立 Skill `oracle-strategies`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 为某工作流/实体生命周期建模状态；从状态模型生成试验并调查时机相关问题 | references/capabilities/state-model-exploration.md | 已晋级为独立 Skill `state-model-exploration`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 识别系统实体并绘制关系图；用 CRUD×启发法组合生成数据试验 | references/capabilities/entity-crud-exploration.md | 已晋级为独立 Skill `entity-crud-exploration`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 调查"无法重现"的间歇性缺陷；让偶发问题更频繁地发生以便定位 | references/capabilities/intermittent-bug-hunting.md | 已晋级为独立 Skill `intermittent-bug-hunting`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 绘制被测系统的生态系统图；用"如果的话"系统性注入依赖故障 | references/capabilities/ecosystem-trust-boundary-exploration.md | references/capabilities/entity-crud-exploration.md、references/capabilities/oracle-strategies.md、references/capabilities/test-heuristics-cheatsheet.md |
| 打破习惯性操作路径生成随机场景；用角色人物视角改变使用软件的方式 | references/capabilities/sequence-interaction-variation.md | references/capabilities/test-heuristics-cheatsheet.md、references/capabilities/charter-session-design.md |
| 在需求评审中发现歧义、假设和范围缺口；从需求文档提取探测章程 | references/capabilities/requirements-exploration.md | references/capabilities/charter-session-design.md、references/capabilities/oracle-strategies.md、references/capabilities/stakeholder-reporting-stop-criteria.md |
| 组织群体头脑风暴识别最担心的风险；把风险转化为可执行的探测章程 | references/capabilities/nightmare-headlines-workshop.md | references/capabilities/charter-session-design.md、references/capabilities/oracle-strategies.md |
| 接手不熟悉的现存系统并快速建立理解；通过干系人采访收集最有价值的问题 | references/capabilities/legacy-system-recon.md | references/capabilities/charter-session-design.md、references/capabilities/ecosystem-trust-boundary-exploration.md、references/capabilities/intermittent-bug-hunting.md |
| 向干系人简明汇报探索进展与发现；判断对某区域的探索是否已充分 | references/capabilities/stakeholder-reporting-stop-criteria.md | references/capabilities/charter-session-design.md、references/capabilities/oracle-strategies.md |

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

- 没有可运行的被测系统且用户只要理论摘要时，仅输出方法论说明不做演练
- 涉及安全关键（医疗/航空）合规裁决时提示需领域专家确认
