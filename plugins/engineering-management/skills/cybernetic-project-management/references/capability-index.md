# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| stability-health-check | 项目稳定性体检（稳定性优先+裕度度量） | critical | 判断项目是否失控/健康度如何；评估项目离失控还有多远 | 稳定性、失控、健康度、裕度、发散回路、stability、margin | capabilities/stability-health-check.md |
| multi-objective-tradeoff | 多目标指标体系与权衡（六项清单+主要矛盾+向量指标） | critical | 设计项目指标体系/KPI；进度质量成本范围多目标权衡决策；拒绝或替代综合评分 | 多目标、权衡、KPI、主要矛盾、帕累托、trade-off、pareto | capabilities/multi-objective-tradeoff.md |
| feedback-cadence-design | 反馈回路与节拍设计（采样周期+双阈值告警+有限收敛） | critical | 设计周报/站会/评审节拍；定义风险告警与升级规则；检查纠偏为何迟迟不收敛 | 反馈、节拍、告警、升级、采样、cadence、alert、escalation | capabilities/feedback-cadence-design.md |
| model-approximation-identification | 建模与估算（工程近似边界+控制量受限+辨识三法） | high | 做工期/成本估算；检验简化假设是否合法；选择估算方法（拆解/试点/历史数据） | 估算、建模、假设、近似、辨识、estimation、capacity | capabilities/model-approximation-identification.md |
| noise-filtering-estimation | 噪声过滤与状态估计（通频带权衡+原理性下限） | high | 判断数据波动是趋势还是噪声；设定汇报/仪表盘平滑口径；确定度量精度的极限 | 噪声、信号、平滑、趋势、估计、signal、noise、smoothing | capabilities/noise-filtering-estimation.md |
| baseline-variance-control | 基线与偏差管理（摄动制导范式） | critical | 制定与冻结项目基线；周期性偏差分析与处置；决定改计划还是加把劲（re-baseline 判定） | 基线、偏差、变更控制、re-baseline、baseline、variance | capabilities/baseline-variance-control.md |
| extremum-seeking-iteration | 自寻最优点的试探迭代（连续测量+步长律+0.618 优选） | high | 在未知领域设计探索迭代节奏；决定试验步子迈多大、节奏多快；单参数调优（0.618 优选法） | 探索、试探、迭代、优选法、步长、iterate、probe、golden-ratio | capabilities/extremum-seeking-iteration.md |
| delay-compensation | 时滞补偿（历史区间思维+最坏情况设计） | high | 处理汇报/审批延迟下的决策；遏制"越纠越振荡"；为延迟反馈设计提前量 | 延迟、时滞、提前量、在途动作、越纠越乱、delay、lag | capabilities/delay-compensation.md |
| decoupling-coordination | 多团队解耦与协调（互不影响设计+协调三原则） | high | 治理多团队互相阻塞；设计接口契约与依赖规则；跨团队目标对齐（协调 vs 解耦） | 解耦、协调、接口、依赖、多团队、decouple、coordination | capabilities/decoupling-coordination.md |
| time-optimal-switching | 最速冲刺与切换时机（bang-bang+存在性优先+终点补稳） | high | 赶工决策（力度与时长）；决定何时停止冲刺转入稳定；设定"够好就停"标准 | 冲刺、赶工、止损、切换、停止标准、crunch、switching | capabilities/time-optimal-switching.md |
| redundancy-fault-tolerance | 冗余与容错设计（自检+热备/冷备/k-N 表决+可靠性口径） | high | 识别关键单点故障；设计关键角色/组件备份；多源估算或评审结论的表决合成 | 冗余、容错、单点故障、备份、bus-factor、redundancy、fault-tolerance | capabilities/redundancy-fault-tolerance.md |
| adaptive-self-stabilization | 自适应与自镇定（开关边界+复杂度定律+分组隔离+方向性检验） | high | 设计真正会触发的应急预案；环境剧变后的自动恢复机制；验收过程改进动作的有效性 | 自适应、韧性、预案、恢复、resilience、contingency、adaptation | capabilities/adaptive-self-stabilization.md |
| large-system-decomposition | 大系统分解-协调（多级递阶+切断重连+全局协调必要） | high | 设计项目群/多项目治理架构；决定决策权上下分配；诊断"各组都好整体却差" | 大系统、治理、分层、项目群、分权、portfolio、governance | capabilities/large-system-decomposition.md |
