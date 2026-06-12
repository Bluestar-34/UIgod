# UIgod

> 将网站设计风格转化为可复用的子技能包

UIgod 从参考网站中提取设计令牌（颜色、字体、形状、间距、交互模式）和内联插画资产，生成标准化的子技能包。每个子技能包含 `DESIGN.md`（设计系统）、`preview.html`（令牌标本）、可复用的代码片段和风格转移示例。

## 已测试的参考站

| 参考站 | 子技能 | 风格特征 | 预览 |
|--------|--------|---------|------|
| [studiobrot.de](https://studiobrot.de) | [studiobrot-playful-agency](skills/studiobrot-playful-agency/) | 德国创意广告 · 红粉交替 · 药丸按钮 · 按压动效 | [→ 示例](skills/studiobrot-playful-agency/examples/index.html) |
| [chiaraluzzana.com](https://chiaraluzzana.com) | [chiara-luzzana-sound-design](skills/chiara-luzzana-sound-design/) | 声音设计师作品集 · 深色极简 · vw极端排版 · 紫灰强调 | [→ 示例](skills/chiara-luzzana-sound-design/examples/index.html) |
| [dodonut.com](https://dodonut.com) | [dodonut-sustainable-design](skills/dodonut-sustainable-design/) | 可持续设计工作室 · 黑底黄绿紫 · 硬阴影 · 装饰圆 | [→ 示例](skills/dodonut-sustainable-design/examples/index.html) |
| [react.gg](https://react.gg) | [react-gg-learning-platform](skills/react-gg-learning-platform/) | 交互式学习平台 · 煤黑底网格纹理 · 暖米色文字 · 食物主题SVG插画 | [→ 示例](skills/react-gg-learning-platform/examples/index.html) |

## 子技能结构

```
child-skill/
├── DESIGN.md           # 设计系统 — 颜色/字体/形状/组件/do-don't
├── SKILL.md            # 代理指令 — 何时用、保留什么
├── README.md           # 人类可读摘要
├── preview.html        # 令牌标本 — 色板/字体/形状
├── references/
│   ├── source-observations.md        # CSS提取记录
│   ├── source-screenshots-or-notes/  # 参考截图
│   └── code-patterns/                # 可复用代码片段
└── examples/
    └── index.html      # 风格转移验证示例
```

## 文档

- [SKILL.md](SKILL.md) — UIgod 元技能操作指令
- [docs/REFERENCE-ANALYSIS-GUIDE.md](docs/REFERENCE-ANALYSIS-GUIDE.md) — CSS 提取规范
- [docs/CHILD-SKILL-SKELETON.md](docs/CHILD-SKILL-SKELETON.md) — 子技能骨架标准
- [docs/QUALITY-CHECKLIST.md](docs/QUALITY-CHECKLIST.md) — 质量检查清单
- [docs/DECISIONS.md](docs/DECISIONS.md) — 产品决策与经验记录
