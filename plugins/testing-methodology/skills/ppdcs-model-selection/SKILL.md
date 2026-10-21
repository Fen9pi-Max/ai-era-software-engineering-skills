---
name: ppdcs-model-selection
description: |
  按五种特征（P流程/P参数/D数据/C组合/S状态）与触发词语规则，用 TEST Heuristics 为单功能选定建模技术。当用户不确定该用判定表、等价类、流程图、状态图还是组合法分析某个功能时使用。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.mfqppdcs.ppdcs-model-selection
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.pirate-testing-mfqppdcs
  cangjie.source-title: 海盗派测试分析MFQ&PPDCS
  cangjie.tags: test-design, ppdcs, model-selection
---
# PPDCS：建模特征选择（Triggers + TEST Heuristics）

## R（原文摘引）
> 当技术类别特征与单功能内部逻辑的主导特征吻合时，即可用该技术分析此单功能。

## I（解释）
五种特征 → 建模技术 → 测试条件：
| 特征 | 识别信号 | 建模技术 | TCon 来源 |
|---|---|---|---|
| P-Process 流程 | 多步骤、步骤间前后约束、多角色，基本不可逆 | 流程图（MF+AF） | 覆盖全路径；复杂时 1 MF + 重要 AF |
| P-Parameter 参数 | 参数组合构成规则 | 判定表/判定树/因果图 | 判定表每行规则 |
| D-Data 数据 | 数据有取值范围、数据间独立 | 等价类+边界值 | 四种覆盖方式 |
| C-Combination 组合 | 因子多状态多、组合爆炸 | 因子-状态表+Pairwise（PICT） | 生成的每条组合 |
| S-State 状态 | 多状态由事件触发、可逆转换 | 状态图（Moore 机） | 覆盖状态转换 |

**Triggers 触发词**（逻辑倾听需求）：听到名字（Names）→ Data；一串名字和动作 → Rules（Parameter）或 States；一系列事件（Sequence of Events）→ Process/State。通常先过滤掉 C（纯为减场景数，对分析业务逻辑无优势，最后才考虑）。

**TEST Heuristics**：
- **T**ake Notes 记录 Triggers 草稿（1-2 张 A4 纸够用）
- **E**ssentials 抓核心：蒸馏信息 + 忽略干扰（佣金问题例：电报月报等描述与计算无关，果断忽略）
- **S**panning Differences：举棋不定时分别用不同特征建模比对差异，可一主一辅
- **T**argets 围绕目标：用 TSP 描述单功能（Topic 主题 + Scope 范围 + Purpose 目的），避免边界混淆

## A1（原书案例）
收银机打印小票：M2 有商品类型/件数/两类优惠的参数组合规则 → P-Parameter 判定表；M1 围绕输入数据合法性 → D-Data 等价类。打印小票全组合 32 个场景 → Pairwise 压缩为 8 个。按摩椅：按键档位与状态切换 → S-State（7 个状态）。

## A2（情境应用）
对每个单功能：
1. 用 TSP 一句话描述（主题/范围/目的）；
2. 逻辑倾听需求文本，标注 Triggers（名词？名词+动作？事件序列？）；
3. 按 PPDCS 表选主导特征；多个特征并存时先用主导的，其他特征的想法作补充（Spanning Differences）；
4. 输出：特征选择结论 + 一句理由 + 即将使用的建模技术。

## E（评测）
- 输入：5 个单功能描述（分别植入流程/参数/数据/组合/状态的主导特征信号）。
- 输出：每个单功能的特征判定+理由+建模技术。
- 通过标准：5 个判定全部与植入信号吻合；理由引用了具体 Trigger。

## B（边界）
选型是启发式不是精确分类，允许一主多辅；选完后如何建模见 modeling-workflow；C-Combination 需工具（PICT）支持。
