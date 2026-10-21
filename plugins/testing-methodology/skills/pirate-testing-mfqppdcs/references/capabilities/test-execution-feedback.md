# 测试执行：反馈环、广度深度与 Fast TAD

## R（原文摘引）
> 主动收集信息；尽早提供反馈；及时调整策略；基于风险测试。（海盗派四条核心原则）

## I（解释）
**TS-TA-TE 反馈环**：TA（分析）变无限为有限；TS（策略）基于风险 RBT 始终最重要；TE（执行）接触真实对象、验证分析、收集信息反馈回 TA/TS。测试人员（知识+技能+协作）处于核心。
**更早更快更频繁**：更早（尽早分析/了解需求/各级反馈：代码/接口/Story/特性/系统级）；更快（探索性测试中上一个测试立即为下一个提供反馈）；更频繁（持续集成、风险与策略调整更频繁）。
**测试广度/深度**：广度=覆盖测试点数；深度=对单点深入层级；深度图可视化（横轴覆盖点，纵轴层级）。深化五手段（源自 Kaner）：Replicate 复现 / Maximize 扩大影响 / Isolate 隔离最小化 / Generalize 证明普遍性 / Externalize 外在影响。easy bug 广度深度 1 即发现；广度深度不可兼得，基于风险取舍。
**拿着 TCon/Te 执行不保证发现 bug** 的三原因：①分析遗漏 ②执行深度不够 ③缺面向实现的测试 IOT（MFQ&PPDCS 属面向业务的 BOT）→ **Tests ≠ Testing**。
**Fast TAD**：高效探索性 Session 中快速交错运用 KYM/TCO/Try/TA/TS/TD/Observe/Communicate/Take Notes/Alternate/Self-Manage/Debrief。

## A1（原书案例）
Word2007 插入页码：多人各 1 小时探索对比记录，引出广度/深度与 easy bug；智慧金字塔 Session：解题过程即 Fast TAD 演示。

## A2（情境应用）
规划测试执行或复盘 Session 时：按四原则检查（信息收集了吗？反馈及时吗？策略调整了吗？风险驱动吗？）；用深度图评估 Session 质量（广度太散或深度不足均调整）；每个 bug 追问"对应 TCon 吗？此前分析能发现吗？"反哺分析。

## E（评测）
输入：一份探索性测试记录（含浅尝辄止与深挖复现两类行为）；输出：广度深度标注+深度图+改进建议。通过标准：正确区分广度点与深度层；建议含五手段中至少两种。

## B（边界）
执行技能无法纸面替代；分析侧输入见 modeling-workflow/test-design-4steps；自动化回归另见 automation-testing-best-practices 包。
