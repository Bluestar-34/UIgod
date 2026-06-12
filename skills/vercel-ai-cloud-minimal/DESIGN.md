---
version: alpha
name: vercel-ai-cloud-minimal-design
description: "A Vercel-inspired developer infrastructure style built on a black canvas, white Geist-like typography, hairline grid borders, centered hero copy, pill CTAs, a luminous triangular mark, spectral deployment rays, dense product cards, and restrained monochrome UI chrome. The style feels precise, fast, technical, and premium. It favors black-and-white contrast, thin dividers, code/infrastructure metaphors, and geometric light effects over decorative illustration."

colors:
  canvas: "#000000"
  canvas-soft: "#050505"
  surface-1: "#080808"
  surface-2: "#0d0d0d"
  ink: "#ffffff"
  ink-muted: "#a1a1a1"
  ink-soft: "#737373"
  hairline: "rgba(255, 255, 255, 0.13)"
  hairline-soft: "rgba(255, 255, 255, 0.08)"
  inverse: "#ffffff"
  inverse-ink: "#000000"
  blue: "#0099ff"
  cyan: "#00d4ff"
  green: "#00ff88"
  amber: "#ffcc00"
  red: "#ff3300"
  violet: "#7c3aed"

typography:
  display-xl:
    fontFamily: "Geist, Inter, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 650
    lineHeight: 1.02
    letterSpacing: "-0.04em"
  display-lg:
    fontFamily: "Geist, Inter, Arial, sans-serif"
    fontSize: 52px
    fontWeight: 620
    lineHeight: 1.07
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Geist, Inter, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.025em"
  body-lg:
    fontFamily: "Geist, Inter, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Geist, Inter, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.58
    letterSpacing: "-0.005em"
  label:
    fontFamily: "Geist, Inter, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 520
    lineHeight: 1.35
    letterSpacing: "-0.01em"
  mono:
    fontFamily: "Geist Mono, SFMono-Regular, Consolas, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0

rounded:
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  pill: 9999px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 72px
  section: 104px

components:
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    height: 64px
  primary-button:
    backgroundColor: "{colors.inverse}"
    textColor: "{colors.inverse-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 13px 22px
  secondary-button:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 13px 22px
  hero-stage:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.xs}"
    padding: 96px 0 0
  grid-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 42px
  terminal-card:
    backgroundColor: "{colors.surface-1}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.mono}"
    rounded: "{rounded.md}"
    padding: 18px
---

## Overview

Vercel AI Cloud Minimal is a black-canvas developer infrastructure system.

Representative use cases: developer tool homepages, AI infrastructure sites, cloud deployment products, engineering portfolios, and technical product launches. New pages should use fresh information architecture for the user's goal while preserving the black-grid infrastructure style.

It mixes:

- austere black-and-white brand discipline
- precise developer product language
- hairline grid architecture
- luminous geometric infrastructure graphics
- compact pill controls
- monochrome cards with tiny code/product UI fragments
- sparse spectral accent light

This style is not generic dark SaaS. Its identity comes from strict black surfaces, Vercel-like triangle geometry, grid framing, and a feeling that every section is part of an infrastructure diagram.

## Colors

The palette is almost entirely black, white, and grey.

- `canvas` is true black and dominates the page
- `surface-1` and `surface-2` are only slight lifts from black
- `ink`, `ink-muted`, and `ink-soft` create hierarchy without changing hue
- `hairline` and `hairline-soft` draw the product grid
- spectral colors are reserved for deployment rays, status dots, and tiny system accents

Use color as emitted light, not as surface decoration.

## Typography

Use a Geist-like sans family with tight tracking and heavy optical precision.

- hero headlines are centered, white, and large
- body copy is muted grey and line-broken carefully
- labels and buttons are compact and medium-weight
- code snippets and telemetry use a mono face

Avoid expressive serif, friendly rounded display fonts, and over-spaced all-caps labels.

## Layout

The layout is centered and grid-locked.

Core moves:

- black top nav with wordmark left, product links center-left, auth actions right
- event/status pill above the hero
- centered hero headline and muted description
- primary white pill CTA plus secondary dark pill CTA
- large bounded hero stage with visible grid lines and a geometric light object
- proof section with a large typographic quote and segmented tabs
- multi-column grid of capability cards separated by hairlines
- infrastructure diagram sections spanning two columns
- dark footer with dense developer links

The page should feel like a terminal-grade launch surface, not a lifestyle landing page.

## Elevation & Depth

Depth comes from light and line, not shadows.

Use:

- hairline borders
- grid backgrounds
- radial glows
- spectral ray fields
- slight surface contrast
- small inset terminal panels

Avoid card shadows, glassmorphism, soft blobs, and glossy gradients.

## Shapes

Shapes are utilitarian:

- most sections and cards are rectangular
- buttons and nav actions use pills
- terminal cards use `8px` to `12px`
- icon buttons are circles or rounded squares
- the triangle mark is the primary brand geometry

Rounded corners should be sparse and functional.

## Components

### Header

- black background
- triangle mark and wordmark
- muted nav links
- dark outlined utility buttons
- white sign-up action

### Event Pill

- compact centered announcement
- small blue label
- white ticket pill
- one arrow token

### Hero

- centered headline
- muted description
- CTA pair
- large grid-framed visual stage
- triangle mark and spectral rays

### Product Grid

- 2x or 3x cards
- hairline dividers
- left-aligned headings
- muted body copy
- small circular arrow action
- optional terminal, browser, or deployment diagram fragment

### Terminal / Code Cards

- near-black panel
- mono text
- tiny status dots
- thin input bars
- minimal icons

### CTAs

- primary is white pill on black
- secondary is black/dark pill with hairline border
- do not introduce colorful filled buttons except tiny status labels

## Do's and Don'ts

### Do

- use a black canvas and strict hairline grids
- center the hero and keep copy concise
- use triangle geometry as the main icon language
- express color as thin light rays or small status dots
- build product cards like infrastructure modules
- keep typography precise and tight

### Don't

- do not turn this into generic neon cyberpunk
- do not use large colorful gradients as surfaces
- do not add friendly illustrations or pastel cards
- do not use heavy shadows or soft card stacks
- do not make every component rounded
- do not dilute the black-and-white discipline with many accents

## Responsive Behavior

On smaller screens:

- nav links collapse behind a compact menu affordance
- hero type reduces but remains centered
- grid-framed hero visual compresses vertically
- product cards become one column
- ray fields can simplify but should remain visible
- buttons stack only when width requires it

The black canvas, grid, and triangle/ray motif should survive mobile.

## Iteration Guide

When expanding this style:

- keep every new section aligned to the same grid shell
- use monochrome cards first, spectral accents second
- prefer technical diagrams and product UI fragments over generic imagery
- make motion subtle: ray shimmer, grid glow, terminal cursor
- preserve the white primary CTA on black

If adapting to another stack, preserve layout geometry and color discipline before changing details.

## Known Gaps

- Exact Vercel assets and proprietary fonts are not bundled; examples synthesize equivalent visual behavior.
- The hero triangle/ray artwork is recreated in CSS rather than copied from the source.
- Lower-page details are represented as style-equivalent modules rather than literal source implementation.
