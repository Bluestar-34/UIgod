# Source Observations

## Sources

- URL: `https://hiitmaster.netlify.app/en/`
- Evidence folder: `inputs/hiitmaster/evidence/`
- Screenshots:
  - `inputs/hiitmaster/screenshots/home-desktop.png`
  - `inputs/hiitmaster/screenshots/home-mobile.png`
  - `inputs/hiitmaster/screenshots/home-after-loader-desktop.png`
  - `inputs/hiitmaster/screenshots/home-after-loader-mobile.png`

## Capture Method

- Tool: `python skills/uigod/tools/extract_style_evidence.py https://hiitmaster.netlify.app/en/ --out inputs/hiitmaster/evidence`
- Browser/screenshots: Chrome headless desktop and mobile captures. Initial captures caught timer states `READY` and `FOCUS`; later captures caught `PREPARE`.
- Missing evidence: no runtime app interaction beyond visible page/timer states. Proprietary source screenshots were recorded as asset leads but are not reused in the child skill.

## CSS Files

| File | Size | Role |
|---|---:|---|
| `02-index.5lybzNdn.css` | 15968 | Main site CSS: tokens, layout, components, motion, loader/timer |
| `01-css2.css` | 1374 | Google Inter font CSS |
| `combined.css` | 17549 | Helper-combined CSS evidence |

Main CSS selection reason: `02-index.5lybzNdn.css` is the largest non-font stylesheet and contains the page variables, hero, buttons, cards, overlays, phone mockup, reveals, and timer loader.

## Theme Detection

- Default theme: black/dark.
- Evidence:
  - `meta theme-color` is `#ff2d00`.
  - `:root` defines `--dark-bg: #000000`, `--light-bg: #0d0d0d`, `--text-color: #ffffff`.
  - Body uses `background-color: var(--dark-bg)` and white text.
  - Screenshots show a black full-screen timer with red-orange numerals.
- Uncertainty: no alternate theme switcher was found in captured markup/CSS.

## Extracted Tokens

### Colors

Resolved CSS custom properties:

| Token | Value |
|---|---:|
| `--primary-color` | `#ff2d00` |
| `--secondary-color` | `#111111` |
| `--accent-color` | `#00ff2a` |
| `--text-color` | `#ffffff` |
| `--dark-bg` | `#000000` |
| `--light-bg` | `#0d0d0d` |
| `--card-bg` | `#141414` |
| `--gradient-brutal` | `linear-gradient(90deg, #ff2d00 50%, #000000 50%)` |

Frequent literal colors:

- `#000` / `#000000`: black canvas, shadow, device border.
- `#fff` / `#ffffff`: primary text and white secondary button.
- `#ff2d00`: red-orange signal, timer, bars, borders, CTA.
- `#ff2d004d`: translucent red shadow.
- `rgba(255,255,255,.03)`: grid overlay.
- `rgba(255,255,255,.05)`: section dividers.
- `rgba(255,255,255,.1)`: card border.

### Typography

- Font source: Google Inter.
- Source variables:
  - `--font-main`: `"Inter", monospace, sans-serif`
  - `--font-heading`: `"Inter", monospace, sans-serif`
- Body: Inter, `line-height: 1.4`, `letter-spacing: -.01em`, `font-weight: 400`.
- Headings: uppercase, `font-weight: 900`, `line-height: .9`, `letter-spacing: -.05em`.
- H1: `8vw`; H2: `3.5rem`; mobile H2: `2.5rem`.
- Card H3: `1.8rem`.
- Button: `1.2rem`, `font-weight: 800`, uppercase.
- Timer: monospace, `25vw`, `font-weight: 900`, `font-variant-numeric: tabular-nums`, red-orange, text shadow.
- Timer label: `1.8rem`, uppercase, `letter-spacing: .4em`, border-top red rule.

### Spacing and Layout

