---
version: alpha
name: template-web-style-skill-design
description: "Replace this description with a concrete style-family summary. This file is the canonical design system document for a generated UIgod child skill."

colors:
  primary: "#2457ff"
  ink: "#111111"
  ink-muted: "#6f6b63"
  canvas: "#f7f4ee"
  surface-1: "#ffffff"
  surface-2: "#f0ece4"
  hairline: "rgba(17, 17, 17, 0.14)"

typography:
  display-xl:
    fontFamily: "Replace Display Font"
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  display-md:
    fontFamily: "Replace Display Font"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: 0
  body:
    fontFamily: "Replace Body Font"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  mono:
    fontFamily: "Replace Mono Font"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em

rounded:
  sm: 8px
  md: 12px
  lg: 18px

borderWidth:
  sm: 1px
  md: 2px
  lg: 3.5px
  xl: 6px

shadow:
  sm: "2px 3px 0 0 rgba(0,0,0,0.15)"
  md: "6px 8px 0 0 #000000"
  lg: "12px 16px 0 0 #000000"

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 40px
  section: 88px
---

## Overview

Replace this section with the core explanation of the style family.

Cover:

- visual atmosphere
- density
- emotional tone
- what makes the style recognizable

## Use Cases

State default representative use cases for this style family.

Do not define the source site as a page template.

## Signature Moves

List 5-8 concrete style behaviors that the transfer example must demonstrate.

Use this shape:

1. `[token/layout/component behavior]`
2. `[token/layout/component behavior]`
3. `[token/layout/component behavior]`
4. `[token/layout/component behavior]`
5. `[token/layout/component behavior]`

Avoid vague mood words. Each move should be visible in `preview.html` or `examples/index.html`.

## Colors

Document:

- base canvas
- text hierarchy
- surface hierarchy
- accent usage
- semantic or signal colors if needed

## Typography

Document:

- display font behavior
- body rhythm
- metadata / mono behavior
- scale contrasts

## Layout

Document:

- shell width
- section spacing
- first viewport structure
- grid behavior
- image / text relationships

## Components

Document the recurring building blocks:

- header / nav
- hero
- content sections
- list or card behavior
- form / action behavior
- footer

## Depth, Borders & Shapes

Document:

- whether depth is flat, layered, editorial, glossy, or cinematic
- shadows: **extract all box-shadow values from CSS** (including offset, blur, spread, color)
- blurs
- borders
- hover transitions that change shadow (e.g., press-down effects)
- corner strategy
- line strategy
- pill usage or avoidance

## Motion & Interaction

Document:

- hover states
- focus states
- transitions
- custom cursor or interaction feedback
- scroll/page transition behavior

## Responsive Behavior

Document:

- mobile stacking behavior
- what can collapse
- what must stay visible
- touch-target considerations if relevant

## Do's and Don'ts

List the style-preserving rules and anti-patterns.

## Prompt Guide

Give concise generation guidance:

- preserve
- adapt
- avoid
- default page type

`examples/index.html` should demonstrate style transfer, not source-site reconstruction.

## Known Gaps

Document uncertainty, inferred areas, or parts that need more source evidence.
