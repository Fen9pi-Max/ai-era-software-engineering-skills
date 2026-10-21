---
name: mfq-analysis-views
description: |
  把被测对象拆成 M（单功能，建模深挖）/F（功能交互，高优先级探索性测试）/Q（质量属性，CRUSPICSTMPL 引导词专项）三维清单。当用户要系统性拆解测试对象、决定交互与质量属性怎么测时使用。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.mfqppdcs.mfq-analysis-views
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.pirate-testing-mfqppdcs
  cangjie.source-title: 海盗派测试分析MFQ&PPDCS
  cangjie.tags: test-analysis, mfq, decomposition
---
# MFQ 三维视角：M/F/Q 拆分与分类规则

## R（原文摘引）
> MFQ 的思路适用于任何我所遇到的被测系统……任何系统都是结构化的，每一个"整体"的被测对象都可以划分成多个"部分"。

## I（解释）
- **M（单功能）**：整体中可独立测试、承担一定功能的部分。M 是相对的：部分相对整体是 M，整体相对更大系统又是 F 的参与者。
- **F（功能交互）**：单功能间、特性/系统与其他特性/系统间的交互点，代表更复杂场景。场景无穷多，不遍历——选高优先级场景做探索性测试。
- **Q（质量属性）**：针对单功能或整体的非功能属性；引导词 CRUSPICSTMPL（HTSM 质量标准去掉 C）或 ISO9126。
**分类规则**：涉及两个及以上部分交互（时间/空间交互）或针对整体的功能性问题（What）→ F；关注"How 做得怎么样"（不论单功能还是整体）→ Q；独立功能点 → M。
**管理应用**：LLT（低级测试）粒度细多做 M；HLT（高级测试）多关注 F 和 Q。

## A1（原书案例）
亚马逊河图片练习：划分 7 个单功能（巨型睡莲、角蛙、河豚、金刚鹦鹉、巴西坚果、亚马逊河、地图）；"河豚与睡莲共生"类交互问题 → F；"河水流速如何"类 → Q。收银机："同时购买多种商品"复杂场景移入 F 做探索性测试。

## A2（情境应用）
分析任何被测系统时：
1. 先列 M 清单（可独立测试的部分，粒度可后拆合）；
2. 扫描两两交互点/端到端场景归 F，按 L×I 挑高优先级场景排探索性测试；
3. 过一遍 CRUSPICSTMPL 找适用的 Q 属性（结合用户痛点取舍）；
4. 输出三维清单 + 各维测试手段（M→建模；F→探索性 Session；Q→专项测试）。

## E（评测）
- 输入：一段系统功能描述（含 4 个功能点、2 处交互、2 处非功能要求）。
- 输出：M/F/Q 三维分类表。
- 通过标准：功能点全进 M、交互进 F、非功能进 Q；F 列出优先级排序依据。

## B（边界）
划分无唯一正确答案，粒度不适中可后续拆分合并；M 的深入建模见 modeling-workflow 与 ppdcs-model-selection；本卡解决"测什么维度"，不解决"怎么测"。
