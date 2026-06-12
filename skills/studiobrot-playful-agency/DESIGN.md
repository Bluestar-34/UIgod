---
version: alpha
name: studiobrot-playful-agency-design
description: "A bold, irreverent German creative agency style built on a vibrant pink (#FFBEF1) and signature red (#ff2a00) canvas, custom FKScreamer display typography, thick black borders (3.5–7px), pill-shaped CTAs with bold drop shadows (6–12px), press-down hover animations, and a bread-motif personality. The style feels unapologetically loud, witty, and art-directed — it favors extreme typographic scale, chunky borders, pink/red section blocks, autoplay video case studies, black-background logo marquees, and personality-driven contact blocks over restrained or minimal design."

colors:
  brand-red: "#ff2a00"
  brand-red-soft: "rgba(255, 42, 0, 0.85)"
  signal-pink: "#FFBEF1"
  ink: "#000000"
  ink-muted: "#1D1D1B"
  ink-soft: "#4a4a48"
  canvas: "#ffffff"
  canvas-warm: "#faf8f5"
  surface-1: "#f5f5f3"
  hairline: "rgba(0, 0, 0, 0.12)"
  hairline-strong: "rgba(0, 0, 0, 0.25)"

typography:
  display-mega:
    fontFamily: "\"FK Screamer\", \"FKScreamer\", Helvetica, Arial, sans-serif"
    fontSize: 400px
    fontWeight: 800
    lineHeight: 0.85
    letterSpacing: "-0.02em"
  display-xxl:
    fontFamily: "\"FK Screamer\", \"FKScreamer\", Helvetica, Arial, sans-serif"
    fontSize: 200px
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "-0.02em"
  display-xl:
    fontFamily: "\"FK Screamer\", \"FKScreamer\", Helvetica, Arial, sans-serif"
    fontSize: 140px
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.015em"
  display-lg:
    fontFamily: "\"FK Screamer\", \"FKScreamer\", Helvetica, Arial, sans-serif"
    fontSize: 100px
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: clamp(60px, 9vw, 140px)
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: "-0.01em"
  subhead:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  body-lg:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.01em
  label:
    fontFamily: "Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.03em"

rounded:
  pill: 45px
  pill-lg: 150px
  card: 30px
  md: 16px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 80px
---

## Overview

Studio Brot is a Stuttgart-based advertising agency (Werbeagentur) with an unapologetically bold visual language. The brand name — "brot" (bread) — is a recurring motif of warmth and craft, but the execution is anything but soft: thick black borders, pill-shaped buttons with heavy drop shadows, custom FKScreamer display typography at extreme sizes, and a distinctive pink-and-red color duet define the experience.

The style is characterized by:

