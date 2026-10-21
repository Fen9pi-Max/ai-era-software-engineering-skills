---
name: effective-software-testing
description: |
  基于《有效软件测试》（Elfriede Dustin, 50 条最佳实践）蒸馏的测试方法论。当用户要审查需求可测试性、估计测试工作量、设计测试数据与用例（等价类/边界值/正交排列）、组织单元测试与 CI、选择测试工具并纠偏自动化期望、重构脆弱脚本为数据驱动框架、搭建回归+烟雾流水线、规划非功能测试（性能/并发/安全/兼容）、建立缺陷流程与测试度量时使用。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.effective-software-testing
  cangjie.capability-count: 10
  cangjie.entrypoint-count: 1
---
# 有效软件测试——提高测试的 50 条建议（Effective Software Testing: 50 Specific Ways） — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 具体测试工具（Selenium/pytest/Jira 等）安装配置教程
- 渗透测试实操
- TDD 流派之争与测试驱动设计细节
- 性能调优本身

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 测试始于项目开始（需求阶段），而非编码完成后
2. 修正缺陷的代价随阶段指数增长，缺陷预防优先
3. 穷尽测试不可能，风险与使用频率驱动优先级
4. 综合使用多种测试技术优于单一技术
5. 自动化是微型开发生命周期：首用工作量反而增加，须纠偏期望
6. 脚本工程：数据驱动、模块化、对象名导航、版本控制
7. 非功能需求必须与功能需求同期定义
8. 一报告一缺陷；仅测试组有权关闭；度量到步骤级

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 审查需求文档的可测试性与质量属性；为需求排优先级并治理变更 | references/capabilities/requirements-testability-review.md | references/capabilities/test-design-techniques.md、references/capabilities/test-effort-estimation.md |
| 估计新项目测试工作量与人员规模 | references/capabilities/test-effort-estimation.md | references/capabilities/requirements-testability-review.md |
| 为功能或性能测试设计数据集；把硬编码数据外置为数据驱动表 | references/capabilities/test-data-design.md | references/capabilities/test-design-techniques.md、references/capabilities/script-engineering.md |
| 从需求设计测试用例集；压缩参数组合爆炸；判断哪些场景值得自动化 | references/capabilities/test-design-techniques.md | references/capabilities/test-data-design.md、references/capabilities/script-engineering.md |
| 组织分层单元测试并接入 CI；用存根支持测试先行 | references/capabilities/unit-test-practices.md | references/capabilities/regression-smoke-pipeline.md |
| 引入测试自动化工具前对齐期望与选型；决定购买还是自制测试工具 | references/capabilities/automation-expectations-and-tool-selection.md | references/capabilities/script-engineering.md、references/capabilities/regression-smoke-pipeline.md |
| 重构脆弱的录制回放脚本；建立可维护的自动化脚本工程规范；用适配器直测核心组件并比对新旧系统 | references/capabilities/script-engineering.md | references/capabilities/test-data-design.md、references/capabilities/regression-smoke-pipeline.md |
| 搭建 CI 测试流水线与准入门禁；选择回归测试范围并持续优化套件 | references/capabilities/regression-smoke-pipeline.md | references/capabilities/unit-test-practices.md、references/capabilities/defect-lifecycle-metrics.md |
| 规划性能/并发/安全/兼容性测试；从需求阶段挖出非功能需求 | references/capabilities/nonfunctional-testing.md | references/capabilities/requirements-testability-review.md、references/capabilities/test-data-design.md |
| 建立或审计缺陷流程；用度量判断测试收尾与修正质量 | references/capabilities/defect-lifecycle-metrics.md | references/capabilities/regression-smoke-pipeline.md |

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

- 需求文本缺失时先索取，不凭记忆审查
- 受监管行业的合规裁决提示需质量部门确认
