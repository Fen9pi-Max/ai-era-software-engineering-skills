---
name: cybernetic-project-management
description: |
  基于《工程控制论》（钱学森、宋健）蒸馏的项目管理方法论。当用户要判断项目是否失控/健康度、做多目标（进度质量成本）权衡与指标设计、设计监控反馈节拍与告警升级规则、做估算建模与资源上限规划、从含噪数据估计真实进度、管理基线与偏差变更、在未知领域设计试探迭代节奏、处理反馈延迟导致的越纠越乱、治理多团队接口解耦与协调、做赶工冲刺与切换决策、识别单点故障并设计冗余容错、设计环境剧变后的自动恢复预案、或设计项目群分层治理架构时使用。不用于目标设定本身、纯技术执行问题或无法度量的场景。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.engineering-cybernetics
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# 工程控制论（上、下册） — 全书能力入口

## 触发与不触发

**适用**：与本书能力域相关的咨询与任务（见下方路由表的意图列）。
**不适用**：
- 目标与产品方向本身的对错（控制论管逼近目标，不管目标设定）
- 无法产生任何执行数据的纯概念讨论
- 个人效能/时间管理（对象是"系统"不是"个人"）
- 具体工具（Jira/飞书等）的操作配置

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 稳定性优先：先判关键回路是否发散（一票否决），再比指标优劣；评估健康度看裕度而非二值
2. 指标相互矛盾：全满足不可能，分别评价后抓当前主要矛盾；拒绝加权合成单一 KPI，保帕累托集
3. 反馈闭环三要素（测量-比较-纠偏）缺一不可；节拍与告警阈值按噪声水平设计，连续 N 次确认才升级
4. 模型是有边界声明的近似；资源上限必须显式化；实测与历史数据优先于理论分解
5. 信息不完备的三条出路：噪声中过滤估计、未知对象试探寻优、剧变环境自适应恢复
6. 可靠性靠结构设计：串联乘积定律定瓶颈，冗余三形态（热备/冷备/k-N 表决）按失效代价选型
7. 大系统分层治理是信息结构必然：分解-独立设计-重连分析耦合，局部最优必须配全局协调

## 能力路由（先读本表，按意图加载 1 张能力卡）

| 用户意图 | 先读 | 补读/备注 |
|---|---|---|
| 判断项目是否失控/健康度如何；评估项目离失控还有多远 | references/capabilities/stability-health-check.md | references/capabilities/multi-objective-tradeoff.md、references/capabilities/adaptive-self-stabilization.md |
| 设计项目指标体系/KPI；进度质量成本范围多目标权衡决策；拒绝或替代综合评分 | references/capabilities/multi-objective-tradeoff.md | references/capabilities/stability-health-check.md、references/capabilities/time-optimal-switching.md |
| 设计周报/站会/评审节拍；定义风险告警与升级规则；检查纠偏为何迟迟不收敛 | references/capabilities/feedback-cadence-design.md | references/capabilities/noise-filtering-estimation.md、references/capabilities/adaptive-self-stabilization.md |
| 做工期/成本估算；检验简化假设是否合法；选择估算方法（拆解/试点/历史数据） | references/capabilities/model-approximation-identification.md | references/capabilities/baseline-variance-control.md、references/capabilities/extremum-seeking-iteration.md |
| 判断数据波动是趋势还是噪声；设定汇报/仪表盘平滑口径；确定度量精度的极限 | references/capabilities/noise-filtering-estimation.md | references/capabilities/feedback-cadence-design.md、references/capabilities/extremum-seeking-iteration.md |
| 制定与冻结项目基线；周期性偏差分析与处置；决定改计划还是加把劲（re-baseline 判定） | references/capabilities/baseline-variance-control.md | references/capabilities/model-approximation-identification.md、references/capabilities/multi-objective-tradeoff.md |
| 在未知领域设计探索迭代节奏；决定试验步子迈多大、节奏多快；单参数调优（0.618 优选法） | references/capabilities/extremum-seeking-iteration.md | references/capabilities/model-approximation-identification.md、references/capabilities/noise-filtering-estimation.md |
| 处理汇报/审批延迟下的决策；遏制"越纠越振荡"；为延迟反馈设计提前量 | references/capabilities/delay-compensation.md | references/capabilities/feedback-cadence-design.md、references/capabilities/noise-filtering-estimation.md |
| 治理多团队互相阻塞；设计接口契约与依赖规则；跨团队目标对齐（协调 vs 解耦） | references/capabilities/decoupling-coordination.md | references/capabilities/large-system-decomposition.md、references/capabilities/adaptive-self-stabilization.md |
| 赶工决策（力度与时长）；决定何时停止冲刺转入稳定；设定"够好就停"标准 | references/capabilities/time-optimal-switching.md | references/capabilities/multi-objective-tradeoff.md、references/capabilities/stability-health-check.md |
| 识别关键单点故障；设计关键角色/组件备份；多源估算或评审结论的表决合成 | references/capabilities/redundancy-fault-tolerance.md | references/capabilities/adaptive-self-stabilization.md、references/capabilities/large-system-decomposition.md |
| 设计真正会触发的应急预案；环境剧变后的自动恢复机制；验收过程改进动作的有效性 | references/capabilities/adaptive-self-stabilization.md | references/capabilities/stability-health-check.md、references/capabilities/redundancy-fault-tolerance.md、references/capabilities/large-system-decomposition.md |
| 设计项目群/多项目治理架构；决定决策权上下分配；诊断"各组都好整体却差" | references/capabilities/large-system-decomposition.md | references/capabilities/decoupling-coordination.md、references/capabilities/adaptive-self-stabilization.md、references/capabilities/multi-objective-tradeoff.md |

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

- 项目无任何历史数据且无度量可能时，如实说明"不可观测"，不凭印象硬判
- 涉及裁员等重大人事决策时只提供结构分析，决定权在人
- 数学推导细节超出转译需要时引用原书章节，不展开演算
