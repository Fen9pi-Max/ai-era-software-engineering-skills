---
name: beyond-legacy-code
description: |
  当用户询问《修改软件的艺术》(Beyond Legacy Code) 相关内容, 或在以下领域寻求做法时调用: 需求表达(怎么写用户故事/验收标准/需求老变怎么办)、交付节奏(故事太大怎么拆/发布周期多长合适/WIP限制)、代码质量(怎么评估代码好坏/内聚耦合封装/为什么代码难改难测)、测试实践(怎么开始TDD/红绿重构/该写多少测试/测试是不是写多了/怎么修bug不复发)、设计时机(要不要预先设计/意图导向编程/圈复杂度/工厂模式何时用)、遗留代码(祖传代码不敢动/重构还是重写/怎么跟老板要重构时间/技术债怎么还)、协作与度量(怎么推行结对编程/回顾会怎么开/开发效率怎么度量/速度能不能考核)、AI agent 编程落地(AI 生成代码要不要先补测试/给 agent 写 spec 与验收标准/人机结对小批次/AI 批量重构前的测试安全网)。不适用于: 具体CI/CD工具配置教程、特定语言框架调试、非软件领域的项目管理。Triggers: 遗留代码/legacy code/用户故事/user story/验收标准/小批次/WIP/TDD/测试先行/红绿重构/单元测试写多少/CLEAN/内聚/耦合/封装/技术债/重构/绞杀者模式/意图导向/圈复杂度/结对编程/回顾会议/开发度量 /AI 编程/agent 重构/人机结对/AI 生成代码
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.beyond-legacy-code
  cangjie.capability-count: 10
  cangjie.entrypoint-count: 1
---
# 修改软件的艺术：构建易维护代码的9条最佳实践（Beyond Legacy Code） — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- CI/CD 具体工具链配置教程(Jenkins/GitLab CI/GitHub Actions 选型与编写)
- 特定编程语言/框架的调试与 API 用法
- 临床式"我的代码哪里错了"的逐行排查(可先用 clean-code-qualities 诊断)
- 非软件领域的项目管理与流程改造

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 软件有人用就会被修改, 所以必须编写可修改的代码——"能跑就行"的质量观是遗留代码的认知根源。
2. 原则给目标(做什么), 实践给路径(怎么做); 不理解原理的实践是空壳(名义上的敏捷)。
3. {'9条实践共享一个主题': '构建可验证的代码行为——用对话取代需求文档, 用小批次换取验证, 用集成清零风险。'}
4. {'内部质量是外部质量的原因': 'CLEAN(内聚/松耦合/封装/自主/无冗余), 可测试性是质量的标尺。'}
5. {'测试先行的本质是用具体实例定义行为': '先写失败测试→刚好让测试通过的代码→重构; bug是缺失的测试。'}
6. {'好设计是演化出来的': '意图导向编程、创建与使用分离、第二次做好(2-3个用例再泛化)。'}
7. {'重构遗留代码': '地雷原则(没坏别修); 动手前先建防护网(图钉测试); 加功能=开闭两步法(先重构出空间, 再只添加代码)。'}

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 怎么写用户故事/验收标准；需求老变/客户说"不是我要的"怎么办；故事卡/需求文档该写到多细 | references/capabilities/user-story-first.md | references/capabilities/small-batches.md、references/capabilities/behavior-specification-tests.md |
| 故事/任务太大怎么拆；为什么估时总不准/任务总挂着90%；要不要限制WIP/看板怎么用；发布周期多长合适 | references/capabilities/small-batches.md | references/capabilities/user-story-first.md、references/capabilities/continuous-integration.md、references/capabilities/measure-development-value.md |
| 集成太痛/合并冲突地狱怎么办；要不要分支/功能开关怎么用；构建要多快/构建失败怎么处理；done 的定义(完成/完整完成/完美完成) | references/capabilities/continuous-integration.md | references/capabilities/small-batches.md、references/capabilities/test-first-tdd.md、references/capabilities/legacy-refactoring.md |
| 怎么推行/试行结对编程；两个人一台电脑不是浪费吗；新人怎么快速上手；回顾会议怎么开才有产出 | references/capabilities/collaboration-pairing.md | references/capabilities/test-first-tdd.md、references/capabilities/clean-code-qualities.md、references/capabilities/measure-development-value.md |
| 这段代码质量怎么样/代码评审看什么；什么是好代码/团队怎么统一质量定义；为什么我的代码难测试难修改 | references/capabilities/clean-code-qualities.md | references/capabilities/test-first-tdd.md、references/capabilities/design-last.md、references/capabilities/legacy-refactoring.md |
| 怎么开始TDD/红绿重构怎么走；为什么测试先行/先写测试还是先写代码；TDD试行失败了(测试越写越沉重)哪里做错了；修bug怎么避免复发 | references/capabilities/test-first-tdd.md | references/capabilities/behavior-specification-tests.md、references/capabilities/clean-code-qualities.md、references/capabilities/continuous-integration.md |
| 该写多少单元测试/测试要写到什么程度；测试是不是写多了/重复了；边界值怎么选测试点；修完bug怎么防复发/回归测试怎么加 | references/capabilities/behavior-specification-tests.md | references/capabilities/test-first-tdd.md、references/capabilities/user-story-first.md、references/capabilities/clean-code-qualities.md |
| 要不要预先设计/大设计前置还是演化设计；怎么降低圈复杂度；意图导向编程/单一抽象层次怎么做；工厂模式什么时候用/加新变体怎么不改调用方；过度设计vs欠设计/什么时候抽象 | references/capabilities/design-last.md | references/capabilities/clean-code-qualities.md、references/capabilities/test-first-tdd.md、references/capabilities/legacy-refactoring.md |
| 祖传/遗留代码不敢动, 怎么安全修改；重构还是重写；怎么说服老板给重构时间；技术债怎么还/什么时候还；绞杀者模式/抽象分支怎么用；给老系统加新功能前要做什么准备 | references/capabilities/legacy-refactoring.md | references/capabilities/clean-code-qualities.md、references/capabilities/test-first-tdd.md、references/capabilities/design-last.md、references/capabilities/continuous-integration.md |
| 开发团队效率怎么度量/KPI怎么定；用速度考核团队行不行；怎么论证TDD/重构/结对的收益 | references/capabilities/measure-development-value.md | references/capabilities/small-batches.md、references/capabilities/collaboration-pairing.md |

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

- 意图在路由表与能力索引中均无法命中 → 明确告知超出本书范围, 不硬套书中框架。
- 请求绑定具体工具操作 → 只给书中机制层检查单, 明示工具层超出范围。
- 纯事实查询(书名/作者/章节) → 用 overview 回答后即停, 不展开方法论建议。
