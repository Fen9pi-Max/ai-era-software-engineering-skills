# 覆盖审计 — engineering-cybernetics

原书关键任务清单（BOOK_OVERVIEW T1–T15）→ 候选 → 判定 → 交付去向。

| 任务 | 候选来源 | 判定 | 交付去向 |
|---|---|---|---|
| T1 项目失控判定 | p01,f04,p10,f14,ce05 | verified | cap01（cap10/cap12 辅） |
| T2 多指标权衡 | p02,p03,p04,f03,p09,p24,f20,ce01,ce06,ce18 | verified | cap02 |
| T3 反馈回路设计 | f11(部分),p16(部分),f13,p26,p17 | verified | cap03（cap07 辅） |
| T4 模型化与工程近似 | f01,p05,f09,ce02 | verified | cap04 + cap06 |
| T5 数据辨识建模 | f02,p07,p27(外模型),ce03,ce04 | verified | cap04（cap13 用外模型思想） |
| T6 噪声状态估计 | f10,p23,ce10,c15 | verified | cap05 |
| T7 未知对象寻优 | f11,f12,p16,p17,p18,ce11,ce12,c03,c04 | verified | cap07 |
| T8 多变量解耦协调 | f05,p11,f06,p12,ce07,c02 | verified | cap09 |
| T9 时滞补偿 | f08,p25,ce09 | verified | cap08 |
| T10 灵敏度/偏差管理 | f04,p10,f09,c09,p08 | verified | cap06（cap01 裕度） |
| T11 冗余容错 | f17,p22,ce15,c07,c08 | verified | cap11 |
| T12 环境剧变自适应 | f14,f15,f16,p19,p20,p21,c05,c06,ce13,ce14 | verified | cap12 |
| T13 大系统分解协调 | f18,f19,f06(部分),p27,ce16,ce17,c11,c12,c14 | verified | cap13（cap09 辅） |
| T14 离散节拍控制 | f13,p26,c12 | verified | cap03 |
| T15 最速/资源切换 | f07,p13,p14,p15,p08,ce08 | verified | cap10 |

**结论**: 15/15 关键任务全部有 verified 候选与明确交付去向，无未解释遗漏。

## 参考材料去向

- glossary 39 条 → `GLOSSARY.md` + Bundle `book/glossary.md`
- 历史起源案例 c01、数学推导细节（D-划分作图法、极大值原理证明、李雅普诺夫函数构造、谱分析）→ Bundle `book/overview.md` 参考区
- c08 复合冗余数值推算细节 → cap11 A1 概述，完整演算为参考
