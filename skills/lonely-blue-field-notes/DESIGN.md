---
version: alpha
name: lonely-blue-field-notes-design
description: "A dark editorial technical-journal system built on near-black paper (#060708), warm ink text (#f1e8d8), serif display headlines, monospaced metadata, and four signal accents: gold, blue, green, and ember. The default mode feels solitary, technically literate, restrained, and quietly cinematic. The optional Signal Brutalist mode is more individual and graphic, using stronger blue/green/ember structural marks, matte slab backgrounds, archival grain, register ticks, and asymmetric field-note composition without becoming neon cyberpunk."

colors:
  primary: "#bf9641"
  ink: "#f1e8d8"
  ink-muted: "#c7bba8"
  ink-soft: "#8e846f"
  canvas: "#060708"
  canvas-soft: "#090d0d"
  surface-1: "#0c1010"
  surface-2: "#101616"
  surface-3: "#151d1b"
  hairline: "rgba(242, 234, 220, 0.13)"
  hairline-strong: "rgba(242, 234, 220, 0.25)"
  signal-blue: "#496b95"
  signal-green: "#5a8364"
  signal-ember: "#9b443c"
  signal-rose: "#9b4e64"

signalBrutalist:
  canvas: "#07090b"
  canvas-deep: "#030406"
  ink: "#fff2dd"
  muted: "#e3d0ad"
  blue: "#245cff"
  green: "#13d979"
  ember: "#ff3d2e"
  gold: "#f4bc46"
  slab: "#0b1015"
  hairline: "rgba(255, 242, 221, 0.18)"
  noiseOpacity: 0.08
  backgroundDensity: "medium-high"

typography:
  display-xl:
    fontFamily: "Noto Serif SC, Songti SC, Georgia, serif"
    fontSize: 96px
    fontWeight: 680
    lineHeight: 0.98
    letterSpacing: 0
  display-lg:
    fontFamily: "Noto Serif SC, Songti SC, Georgia, serif"
    fontSize: 64px
    fontWeight: 680
    lineHeight: 1.02
    letterSpacing: 0
  headline:
    fontFamily: "Noto Serif SC, Songti SC, Georgia, serif"
    fontSize: 34px
    fontWeight: 680
    lineHeight: 1.1
    letterSpacing: 0
  body-lg:
    fontFamily: "Aptos, Segoe UI Variable, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.78
    letterSpacing: 0
  body:
    fontFamily: "Aptos, Segoe UI Variable, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  body-sm:
    fontFamily: "Aptos, Segoe UI Variable, PingFang SC, Microsoft YaHei, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  mono:
    fontFamily: "Cascadia Code, SFMono-Regular, Consolas, monospace"
    fontSize: 12px
    fontWeight: 800
    lineHeight: 1.4
    letterSpacing: 0.08em

rounded:
  xs: 8px
  sm: 10px
  md: 12px
  lg: 14px
  xl: 18px
  pill: 9999px

spacing:
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 34px
  xxl: 52px
  section: 88px

components:
  top-nav:
    backgroundColor: "color-mix(in srgb, {colors.canvas} 88%, transparent)"
    textColor: "{colors.ink-muted}"
    typography: "{typography.mono}"
    rounded: "{rounded.xs}"
    height: 56px
  profile-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xl}"
    padding: 22px
  stream-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xs}"
    padding: 18px 0
  stream-cover:
    backgroundColor: "{colors.surface-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 0
  signal-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.mono}"
    rounded: "{rounded.xs}"
    padding: 28px 0
  utility-dock:
    backgroundColor: "color-mix(in srgb, {colors.surface-1} 82%, transparent)"
    textColor: "{colors.ink}"
    typography: "{typography.mono}"
    rounded: "{rounded.pill}"
    padding: 9px 7px
---

## Overview

Lonely Blue Field Notes is a dark editorial technical-journal system.

Representative use cases: personal technical journals, research portfolios, security writeup hubs, reflective creator homepages, and field-note style knowledge bases. New pages should use fresh information architecture for the user's goal while preserving the dark editorial field-notes style.

It mixes:

- private notebook energy
- long-form writing credibility
- restrained security-lab atmosphere
- warm literary display type
- monospaced system-like metadata

The interface should feel like a quiet signal transmitted across a dark screen. It is intimate rather than monumental, precise rather than glossy, and atmospheric without becoming decorative fog.

This style is not generic dark tech and not startup launch theater. It is closer to authored field notes for technical work.

## Use Cases

Best fits:

- personal technical journal homepages
- security writeup and lab-note hubs
- AI experiment logs
- research portfolios
- reflective creator sites
- knowledge-base portals with authored identity

