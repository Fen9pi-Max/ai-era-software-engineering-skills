---
name: slime-efficient-testing
description: |
  时间有限时按 SLIME 顺序排测试（安全最先因架构级返工/语言 Unicode 五条件/只测新增/Load→Performance→Stress→Scalability/未变部分自动化），配图案化文字验证国际化、oracle 脚本校验数据、思维导图补盲区。当用户测试时间紧要快速排优先级时使用。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.bt.slime-efficient-testing
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.beautiful-testing
  cangjie.source-title: 测试之美（Beautiful Testing）
  cangjie.tags: test-prioritization, slime, efficiency
---
# SLIME 高效测试顺序与实用脚本

## R（原文摘引）
> SLIME 是一个易记的单词，它可以指导你系统地进行测试。（第17章）

## I（解释）
**SLIME 顺序**（时间有限时按序投入）：
1. **S**ecurity 安全（最先：架构级安全返工会推翻一切用例）：跨站脚本（找所有客户端→Web 提交接口；**永不信任客户端数据**，服务端校验，白名单优于黑名单）、SQL 注入（参数化+代码扫描）、越权访问（授了权限能否且仅能做该级操作）、信息泄露（多租户隔离）。
2. **L**anguages 语言（第一轮即测）：5 条件=允许输入任何语言字符→存储→内部处理→检索→显示；Charmap 复制有趣字符；两快查：浏览器默认语言/数据库字符列是否 Unicode。**图案化文字**：资源文件串全大写+首字母^+末字母$，检查未翻译/硬编码/不该翻译被翻译/一句多次图案化（动态拼接）。
3. **requI**rements 必要性（新增）：只测本版新增功能，旧代码回归交开发单元测试兜底。
4. **M**easurement 度量（按序）：Load（受限资源压到瘫痪→修复→反复到稳定）→Performance（每 Y 时段 X 次操作）→Stress（负载大增大减，如 ATM 早晚高峰）→Scalability（加资源应得合理提升）；未确定最大负载前勿做压力测试。
5. **E**xisting 已存在（最后快速略过）；**机会成本规则**：未变代码加自动化（Selenium/Watir），人工时间投给变化部分。
**实用脚本三件套**：
- Oracle 脚本：输 ID 自动查多库多表验证生成数据正确性（前提：懂业务逻辑）；
- 测试数据生成脚本：连应用库检索"信用合格的经销商"等有效数据，取代维护电子表格；
- 组合：前端 Selenium 取数做 UI 自动化+后端 oracle 验证；附 TODO/FIXME 扫描脚本提高可见度。
脚本语言选型 5 问：我了解/能学？支持产品所有平台？能与组件（.NET/JAR）交互？能与其他工具交互？能连数据库/LDAP？
**思维导图测试设计**：中心=被测功能，越远越具体；叶子=一对多测试思路留执行者想象空间；团队每人画自己领域→轮流查看→有经验者现场加分支；三注意：认同（先小模块证明价值）、命名组织（失败时能答"哪类用例失败"）、多用户（按功能模块拆多张）。

## A1（原书案例）
Adam Goucher 用 SLIME 给发布组快速提供质量信息；图案化文字每周检查万行资源文件（人工不可行→脚本化）；思维导图团队早期发现遗漏+知识共享。

## A2（情境应用）
版本临近发布时间紧：
1. 按 SLIME 顺序排测试优先级（安全清单→i18n→新增→性能四步→未变部分）；
2. 图案化文字脚本验证资源完备性；
3. 为跨库数据写 oracle 脚本；
4. 用思维导图快速补盲区并留想象空间。

## E（评测）
- 输入：一个版本变更清单（含新增功能、未变模块、i18n 风险、安全敏感点）与有限时间。
- 输出：SLIME 排序的测试计划+至少一个脚本方案。
- 通过标准：顺序符合 SLIME 及其理由（安全最先的理由正确）；机会成本规则体现在未变模块的处置上。

## B（边界）
SLIME 是启示不是标准流程；性能深测见 performance-testing-collaboration；模糊测试找崩溃类缺陷见 fuzzing-testing。
