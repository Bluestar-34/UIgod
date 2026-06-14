# Source Observations

Evidence log for the `lonely-blue-field-notes` child skill.

## Sources

- Source URL: `https://www.neurohack.blue/`
- Captured HTML: `inputs/neurohack-blue/index.html`
- Captured CSS: `inputs/neurohack-blue/BaseLayout.css`
- Child skill preview: `preview.html`
- Transfer proof: `examples/index.html`

Non-transferable source items: Neuroblue name, original copy, avatar, social links, article titles, article images, site data, exact route structure, and source SVG/icons. Use them as evidence only.

## Capture Method

- Local evidence was captured before this repair pass and stored under `inputs/neurohack-blue/`.
- HTML shows an Astro-generated static page with `<html lang="zh-CN" data-theme="dark">`.
- The linked stylesheet was saved as `BaseLayout.css`.
- This repair pass re-read the local HTML/CSS, preserved the existing transfer example, and normalized evidence/design sections to the current UIgod contract.

## CSS Files

| File | Size | Role |
| --- | ---: | --- |
| `inputs/neurohack-blue/BaseLayout.css` | 102,772 bytes | Main stylesheet; contains theme tokens, layout, components, motion, responsive rules, and utility dock behavior. |

Main CSS selection reason: the HTML links a single Astro CSS asset (`/_astro/BaseLayout.CIiC19Yw.css`), and the local file contains the full token and component grammar.

## Theme Detection

- Default source HTML uses `data-theme="dark"`.
- CSS defines both `:root` light tokens and `html[data-theme=dark]` dark tokens.
- Dark mode is the representative style for this child skill because the captured page loads in dark mode and the homepage mood depends on near-black canvas, warm ink, and sparse signal accents.
- Theme toggle JavaScript stores `theme-mode` in `localStorage`; this is source behavior evidence, not required for migration.

## Extracted Tokens

Dark theme tokens extracted from `html[data-theme=dark]`:

| Role | Value |
| --- | --- |
| `canvas` / `--bg` | `#060708` |
| `canvas-soft` / `--bg-soft` | `#090d0d` |
| `surface-1` / `--paper` | `#0c1010` |
| `surface-2` / `--paper-2` | `#101616` |
| `surface-3` / `--paper-3` | `#151d1b` |
| `ink` / `--ink` | `#f1e8d8` |
| `ink-muted` / `--muted` | `#c7bba8` |
| `ink-soft` / `--soft` | `#8e846f` |
| `hairline` / `--line` | `rgba(242, 234, 220, .13)` |
| `hairline-strong` / `--line-strong` | `rgba(242, 234, 220, .25)` |
| `primary` / `--accent` | `#bf9641` |
| `accent-soft` | `rgba(191, 150, 65, .11)` |
| `accent-ink` | `#14100a` |
| `signal-blue` / `--blue` | `#496b95` |
| `signal-green` / `--signal` | `#5a8364` |
| `signal-rose` / `--rose` | `#9b4e64` |
| `signal-ember` / `--ember` | `#9b443c` |
| `gold` / `--gold` | `#c7a04e` |
| `radius-xl` | `20px` extracted; child skill normalizes major surfaces to `18px` where preview examples need tighter fit. |
| `radius-lg` | `16px` extracted; child skill normalizes to `14px` for transfer example. |
| `radius-md` | `12px` extracted; child skill uses `10px` for compact rows. |
| `radius-sm` | `8px` |
| `ease` | `cubic-bezier(.16, 1, .3, 1)` |

Typography tokens:

- UI/body: `"Aptos", "Segoe UI Variable", "PingFang SC", "Microsoft YaHei", sans-serif`
- Display: `"Noto Serif SC", "Songti SC", Georgia, serif`
- Mono: `"Cascadia Code", "SFMono-Regular", Consolas, monospace`
- Body base: `17px`, line-height `1.7`
- Homepage manifesto heading: `clamp(52px, 8vw, 116px)`, weight `680`, line-height `.98`
- Stream title behavior: serif title, mono index, quiet sans summary.

## Signature Moves

1. Near-black dark canvas with warm paper-like text and ambient radial washes.
2. Split homepage gate: left profile rail, right manifesto field.
3. Serif display headlines mixed with monospaced nav, labels, stats, and metadata.
4. Thin borders and line-based section dividers instead of card-heavy depth.
5. Ranked stream rows with cover image, index, title, summary, and arrow.
6. Four sparse signal colors: gold, blue, green, ember/rose.
7. Slow repeated-text signal band (`glyph-track`) between page zones.
8. Fixed scroll dock with vertical progress fill and compact mono percent output.

## Extracted vs Inferred vs Synthesized

Extracted:

- Dark default theme via `data-theme="dark"`.
- Astro source and single linked CSS file.
- Dark/light CSS variable sets.
- Font stacks, body size, headline clamp, line-height, easing curve, major radii.
- Sticky translucent header with `backdrop-filter: blur(18px) saturate(1.08)`.
- Homepage profile rail plus manifesto layout.
- Stream-list structure.
- Glyph/signal band animation.
- Scroll dock interaction structure and reduced-motion CSS.

Inferred:

- The style works best for personal technical journals, research portfolios, and writeup hubs because the source content and layout are author-centered.
- Dark mode should be treated as canonical even though a light token set exists.
- Accent colors should stay sparse because the CSS uses them as cues, lines, and hover states rather than full-color sections.

Synthesized:

- The `Blue Field Atelier` transfer example uses new content, new imagery, and a broader portfolio/atelier information architecture.
- `DESIGN.md` normalizes component names, token roles, and prompt guidance for future agents.
- Code patterns are reusable fragments, not direct source clones.

## Known Uncertainty

- Exact production screenshot dimensions from the original capture are not present in this folder.
- Some source assets referenced by HTML were not copied, so preview/example pages use generated CSS shapes or remote non-source images.
- Deep page types are inferred from the stylesheet and homepage evidence, not separately captured as full screenshots.
