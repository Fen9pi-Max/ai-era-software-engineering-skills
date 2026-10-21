---
name: how-google-tests-software
description: |
  基于《Google软件测试之道》（Whittaker/Arbon/Carollo, 2012）蒸馏的 Google 级测试方法论。
  当用户要做 ACC 测试计划（特质-组件-能力矩阵）、测试风险排序（频率×影响热图）、测试规模分类
  （小/中/大型与 70/20/10）、设计探索式漫游测试、设计渐进发布版本链（金丝雀→开发→测试→beta）、
  划分 SWE/SET/TE 测试职责、SET 早期介入与可测试性评审、推行测试认证让开发负责测试、
  诊断测试组织病理与转型、bug 定级与生命周期、自动化范围取舍与遗留用例瘦身、
  编写大型项目基于风险的测试计划、组织众包/内部试用/外部供应商测试时使用。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.how-google-tests-software
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# Google软件测试之道（How Google Tests Software） — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- Google 已停维护内部工具的安装使用（Autotest/GTA/BITE/RPF/Buganizer）
- 具体测试框架（Selenium/pytest）的代码教程
- 测试人员招聘面试全流程（仅 overview 参考区）
- 性能调优与压测实施本身（仅参考区实录）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 质量是内建的预防行为，不是测试环节外加的检测；开发与测试融合到无法区分
2. 开发对质量负责（你构建它，你测试它）；专职测试者的使命是让别人更好地测试
3. 测试按范畴规模（小/中/大）分类而非形式（单元/集成/系统），分类自带执行约束
4. 测试计划必须是简明列表，最终直接指导测试用例编写，否则是浪费时间
5. 风险=失败频率×影响的定性相对值，只求排序不求精确；不能全测就先测风险最大的
6. 探索式测试用漫游隐喻结构化，与 ACC 矩阵行/列分工避免重叠
7. 自动化取舍：能自动化的自动化，需人类智慧的留给手动，20%用例覆盖80%场景
8. 是谁在做测试不重要，关键是进行了测试（内部试用者/众包/真实用户可能更有效）

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 为产品制定简明测试计划；把产品功能分解为可测试的能力矩阵；组织测试分工（矩阵行/列切片） | references/capabilities/acc-test-planning.md | references/capabilities/risk-heat-map.md、references/capabilities/touring-exploratory-testing.md、references/capabilities/risk-based-test-plan-template.md |
| 为测试对象排优先级；用风险热图做发布决策；收集相关方风险意见 | references/capabilities/risk-heat-map.md | references/capabilities/acc-test-planning.md、references/capabilities/risk-based-test-plan-template.md、references/capabilities/bug-lifecycle.md |
| 判断一个测试属于小/中/大型；规划项目测试组合比例；诊断测试组合失衡 | references/capabilities/test-size-model.md | references/capabilities/automation-scope-and-maintenance.md、references/capabilities/set-early-involvement.md、references/capabilities/swe-set-te-role-model.md |
| 设计探索式测试会话；为被测应用选择漫游组合；组织多人探索式测试分工 | references/capabilities/touring-exploratory-testing.md | references/capabilities/acc-test-planning.md、references/capabilities/crowd-and-dogfood-testing.md、references/capabilities/risk-heat-map.md |
| 评审设计文档的可测试性；规划测试基础设施与自动化计划；决定测试介入项目时机 | references/capabilities/set-early-involvement.md | references/capabilities/test-size-model.md、references/capabilities/swe-set-te-role-model.md、references/capabilities/automation-scope-and-maintenance.md |
| 决定哪些测试该自动化；清理精简遗留测试用例；项目转维护期的测试撤离 | references/capabilities/automation-scope-and-maintenance.md | references/capabilities/test-size-model.md、references/capabilities/bug-lifecycle.md、references/capabilities/set-early-involvement.md |
| 设计产品发布与测试版本节奏；规划灰度放量的各级用户与晋级标准 | references/capabilities/crawl-walk-run-release.md | references/capabilities/risk-heat-map.md、references/capabilities/risk-based-test-plan-template.md、references/capabilities/crowd-and-dogfood-testing.md |
| 划分团队的测试职责与角色；判断成员适合 SET 还是 TE；决定测试人员编制规模 | references/capabilities/swe-set-te-role-model.md | references/capabilities/test-org-pathologies.md、references/capabilities/set-early-involvement.md、references/capabilities/test-certified-ladder.md |
| 评估团队测试成熟度；设计让开发写测试的推行机制 | references/capabilities/test-certified-ladder.md | references/capabilities/swe-set-te-role-model.md、references/capabilities/test-org-pathologies.md、references/capabilities/test-size-model.md |
| 诊断测试组织的问题；规划测试团队转型方向；评估独立测试部门存废 | references/capabilities/test-org-pathologies.md | references/capabilities/swe-set-te-role-model.md、references/capabilities/crowd-and-dogfood-testing.md、references/capabilities/test-certified-ladder.md |
| 给 bug 定级（严重性/优先级）；设计 bug 处理流程；治理 bug 积压 | references/capabilities/bug-lifecycle.md | references/capabilities/risk-heat-map.md、references/capabilities/automation-scope-and-maintenance.md |
| 编写大型/硬件项目完整测试计划；设计分级测试执行节奏 | references/capabilities/risk-based-test-plan-template.md | references/capabilities/risk-heat-map.md、references/capabilities/acc-test-planning.md、references/capabilities/crawl-walk-run-release.md |
| 组织众包或外包测试；建立内部试用（dogfood）机制；选择外部专业测试供应商 | references/capabilities/crowd-and-dogfood-testing.md | references/capabilities/touring-exploratory-testing.md、references/capabilities/acc-test-planning.md、references/capabilities/test-org-pathologies.md |

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

- 无产品/系统描述时先索取，不凭空编 ACC 矩阵
- 测试规模时间/资源精确数值原书在插图中未解析，不引用具体分钟数
- 组织转型建议须确认团队规模与文化前提，Google 大厂机制不直接照搬小团队
