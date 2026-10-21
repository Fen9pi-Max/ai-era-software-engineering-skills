# 压力测试结果 — cybernetic-project-management (single, v1.0.0)

日期: 2026-09-25 ｜ 方式: 独立 sub-agent 盲测（未参与蒸馏）＋ 实际输出评测

## 一、触发精度盲测（10 用例）

| 用例 | 类型 | 预期 | 盲测结果 | 判定 |
|---|---|---|---|---|
| should-trigger-01 (Q2) | should_trigger | stability-health-check | 命中，动作符合（回路判定+裕度） | ✅ |
| should-trigger-02 (Q4) | should_trigger | multi-objective-tradeoff | 命中，明确拒绝合成打分公式 | ✅ |
| should-trigger-03 (Q7) | should_trigger | noise-filtering-estimation | 命中，噪声底+2 倍阈值动作正确 | ✅ |
| should-trigger-04 (Q6) | should_trigger | time-optimal-switching | 命中，切换时机+收手标准 | ✅ |
| should-trigger-05 (Q9) | should_trigger | decoupling-coordination | 命中，先判耦合强度再定拆分 | ✅ |
| should-not-trigger-01 (Q1) | 诱饵:工具脚本 | 不触发 | 不触发 | ✅ |
| should-not-trigger-02 (Q5) | 诱饵:个人效能 | 不触发 | 不触发 | ✅ |
| should-not-trigger-03 (Q8) | 诱饵:战略方向 | 不触发 | 不触发 | ✅ |
| edge-01 (Q10) | edge_case | 拒绝加总分，走 stability/multi-objective 之一 | 触发且拒绝加总，选 multi-objective-tradeoff（预期对内），补读 large-system | ✅（卡序偏差，安全属性达成） |
| edge-02 (Q3) | edge_case | delay-compensation 或 adaptive-self-stabilization | 选 adaptive-self-stabilization，动作含"见效延迟不凭单周撤回+方向性检验" | ✅ |

**汇总**: 触发判定 10/10；诱饵拦截 3/3（0 误触发）；卡路由精确 9/10，1 条为预期对内可接受选择。

## 二、实际输出评测（2 代表任务）

### 任务 A（正常场景: stability-health-check E 段）
输入: 5 周缺陷/修复/缓冲/范围/人员数据。
机械核对:
- 积压净增 2+7+15+24+32=80 ✅（复算一致）
- 修复/新增比 0.94→0.82→0.67→0.54→0.45 ✅（逐项复算一致）
- 判定红 + 回路闭环句清单 + 裕度表 + 结构性切断建议 ✅ 输出契约四件齐
- 发散即止纪律 ✅（明示跳过第 4 步乐观评估）
- "加大力度"识别为方向错误 ✅ 符合 B 段
结论: **通过**

### 任务 B（缺输入场景: model-approximation-identification 判停）
输入: 无历史无结构的新项目估算请求。
核对:
- 判停触发 ✅ 输出"不可估"，拒绝给出任何数字（含保守区间）
- 辨识三法逐项检查表 ✅
- 转介 extremum-seeking-iteration ✅ 符合 B 段出口
- 补齐路径（探针/交叉校验/输入契约）✅
- 加载纪律 ✅（每任务 1 卡，未多读）
结论: **通过**

## 三、结论

阶段 4 通过，无需回炉。Q10 的卡序偏差记录为已知行为（两卡均在预期对内且安全属性达成），不构成修复理由。