Avoid using it for ecommerce, bright SaaS marketing, playful consumer apps, dashboards that need dense tabular operations, or pages where anonymous neutrality matters more than authorial voice.

## Signature Moves

1. Near-black field-notes canvas with warm paper-ink text and faint ambient signal washes.
2. Serif manifesto headline paired with monospaced labels, counters, nav, and metadata.
3. First viewport split into an identity/profile rail and a wider manifesto or index field.
4. Thin hairline borders define structure; shadows are rare and low-volume.
5. Ranked stream rows replace card grids: cover, mono index, serif title, short note, arrow.
6. Sparse signal accents in gold, blue, green, and ember mark state or emphasis.
7. Slow repeated-text signal band interrupts the page like a transmission.
8. Instrument-like utility UI, especially a slim scroll dock or compact index rail.

## Intensity Modes

### Calm Field Notes

Use this by default. Keep the original quiet technical-journal mood: sparse color, lots of dark negative space, warm serif headlines, precise mono metadata, rails, streams, and restrained motion.

### Signal Brutalist

Use this when the prompt asks for stronger personality, 野兽派, brutalist, blue/green/red, more background elements, harder contrast, or a less polite version of the style.

Signal Brutalist is not cyberpunk. It should feel like a private research notebook damaged by signal artifacts and print registration marks:

- off-black matte paper rather than pure black
- stronger blue / green / ember, used as structural ink
- hard-edge slabs, vertical bars, index ticks, torn strips, side registers, scan lines, and low-alpha paper grain
- serif headlines may use subtle red/blue offset shadows, but not glowing gradients
- small mono labels may sit in stamped boxes, skew slightly, or use color-keyed borders
- keep one large quiet field per page so the composition does not become a cockpit

When applying Signal Brutalist, read `references/signal-brutalist-backgrounds.md` for background recipes and copyable CSS primitives.

## Colors

The palette is dark-first but not void-minimal.

- `canvas` and `canvas-soft` establish near-black paper
- `ink` and `ink-muted` create warm reading contrast
- `surface-1` through `surface-3` create low-volume layers for rails, covers, and utility pieces
- `hairline` and `hairline-strong` do most of the structural work

Accent behavior is tightly controlled:

- `primary` gold is the main emphasis color
- `signal-blue`, `signal-green`, and `signal-ember` behave like sparse signal colors
- `signal-rose` is secondary and should remain rare

These signal colors should not become a rainbow interface. They are markers, not decoration.

In Signal Brutalist mode, increase the visibility of blue / green / ember but keep them functional:

- blue: primary structural mark, side rail, active edge, title offset
- green: status/signal trace, small rule, secondary register
- ember: warning, fracture, punch line, alternate title offset
- gold: warm editorial emphasis and quote highlight

Never use all accents as equal full-page gradients. Use 1-3 hard marks per viewport plus grain or slabs. If the background starts to look like a generic neon mesh, remove the gradient and return to matte slabs.

## Typography

The type system is the main lock on the style.

- large headlines use a serif display voice
- metadata, nav, counters, and utility labels use mono
- body copy stays in a quiet modern sans with generous line height

Rules:

- headlines should be dramatic but not compressed
- mono labels should feel precise and slightly technical
- body text should read calmly over long passages

Replacing the serif display layer with a generic grotesk collapses the identity immediately. If webfonts are unavailable, use Georgia/Songti for display and Segoe/Aptos for body rather than falling back to an all-sans system.

## Layout

The layout system is editorial, not marketing-first.

Core moves:

- full-width translucent sticky header
- split first viewport with a narrow profile rail and larger manifesto field
- vertical section breaks marked with 1px lines
- wide shell around `1280px`
- ranked horizontal streams instead of repeated card grids
- an identity band between major content zones
- small instrument-like floating utilities

The first screen should feel like an authored portal into work, not a conversion hero.

Signal Brutalist layout adds controlled graphic pressure:

- place one active signal edge on the left or right, not both at full intensity
- use asymmetric spacing: a narrow rail, a large silent text field, and one hard offset strip
- let background elements align with content axes; do not float random ornaments
- use boxy stamped labels for small metadata when the page needs attitude
- avoid centered poster layouts unless the page is a quote or closing statement

## Components

### Header

- sticky
- translucent
- mono navigation
- serif brand wordmark
- active state uses underline, not pill tabs

### Profile Rail

- left-side identity stack
- portrait, role, small stats, utility links
- separated from the main field by a 1px border

### Manifest Field

- large serif statement
- short calm supporting copy
- sparse colored cue lines
- entry links and one latest-note block

### Stream Rows

- cover image
- mono index
- serif title
- quiet summary
- directional arrow token

Rows should feel editorial and airy rather than like product cards.

