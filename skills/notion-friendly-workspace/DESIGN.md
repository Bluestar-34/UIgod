---
version: alpha
name: notion-ai-night-shift-design
description: "A Notion-inspired AI workspace campaign system built from two coordinated layers: a deep midnight-blue hero campaign with electric hand-drawn tracks, sticker-like AI agents, a large white product window, and a logo belt; followed by warm white/off-white productivity sections with bento cards, soft pastel feature panels, compact rounded controls, and humanist NotionInter typography. The style feels friendly, playful, and trustworthy, but the first impression is cinematic and campaign-specific rather than generic light SaaS."

colors:
  primary: "#455dd3"
  primary-strong: "#213183"
  link: "#0075de"
  ink: "rgba(0, 0, 0, 0.898)"
  ink-strong: "rgba(0, 0, 0, 0.95)"
  ink-muted: "#615d59"
  ink-soft: "#a39e98"
  canvas: "#ffffff"
  canvas-warm: "#f6f5f4"
  canvas-warm-2: "#f7f7f5"
  hero-midnight: "#000530"
  hero-midnight-soft: "#030b46"
  hero-glow: "#151f66"
  track-blue: "#2f4ee9"
  surface-dark: "#02093a"
  hairline: "rgba(0, 0, 0, 0.09)"
  hairline-strong: "rgba(0, 0, 0, 0.16)"
  dark-hairline: "rgba(255, 255, 255, 0.14)"
  block-blue: "#62aef0"
  block-yellow: "#ffc95e"
  block-coral: "#f77463"
  block-teal: "#2a9d99"
  block-brown: "#b18164"
  sticker-purple: "#9b6df0"
  sticker-orange: "#ff8a34"

typography:
  display-xl:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 72px
    fontWeight: 750
    lineHeight: 1.02
    letterSpacing: "-0.03em"
  display-lg:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 52px
    fontWeight: 750
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  subhead:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 22px
    fontWeight: 650
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body-lg:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 19px
    fontWeight: 450
    lineHeight: 1.55
    letterSpacing: 0
  body:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 16px
    fontWeight: 450
    lineHeight: 1.6
    letterSpacing: 0
  label:
    fontFamily: "NotionInter, Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0

rounded:
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  product: 10px
  pill: 9999px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 96px

components:
  campaign-nav:
    backgroundColor: "{colors.hero-midnight}"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    height: 68px
  primary-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 10px 18px
  secondary-button:
    backgroundColor: "color-mix(in srgb, {colors.primary} 74%, {colors.hero-midnight})"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 10px 18px
  campaign-hero:
    backgroundColor: "{colors.hero-midnight}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.xl}"
    padding: 82px 0 0
  product-window:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.product}"
    padding: 0
  bento-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 28px
  pastel-card:
    backgroundColor: "{colors.block-yellow}"
    textColor: "{colors.ink-strong}"
    typography: "{typography.subhead}"
    rounded: "{rounded.lg}"
    padding: 32px
  logo-belt:
    backgroundColor: "{colors.hero-midnight}"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 18px 0
---

## Overview

Notion AI Night Shift is a campaign-homepage style for an AI workspace product.

Default representative page type: an AI workspace campaign homepage. The first viewport should be a dark campaign hero with a large white product window and playful agent stickers. Lower sections shift into Notion's familiar warm productivity language: white/off-white surfaces, bento feature cards, pastel panels, logo proof, and compact CTAs.

It mixes:

- cinematic midnight AI campaign atmosphere
- friendly Notion productivity warmth
- sticker-like illustrated agents and app badges
- large product-window screenshots or synthesized product UI
- bento feature storytelling on warm neutral surfaces
- compact rounded controls and a disciplined sans type system

This style is not a generic light SaaS homepage. The dark hero campaign is the visual hook; the warm white sections are the supporting product language.

## Colors

The palette has two layers.

Campaign layer:

- `hero-midnight` and `hero-midnight-soft` create the dark first impression
- `hero-glow` adds soft center illumination behind the headline
- `track-blue` draws thick hand-made paths around the product window
- `primary` is the CTA blue used in both dark and light zones
- sticker colors such as `sticker-purple`, `sticker-orange`, coral, yellow, and teal create playful agent moments

Productivity layer:

- `canvas` and `canvas-warm` carry the lower page
- `ink`, `ink-strong`, `ink-muted`, and `ink-soft` create Notion-like readability
- `block-*` colors are used for bento cards and feature panels, not all at once inside one small component

Do not flatten this into only white/off-white. The dark campaign layer is required for the current reference.

## Typography

Use one humanist sans family throughout.