- `section`: `padding: 10rem 2rem`, `border-bottom: 1px solid rgba(255,255,255,.05)`.
- `.hero`: min-height `100vh`, two-column grid `1fr 1fr`, no padding.
- `.hero-content`: `padding: 5rem`, flex column centered vertically.
- `.buttons`: flex row, `gap: 2rem`, margin-top `4rem`.
- `.feature-grid`: `repeat(auto-fit, minmax(300px,1fr))`, gap `2rem`.
- `.feature-card`: `padding: 3rem 2rem`.
- Responsive:
  - `max-width: 1100px`: hero and why sections stack.
  - `max-width: 768px`: h1 grows in source CSS, h2 becomes `2.5rem`, feature grid one column, buttons stack full-width.
  - `max-width: 480px`: store badge shrinks.

### Borders, Radii, and Shadows

- Most components: `border-radius: 0`.
- Feature card: `1px solid rgba(255,255,255,.1)`.
- Card title underline: `4px solid #ff2d00`.
- Future card: `5px solid #ff2d00`.
- Image/device framing: `10px solid #000`, `15px solid #000`, device radius `20px`.
- Extracted shadows:
  - `-20px 20px #000`
  - `20px 20px #000`
  - `10px 10px #ff2d004d`
  - `8px 8px #00000080`
  - `12px 12px #ff2d004d`

### Motion and Interactions

- Button hover: translate up `-5px`; primary gains hard black shadow.
- Feature card hover: translate up `-10px`, border turns red.
- Glitch hover: `animation: glitch .3s linear infinite`.
- Reveal classes:
  - bottom/left/right/scale: `.8s cubic-bezier(.16,1,.3,1)`.
  - glitch reveal: `.4s ease`.
  - cut reveal: `.5s steps(5,end)`.
- Timer blink: `.2s infinite alternate`.
- Top progress line: fixed top, 5px high, red, `transition: width .1s linear`.
- Image load wipe: red block scales away over `.6s cubic-bezier(.16,1,.3,1) .2s`.
- Cursor: links/buttons use `crosshair`.

### Assets and SVG

- Source asset leads:
  - `https://hiitmaster.netlify.app/home_screen.png`
  - `https://hiitmaster.netlify.app/home_screen_drawerbar.png`
  - Google Inter font files.
  - Inline SVG noise filter references.
- Reuse policy: source screenshots and app assets are evidence only. Do not copy them into generated transfer examples unless a user explicitly supplies reusable rights.

## Signature Moves

- Move 1: black full-screen timer stage with red-orange tabular numerals.
- Move 2: short uppercase command state below a red rule.
- Move 3: heavy uppercase Inter headings with compressed line-height.
- Move 4: zero-radius slabs with red borders, red underlines, and black surfaces.
- Move 5: hard offset shadows rather than soft elevation.
- Move 6: fixed red top progress line plus faint 50px grid and SVG noise overlays.
- Move 7: hover/reveal motion built from translate, cut, glitch, blink, and wipe mechanics.
- Move 8: tilted phone/device slab motif with heavy border and hard shadow, translated into fresh app/console panels.

## Code Patterns

- `references/code-patterns/style-foundation.css`
- `references/code-patterns/progress-grid-noise.css`
- `references/code-patterns/timer-stage.html`
- `references/code-patterns/brutal-buttons.html`
- `references/code-patterns/feature-card.html`
- `references/code-patterns/device-slab.html`

## Extracted vs Inferred vs Synthesized

- Extracted:
  - CSS variables, colors, font stacks, type sizes, section spacing, border/radius values, shadows, media breakpoints, grid/noise/progress mechanics, timer values, and motion timings.
- Inferred:
  - Default style role names such as `canvas`, `surface`, `signal`, and `success`.
  - The overall portable category: brutal interval-timer command interface.
  - The timer stage as the strongest reusable visual anchor because screenshots repeatedly captured it.
- Synthesized:
  - The example brand and content (`Circuit Forge`).
  - Transfer components such as protocol rows, command metrics, and console slabs.
  - Accessibility guidance to use fixed tested breakpoints instead of source viewport-sized timer typography when clipping risk is high.
