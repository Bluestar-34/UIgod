# Source observations

## Sources

创作源地址（用户提供）：[抖音灰度思维参考视频](https://www.douyin.com/jingxuan/search/%E7%81%B0%E5%BA%A6%E6%80%9D%E7%BB%B4?aid=bc2a1580-7c23-4f0b-8657-2eb472c8d99a&modal_id=7693969558939421994&type=general)。视频 ID：7693969558939421994。网页工具未能读取其内容，未下载、转写或核验作者；仅用于选题/文案来源追溯，不是本包视觉证据。

实际视觉母版仍是下列用户本地制作成片，不能把源抖音的图片自动当作审美参考。

用户作品：F:/Obsi-neuroBlue/08_创作/02-内容库/vibe知识大赏/灰度思维/project/
主视频 renders/灰度思维-发布版.mp4；同时参照 public/film.css、public/film.js、src/scenes.html、timing.json、制作记录.md。
ffprobe 实测：H264/AAC，1920×1080，30fps，125.266667 秒。库中不复制大型成片；为预览仅附一个必要字体及授权；下列关键帧从发布版重新提取，frames/index.json 含采样时间与源文件 SHA256。

## Capture Method

查看源 snapshots/v2/contact-sheet-1.jpg 与 contact-sheet-2.jpg 后，用 ffmpeg 从发布版抽取代表帧，核对实际渲染而不只读 CSS。时序、缓动与合成逻辑来自源码；未逐秒人工审片或听音。字体与配乐信息由源码和记录交叉提供。

## CSS Files

public/film.css 是实际风格主文件；index.html 是构建产物，避免把重复样式当另一套风格。public/film.js 提供时间线和程序图形，src/scenes.html 提供主体版式。这里只读与风格相关的源文件，未重建旧框架。

## Theme Detection

默认近黑底，选择/练习段落转暖白；结尾回黑。黑白对照服务内容，不是用户切换主题的 UI。

## Extracted Tokens

--ink #0b0b0b / --paper #efede8 / --acc #ff3d1f；g1–g4 #262626/#4d4d4d/#808080/#b3b3b3。Noto Sans SC 主字，Noto Serif SC 结尾，Bahnschrift 数字，Consolas 小标。字号 44px 字幕、190–300px 主题、440–560px 单字。安全布局 left130,width1660；grain .11。

## Signature Moves

2.3s 巨字“你”；8.6s 黑白对照；21.3s 方阵；30.9s 网点球+标题；44.3s 侧影与指针；57.2s 黑白卡片；70.6s 等待进度；96.9s 红色反转；121.8s 回收网点母题。代码以 8×8 Bayer 在 480×270 缓冲中实现二值光照，每帧确定性绘制；动画以行、词时刻驱动，expo.out / power4.out 等快停缓动。

## Extracted vs Inferred vs Synthesized

- 提取：以上色值、字族、字号、图层参数、时长、Bayer 缓冲与缓动。
- 推断：海报式版式与“文字判断+图形关系”的视觉语法，由多帧归纳。
- 用户偏好修订：删除 HUD、角标、英文小字、标尺、字幕装饰；新首帧不可纯白闪。
- 新设计：螃蟹/AI 迁移建议、朱红替代色、examples 的“看见的不是全部”选择偏差视觉样例。示例形体为示意，不是真实统计。
- 历史实现使用 HyperFrames，但这不属于可迁移要求，新制作明确禁止。

## Verification

验证状态与结果见 style.json 和 examples/verification.json。未验证声音与一分钟完整迁移，不声称制作质量已获用户认可。

## Final content

references/文案.md 为本地发布版 script.json 中的最终台词，不是本次从抖音转写的文本。examples/文案.md 对应十秒迁移样例；封面使用 examples/frame-0s.png。只保留最终样例和必要的原作关键帧，清理重复预览截图。
