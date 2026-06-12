# UIgod Contract

This is the only contract a generated web-style child skill must satisfy.

## Design Target

The child skill must capture a portable style grammar, not a page clone.

Define these before writing files:

- **Source set**: URLs, screenshots, code, or brief used as evidence.
- **Default page type**: the page type this style expresses best.
- **Signature moves**: 5-8 concrete visual behaviors that make the style recognizable.
- **Non-transferable items**: source content, proprietary images, exact layouts, logos, names, or app logic that must not be copied.

## Required Structure

```text
child-skill-name/
├── SKILL.md
├── DESIGN.md
├── preview.html
├── references/
│   ├── source-observations.md
│   └── code-patterns/
└── examples/
    └── index.html
```

Optional, only when useful: `README.md`, `preview.png`, `preview-dark.html`, `references/source-screenshots-or-notes/`, `examples/README.md`.

## File Roles

- `SKILL.md`: short trigger, read order, and how to apply the style. Do not repeat `DESIGN.md`.
- `DESIGN.md`: main artifact. A future agent should be able to generate a new site in the style from this file alone.
- `preview.html`: local visual catalog for palette, typography, shape, component atoms, and motifs. It is not a source clone.
- `references/source-observations.md`: evidence log: source set, CSS files, resolved tokens, theme detection, fonts, layout facts, interactions, assets, uncertainty.
- `references/code-patterns/`: small reusable mechanics such as `nav.html`, `hero.html`, `card.html`, `section.html`, `button.html`, `motif.css`.
- `examples/index.html`: fresh transfer proof with new content. It must preserve style DNA without copying source layout/content/assets.

## DESIGN.md Shape

Use practical frontmatter:

```yaml
---
version: alpha
name: style-name
description: "One concrete sentence about the style."
colors:
  canvas: "#000000"
typography:
  display:
    fontFamily: "..."
    fontSize: "..."
rounded:
  none: "0"
spacing:
  section: "..."
---
```

Required sections:

1. `## Overview`
2. `## Use Cases`
3. `## Signature Moves`
4. `## Colors`
5. `## Typography`
6. `## Layout`
7. `## Components`
8. `## Depth, Borders & Shapes`
9. `## Motion & Interaction`
10. `## Responsive Behavior`
11. `## Do's and Don'ts`
12. `## Prompt Guide`
13. `## Known Gaps`

## Writing Rules

- Prefer exact extracted values over aesthetic guesses.
- Mark values as extracted, inferred, or synthesized.
- Name portable style moves, not source-site content.
- Explain token roles: `canvas`, `surface`, `ink`, `accent`, `line`, `danger`, `signal`, not only raw hex lists.
- Describe layout grammar: density, grids, first viewport, image/text relationship, section rhythm.
- Describe interaction grammar: hover, focus, active, cursor, motion timing, reduced-motion behavior.
- Keep one style family per child skill.
- Put prompt guidance in `DESIGN.md`; do not create separate prompt files.
- Do not create zip packages unless the user explicitly asks.

## Final Gate

Before calling a child skill ready:

- Required files exist.
- `python tools/validate_child_skill.py skills/<child-skill-name>` passes when working inside this repo.
- URL inputs have fetched HTML and all linked CSS files.
- Main CSS selection is documented by size/relevance.
- CSS variable chains are resolved to literal values.
- Default theme is detected or uncertainty is stated.
- Fonts, colors, type scale, borders, shadows, layout, responsive rules, interactions, and assets are captured.
- `DESIGN.md` reads as one coherent design system and traces values to `source-observations.md`.
- `preview.html` opens with `file://` and shows visual tokens/components.
- `examples/index.html` uses fresh content and works on desktop/mobile.
- Transfer example demonstrates at least five signature moves from `DESIGN.md`.
- Transfer example changes information architecture instead of copying source page order.
- Proprietary source assets are documented as evidence, not reused by default.
- Another agent could build a new site in the style without reopening the original reference.