### Signal Band

- oversized repeated mono text
- slow linear motion
- bordered above and below
- fades at the edges

### Utility Dock

- narrow persistent vertical control
- tactile but compact
- gradient progress only inside actual instrumentation

### Actions

- links and slim controls should dominate
- filled buttons should be sparse and deliberate

## Depth, Borders & Shapes

Depth is subtle and mostly structural.

Use:

- paper-dark surfaces
- thin line borders
- light hover lift on tactile elements
- restrained blur for sticky chrome and utility dock
- low-volume shadow only when a surface needs a slight lift

Do not build thick stacked cards, glossy planes, or dramatic z-depth layers.

Shape language:

This style uses a mixed shape language:

- most information architecture is line-based and rectangular
- image covers and some utility surfaces use moderate rounding
- pills are acceptable only for instrumentation or compact utilities

Rounded corners should usually stay within `8px` to `18px`.

For Signal Brutalist, reduce rounding:

- major slabs and cards: `0px` to `4px`
- utility pills can remain rounded only if they behave like instrumentation
- use offset shadows as flat ink blocks, not blurred glow
- prefer 1px hairlines, 3-8px signal bars, and hard-edged background rectangles

## Motion & Interaction

Interaction is quiet, tactile, and instrument-like.

- Header/nav hovers shift color to gold and lift by about 1-2px.
- Stream rows and rail links use small horizontal nudges, not dramatic scaling.
- Image covers may slightly increase contrast and scale on hover.
- Signal bands move slowly and linearly; `46s linear infinite` is a useful reference rhythm.
- Scroll docks reveal only when useful, then expose a vertical progress fill and thumb.
- Focus rings use a 2px gold-tinted outline with clear offset.
- Reduced-motion mode should collapse transitions and animations to near-instant behavior.

Keep animation as a low-frequency signal. Do not add bouncy UI, scroll-jacking theatrics, neon pulses, or parallax spectacle.

## Do's and Don'ts

### Do

- use near-black backgrounds with warm ink text
- pair serif display headlines with mono metadata
- use rails, lists, ranks, and thin borders
- reserve signal colors for sparse emphasis
- use subtle hover motion and slow signal motion
- when asked for more personality, use the Signal Brutalist variant with matte slab backgrounds, grain, register ticks, and stronger blue/green/ember structural marks

### Don't

- do not turn this into a glossy SaaS landing page
- do not replace the serif system with generic sans heroes
- do not flood the page with bright hacker-green or cyan neon
- do not overuse nested cards, giant shadows, or soft blob gradients
- do not center everything into a generic template
- do not make every action a pill button
- do not use ugly multi-color mesh gradients or generic grid wallpaper on dark pages; use hard slabs, paper noise, and precise signal marks instead

## Responsive Behavior

On smaller screens:

- the split first viewport collapses to a single column
- the profile rail becomes a top block with a bottom divider
- stream covers expand to full-width rows
- directional arrows can disappear if space gets tight
- the floating utility dock moves to the lower right and shrinks

The authored split structure should soften on mobile, but the rail-versus-field logic should still be legible.

## Prompt Guide

Use this compact prompt when asking an agent to generate with this child skill:

> Build a dark editorial technical-journal site in the Lonely Blue Field Notes style. Use a near-black canvas, warm ink text, serif manifesto headings, monospaced metadata, sparse gold/blue/green/ember signal accents, thin hairline borders, a profile or index rail, ranked stream rows, and a slow signal band. Keep it intimate, technically literate, and authored. Avoid glossy SaaS, neon cyberpunk, generic card grids, and copied source content.

Use this compact prompt for the expressive variant:

> Build in the Signal Brutalist variant of Lonely Blue Field Notes. Keep the warm serif / mono / sans hierarchy and authored field-note structure, but increase personality with matte off-black backgrounds, paper grain, hard-edge slabs, side registers, index ticks, torn strips, and clearly visible blue / green / ember structural marks. Avoid neon glow, rainbow gradients, generic grid wallpaper, and SaaS cards.

When expanding the style:

- preserve the editorial split between identity and content
- preserve the serif / mono / sans hierarchy
- add new components as quiet structural extensions, not as novelty widgets
- keep signal colors sparse and meaningful in Calm mode; make them more visible but still structural in Signal Brutalist mode
- prefer list and rail patterns over card-heavy expansion

If adapting to another stack, keep the layout and typography behavior intact before translating micro-details.

## Known Gaps

- The source reference is strongest on homepage behavior; deeper page types remain partially inferred.
- Some component states are synthesized because the exact implementation source was not available.
- This style has been validated on a portfolio example and component examples, but not yet across a full multi-page live site.
