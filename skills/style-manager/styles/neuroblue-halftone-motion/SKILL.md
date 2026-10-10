---
name: neuroblue-halftone-motion
description: 灰度思维母版的网点海报动态风格，用于认知、心理与技术知识动画。保留满版黑体、黑白场切换、单色信号与抖动网点主体，可换主题及配色。
---
# 网点海报动态 · 灰度思维母版

先读 DESIGN.md，再查看 showcase.html 中的 v2 原作画面与 references/frames/contact-sheet.jpg。需要精确来源时读 references/source-observations.md；examples/index.html 是迁移样例，不能当成原作。

保留：大字与单一主体的层级、网点成形、强黑白明暗关系、语义触发的动作、快入场后稳定阅读。可变：强调色、主体轮廓、文案、画幅、场景数和实现工具。

默认不复用原片 HUD、裁切角、底部标尺、英文小字及字幕红边。主题“灰度思维”不进入新片；不复用原 37 行索引与 125 秒时序；不使用原 HyperFrames 配置。声音使用生产工作流的默认配置，风格包不代替完整视频生产工具。

用户只说“参考灰度思维”时默认忠实迁移设计语言并去除装饰；用户要求换色换主体时，按 DESIGN.md 的变量边界改。新首帧必须有视觉焦点，不复制原作白闪起帧。制作声音、时长、工具及首帧确认方式读取工作区与库根 preferences.local.json。
