# UIgod

UIgod is a flat skills repository for turning website and UI references into reusable Codex web-design styles.

The layout follows the same broad shape as the Superpowers skills directory: every installable skill lives at `skills/<skill-name>/` and owns its own `SKILL.md`.

## Default Install

Install only the visible coordinator skills:

```text
skills/uigod/
skills/style-manager/
```

`uigod` extracts reference evidence, writes `DESIGN.md`, builds preview pages, creates transfer examples, and generates managed style packages.

`style-manager` lists, selects, and applies the managed style packages.

Managed styles live under `skills/style-manager/styles/`. They keep their own nested `SKILL.md`, so agents can still discover and load a specific style when nested skill scanning is enabled, while the manager remains the friendly catalog and default selection layer.

## Usage

### List Available Styles

Use the manager to show every bundled style with a short description:

```bash
python skills/style-manager/tools/list_styles.py
```

Machine-readable output:

```bash
python skills/style-manager/tools/list_styles.py --json
```

### Choose A Style

If the user explicitly names a style, use that style.

If the user asks to choose from the library, run the list command and ask them to pick one.

If there is no conversation step, choose automatically:

```bash
python skills/style-manager/tools/list_styles.py --choose
```

Choose from a project brief or preference hint:

```bash
python skills/style-manager/tools/list_styles.py --choose --prefer "dark editorial technical portfolio"
```

The default choice comes from `skills/style-manager/preferences.json` when present, otherwise from `preferences.example.json`.

### Apply A Style

After selecting a style, read:

```text
skills/style-manager/styles/<style-name>/SKILL.md
skills/style-manager/styles/<style-name>/DESIGN.md
```

Use `references/source-observations.md` and `references/code-patterns/` only when deeper implementation detail is needed. Build fresh content in the selected style; do not clone the original reference site.

Example prompt:

```text
Use style-manager to choose a style for a dark personal knowledge-base homepage, then build the page using the selected style.
```

Direct style prompt:

```text
Use the lonely-blue-field-notes style to design a technical writing portfolio.
```

### Generate A New Style

Use `uigod` when adding a new reference style:

```text
Use uigod to extract the style from https://example.com and add it to the managed style library.
```

The generated package should land under:

```text
skills/style-manager/styles/<new-style-name>/
```

Run validation before publishing:

```bash
python skills/uigod/tools/validate_child_skill.py skills/style-manager/styles/<new-style-name>
```

## Skill Gallery

| Preview | Reference | Skill | Style |
|---|---|---|---|
| ![nicchan pixel desktop portfolio](skills/style-manager/styles/nicchan-pixel-desktop-portfolio/examples/preview.png) | nicchan.me | [nicchan-pixel-desktop-portfolio](skills/style-manager/styles/nicchan-pixel-desktop-portfolio/) | Pixel desktop portfolio, lo-fi retro UI, monospace display |
| ![lonely blue field notes](skills/style-manager/styles/lonely-blue-field-notes/examples/preview.png) | neurohack.blue | [lonely-blue-field-notes](skills/style-manager/styles/lonely-blue-field-notes/) | Dark editorial journal, serif display, signal accents |
| ![namesake soft civic guides](skills/style-manager/styles/namesake-soft-civic-guides/examples/preview.png) | namesake.gg | [namesake-soft-civic-guides](skills/style-manager/styles/namesake-soft-civic-guides/) | Soft civic guide pages, warm neutral palette, serif headers |
| ![hiitmaster brutal interval timer](skills/style-manager/styles/hiitmaster-brutal-interval-timer/examples/preview.png) | hiitmaster.app | [hiitmaster-brutal-interval-timer](skills/style-manager/styles/hiitmaster-brutal-interval-timer/) | Brutal interval timer, dark mode, bold numbers |

## Flat Skill Namespace

```text
skills/
├── uigod/                         # visible meta-skill
└── style-manager/                 # visible style selector
    └── styles/                    # nested managed style library
        ├── hiitmaster-brutal-interval-timer/
        ├── lonely-blue-field-notes/
        ├── namesake-soft-civic-guides/
        └── nicchan-pixel-desktop-portfolio/
```

## Managed Style Contract

Each generated managed style package uses:

```text
skills/style-manager/styles/<style-name>/
├── SKILL.md
├── DESIGN.md
├── preview.html
├── references/
│   ├── source-observations.md
│   └── code-patterns/
└── examples/
    └── index.html
```

`DESIGN.md` is the design brain. `SKILL.md` is the short operational wrapper. `preview.html` is a local token and component specimen. `examples/index.html` proves that the style transfers to fresh content.

## UIgod Package

- [skills/uigod/SKILL.md](skills/uigod/SKILL.md): meta-skill workflow
- [skills/uigod/docs/CONTRACT.md](skills/uigod/docs/CONTRACT.md): generated style skill contract
- [skills/uigod/docs/REFERENCE-ANALYSIS-GUIDE.md](skills/uigod/docs/REFERENCE-ANALYSIS-GUIDE.md): CSS and HTML evidence extraction protocol
- [skills/uigod/tools/extract_style_evidence.py](skills/uigod/tools/extract_style_evidence.py): helper for fetching HTML/CSS evidence
- [skills/uigod/tools/validate_child_skill.py](skills/uigod/tools/validate_child_skill.py): contract validator
- [skills/style-manager/SKILL.md](skills/style-manager/SKILL.md): style listing, selection, and application workflow
- [skills/style-manager/tools/list_styles.py](skills/style-manager/tools/list_styles.py): managed style catalog helper
