---
version: alpha
name: hiitmaster-brutal-interval-timer
description: "A brutal interval-timer web style: black stage, red-orange signal, giant tabular numerals, uppercase command typography, hard slabs, grid/noise overlays, and cut/glitch motion."
colors:
  canvas: "#000000"
  canvas-soft: "#0d0d0d"
  surface: "#141414"
  surface-strong: "#111111"
  ink: "#ffffff"
  signal: "#ff2d00"
  success: "#00ff2a"
  line: "rgba(255,255,255,0.10)"
  line-faint: "rgba(255,255,255,0.05)"
  grid: "rgba(255,255,255,0.03)"
  shadow: "#000000"
typography:
  display:
    fontFamily: "\"Inter\", ui-sans-serif, system-ui, sans-serif"
    fontSize: "8vw extracted; implement with tested breakpoints"
    fontWeight: 900
    lineHeight: 0.9
  timer:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "25vw extracted; implement with tested breakpoints"
    fontWeight: 900
    fontVariantNumeric: "tabular-nums"
  body:
    fontFamily: "\"Inter\", ui-sans-serif, system-ui, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 400
    lineHeight: 1.4
rounded:
  slab: "0"
  badge: "8px extracted for store badge only"
  device: "20px extracted for phone mockup only"
spacing:
  section: "10rem 2rem"
  card: "3rem 2rem"
  button: "1.5rem 3rem"
---

## Overview

Hiitmaster Brutal Interval Timer is a high-intensity command interface for training, countdowns, physical challenges, and performance tools. It feels closer to a gym clock, mission timer, or competition wallboard than a wellness landing page.

The style should be sparse and forceful: black dominates, red-orange carries urgency, and every component looks like it was cut from rectangular panels. The most recognizable artifact is the giant timer stage with tabular numerals and a short state label.

## Use Cases

- Interval timer web apps
- Fitness challenge pages
- Workout protocol landing pages
- Performance coaching dashboards
- Competition, bootcamp, or studio schedule pages
- Any tool where time, rounds, readiness, and output are the core information

Default representative page type: a dark training command homepage with hero timer, protocol cards, session metrics, device/console slab, and a final high-urgency CTA.

## Signature Moves

1. Full black stage with `#ff2d00` as the only loud visual signal.
2. Giant tabular timer numerals, usually centered or used as the hero anchor.
3. Short uppercase state label below the timer with a red rule above it.
4. Heavy uppercase headings: Inter-like 900 weight, compressed line-height, command tone.
5. Brutal slabs: zero radius, hard red borders, black surfaces, and no soft elevation.
6. Offset shadows such as `-20px 20px #000000` or translucent red shadow for hover emphasis.
7. Fixed top progress line, faint 50px grid overlay, and subtle noise texture.
8. Cut/glitch/blink/reveal motion used for active states, not decorative flourish.

## Colors

Extracted source tokens:

| Token | Value | Role |
|---|---:|---|
| `canvas` | `#000000` | full page background, loader, timer stage |
| `canvas-soft` | `#0d0d0d` | alternate dark section background |
| `surface` | `#141414` | cards and slabs |
| `surface-strong` | `#111111` | phone/device mockup fill and dark panels |
| `ink` | `#ffffff` | primary text |
| `signal` | `#ff2d00` | timer, CTA fill, borders, bars, progress, badges |
| `success` | `#00ff2a` | rare active/success accent; use sparingly |
| `line` | `rgba(255,255,255,0.10)` | card borders and separators |
| `line-faint` | `rgba(255,255,255,0.05)` | section dividers |
| `grid` | `rgba(255,255,255,0.03)` | fixed 50px grid overlay |
| `red-shadow` | `#ff2d004d` | translucent red offset hover shadow |
| `black-shadow` | `#000000` | hard slab shadow |

Use red-orange as signal, not decoration everywhere. A strong page is mostly black, white, and red, with the green accent only for small "complete", "live", or "recovered" states.

## Typography

Source font: Google Inter weights 300, 400, 600, 700, 800, 900. The source also uses monospace for the timer.

Extracted typography facts:

| Role | Extracted values |
|---|---|
| Body | Inter, `1.2rem`, `line-height: 1.4`, `font-weight: 400` |
| Headings | Inter, uppercase, `font-weight: 900`, `line-height: .9`, source used tight tracking |
| Hero h1 | `8vw` on desktop source CSS |
| Section h2 | `3.5rem` desktop, `2.5rem` mobile |
| Card h3 | `1.8rem`, `font-weight: 900` |
| Button | `1.2rem`, `font-weight: 800`, uppercase |
| Timer | monospace, `25vw`, `font-weight: 900`, tabular numerals |
| State label | `1.8rem`, uppercase, source used very wide tracking |

Implementation guidance:

- Use Inter or a close geometric sans for all non-timer text.
- Use a monospace font with `font-variant-numeric: tabular-nums` for countdowns.
- Keep headings uppercase and heavy; let weight and line-height create compression.
- For mobile, prefer fixed breakpoint sizes over fluid viewport typography so large numerals never clip.
- If a runtime environment forbids negative tracking, keep tracking at zero and preserve the source feel through weight, scale, and explicit spaced label text like `P R E P A R E`.

## Layout

- Page background is black from edge to edge.
- Sections are large, usually `10rem 2rem`, with bottom dividers at `rgba(255,255,255,.05)`.
- Hero can be either:
  - a full viewport centered timer stage, or
  - a split command landing: copy/CTAs on one side, timer or device slab on the other.
