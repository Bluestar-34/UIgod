# UIgod

> Agent-invoked website style extraction skill.
>
> 可由 AI agent 自动识别并调用的网站风格抽取 skill。

[中文](#中文) | [English](#english)

---

## 中文

UIgod 本身应该作为一个 Codex skill 被 agent 自动识别和调用，而不是作为需要人工逐步操作的工具箱。

当用户给出网站 URL、截图、HTML/CSS 或风格 brief，并表达“测试网站、抽取风格、生成 skill 包、生成参考站、迁移网站风格、写 DESIGN.md”等意图时，agent 应自动触发 UIgod，完成证据抓取、风格提炼、子 skill 打包和验证。

核心产物不是一次性网页，而是：

```text
skills/<child-skill-name>/DESIGN.md
```

它是未来 agent 复用该网站风格的主要依据。

### Agent 如何触发

安装为 Codex skill 后，UIgod 依靠 `SKILL.md` frontmatter 中的 `description` 被自动匹配。

典型触发请求：

- `测试 https://example.com/，生成 skill 包和参考站`
- `抽取这个网站的风格，做成可复用子 skill`
- `根据这些截图生成 DESIGN.md`
- `把这个 landing page 的视觉语言迁移成一个 agent 可用的风格包`
- `create a reusable child skill from this website style`
- `extract this site's visual system and build a reference example`

用户不需要手动运行 `tools/` 下的脚本。脚本是给 agent 在 skill 执行过程中自动调用的。

### Agent 执行流程

UIgod 的自动协议是：

```text
Scope -> Capture -> Extract -> Distill -> Package -> Verify
```

- **Scope**：确认参考来源、子 skill 名称、默认页面类型、不可迁移资产。
- **Capture**：抓取 HTML、全部 linked CSS、截图和证据。
- **Extract**：生成 `references/source-observations.md`，记录字体、颜色、变量、布局、组件、动效和不确定性。
- **Distill**：生成 `DESIGN.md`，把证据提炼成可执行的设计系统。
- **Package**：生成子 skill 的 `SKILL.md`、`preview.html`、`examples/index.html` 和必要代码片段。
- **Verify**：运行结构验证，检查桌面/移动视觉效果，确保示例迁移风格而不是复制原站。

### Skill 目录

```text
UIgod/
├── SKILL.md                         # agent 自动触发与执行协议
├── agents/
│   └── openai.yaml                  # UI 展示与隐式调用元数据
├── docs/
│   ├── CONTRACT.md                  # 子 skill 输出契约
│   └── REFERENCE-ANALYSIS-GUIDE.md  # 证据抽取细则
├── tools/
│   ├── extract_style_evidence.py    # agent 调用的 HTML/CSS 证据抽取器
│   └── validate_child_skill.py      # agent 调用的子 skill 验证器
├── inputs/                          # 抓取证据、截图和临时输入
└── skills/                          # 生成的 web-style 子 skill
```

### 子 Skill 输出结构

UIgod 生成的子 skill 应保持精简：

```text
skills/<child-skill-name>/
├── SKILL.md
├── DESIGN.md
├── preview.html
├── references/
│   ├── source-observations.md
│   └── code-patterns/
└── examples/
    └── index.html
```

`DESIGN.md` 是主脑；不要把子 skill 变成冗余文档合集。

### 质量标准

一个子 skill 可用前，agent 必须确认：

- URL 输入已抓取 HTML 和全部 linked CSS。
- 主 CSS、默认主题、变量解析和不确定性已记录。
- `DESIGN.md` 有 5-8 个可识别的 signature moves。
- token 按角色解释，而不是只列色值。
- `examples/index.html` 使用全新内容和信息架构。
- 没有复制原站 logo、截图、文案、专有图片或产品资产。
- `python tools/validate_child_skill.py skills/<child-skill-name>` 通过。
- 桌面和移动预览经过视觉 QA。
- 只有用户明确要求时才生成 zip。

### 当前示例

已生成或测试中的子 skill 包括：

- `hiitmaster-brutal-interval-timer`
- `lonely-blue-field-notes`
- `namesake-soft-civic-guides`
- `nicchan-pixel-desktop-portfolio`

以验证结果和视觉 QA 为最终准则。

---

## English

UIgod is meant to run as a Codex skill that agents can automatically recognize and invoke. It is not a human-operated checklist.

When a user provides a website URL, screenshot, HTML/CSS, or written style brief and asks to test a site, extract style, generate a skill package, create a reference site, migrate a visual language, or write a `DESIGN.md`, the agent should invoke UIgod and handle the capture, extraction, packaging, and verification work.

The core output is not a one-off website. It is:

```text
skills/<child-skill-name>/DESIGN.md
```

That file is the main design brain future agents use to reuse the captured style.

### Agent Triggering

Once installed as a Codex skill, UIgod is matched through the `description` field in `SKILL.md` frontmatter.

Typical trigger prompts:

- `Test https://example.com/ and generate a skill package plus reference site.`
- `Extract this website style into a reusable child skill.`
- `Generate a DESIGN.md from these screenshots.`
- `Turn this landing page's visual language into an agent-usable style package.`
- `create a reusable child skill from this website style`
- `extract this site's visual system and build a reference example`

The user should not need to run scripts in `tools/`. Those scripts are bundled resources for the agent to call during skill execution.

### Agent Workflow

UIgod's automatic protocol is:

```text
Scope -> Capture -> Extract -> Distill -> Package -> Verify
```

- **Scope**: define source set, child skill name, default page type, and non-transferable assets.
- **Capture**: collect HTML, all linked CSS, screenshots, and evidence.
- **Extract**: write `references/source-observations.md` with fonts, colors, variables, layout, components, motion, and uncertainty.
- **Distill**: write `DESIGN.md` as an executable design system.
- **Package**: create the child skill `SKILL.md`, `preview.html`, `examples/index.html`, and focused code snippets.
- **Verify**: run structure validation, inspect desktop/mobile visuals, and confirm the example transfers style instead of cloning the source.

### Skill Directory

```text
UIgod/
├── SKILL.md                         # agent trigger and execution protocol
├── agents/
│   └── openai.yaml                  # UI metadata and implicit invocation policy
├── docs/
│   ├── CONTRACT.md                  # child skill output contract
│   └── REFERENCE-ANALYSIS-GUIDE.md  # evidence extraction details
├── tools/
│   ├── extract_style_evidence.py    # HTML/CSS evidence extractor for agents
│   └── validate_child_skill.py      # child skill validator for agents
├── inputs/                          # captured evidence, screenshots, and raw inputs
└── skills/                          # generated web-style child skills
```

### Child Skill Output

UIgod should keep generated child skills lean:

```text
skills/<child-skill-name>/
├── SKILL.md
├── DESIGN.md
├── preview.html
├── references/
│   ├── source-observations.md
│   └── code-patterns/
└── examples/
    └── index.html
```

`DESIGN.md` is the design brain. Do not turn a child skill into a bloated documentation bundle.

### Quality Gate

Before a child skill is considered ready, the agent must confirm:

- URL inputs fetched HTML and all linked CSS.
- Main CSS, default theme, resolved variables, and uncertainty are documented.
- `DESIGN.md` contains 5-8 recognizable signature moves.
- Tokens are mapped to roles, not only listed as raw values.
- `examples/index.html` uses fresh content and a new information architecture.
- No source logo, screenshots, copy, proprietary images, or product assets are copied.
- `python tools/validate_child_skill.py skills/<child-skill-name>` passes.
- Desktop and mobile previews have visual QA.
- Zip output is created only when the user explicitly asks.

### Current Examples

Generated or tested child skills include:

- `hiitmaster-brutal-interval-timer`
- `lonely-blue-field-notes`
- `namesake-soft-civic-guides`
- `nicchan-pixel-desktop-portfolio`

Trust validation results and visual QA as the final readiness signal.