- hero headlines are large, heavy, and tightly tracked
- nav, buttons, and card labels use weight 600
- body copy is calm and readable with muted ink
- avoid decorative display fonts, mono metadata systems, or serif editorial voices

The type should feel direct and friendly. It should not feel corporate, futuristic, or dashboard-dense.

## Layout

The layout starts with a campaign-stage hero, then relaxes into bento product storytelling.

Core moves:

- slim language strip above the main nav when localization is relevant
- dark sticky or top-aligned nav on the hero
- centered headline and subhead
- two compact blue CTAs
- large white product window overlapping the lower part of the hero
- hand-drawn electric-blue tracks sweeping behind stickers and product chrome
- dark logo belt directly under or overlapping the product window
- warm off-white lower sections with dense but friendly bento cards
- final download / try-for-free grid and compact footer

The first screen should feel like a branded campaign, not a quiet docs page.

## Elevation & Depth

Depth is split by layer.

Campaign layer:

- soft radial glow behind the headline
- product window with subtle shadow and rounded desktop chrome
- sticker badges floating above the tracks
- dark logo belt pinned near the bottom of the hero

Productivity layer:

- warm paper surfaces
- light card shadows
- thin hairlines
- rounded bento cells

Avoid glassmorphism, neon haze, and heavy generic SaaS shadows.

## Shapes

Use friendly, practical rounding:

- buttons: `8px`
- small cards and tabs: `8px` to `12px`
- bento cards: `12px` to `16px`
- large product windows: around `10px`
- sticker badges: circular or squircle shapes with thick outlines

The hero paths should feel hand-drawn and imperfect. The product UI should stay crisp.

## Components

### Campaign Header

- dark hero background
- Notion-like square wordmark on the left
- medium-weight nav links
- primary CTA on the right
- login link secondary
- optional language strip above the nav

### Campaign Hero

- deep midnight background
- massive centered headline
- muted white supporting sentence
- CTA pair: primary blue plus darker blue secondary
- thick hand-drawn track lines running behind stickers

### Sticker Agents

- circular or squircle badges
- thick white/near-black outlines
- simple icon symbols inside
- placed near track paths, not in a clean grid
- small notification dots can add life

### Product Window

- large white desktop-like frame
- left sidebar, top toolbar, tabs, kanban/task columns, or assistant panels
- crisp tiny UI rows and pills
- should be the largest visual object in the first viewport

### Logo Belt

- dark strip under the product window
- white partner names/logos separated by small dots
- compressed height, dense but readable

### Bento Sections

- warm off-white background
- large section titles
- white rounded cards with one feature per card
- occasional pastel card backgrounds for AI/product stories
- small circular arrow controls

### CTAs

- primary action remains blue
- on dark surfaces, secondary action is a darker blue fill or outlined white control
- on light surfaces, secondary action can be a text link or quiet border button

## Do's and Don'ts

### Do

- lead with a dark AI campaign hero
- make the product window large and central
- use sticker agents and hand-drawn blue tracks as the memorable visual motif
- keep lower sections warm, white, and bento-based
- preserve Notion-like compact rounded buttons
- use one humanist sans type system

### Don't

- do not reduce the style to a generic white SaaS homepage
- do not replace the dark hero with a calm centered light hero
- do not make all features pastel split panels
- do not introduce cyberpunk neon, terminal UI, or glossy AI gradients
- do not make the product window a vague grey skeleton only
- do not overfill the page with random stickers; place them as campaign accents

## Responsive Behavior

On smaller screens:

- the nav collapses to brand, CTA, and menu control
- hero type reduces but remains bold and centered
- track lines can simplify or fade
- sticker agents should not block text or CTAs
- product window becomes horizontally compressed or switches to a mobile app-like product card
- bento sections collapse to one column
- logo belt scrolls or wraps tightly

The dark campaign identity must survive mobile; do not switch to an all-white mobile hero.

## Iteration Guide

When expanding this style:

- decide whether a new section belongs to the campaign layer or productivity layer
- keep campaign visuals concentrated in the hero and major AI sections
- keep standard product explanations in warm bento layouts
- use stickers to explain agents, automation, or integrations
- keep the CTA system compact and blue
- use real product imagery when available; otherwise synthesize a crisp product window, not abstract blobs

If adapting to another stack, preserve the hero/product-window/sticker/track composition before tuning micro details.

## Known Gaps

- The exact Notion brand assets, icons, video, and partner logos are not bundled; examples synthesize equivalent visual behavior.
- Some lower-page sections are inferred from captured screenshots rather than reconstructed from source implementation.
- The style has been validated as a single-page campaign showcase; deeper docs, pricing, and in-product surfaces remain future work.
