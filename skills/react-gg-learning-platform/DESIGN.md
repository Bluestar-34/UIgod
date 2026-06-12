---
version: alpha
name: react-gg-learning-platform
description: "交互式学习平台深色主题：煤黑(#0f0d0e)背景+炭色网格纹理、暖米色(#f9f4da)文字、金黄油(#fcba28)主强调、Paytone One大写展示字+Outfit正文、药丸按钮+薄阴影、页面外框、多彩辅助色(粉/绿/蓝/橙/红/紫)。Interactive learning platform dark theme: coal bg with grid texture, warm beige text, golden yellow accent, Paytone One display + Outfit body, pill buttons, page border frame, multiple vibrant secondaries."

colors:
  canvas: "#0f0d0e"
  canvas-secondary: "#231f20"
  ink: "#f9f4da"
  accent-yellow: "#fcba28"
  accent-pink: "#f38ba3"
  accent-green: "#0ba95b"
  accent-blue: "#12b5e5"
  accent-orange: "#fc7428"
  accent-red: "#ed203d"
  accent-purple: "#7b5ea7"

typography:
  display:
    fontFamily: "\"Paytone One\", Outfit, -apple-system, sans-serif"
    fontSize: "clamp(2rem, 8vw, 4rem)"
    fontWeight: 400
    lineHeight: 1.2
    textTransform: uppercase
  headline:
    fontFamily: "\"Paytone One\", Outfit, -apple-system, sans-serif"
    fontSize: "clamp(1.6rem, 4vw, 2.1rem)"
    fontWeight: 400
    lineHeight: 1.2
    textTransform: uppercase
  body:
    fontFamily: "Outfit, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: "clamp(1.2rem, 2.5vw, 1.5rem)"
    fontWeight: 400
    lineHeight: 1.4
  mono:
    fontFamily: "\"Fira Code\", ui-monospace, monospace"
    fontSize: "16px"
    fontWeight: 400

rounded:
  pill: "9999px"
  card: "6px"
  review: "15px"
  small: "4px"
  toggle: "0.5em"

border:
  dark: "0.12rem solid #231f20"
  light: "0.07rem solid rgba(249,244,218,0.5)"
  body: "1.3rem solid #231f20"

shadow:
  button: "2px 2px 0 #231f20"
  focus: "0 0 0 0.2rem #12b5e5, 0 0 0 0.27rem #f9f4da"
---

## Overview

react.gg 是一个交互式 React 学习平台。深色煤黑背景上叠加炭色网格纹理，暖米色文字（非纯白！），金黄油作为主强调色。Paytone One 大写展示字体给标题带来独特的个性。整个页面被物理边框包围，营造"画框"感。多彩的辅助色用于 review 卡片、课程模块、定价层级。

默认页面类型：交互式学习平台首页。

## Colors

| 令牌 | 值 | 用途 |
|------|-----|------|
| canvas | #0f0d0e | 煤黑主背景 |
| canvas-secondary | #231f20 | 炭色次背景（卡片、边框） |
| ink | #f9f4da | 暖米色文字（非纯白！） |
| accent-yellow | #fcba28 | 金黄主强调 — 链接、按钮、活跃态 |
| accent-pink | #f38ba3 | 粉色 — review 卡片、价格 header |
| accent-green | #0ba95b | 绿色 — 成功态、review 卡片 |
| accent-blue | #12b5e5 | 蓝青 — 焦点环、交互反馈 |
| accent-orange | #fc7428 | 橙色 — review 卡片 |
| accent-red | #ed203d | 红色 — review 卡片 |
| accent-purple | #7b5ea7 | 紫色 — review 卡片、FAQ 分隔线 |

### 颜色轮换系统（Review 卡片）
每 6 张卡片一组：
1: 绿名+黄引用 | 2: 粉名+红引用 | 3: 紫名+绿引用 | 4: 蓝名+粉引用 | 5: 橙名+蓝引用 | 6: 红名+紫引用

## Typography

| 角色 | 字体 | 特征 |
|------|------|------|
| 标题 | Paytone One | 大写、400w、粗重展示 |
| 正文 | Outfit | 可变字重(400/500/700/900)、温暖现代 |
| 代码 | Fira Code | 等宽、连字支持 |

标题全部大写。链接 hover 时反转：黄底+黑字。

## Layout

```
[Page Frame] — 1.3rem 炭色边框包围整页
├─ [Nav]
├─ [Hero] — flex row-reverse, 交互式代码预览
├─ [Logo Strip] — 合作方/学生公司 logo
├─ [Reviews] — 3列测评卡片（多色轮换）
├─ [Story] — "Learning React Sucks" 说服段落
├─ [Course Sections 01-10] — 课程模块展示
├─ [Pricing Tiers] — 定价卡片（flex 布局）
│   ├─ Starter (基础)
│   ├─ Full (完整) — 高亮
│   └─ Expansion Pack (年度)
├─ [FAQ] — 折叠面板
├─ [Footer]
└─ [Frame End]
```

## Shapes

- **药丸按钮** (9999px) + 薄阴影 (2px 2px 0)
- **页面外框** — body 本身有 1.3rem 炭色 border
- **卡片** — 6px 圆角 + 浅边
- **Review 卡片** — 15px 外层圆角 + 内层圆角 = 层叠卡片效果
- **Toggle 开关** — 黄圆形标记
- **焦点环** — 双层 (蓝 + 米色)

## Components

**Button:** `border-radius:9999px` + `border:var(--border-dark)` + `box-shadow:2px 2px 0 var(--charcoal)` + `uppercase Outfit`。多种颜色变体(yellow/green/pink/outlined)。

**Link:** `color:yellow; text-decoration:underline`。Hover: `background:yellow; color:coal`（完整反转）。

**Review Card:** 15px 圆角外层，内层 grid 布局(avatar + name + quote)。每 6 张轮换配色。

**Pricing Tier:** flex 布局，中间层级高亮（绿色/蓝色 header），带负 margin 重叠效果。

**Course Outline:** 编号圆圈 + 标题 + 标签。圆形计数器带阴影。

**FAQ:** `<details>` 折叠面板，"+" → "−" 切换，紫色分隔线。

## Do's and Don'ts

✅ 煤黑底(#0f0d0e) + 网格纹理 · 暖米色文字(#f9f4da) · 金色强调(#fcba28) · Paytone One 大写标题 · 药丸按钮 · 页面外框 · 多彩辅助色轮换
❌ 不用纯白文字 · 不用单色设计 · 不用直角按钮 · 不用无衬线展示 · 不要忘记页面边框

## Responsive

- 页面外框随屏幕缩小：1.3rem → 0.7rem (≤700px)
- Hero 在窄屏时变为 column + 居中
- Pricing tiers 在窄屏时变为 column 堆叠
- Review 列数：1 (mobile) → 2 (≥700px) → 3 (≥1350px)

## Known Gaps

Paytone One 和 Outfit 是自定义字体，替代：Outfit → Inter/Manrope；Paytone One → Oswald/Bebas Neue。网格纹理和交互式代码编辑器无法纯 CSS 完美复现。
