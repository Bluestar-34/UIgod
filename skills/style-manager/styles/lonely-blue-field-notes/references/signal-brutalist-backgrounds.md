# Signal Brutalist Backgrounds

Use this reference when the user asks for a more individual, brutalist, signal-heavy version of Lonely Blue Field Notes: stronger blue / green / ember, more background elements, less polite layouts, or 野兽派 energy.

The goal is a matte editorial field note with physical signal artifacts, not neon cyberpunk.

## Background stack

Every dark Signal Brutalist page should use 4-7 deliberate layers:

1. **Matte off-black base**: `#07090b` or `#030406`, never pure black.
2. **Paper grain**: low-alpha fixed noise; opacity around `.06-.12`.
3. **Hard slabs**: large vertical or horizontal rectangles in `#0b1015`, `#0a0e10`, or `#101817`.
4. **Signal bars**: 1-3 blue / green / ember strips, usually near an edge or aligned to content.
5. **Register ticks**: short crop marks, index ticks, calibration bars, or page-edge marks.
6. **Archival lines**: one subtle horizontal or vertical hairline to anchor content.
7. **Optional tear strip**: rough but controlled strip behind a title or rail.

Keep one large quiet zone. If every area is active, the page becomes a cockpit instead of field notes.

## Color roles

- `#245cff` blue: active edge, title offset, rail spine, first proof mark.
- `#13d979` green: status trace, secondary register, proof line.
- `#ff3d2e` ember: fracture, warning, punchline, red offset.
- `#f4bc46` gold: quote emphasis, warm annotation, final takeaway.

Use the colors as ink, not light. Prefer flat fills and crisp borders over glow.

## Dark page recipe

```css
:root {
  --lbf-brutal-bg: #07090b;
  --lbf-brutal-deep: #030406;
  --lbf-brutal-ink: #fff2dd;
  --lbf-brutal-slab: #0b1015;
  --lbf-brutal-blue: #245cff;
  --lbf-brutal-green: #13d979;
  --lbf-brutal-ember: #ff3d2e;
  --lbf-brutal-gold: #f4bc46;
  --lbf-brutal-line: rgba(255, 242, 221, 0.18);
}

.lbf-brutal-page {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background: var(--lbf-brutal-bg);
  color: var(--lbf-brutal-ink);
}

.lbf-brutal-page::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -2;
  pointer-events: none;
  opacity: .78;
  background:
    linear-gradient(90deg, transparent 0 8vw, rgba(36,92,255,.28) 8vw calc(8vw + 8px), transparent calc(8vw + 8px)),
    linear-gradient(90deg, transparent 0 78vw, rgba(11,16,21,.86) 78vw 86vw, transparent 86vw),
    linear-gradient(180deg, transparent 0 84%, rgba(255,242,221,.12) 84% calc(84% + 1px), transparent calc(84% + 1px));
}

.lbf-brutal-page::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  opacity: .09;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)' opacity='.75'/%3E%3C/svg%3E");
}
```

Use this only as a base. Move the slabs and signal bars so they align with the page content.

## Background element patterns

### Edge register

Use for opening pages, profile rails, or any slide with a strong left identity stack.

```css
.edge-register {
  position: absolute;
  inset: 0 auto 0 7.5vw;
  width: 34px;
  pointer-events: none;
}
.edge-register::before,
.edge-register::after {
  content: "";
  position: absolute;
  top: 34%;
  width: 7px;
  height: 34vh;
}
.edge-register::before { left: 0; background: #245cff; }
.edge-register::after { left: 13px; background: #ff3d2e; box-shadow: 13px 0 0 #13d979; }
```

### Calibration ticks

Use for small metadata zones. This adds detail without creating a generic grid.

```css
.calibration-ticks {
  position: absolute;
  right: 4vw;
  top: 12vh;
  display: grid;
  gap: 10px;
  opacity: .42;
}
.calibration-ticks span {
  display: block;
  width: 42px;
  height: 1px;
  background: rgba(255,242,221,.55);
}
.calibration-ticks span:nth-child(2n) { width: 18px; margin-left: 24px; background: #13d979; }
.calibration-ticks span:nth-child(3n) { width: 30px; background: #ff3d2e; }
```

### Torn slab

Use behind a quote, kicker, or side note. Keep it flat and low-alpha.

```css
.torn-slab {
  position: absolute;
  left: 46vw;
  top: 0;
  width: 9vw;
  height: 100%;
  pointer-events: none;
  background: #0b1015;
  opacity: .82;
  clip-path: polygon(16% 0, 100% 0, 86% 100%, 0 100%);
}
```

### Signal underline

Use for closing pages, title emphasis, and proof statements.

```css
.signal-underline {
  display: grid;
  grid-template-columns: 1fr;
  gap: 7px;
}
.signal-underline::before,
.signal-underline::after {
  content: "";
  display: block;
  height: 3px;
}
.signal-underline::before { background: #245cff; }
.signal-underline::after { background: #ff3d2e; box-shadow: 0 7px 0 #13d979; }
```

## Typography treatment

Use stronger typography only in Signal Brutalist mode:

- Display serif: weight `680-900`, tracking `-.04em` to `-.06em`.
- Sans/body: use a characterful sans such as Outfit, Satoshi, Geist, or Cabinet Grotesk.
- Mono labels: boxed, skewed, or stamped, but keep them short.
- Title shadows: allow 1-2px blue/ember offset. Do not use blurred glow.

```css
.brutal-title {
  letter-spacing: -.055em;
  text-shadow:
    -2px 0 0 rgba(36,92,255,.62),
     2px 2px 0 rgba(255,61,46,.42);
}

.brutal-kicker {
  display: inline-block;
  width: max-content;
  padding: .48em .72em;
  border: 1px solid rgba(255,242,221,.38);
  background: #0b1015;
  transform: skewX(-7deg);
  box-shadow: 6px 6px 0 rgba(36,92,255,.46);
}
```

## Composition rules

- Use no more than 3 saturated marks in one viewport.
- Keep background elements aligned to rails, headline edges, or footnote baselines.
- Avoid random floating ornaments.
- Avoid pure CSS mesh gradients on dark pages.
- Avoid generic square-grid wallpaper.
- If a page feels dirty, remove one color before reducing typography.
- If a page feels empty, add calibration ticks or a slab before adding another card.

## Quick prompt

> Use the Signal Brutalist variant of Lonely Blue Field Notes: matte off-black paper, warm serif headlines, precise mono labels, stronger blue/green/ember structural marks, hard slabs, paper grain, register ticks, torn strips, and one large quiet zone. No neon glow, rainbow mesh, generic grid wallpaper, or SaaS cards.