- **Vibrant pink (#FFBEF1) + signature red (#ff2a00)** as alternating section backgrounds
- **Custom FKScreamer display font** — a bold, condensed grotesque at extreme scales (up to 400px)
- **Thick black borders** (3.5–7px) on buttons, cards, and inputs
- **Pill-shaped CTAs** (45px border-radius) with bold box-shadows (6–12px)
- **Press-down hover effect** — buttons shift (+6px/+8px) and lose their shadow
- **Black-background client logo marquee** with fade edges
- **Autoplay video case studies** on alternating pink background
- **Self-aware, witty copy** mixing German and English wordplay
- **Bread GIF mascot** as a signature personality element

Default representative page type: a creative agency homepage. When the user does not specify a page type, generate one with: hero (red bg + mega headline) → showreel → intro (white) → logo marquee (black bg) → case studies (pink bg) → services (white, thick-border cards) → statement (extreme typography) → contact (pink bg) → newsletter → footer (red bg).

## Colors

### Core Duet
- `--brand-red`: **#ff2a00** — signature red; used as hero background, footer background, hover accent, the brand's main energy color
- `--signal-pink`: **#FFBEF1** — candy pink; used as project list background, contact section background, social icon fill

### Base
- `--canvas`: **#ffffff** — white for intro, services, newsletter
- `--ink`: **#000000** — pure black for borders and text
- `--ink-muted`: #1D1D1B — body text
- `--ink-soft`: #4a4a48 — secondary text

### Strokes
- `--hairline`: rgba(0, 0, 0, 0.12) — thin dividers
- `--hairline-strong`: rgba(0, 0, 0, 0.25)

**Usage rule:** Sections alternate between red background, pink background, white background, and black background (marquee). Do not blend them — each section gets one bold color.

## Typography

### Display (FKScreamer)
- **Display Mega** (400px/0.85): reserved for extreme statement words — "Leise ist kaputt."
- **Display XXL** (200px/0.9): main page titles, "breaking bread with brands."
- **Display XL** (140px/0.92): section headers like "Breaking Newsletter"
- **Display LG** (100px/0.95): h1 entries, "Mehr Cases" button

### Body (Helvetica/Arial)
- **Headline** (clamp 60–140px/0.95): project case titles, "Cam, saw, conquered."
- **Body LG** (20px/1.6): intro paragraphs, service descriptions
- **Body** (17px/1.55): standard content
- **Label** (14px/1.3, 600w): navigation items

FKScreamer is a custom typeface. For applied examples, use "FK Screamer" if available via @font-face, or approximate with a bold condensed sans-serif (e.g., Bebas Neue, Oswald, or Impact at 800 weight with tight tracking).

## Layout

### Shell
- Max content width: ~1280px centered
- Fixed header at top (z-index: 9999, 30px padding)
- Main content starts at 140px padding-top (to clear fixed header)
- Sections alternate background colors like a striped pattern

### Section Flow (Homepage)
1. **Header** (fixed, white bg) — logo (left) + bread GIF (right) + nav
2. **Hero** (RED bg #ff2a00) — one massive headline "breaking bread with brands." fills the viewport
3. **Showreel video** (white bg or transparent) — autoplay muted loop landscape video
4. **Intro** (WHITE bg) — two-column: headline (6 cols) + body (6 cols), "Agentur für Markenaufbau, Design und Kommunikation."
5. **Logo Marquee** (BLACK bg) — two rows of grayscale client logos scrolling horizontally, with CSS mask fade edges
6. **Case Studies** (PINK bg #FFBEF1) — project cards in a flexible grid (33.3% desktop), each with 5:6 aspect ratio image/video, witty title, description, bottom-border CTA
7. **Services** (WHITE bg) — swiper carousel with 15px black pagination bullets; each card has 6px black border, 30px radius, SVG illustration
8. **Statement** (WHITE or transparent) — centered intro paragraph + "Leise ist kaputt." at extreme scale (up to 388px)
9. **Contact** (PINK bg) — two-column: full-height team photo + contact info, pill CTAs with shadow
10. **Newsletter** (WHITE bg) — "Breaking Newsletter" headline + pill email input with arrow button
11. **Footer** (RED bg #ff2a00) — logo, address, phone/email, social icons
12. **Custom cursor** (mf-cursor) — pink background text label on hover

### Grid
- 12-column CSS grid with `--columns` custom property
- Desktop: `grid-template-columns: repeat(12, 1fr)` with `--gutter: 3rem`
- Mobile: single column

## Elevation & Depth

The style uses **flat boldness with physical shadow depth**:

- **Box-shadows** are a key signature: 6px 8px #000 on buttons, 12px 16px #000 on the "Mehr Cases" button
- **Press-down animation**: on hover, buttons translate (6px, 8px) and lose their shadow — simulating a physical button being pressed
- **No blur or frosted glass** effects
- **Custom cursor** (mf-cursor) provides interactive feedback
- Smooth scroll is present but subtle

## Shapes

- **Pill shapes** (45px border-radius) for buttons and inputs — this is the dominant shape
- **30px border-radius** for service cards
- **16px border-radius** for image hover states
- **No straight square corners** on interactive elements
- **Thick borders** (3.5px to 7px) on everything interactive

## Components

### Header / Nav (fixed, white bg)
```
Logo (svg wordmark, 200px wide) | [nav links] | Bread GIF (100px)
```
- Navigation: inline list items with 50px spacing, `border-bottom: 1px solid #000` links
- OR: nav links styled as pill buttons (same as CTA buttons)
- Mobile: hidden nav, burger menu toggles overlay

### Hero Headline (red bg)
- The hero is simply **one massive wordmark headline** on the brand red background
- Uses FKScreamer at extreme size (up to 200px on desktop)
- No subhead, no CTA — just the confident tagline

### Video Showreel
- Full-width autoplay muted loop video
- Desktop: 16:9 landscape
- Mobile: 9:16 portrait
- Simple, no decorative frame

### Logo Marquee (black bg)
- Background: #000
- CSS mask-image gradient on wrapper for fade edges
- Two horizontal scrolling rows of client logos (white/grayscale SVGs)
- Desktop animation: 20s linear infinite
- Mobile animation: 10s linear infinite

### Case Study Grid (pink bg)
- Container background: #FFBEF1
- Flexible wrapping grid with gap
- Desktop: 3 columns (33.3% each)
- Each card: image/video (5:6 aspect ratio on mobile, 1:1 on desktop) → witty h2 → description → "zur Story" link with border-bottom
- Image/video hover: border-radius transition to 16px
- "zur Story" CTA: `border-bottom: 1px solid #000`, hover turns red

### Services Swiper (white bg)
- Swiper carousel with 15px black pagination dots
- Each card: 6px solid black border, 30px radius
- Card content: centered SVG illustration (max 200px), h3 title, body paragraph
- Full-height cards with 40px padding (desktop)

### Statement Block
- Centered layout
- Short intro paragraph (body style)
- "Leise ist kaputt." at Display Mega scale (clamp 100px–19vw–388px)
- The extreme scale contrast IS the statement

### Contact Section (pink bg)
- Container background: #FFBEF1
- Two-column: team photo (full height, object-fit cover) + content
- Content: personal intro, "Let's get it on!" CTA headline
- Buttons: pill-shaped (45px), 3.5px black border, 6px 8px black shadow
- Phone button is smaller padding

### Newsletter (white bg)
- Headline: FKScreamer at large scale
- Input: pill-shaped (45px border-radius), 3.5px black border, 67px height
- Submit button: absolutely positioned inside input wrapper (arrow SVG)
- Hover: button turns black, arrow turns white

### Footer (red bg)
- Container background: #ff2a00
- Content: logo (white version), address (font-size: 28px), phone/email links
- Links: `border-bottom: 2px solid #000`, hover turns pink
- Social icons: Linkedin + Instagram SVGs, fill pink (#FFBEF1)
- Legal links (Datenschutz, Impressum)

### Custom Cursor
- The site uses mf-cursor library for a custom mouse cursor
- Button hover: pink background pill label with text

## Do's and Don'ts

**Do:**
- Use the red/pink color duet as section backgrounds — alternate boldly
- Use FKScreamer (or equivalent bold condensed) for display typography at extreme sizes
- Apply thick black borders (3.5px+) to buttons, cards, and inputs
- Use pill shapes for all interactive elements
- Add bold box-shadows (6px 8px or larger) with press-down hover effects
- Write headlines with wordplay, confidence, and humor
- Use autoplay muted video for case study covers on pink background
- Show client logos scrolling on a black background with fade edges
- Keep the layout loud and unapologetic — this is not a quiet style

**Don't:**
- Do not use subtle or minimalist design elements — everything should feel intentionally oversized
- Do not use multiple accent colors — stick to the red/pink duet, black, and white
- Do not use flat/rectangular buttons — always pill-shaped with shadow
- Do not use thin borders (1px) — all borders should be 3.5–7px
- Do not use serif or light-weight display fonts
- Do not make sections all the same background color — alternate between red, pink, white, and black
- Do not use the footer as a dark neutral — it must be brand red
- Do not lose the playful, self-aware tone — the brand is witty, not corporate

## Responsive Behavior

### Mobile (<768px)
- Hero headline reduces proportionally (clamp to ~44px), no longer full-height
- Showreel switches to portrait 9:16 video
- Case studies stack as single column
- Services swiper still works with touch swipe
- Header nav becomes hamburger menu with overlay
- Bread GIF may be smaller or hidden
- Logo marquee animates faster (10s)

### Tablet (768–1024px)
- Grid adjusts spacing
- 2-column case study grid possible
- Typography scales down via clamp values

### Desktop (1024px+)
- Full experience as described
- Images go to 1:1 aspect ratio
- Nav fully visible inline

### Reduced Motion
- `@media (prefers-reduced-motion: reduce)` — disable marquee animation, disable custom cursor, disable video autoplay

## Iteration Guide

When extending this style for new pages:

1. Read `DESIGN.md` first to internalize the loud, bold system.
2. Review `references/code-patterns/` for reusable component implementations.
3. The key formula: **thick borders + pill shapes + bold shadows + press-down hover + alternating section colors + extreme typography**.
4. Keep the red/pink color duet — do not introduce new accent colors.
5. Use FKScreamer (or equivalent) for any display text — never use a light font for headings.

Applied examples belong in `examples/applied/` only after this skill has been used on a fresh prompt and the result has been confirmed.

## Known Gaps

- FKScreamer is a custom typeface by [F37 Foundry](https://f37foundry.com/) — applied examples cannot use the exact font without licensing. Use a close approximation (Bebas Neue, Oswald 800, or Impact with tight tracking) and note the substitution.
- The bread GIF is a specific animated asset; use a bread emoji (🍞) or custom SVG in examples as a simplified equivalent.
- The custom cursor (mf-cursor) requires JS library inclusion; applied examples may omit it without breaking the core style.
- The exact showreel videos are agency-specific; applied examples should use placeholder video with poster images.
