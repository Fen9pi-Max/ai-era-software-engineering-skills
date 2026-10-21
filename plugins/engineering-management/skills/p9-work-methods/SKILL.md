---
name: p9-work-methods
description: |
  基于《P9 工作法》（朱春茂等，蚂蚁国际五位资深技术专家，2024）蒸馏的技术人三力工作法。当用户要：把代码改造到"一眼看到底"或安全重构、写系统分析文档/接口契约、做领域建模、设计自测用例、排查幂等/错误码/分布式事务/缓存/异步/高可用六类分布式盲区、处理要事优先与高效会议等日常软技能、线上应急与风险暴露、架构师三心魔自检、架构取舍（七见模型/五步生长法/资金保障系数）、高可用资损防控兜底、架构演进与决策文档、业产技系统思维、团队目标与绩效对话、技术规划拆解咬合、团队成长与主管修炼时使用。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.p9-work-methods
  cangjie.capability-count: 18
  cangjie.entrypoint-count: 1
---
# P9 工作法：夯实技术硬实力、架构力和领导力 — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 蚂蚁内部工具与平台的具体使用（图注提及的内部系统）
- 具体语言/框架编码教程（书以 Java 支付系统为语境，不教语法）
- 职级晋升答辩技巧（P9 是能力画像非职级攻略）
- 非互联网行业的组织管理移植（默认大厂语境，小团队需降配）

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 技术能力=解决问题的能力；同一件事的做法层次（就事论事→文档→工具化→根因/全局）决定价值
2. 术（硬实力，职责驱动）、法（架构力，问题驱动）、道（领导力，使命驱动）三层递进
3. 好代码/好系分的标准是可构造的：一眼看到底七步、上承需求下启代码的范式
4. 分布式每个专题都有盲区，本质多归于异构系统数据一致性；确定性是应对 VUCA 的唯一解药
5. 架构是取舍：先过完美主义/风险主义/单一主义三心魔，再谈方法；演进以经营者姿态用极致目标约束
6. 技术与业务双螺旋：没有业务成功就没有技术先进性；目标要咬合、路径要拆解、里程碑要反馈
7. 团队上限由主管决定：成就他人、追过程、负反馈、统一思想，从管事走向修己

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 把一段代码改造成别人能顺序读懂；自查或评审团队的编码坏习惯；决定要不要重构以及重构多大范围；安全执行重构不引入生产故障 | references/capabilities/p9-clean-code.md | references/capabilities/p9-system-analysis.md、references/capabilities/p9-self-test-quality.md、references/capabilities/p9-domain-modeling.md |
| 写一份合格的系统分析/技术方案文档；把产品需求转成技术方案并达成团队共识；组织一场有结论的系分评审；检查系分质量是否空洞走形式；划定跨系统功能职责边界；评估改造工作量与里程碑 | references/capabilities/p9-system-analysis.md | references/capabilities/p9-clean-code.md、references/capabilities/p9-interface-contract.md、references/capabilities/p9-arch-modeling.md |
| 为跨团队接口制定契约文档；治理存量接口的契约缺失；定义接口状态码与错误码处理规则；降低端到端联调测试成本；让旧接口敢重构 | references/capabilities/p9-interface-contract.md | references/capabilities/p9-system-analysis.md、references/capabilities/p9-arch-evolution.md |
| 对新业务域抽象实体、关系与边界；评审领域模型/实体设计的好坏；决策新能力是改老模型还是新增模型；判断某系统/服务该不该用领域模型；设计模型演进与兼容性方案 | references/capabilities/p9-domain-modeling.md | references/capabilities/p9-arch-modeling.md、references/capabilities/p9-clean-code.md、references/capabilities/p9-systems-thinking.md |
| 提测前设计自测用例；以用户场景穷举验证功能准确性；为关键设计与非功能需求写保障用例；治理不稳定、膨胀、无效的自测用例；重构前补测试保护核心逻辑 | references/capabilities/p9-self-test-quality.md | references/capabilities/p9-clean-code.md、references/capabilities/p9-idempotency-errorcode.md |
| 排查重复扣款/重复提现等幂等失效故障；设计或评审幂等控制方案（字段/存储/逻辑）；映射外部接口错误码（超时/交互失败/查无交易）；设计推拉补偿与 SLA 时间窗口；切流/迁移期间防跨系统重复处理 | references/capabilities/p9-idempotency-errorcode.md | references/capabilities/p9-dist-tx-cache.md、references/capabilities/p9-async-ha.md、references/capabilities/p9-self-test-quality.md |
| 选择分布式事务方案；排查与预防事务悬挂；评估缓存引入前的适用性与风险；排查缓存可用性故障；设计缓存与数据库一致性方案；判断缓存能否承担某职责 | references/capabilities/p9-dist-tx-cache.md | references/capabilities/p9-idempotency-errorcode.md、references/capabilities/p9-arch-stability.md、references/capabilities/p9-async-ha.md |
| 设计异步化任务与监控；排查异步任务积压或消失；设计事务消息回查逻辑；审查分库分表与读写分离的盲区；设计流水型或状态型数据 FailOver；评估高可用方案的业务适配性 | references/capabilities/p9-async-ha.md | references/capabilities/p9-dist-tx-cache.md、references/capabilities/p9-arch-stability.md、references/capabilities/p9-emergency-risk.md |
| 识别要事并学会拒绝；准备一次关键沟通；组织汇报或答辩表达；组织高效会议并写纪要；推进卡住的跨团队协作；决定是否补位 | references/capabilities/p9-daily-soft-skills.md | references/capabilities/p9-emergency-risk.md、references/capabilities/p9-team-performance.md |
| 组织生产故障的应急响应指挥；判断资金类故障的存量影响与处理时效；建设runbook与常态化应急演练；判断风险上报的时机与话术；把风险暴露给有决策权的人 | references/capabilities/p9-emergency-risk.md | references/capabilities/p9-daily-soft-skills.md、references/capabilities/p9-arch-stability.md |
| 架构方案评审或规划前做心态自检；制定合理的故障与风险KPI；向业务给出确定而不夸口的SLA承诺；判断议题是否在架构解题范围内并转交；在复盘会上用帮而非抓的方式对待风险 | references/capabilities/p9-arch-mindset.md | references/capabilities/p9-arch-modeling.md、references/capabilities/p9-arch-stability.md、references/capabilities/p9-systems-thinking.md |
| 重构简化臃肿混乱的老系统；把降本提效优化类虚课题做实；推导理论公式与能力树并定义性能参数；为新领域寻找真问题与切入点；用七见叙事链讲清架构的位置与价值 | references/capabilities/p9-arch-modeling.md | references/capabilities/p9-arch-mindset.md、references/capabilities/p9-domain-modeling.md、references/capabilities/p9-arch-stability.md |
| 设计高可用方案；防控资损与资金风险敞口；建立风险兜底体系；管控生产变更流程；制定可用率目标与故障分级口径；故障/资损复盘后补齐防控缺口 | references/capabilities/p9-arch-stability.md | references/capabilities/p9-arch-modeling.md、references/capabilities/p9-async-ha.md、references/capabilities/p9-emergency-risk.md |
| 推进架构治理与归一；论证架构升级的业务价值；制定演进目标与里程碑节奏；记录与沉淀架构决策；做架构传承（原则/审计/白皮书）；判断何时启动架构升级 | references/capabilities/p9-arch-evolution.md | references/capabilities/p9-arch-stability.md、references/capabilities/p9-tech-planning.md、references/capabilities/p9-systems-thinking.md |
| 定位架构师角色与权责边界；改善业务-产品-技术协作模式；为当前问题选择架构思考方法；从多因素中识别关键点；根因分析（防过浅/过深）；规划架构师个人成长路径 | references/capabilities/p9-systems-thinking.md | references/capabilities/p9-arch-mindset.md、references/capabilities/p9-arch-evolution.md、references/capabilities/p9-team-growth-self.md |
| 为团队或成员设定绩效目标；做目标过程管理与风险决策；给成员打绩效并撰写评价；准备和开展绩效面谈；诊断目标执行偏差；新任主管角色转型自检 | references/capabilities/p9-team-performance.md | references/capabilities/p9-tech-planning.md、references/capabilities/p9-team-growth-self.md、references/capabilities/p9-daily-soft-skills.md |
| 制定团队年度/半年度技术规划；评审技术规划的质量（高度/深度/锐度）；把业务目标转化为技术目标；拆解目标为路径与里程碑；规划技术底盘与长期投入 | references/capabilities/p9-tech-planning.md | references/capabilities/p9-team-performance.md、references/capabilities/p9-arch-evolution.md |
| 建设团队专业性与知识沉淀；设计新人融入机制；用负反馈问题清单推动团队跃迁；配置主管精力与守住本职；跨越组织边界建立影响力；规划个人成长与心态调节 | references/capabilities/p9-team-growth-self.md | references/capabilities/p9-team-performance.md、references/capabilities/p9-systems-thinking.md |

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

- 涉及资金/高可用决策但缺系统与团队信息时先索取，不凭空编公式参数
- 公式口径缺口（E(X) 中 N 语义、D(X) 折算、可用率换算）以原文为准并声明，不用常识补齐
- 管理类方法须确认团队规模与文化前提；蚂蚁语境的机制不直接照搬小团队
- 插图数值未入 epub 文本处按正文执行并声明差异（履带板块 9/10 等）
