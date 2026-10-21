---
name: beautiful-testing
description: |
  《测试之美》来源路由入口：访问本书全部 10 个能力（6 个晋级 + 4 个路由），含大规模自动化运营、协议测试四层抽象、变化中心测试、核心原则等能力卡与术语表。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: router
  cangjie.bundle-id: bundle.beautiful-testing
  cangjie.capability-count: 10
  cangjie.entrypoint-count: 7
---
# 测试之美（Beautiful Testing） — 来源路由入口（compact pack）

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 测试分析与用例设计（见 pirate-testing-mfqppdcs 技能包）
- 自动化框架架构与试点（见 automation-testing-best-practices 技能包）
- 具体工具（Selenium/Jenkins/Javalanche）的安装配置教程
- 安全渗透测试专项

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 完美的测试让利益相关者满意——有效、高效、优雅三维对齐，而非测试者自评
2. 测试者是发现并报告问题的顾问，不是质量把关人
3. 检验（checking）≠调查（investigating）；自动化测试≠人类做的测试
4. 没有 95% 通过率魔法数字，要 100% 失败调研
5. 覆盖率只反映执行不反映断言——测试集本身也要被测试（变异测试）
6. 时间有限按 SLIME 顺序：安全→语言→新增→度量→已存在
7. 与其全量重跑，先问黑天鹅问题：哪些测试一直没问题

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 建立或改进测试度量体系；向干系人对齐测试价值定义 | references/capabilities/stakeholder-test-metrics.md | 已晋级为独立 Skill `stakeholder-test-metrics`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 对解析型程序做模糊测试；建立模糊测试的种子与回归库 | references/capabilities/fuzzing-testing.md | 已晋级为独立 Skill `fuzzing-testing`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 度量并改进测试用例有效性；规范缺陷报告与逃逸分析 | references/capabilities/test-case-effectiveness.md | 已晋级为独立 Skill `test-case-effectiveness`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 把性能需求转为可测试的阈值承诺；协作排查性能异常 | references/capabilities/performance-testing-collaboration.md | 已晋级为独立 Skill `performance-testing-collaboration`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 版本临近时排布测试优先级；用脚本加速测试准则与数据准备 | references/capabilities/slime-efficient-testing.md | 已晋级为独立 Skill `slime-efficient-testing`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 评估测试集的真实检出能力；用变异杀灭率驱动补测试 | references/capabilities/mutation-testing.md | 已晋级为独立 Skill `mutation-testing`（已安装时优先直接使用；本卡仅作原文与背景补充） |
| 规模化自动化体系体检与改进；大规模页面/多机场景测试组织 | references/capabilities/large-scale-automation-ops.md | references/capabilities/beautiful-testing-principles.md、references/capabilities/stakeholder-test-metrics.md |
| 测试协议/API 客户端的分层设计；复杂会话协议的场景测试 | references/capabilities/protocol-testing-layers.md | references/capabilities/mutation-testing.md、references/capabilities/large-scale-automation-ops.md |
| 大代码库的回归测试选择；代码变更影响分析 | references/capabilities/change-centric-testing.md | references/capabilities/large-scale-automation-ops.md、references/capabilities/test-case-effectiveness.md |
| 评审测试策略与团队流程；校准测试观念 | references/capabilities/beautiful-testing-principles.md | references/capabilities/stakeholder-test-metrics.md、references/capabilities/slime-efficient-testing.md |

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

- 度量类任务缺少缺陷历史数据时，先建记录再计算（TCE/DDP 需要逃逸记录）
- 性能承诺涉及合同条款时提示需法务/管理层确认
