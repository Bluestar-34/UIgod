# Source Observations

## Sources

- URL: https://namesake.fyi/
- Type: public-benefit name/gender marker guide homepage
- Captured date: 2026-06-12
- Local evidence folder: `inputs/namesake/evidence/`
- Screenshots: `references/source-screenshots-or-notes/home-desktop.png`, `references/source-screenshots-or-notes/home-mobile.png`

## Capture Method

- Tool: `python tools/extract_style_evidence.py https://namesake.fyi/ --out inputs/namesake/evidence`
- Browser/screenshots: Chrome headless, `1440x1200` desktop and `390x1000` mobile.
- Missing evidence: full JavaScript support-map behavior was not replicated; static state and CSS behavior were observed.

## CSS Files

| File | Size | Role |
| --- | ---: | --- |
| `02-BaseLayout.Y6MD1L2q.css` | 11,614 bytes | main token/layout/component CSS |
| `01-index.DKQLJVVz.css` | 4,905 bytes | homepage sections: hero, support map, sponsors |

Main CSS selection: `BaseLayout.Y6MD1L2q.css` is the larger file and contains root tokens, typography, header, footer, buttons, global canvas, and forced-color rules.

## Theme Detection

- `<html lang="en">`, no dark theme class.
- `<body data-color="purple">`.
- `<meta name="color-scheme" content="light">`.
- `<meta name="theme-color" content="#CDA5EF">`.
- CSS supports pastel `data-color` variants but no dark theme baseline.
- Default theme: light purple canvas.

## Extracted Tokens

### Colors

Extracted custom properties:

| Token | Value |
|---|---:|
| `--namesake-black` | `#111` |
| `--namesake-white` | `#e1e1e1` |
| `--namesake-purple` | `#cda5ef` |
| `--namesake-pink` | `#ecadd4` |
| `--namesake-blue` | `#96c7f2` |
| `--namesake-yellow` | `#ecdd85` |
| `--namesake-green` | `#97cf9c` |
| `--namesake-brown` | `#ddb896` |
| `--invalid-color` | `#9a0c14` |
| `--highlight-background-invalid` | `#5e0a0d` |
| `--highlight-overlay` | `#6f46ed26` |

Role mapping:

- `--background-color`: resolves to `--namesake-purple` from `body[data-color=purple]`.
- `--text-color`: resolves to `--namesake-black`.
- `--field-background`, `--overlay-background`, and `--button-background`: resolve to active background.
- `--highlight-background`: resolves to black.
- `--highlight-foreground`: resolves to active background.

Forced-colors mode maps to system colors such as `Canvas`, `ButtonText`, `Highlight`, `ButtonBorder`, and `FieldText`.

### Typography

Inline source HTML includes `@font-face` declarations for `Atkinson Hyperlegible Soft-6055adfe5728b321` at 400/700 normal/italic plus adjusted Arial fallback.

Root stack:

```css
--font-sans: "Atkinson Hyperlegible Soft-6055adfe5728b321",
  "Atkinson Hyperlegible Soft-6055adfe5728b321 fallback: Arial",
  Helvetica, Arial, sans-serif;
```

Extracted scale:

```css
--step--2: clamp(.7813rem, .7409rem + .1795vw, .88rem);
--step--1: clamp(.9375rem, .871rem + .2955vw, 1.1rem);
--step-0: clamp(1.125rem, 1.0227rem + .4545vw, 1.375rem);
--step-1: clamp(1.35rem, 1.1991rem + .6705vw, 1.7188rem);
--step-2: clamp(1.62rem, 1.4038rem + .9608vw, 2.1484rem);
--step-3: clamp(1.944rem, 1.6406rem + 1.3483vw, 2.6855rem);
--step-5: clamp(2.7994rem, 2.2279rem + 2.5396vw, 4.1962rem);
--step-6: clamp(3.3592rem, 2.5877rem + 3.429vw, 5.2452rem);
```

