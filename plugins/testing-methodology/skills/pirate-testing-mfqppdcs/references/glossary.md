# 术语表（Glossary）

| 术语 | 定义 |
|---|---|
| MFQ | 测试分析三维视角：M 单功能测试、F 功能交互测试、Q 质量属性测试。 |
| PPDCS | 五种建模特征：P-Process 流程、P-Parameter 参数、D-Data 数据、C-Combination 组合、S-State 状态。 |
| KYM（Know Your Mission） | 测试前通过不断问问题了解上下文、明确测试目标的启发式方法。 |
| CIDTESTD | KYM 的 8 个引导词：Customers/Information/Deliverables/Test Item/Equipment & Tools/Schedule/Test Team/Developer Relations。 |
| TCO（Testing Coverage Outline） | 测试覆盖大纲：从测试角度定义需求的信息重组产物（思维导图）。 |
| Curation and Subtraction | TCO 的过滤与剔除启发式：提取有价值信息、剔除无需关注的。 |
| SFDIPOT | HTSM 产品元素引导词（Structure/Function/Data/Interfaces/Platform/Operations/Time），可作 TCO 一级节点。 |
| CRUSPICSTMPL | HTSM 质量属性引导词（Q 分析用，去掉 C）。 |
| M（单功能） | 被测对象整体中可单独测试、承担一定功能的部分。 |
| F（功能交互） | 单功能间/系统间交互点；场景无穷，选高优先级做探索性测试。 |
| Q（质量属性） | 针对单功能或整体的非功能质量属性。 |
| M1/M2 | 收银机例的两个单功能：输入数据处理（D 主导）/业务规则处理（P 主导）。 |
| TSP Heuristic | 描述单功能三段式：Topic 主题 + Scope 范围 + Purpose 目的。 |
| TEST Heuristics | 选 PPDCS 特征的方法：Take notes/Essentials/Spanning Differences/Targets。 |
| Triggers（触发词） | 逻辑倾听需求：名字→Data；名字+动作→Rules/States；事件序列→Sequence。 |
| TCon（Test Condition） | 测试条件：测试分析输出，粗线条场景；判定表每行规则=1个 TCon。 |
| Te（Test example） | 测试实例：测试设计输出，变量取值具体确定，可直接执行。 |
| Given-When-Then | TCon 三段式描述：预置状态/触发动作/预期反应+状态变化。 |
| MF/AF | 主流程 Main Flow / 可选（异常）流程 Alternative Flow。 |
| VEC/IVEC | 有效/无效等价类（编号 A-V-1、B-IV-4 式）。 |
| 四种覆盖 | Weak/Strong × Normal/Robust：等价类覆盖的四种方式，按风险选择。 |
| Test Oracle | 帮助识别问题的启发式原则或机制（识别问题≠必然是bug）。 |
| Heuristics | 可能出错但大多数时候有帮助的实用求解法；应用而非盲从。 |
| TS-TA-TE 反馈环 | 测试策略-测试分析-测试执行的循环；测试人员处于核心。 |
| RBT | 基于风险的测试；风险=可能性 L × 影响 I。 |
| Fast TAD | 探索性测试中快速交错运用 KYM/TCO/TD 等技能的快速测试分析与设计。 |
| 测试广度/深度 | 覆盖测试点的数量 vs 对单点深入程度；深度图可视化；深化手段：Replicate/Maximize/Isolate/Generalize/Externalize。 |
| BOT/IOT | 面向业务的测试（MFQ&PPDCS 属此）/ 面向实现的测试。 |
| LLT/HLT | 低级别测试（多做 M）/ 高级别测试（多关注 F 和 Q）。 |
| Tests ≠ Testing | Tests 是写成文字的认知与猜测；Testing 需接触真实被测对象挖掘未知。 |
| PICT | 微软 Pairwise 组合测试工具：`pict ModelFile.txt > out.xls`。 |
