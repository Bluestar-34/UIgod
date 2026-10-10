# 视频风格收录合同

文件取舍统一遵守 [作品与风格包标准](WORK-CONTRACT.md)，本合同只补充视频特有要求。

沿用 skills/style-manager/styles/<style-id>/；网页仍使用 CONTRACT.md，不强迫视频实现网页组件。

## 必需文件

- SKILL.md：触发、读取顺序、保留与可变项。
- DESIGN.md：视觉与运动主规则，包含 5–8 个可识别特征、角色化令牌、版式、主体、材质、动效、节奏、字幕与声音、变量、反例、Prompt Guide、Known Gaps。
- references/source-observations.md：来源、版本、采样时间、源码依据、提取/推断/修订区分。标明静态截图无法验证的内容。
- references/frames/：来自真实成片的代表性关键帧与时间索引。
- references/code-patterns/：可选，只放真实可重复使用的代码机制；不强制空目录或单独说明文件。
- deliverables.preview 指定文件：本地可查看的作品展示或动效样本，静帧必须标注用途，不冒充动画。
- examples/index.html：换主题的迁移样例。已导出时可附 transfer.mp4；验证样例不冒充用户批准的正式片。
- style.json：id、media、aliases、tags、sources、deliverables、可改变量、证据与验证状态。
- references/文案.md 与 examples/文案.md：原作品已提供的最终制作文案和当前样例文案，明确用途。

## 实际工作

先查看成片采样与源码，提炼规则再做新主题样例。视频必须记录时序、节拍及语义锚点，不能只写色板。技术实现是证据，不是强制框架。

catalog.json 为生成检索目录。权威元数据来自 style.json、collections 和 editorial.json；分类与排序遵守库根 docs/LIBRARY-RULES.md。别名可含原项目名，但主题相关性不能代替风格匹配。

## 验证与状态

draft = 只有文字或尚未检查；sample-verified = 新主题样例已视觉检查及真实导出；production-verified = 新主题正式片经用户确认且全片检查完成。结构校验本身不提升状态。

验证本地预览、横竖屏布局或缩放、随机时间跳转、字体加载与导出解码。至少展示五个特征，说明哪些未验证（例如配音、音乐或完整一分钟迁移）。用 skills/uigod/tools/validate_video_style.py 校验结构。不要承诺一条提示词必然等效，先以首帧及短动态核对。