Other extracted type tokens:

```css
--weight-normal: 400;
--weight-bold: 700;
--line-height-single: 1;
--line-height-display: 1.05;
--line-height-body: 1.35;
--letter-spacing-condensed: -.02em;
```

### Spacing and Radius

```css
--space-2xs: clamp(.25rem, .1989rem + .2273vw, .375rem);
--space-xs: clamp(.375rem, .2983rem + .3409vw, .5625rem);
--space-s: clamp(.5rem, .3977rem + .4545vw, .75rem);
--space-m: clamp(.75rem, .5966rem + .6818vw, 1.125rem);
--space-l: clamp(1rem, .7955rem + .9091vw, 1.5rem);
--space-xl: clamp(1.5rem, 1.1932rem + 1.3636vw, 2.25rem);
--space-2xl: clamp(2rem, 1.5909rem + 1.8182vw, 3rem);
--space-3xl: clamp(3rem, 2.3864rem + 2.7273vw, 4.5rem);
--radius-s: var(--space-s);
```

Repeated concrete radius values: `5px`, `4.5px`, `4px`, `100%`.

### Borders, Depth, and Motion

- Buttons: `border: 3px solid #0000`, 5px radius.
- Primary button: black fill, active background text, black border.
- Secondary button: active background fill, black text, black border.
- Banner: 1px solid black border with black icon column.
- No extracted `box-shadow` values.
- Footer motif: `animation: 300s linear -24s infinite snailing`.
- Focus: `outline: 3px solid var(--text-color); outline-offset: 2px`.

### Layout

- Global `main`: max-width 1200px, centered, `padding-inline: var(--space-l)`.
- Header: flex row, baseline aligned, wraps, no hamburger.
- Hero: row flex, width `min(100vw, 1200px)`, left text column and right image.
- Hero image: `mix-blend-mode: multiply`, shrinks across breakpoints, hidden below `580px`.
- Support section: centered header, wide map, legend below.
- Sponsors: two-column grid, 80px row height.
- Footer: full-width black inverse block with content rows and large logo.

## Signature Moves

1. Purple `#cda5ef` light canvas with black speckle texture.
2. Black ink is used for all contrast, including type, nav, map marks, buttons, icon rail, and footer.
3. Atkinson Hyperlegible Soft-like huge rounded headline and large readable body.
4. Hero copy pairs with a black mixed-blend illustration that disappears on mobile.
5. A hand-drawn oval annotation circles a key word in the headline.
6. Primary button uses black fill with pastel text; secondary action remains an underlined link.
7. Fundraiser/notice banner uses 1px black border and a black icon column.
8. Status map uses dot/hatch/solid patterns with legend counts.

## Code Patterns

- `references/code-patterns/style-foundation.css`
- `references/code-patterns/hero.html`
- `references/code-patterns/notice-banner.html`
- `references/code-patterns/status-map.html`
- `references/code-patterns/footer.html`

## Extracted vs Inferred vs Synthesized

- Extracted: colors, type scale, font family, spacing scale, radius values, button behavior, banner structure, footer inverse treatment, screenshot layout, support-map legend behavior.
- Inferred: "soft civic guide" naming, civic data pattern as a general reusable design move.
- Synthesized: preview specimens, transfer example content, CSS speckle texture, hand-drawn SVG annotation, fictional resource map/list data.

## Non-Transferable Source Items

- Source content: Namesake copy, guide/state claims, sponsor names/logos, donation wording.
- Proprietary assets: passport image, Superbloom/MTPC logos, snail image, exact logo SVG.
- Exact layout/app logic: interactive support map JS, donation embeds, analytics, Cloudflare scripts.

## Known Uncertainty

The exact asset artwork is source-specific. The child skill preserves the visual role of monochrome mixed-blend illustration and tiny footer motion through synthesized CSS/SVG patterns rather than copying the raster assets.
