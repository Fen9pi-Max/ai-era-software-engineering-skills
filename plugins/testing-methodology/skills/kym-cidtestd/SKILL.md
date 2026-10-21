---
name: kym-cidtestd
description: |
  用 CIDTESTD 八个引导词（用户/信息/交付件/测试项/设备工具/进度/团队/开发关系）调研测试任务，输出含风险与问题清单的 KYM 导图。当用户接手新测试任务、新项目或需求，要先明确测试目标与上下文时使用。
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.capability-id: cap.mfqppdcs.kym-cidtestd
  cangjie.capability-revision: 1
  cangjie.bundle-id: bundle.pirate-testing-mfqppdcs
  cangjie.source-title: 海盗派测试分析MFQ&PPDCS
  cangjie.tags: test-analysis, kym, context
---
# KYM：了解测试任务（CIDTESTD 引导词法）

## R（原文摘引）
> 比 How 更重要的，是先想清楚 Why 的问题，了解清楚任务本身以及任务的背景，明确最终要达到的目的……我把这种做法叫 Know Your Mission。

## I（解释）
测试=对被测系统问问题；资源有限，先明确任务再选方法。风险 = L（可能性，与开发过程相关，如新手模块）× I（影响，与用户痛点相关）。
用 CIDTESTD 八个引导词逐项提问收集信息（概括"用户、项目、任务"三方面）：
1. **Customers 用户**：产品是什么？用户是谁？痛点？最关心什么？
2. **Information 信息**：关键信息/文档？全新还是改型？历史问题？向谁追问？
3. **Deliverables 交付件**：需要什么测试交付物？模板？时间要求？
4. **Test Item 测试项**：主要测什么？哪些降级/不测？哪些新增/修改？
5. **Equipment & Tools 设备工具**：环境/工具/自动化脚本？可测试性？
6. **Schedule 进度**：何时交付？周期多长？最早何时拿到可测版本？
7. **Test Team 团队**：人员/经验/熟悉度/稳定度？
8. **Developer Relations 开发关系**：谁开发？敏捷还是瀑布？复杂在哪？开发做过什么测试？
可配批判式三问：Huh?（真理解了吗）Really?（有证据吗）So?（与我何干、下一步）。
反模式：强制模板化、重导图轻过程、陷入需求细节。15 分钟～2 小时，越早越好、贯穿始终。

## A1（原书案例）
小 D 原计划 4 天中花 2 天读文档；改为 0.5h 画 KYM + 0.5h 画 TCO 后直接进入 2 小时探索 Session，学习时间压缩到半天。KYM 导图记录了客户、交付时间、测试环境、2天测试时间、已发现 4 个 bug、2 个风险点。

## A2（情境应用）
接到新测试任务（新项目/新需求/新模块/接手他人任务）时：
1. 按八个引导词各写 1–3 个问题，向需求方/开发/文档要答案；
2. 未知处标记问号并指定追问对象；
3. 输出一页 KYM 导图：Mission（目标）、关键约束（时间/环境/团队）、已知风险 L×I、问题清单；
4. 以此决定后续投入：先 TCO 还是直接探索。

## E（评测）
- 输入：一段项目背景自述（产品、团队、时间、痛点信息分散埋设）。
- 输出：KYM 导图（含 8 个引导词分支与问题清单、至少 2 个 L×I 风险项）。
- 通过标准：8 分支齐全；测试目标可复述；识别出信息缺口与追问对象。

## B（边界）
KYM 是启发式不是流程步骤，可跳过细节抓主干；与 TCO 顺序由上下文决定；不产出测试用例（见 modeling-workflow）。
