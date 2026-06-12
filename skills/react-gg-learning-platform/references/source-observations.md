# Source Observations — react.gg
## Reference
URL: https://react.gg/ | 交互式 React 学习平台 | Astro + Tailwind v4

## CSS Extraction
Source: `/_astro/_404_.DvZe5c57.css` (22589 bytes — 最大文件，完整的 `:root` 定义 + Tailwind + 组件样式)
Supporting: `/_astro/index.BnP43qHa.css` (10773 bytes — 页面组件样式)

### 主题检测
单主题（深色）— 无 `.light`/`.dark` 类。Body 直接使用 `background-color: var(--coal)`。
```css
body {
  background-color: var(--coal);        /* #0f0d0e */
  background-image: repeating-linear-gradient(to right, ...), repeating-linear-gradient(to bottom, ...); /* 炭色网格纹理 */
  border: var(--body-border) solid var(--charcoal); /* 页面外框 */
}
```

### CSS 变量链追踪
```
:root {
  --brand-coal: #0f0d0e;     → --coal = var(--brand-coal) = #0f0d0e (主背景)
  --brand-charcoal: #231f20;  → --charcoal = var(--brand-charcoal) = #231f20 (次背景)
  --brand-yellow: #fcba28;    → --yellow = var(--brand-yellow) = #fcba28 (主强调)
  --brand-beige: #f9f4da;    → --white = var(--brand-beige) = #f9f4da (文字色!)
  --brand-pink: #f38ba3;     → --pink
  --brand-green: #0ba95b;    → --green
  --brand-blue: #12b5e5;     → --blue
  --brand-orange: #fc7428;   → --orange
  --brand-red: #ed203d;      → --red
  --brand-purple: #7b5ea7;   → --purple
  --brand-gray: #262522;     → --gray
}
```

### 字体
| 用途 | font-family | 字重 | 来源 |
|------|-------------|------|------|
| 标题/展示 | `Paytone One, Outfit, sans-serif` | 400 | @font-face /woff2 |
| 正文 | `Outfit, -apple-system, BlinkMacSystemFont, ...` | 400/500/700/900 | @font-face /woff2 |
| 代码 | `Fira Code` | 400 | @font-face /woff2 |

### 排版
| 用途 | 值 |
|------|-----|
| h1 | `clamp(2rem, 8vw, 4rem)` PaytoneOne, uppercase |
| h2 | `clamp(1.6rem, 4vw, 2.1rem)` PaytoneOne, uppercase |
| h3 | `clamp(1.2rem, 2.5vw, 1.5rem)` PaytoneOne, uppercase |
| body | `clamp(1.2rem, 2.5vw, 1.5rem)` Outfit, line-height 1.4 |
| small | `clamp(.8rem, 2vw, 1rem)` |

### 形状
| 元素 | border-radius | border | box-shadow |
|------|---------------|--------|------------|
| 按钮 | 9999px (pill) | .12rem solid var(--charcoal) | 2px 2px 0 var(--charcoal) |
| 卡片 | 6px | var(--border-light) | — |
| Review 卡片 | 15px (外层) | var(--border-dark) | — |
| Page body | — | 1.3rem solid var(--charcoal) | — |
| 焦点环 | — | — | 0 0 0 .2rem var(--blue), 0 0 0 .27rem var(--white) |

### 链接交互
```css
a { color: var(--yellow); text-decoration: underline; }
a:not(.logo):hover { background-color: var(--yellow); color: var(--coal); }
```
链接悬停时变成黄底黑字 — 高对比度的反转效果。

### 装饰元素
- Body 带 repeating-linear-gradient 网格纹理
- 页面外框 (--body-border)
- review 卡片每 6 个一组循环不同配色
- 圆形计数器 (course outline li::before)
- 价格切换 toggle switch 带黄圆标记

### 独特性
- **暖米色文字** (非纯白!)
- 页面有**物理边框/画框感**
- **Paytone One** 大写展示字
- 链接 hover 反转（黄底黑字）
- **黄(#fcba28)为主强调色**