- Source landing used `grid-template-columns: 1fr 1fr` and stacked under `1100px`.
- Content cards use responsive grids such as `repeat(auto-fit, minmax(300px, 1fr))`.
- Section headings are left aligned and marked with a red bar below.
- CTAs group into horizontal command blocks on desktop and stack full-width on mobile.

Do not make a soft wellness layout. This style needs stark empty space, hard alignment, and clock-like hierarchy.

## Components

**Timer Stage**

Full black panel. Giant red tabular time sits center. Below it, a short uppercase state label sits under a red rule. Use states like `R E A D Y`, `A C T I V E`, `R E S T`, `F O C U S`, or domain-specific equivalents.

**Header / Nav**

Keep it utilitarian: small uppercase labels, white text, red hover or active state, thin divider. A sticky header can work, but the top progress line is the stronger navigation cue.

**Buttons**

Primary button: red fill, black text, no radius, uppercase, heavy weight. Hover translates up by about `-5px` and may gain a hard black shadow. Secondary button: transparent with a white 2px border; hover inverts to white fill and black text.

**Feature Card**

Surface `#141414`, no radius, `1px solid rgba(255,255,255,.1)`, padding `3rem 2rem`. On hover, translate up `-10px` and switch border to `#ff2d00`. Card titles get a `4px` red underline.

**Future / Badge Card**

A heavier slab can use `5px solid #ff2d00`, minimum height around `300px`, and an absolute red badge in the top right. Use for upcoming protocols, locked modules, or high-priority states.

**Progress Line**

Fixed top line, `5px` tall, red, width driven by scroll or state. This is a signature mechanic and should appear in examples.

**Grid And Noise**

Use a fixed 50px grid overlay at `rgba(255,255,255,.03)` and optional SVG fractal noise at `opacity: .03`. These are background instruments, never foreground texture.

**Device Slab**

Source used a tilted phone mockup: `300px x 600px`, `15px solid #000`, `20px` radius, `-20px 20px #000` shadow, and slight rotation. For transfer work, reinterpret it as a training console/device slab rather than copying app screenshots.

## Depth, Borders & Shapes

- Most radius is `0`.
- Primary borders: `4px solid #ff2d00`, `5px solid #ff2d00`, or `1px solid rgba(255,255,255,.1)`.
- Strong framing can use `10px solid #000000`.
- Hard shadows:
  - `-20px 20px #000000`
  - `20px 20px #000000`
  - `10px 10px #ff2d004d`
  - `8px 8px #00000080`
- Avoid blur, glass, soft card shadows, and rounded SaaS cards.

## Motion & Interaction

Extracted source motion:

- Button hover: `translateY(-5px)` with hard shadow.
- Card hover: `translateY(-10px)` and red border.
- Glitch hover: `.3s linear infinite`.
- Scroll reveal: `.8s cubic-bezier(.16,1,.3,1)`.
- Cut reveal: `.5s steps(5,end)`.
- Timer blink: `.2s infinite alternate`, slight opacity and scale change.
- Image red wipe: `.6s cubic-bezier(.16,1,.3,1) .2s`.
- Top progress line: `width .1s linear`.

Use motion as an intensity cue. Do not animate every block. The timer, current state, CTA hover, and active reveal are enough.

Always include a `prefers-reduced-motion: reduce` path that disables glitch, blink, and large translations.

## Responsive Behavior

- Under about `1100px`, split heroes stack.
- Under about `768px`, feature grids become one column, buttons become full width, and section spacing tightens.
- Timer numerals must be tested on a narrow mobile screenshot. The source uses extremely large viewport typography, but generated sites should use fixed breakpoints if clipping risk exists.
- Keep the state label readable; if wide tracking causes clipping, write the letters with spaces and keep CSS tracking neutral.
- Device slabs shrink from about `300x600` to `220x440` or become a flat console panel.
- Never hide the core timer on mobile. It is the style's main signal.

## Do's and Don'ts

Do:

- Start from black, red, white, and one tiny green signal.
- Make the timer or command metric the first visual read.
- Use hard slabs, red rules, and zero-radius controls.
- Add grid/noise/progress mechanics for industrial pressure.
- Keep copy short, uppercase when it behaves like a command.
- Test desktop and mobile screenshots.

Don't:

- Copy HIIT Master name, copy, screenshots, product badges, or exact app flow.
- Use lifestyle gym photography as the main hero.
- Add soft gradients, rounded pastel wellness cards, glass panels, or friendly illustrations.
- Use red on every text element; it should remain a signal.
- Let timer numerals or uppercase labels overflow on mobile.

## Prompt Guide

Preserve: black full-screen field, `#ff2d00` signal color, huge tabular timer, uppercase command labels, brutal zero-radius slabs, red section bars, hard offset shadows, top progress line, faint grid/noise, cut/glitch/blink motion.

Adapt: brand name, training domain, IA, protocols, metrics, device slab content, state labels, and copy tone.

Avoid: source brand/assets/content, generic SaaS landing patterns, soft wellness styling, glassmorphism, and mobile clipping.

Default page type: a high-intensity training command homepage with a hero timer, protocol grid, live status panel, and red CTA.

## Known Gaps

The source is an Astro/static site with app screenshots and a loader-style timer. This child skill captures the visual system and reusable HTML/CSS mechanics, not the original app logic.

The extracted source CSS includes negative and very wide letter spacing plus viewport-sized typography. Transfer implementations should preserve the visual feeling while obeying the target project's accessibility and responsive constraints.

The green accent `#00ff2a` is present in variables but not strongly visible in screenshots; use it sparingly and mark heavy green use as synthesized.
