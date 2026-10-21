# 《修改软件的艺术》(Beyond Legacy Code) — 总览与参考

> Bundle 的 book/overview.md。承接 BOOK_OVERVIEW.md 的骨架与 references.md 中"有依据但不独立执行"的参考内容。

## 基本信息

- **书名**: 修改软件的艺术:构建易维护代码的9条最佳实践(Beyond Legacy Code: Nine Practices to Extend the Life (and Value) of Your Software)
- **作者**: David Scott Bernstein(戴维·斯科特·伯恩斯坦),30 年从业者/咨询师;李满庆 译;Ward Cunningham 作序
- **出版**: The Pragmatic Programmers 2015;人民邮电出版社(图灵)2017;ISBN 978-7-115-46776-8
- **一句话主旨**: 软件有人用就会被修改,必须用围绕"可验证、可修改行为"的工程实践写代码,否则代码必然沦为遗留代码——而维护成本(约占总成本80%)会吞掉软件的全部价值。

## 危机背景(第1–2章,动机)

- 瀑布模型把集成/测试推迟到最后,风险持续累积("直到最后阶段才做集成,基本上是在玩轮盘赌")。
- 引证损失量级(引用需注明出处与年代):NIST 2002 估算软件缺陷每年致美国损失近 600 亿美元;~80% 开发成本花在排查修复;Glass 2001:约60%所有者成本在优化、17%在错误修正;Boehm:交付后修 bug 成本≈需求阶段 100 倍。
- Standish 混乱报告(1994–2012)被广泛引用,但书中第2章自己论证其"成功"定义有根本缺陷——数字量级可参考,精度不可依赖。
- 近半数功能从未被使用、45% 从不使用(20% 常用)——镀金的代价。

## 敏捷源流(第3章,背景)

Deming(1950 日本)→持续质量改进→丰田精益(消除浪费;软件的浪费=WIP)→XP(Kent Beck/克莱斯勒)/Scrum;2001 敏捷宣言。敏捷正"跨越鸿沟"(Moore 技术采用周期),但常被降格为管理仪式;敏捷宣言十周年共识:**追求技术卓越是第一成功要素**(Jeff Sutherland)。

## 元框架:原则与实践(第4章,学习方法论)

- **原则**=高层次目标,告诉你做什么不告诉你怎么做("低价买,高价卖");**实践**=达成路径("成本平均法")。二者相辅相成,缺一则成空想家或无头绪实干家。
- **实践的准入三判据**:多数情况下产生价值;容易学习且容易传授;简单到无需思考。
- **守破离**:先照规则做(守)→从经验理解原理(破)→融会创变(离)。毕加索先精通传统技法再开创新风;不理解规则就"打破"是蛮干。
- **好软件的定义**:内部质量(可修改性)是外部质量的原因;"如果软件会被使用,那么它便会被修改,所以它必须被编写得可以被修改"。
- 9 条实践共享主题:**构建可验证的代码行为**。可按任意顺序采用,但须先理解每条背后要解决的问题;若有别的方法解决同一问题,可安全替换(和毕加索一样,破规则前先懂规则)。

## 9 条实践与能力映射

| # | 实践 | 能力卡 | 去向 |
|---|---|---|---|
| 1 | 先问做什么/为什么/给谁做 | user-story-first | promoted |
| 2 | 小批次构建 | small-batches | promoted |
| 3 | 持续集成 | continuous-integration | router |
| 4 | 协作 | collaboration-pairing | router |
| 5 | 编写整洁的代码(CLEAN) | clean-code-qualities | promoted |
| 6 | 测试先行 | test-first-tdd | promoted |
| 7 | 用测试描述行为 | behavior-specification-tests | promoted |
| 8 | 最后实现设计 | design-last | promoted |
| 9 | 重构遗留代码 | legacy-refactoring | promoted |
| 附 | 度量开发的7策略(6.13.1) | measure-development-value | router |

## 实证研究(第14章,参考证据)

转述含出处:IBM 缺陷率-40%、微软-60%~90%(Nagappan 等,2008);微软 Windows/MSN TDD 质量超2倍(Bhat&Nagappan);NC State:通过率+18%/耗时+16%/覆盖92–98%(George&Williams);XP:效率+50%、发布前质量+65%(Layman 等);QSM:福莱特周期-5个月、缺陷减半、省130万×6次;Hilton 开源研究:内聚+21.33%、复杂度-30.98%。**注意**:样本与年代有限(2008–2013),书中自注"这些数据并未被广泛认知"。

## 作者的局限(批判,供 Boundary 参考)

- 2015 成书:CI/CD 平台化、trunk-based、容器化等当代实践在书后;"避免分支"的一概否定在当代有正当例外。
- 深度绑定 OO/企业级 Java 咨询语境;对函数式等范式仅一句带过("很多场景下面向对象和TDD不适用")。
- 引用数据陈旧且部分被作者自己驳斥过(Standish);效率表存在表内基准不一致(见 needs-review nr-01)。
- 对实践的乐观断言(结对15%、三分之一时间节省)以亲历案例与有限研究支撑。

## 学习顺序建议(从依赖关系推出)

1. `clean-code-qualities`(公共语言)→ 2. `user-story-first` → 3. `test-first-tdd` + `behavior-specification-tests`(一体两翼)→ 4. `small-batches` + `continuous-integration`(流程地基)→ 5. `design-last` → 6. `legacy-refactoring`(收束)→ 配套 `collaboration-pairing`、`measure-development-value`。
