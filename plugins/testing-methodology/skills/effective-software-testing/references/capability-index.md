# 能力索引（完整版）

| capability_id | 标题 | 重要度 | 意图 | 关键词 | 能力卡 |
|---|---|---|---|---|---|
| requirements-testability-review | 需求可测试性审查与优先级 | critical | 审查需求文档的可测试性与质量属性；为需求排优先级并治理变更 | 需求审查、可测试性、质量测度标准、CCB、优先级打分 | capabilities/requirements-testability-review.md |
| test-effort-estimation | 测试工作量估计四法 | high | 估计新项目测试工作量与人员规模 | 工作量估计、测试计划、人员比例、人小时 | capabilities/test-effort-estimation.md |
| test-data-design | 测试数据设计（深度·宽度·范围·完整性·条件） | high | 为功能或性能测试设计数据集；把硬编码数据外置为数据驱动表 | 测试数据、边界值、数据驱动、数据字典 | capabilities/test-data-design.md |
| test-design-techniques | 测试设计技术组合（五法+辐射分析+探索性） | critical | 从需求设计测试用例集；压缩参数组合爆炸；判断哪些场景值得自动化 | 等价类、边界值、正交排列、辐射分析、自动化候选 | capabilities/test-design-techniques.md |
| unit-test-practices | 实用单元测试（分层·先写·接入生成） | high | 组织分层单元测试并接入 CI；用存根支持测试先行 | 单元测试、存根、基于接口、每日构建 | capabilities/unit-test-practices.md |
| automation-expectations-and-tool-selection | 自动化期望纠偏与工具选择 | critical | 引入测试自动化工具前对齐期望与选型；决定购买还是自制测试工具 | 工具选型、自动化期望、原型验证、自制工具 | capabilities/automation-expectations-and-tool-selection.md |
| script-engineering | 自动化脚本工程五技术 | critical | 重构脆弱的录制回放脚本；建立可维护的自动化脚本工程规范；用适配器直测核心组件并比对新旧系统 | 脚本工程、数据驱动、GUI Map、适配器、版本控制 | capabilities/script-engineering.md |
| regression-smoke-pipeline | 回归·烟雾·自动生成流水线 | critical | 搭建 CI 测试流水线与准入门禁；选择回归测试范围并持续优化套件 | 烟雾测试、回归测试、冲击矩阵、CI、入口标准 | capabilities/regression-smoke-pipeline.md |
| nonfunctional-testing | 非功能测试框架（性能·并发·安全·兼容） | high | 规划性能/并发/安全/兼容性测试；从需求阶段挖出非功能需求 | 性能测试、并发模型、安全测试、兼容性矩阵 | capabilities/nonfunctional-testing.md |
| defect-lifecycle-metrics | 缺陷生命周期与测试执行度量 | high | 建立或审计缺陷流程；用度量判断测试收尾与修正质量 | 缺陷流程、优先级、出口标准、缺陷趋势、重现率 | capabilities/defect-lifecycle-metrics.md |
