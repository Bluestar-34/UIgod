# Reference Analysis Guide

Use this when extracting a style before writing `DESIGN.md`. The output is evidence for `references/source-observations.md`, not another design document.

For URL or local HTML input, prefer the helper first:

```bash
python skills/uigod/tools/extract_style_evidence.py <url-or-html-file> --out inputs/<slug>/evidence
```

Then inspect the saved HTML/CSS and screenshots manually when available.

## URL Input

1. Fetch the HTML.
2. Extract and fetch every linked CSS file.
3. Sort CSS files by size and relevance; the main theme CSS is often the largest file, not the first file.
4. Detect the default theme from body classes, `data-theme`, active switchers, and `prefers-color-scheme`. State uncertainty.
5. Resolve all `var(--token)` chains until they become literal values.
6. Extract:
   - custom properties
   - `@font-face` and font stacks
   - colors by role and section
   - font sizes, weights, line heights, letter spacing, `clamp()` scales
   - spacing, grid/container widths, breakpoints
   - borders, radii, shadows, depth rules
   - hover, focus, active, transition, animation behavior
   - inline SVG, decorative assets, cursor/illustration motifs

If CSS was not fetched, mark the child skill incomplete.

## Signature Move Pass

After token extraction, identify 5-8 signature moves. A signature move is a concrete visual behavior, not a mood word.

Good:

- `3px black window borders with lavender-to-teal title bars`
- `fixed left desktop-icon rail plus bottom taskbar`
- `monospace all-caps metadata above warm serif headlines`

Weak:

- `modern`
- `playful`
- `clean`

These moves become the transfer checklist for `examples/index.html`.

## Screenshot Input

- Infer values conservatively.
- Use ranges when exact values are unknowable.
- Mark inferred values explicitly.
- Do not invent precise tokens from visual vibes.

## Code Or Brief Input

- Extract tokens directly from CSS, inline styles, utility classes, or framework config.
- Record framework context only when it changes the style mechanics.
- For briefs, separate user-stated rules from synthesized design decisions.

## source-observations.md Shape

```markdown
# Source Observations

## Sources
- URL / screenshot / code / brief

## Capture Method
- Tool:
- Browser/screenshots:
- Missing evidence:

## CSS Files
| File | Size | Role |
| --- | ---: | --- |

## Theme Detection
- Default theme:
- Evidence:
- Uncertainty:

## Extracted Tokens
- Colors:
- Typography:
- Spacing/layout:
- Borders/radii/shadows:
- Motion/interactions:
- Assets/SVG:

## Signature Moves
- Move 1:
- Move 2:
- Move 3:
- Move 4:
- Move 5:

## Code Patterns
- `references/code-patterns/nav.html`
- `references/code-patterns/card.html`

## Extracted vs Inferred vs Synthesized
- Extracted:
- Inferred:
- Synthesized:
```

## Failure Modes

- Fetching only the first CSS file.
- Choosing the wrong light/dark theme.
- Leaving unresolved CSS variables in `DESIGN.md`.
- Replacing custom fonts with generic guesses without noting it.
- Missing extreme type scale because it looks unreasonable.
- Ignoring section color alternation and decorative SVG/asset motifs.
- Copying source layout/content instead of distilling transferable style.
- Writing an example that looks good but lacks the declared signature moves.
