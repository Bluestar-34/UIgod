---
version: alpha
name: namesake-soft-civic-guides
description: "Accessible soft civic guide style: pastel paper canvas, black ink, Atkinson Hyperlegible Soft typography, speckled texture, hand-drawn annotation, inverse buttons, and practical status/map patterns."
colors:
  ink: "#111111"
  canvas: "#cda5ef"
  canvas-purple: "#cda5ef"
  canvas-pink: "#ecadd4"
  canvas-blue: "#96c7f2"
  canvas-yellow: "#ecdd85"
  canvas-green: "#97cf9c"
  canvas-brown: "#ddb896"
  muted-white: "#e1e1e1"
  invalid: "#9a0c14"
  invalid-dark: "#5e0a0d"
typography:
  display:
    fontFamily: "\"Atkinson Hyperlegible Soft\", \"Atkinson Hyperlegible\", Arial, Helvetica, sans-serif"
    fontSize: "clamp(3.3592rem, 2.5877rem + 3.429vw, 5.2452rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
  body:
    fontFamily: "\"Atkinson Hyperlegible Soft\", \"Atkinson Hyperlegible\", Arial, Helvetica, sans-serif"
    fontSize: "clamp(1.125rem, 1.0227rem + .4545vw, 1.375rem)"
    fontWeight: 400
    lineHeight: 1.35
rounded:
  control: "5px"
  legend: "4.5px"
  circle: "100%"
spacing:
  section: "clamp(3rem, 2.3864rem + 2.7273vw, 4.5rem)"
  shell: "min(1200px, 100%)"
---

## Overview

Namesake Soft Civic Guides is a public-benefit web style that feels handmade, accessible, and legally practical. It uses one pastel canvas at a time, black ink, big friendly typography, civic diagrams, and tiny tactile details instead of glossy product polish.

The style is especially strong when a site must make intimidating administrative information feel approachable without becoming childish.

## Use Cases

- Legal aid and name/gender marker guide sites
- Mutual-aid resource directories
- Public-benefit tool homepages
- Civic status dashboards
- Nonprofit campaign pages
- Plain-language documentation portals

Default representative page type: a guide/resource homepage with hero, action buttons, notice banner, status map or resource grid, partner/sponsor area, and dark inverse footer.

## Signature Moves

1. Single pastel canvas, default purple `#cda5ef`, with black speckle texture layered over it.
2. Black ink is the only primary contrast color: text, logo, nav, borders, map marks, footer, and filled buttons.
3. Atkinson Hyperlegible Soft-like type: very readable body text plus heavy rounded display headlines.
4. Hero composition pairs plain-language civic copy with a monochrome mixed-blend illustration that disappears on small screens.
5. One keyword or phrase receives a rough hand-drawn oval annotation.
6. Primary CTA is an inverse black rectangle with pastel text; secondary CTA is an underlined text link.
7. Information banners use a 1px black border with a black icon column and pastel content field.
8. Civic data is shown through map/table/list patterns with dot or hatch fills, small legends, and direct status counts.

## Colors

The palette is extracted from CSS custom properties.

| Token | Value | Role |
|---|---:|---|
| `ink` | `#111111` | all main type, icons, borders, filled buttons, footer background |
| `canvas-purple` | `#cda5ef` | default page background and brand field |
| `canvas-pink` | `#ecadd4` | alternate section/page color |
| `canvas-blue` | `#96c7f2` | alternate section/page color |
| `canvas-yellow` | `#ecdd85` | status or alternate page color |
| `canvas-green` | `#97cf9c` | positive/support status color |
| `canvas-brown` | `#ddb896` | warm neutral alternate color |
| `muted-white` | `#e1e1e1` | rare light neutral |
| `invalid` | `#9a0c14` | error text |
| `invalid-dark` | `#5e0a0d` | error highlight |

Use one pastel canvas as the main page color. Do not gradient between them. Black and the active canvas form the main two-color system.

## Typography

Source font: `Atkinson Hyperlegible Soft` with normal/italic and 400/700 faces. Use it when available. Fallback to `Atkinson Hyperlegible`, then Arial/Helvetica/sans-serif.

Extracted scale:

| Token | Value |
|---|---|
| step--2 | `clamp(.7813rem, .7409rem + .1795vw, .88rem)` |
| step--1 | `clamp(.9375rem, .871rem + .2955vw, 1.1rem)` |
| step-0 | `clamp(1.125rem, 1.0227rem + .4545vw, 1.375rem)` |
| step-1 | `clamp(1.35rem, 1.1991rem + .6705vw, 1.7188rem)` |
| step-2 | `clamp(1.62rem, 1.4038rem + .9608vw, 2.1484rem)` |
| step-3 | `clamp(1.944rem, 1.6406rem + 1.3483vw, 2.6855rem)` |
| step-5 | `clamp(2.7994rem, 2.2279rem + 2.5396vw, 4.1962rem)` |
| step-6 | `clamp(3.3592rem, 2.5877rem + 3.429vw, 5.2452rem)` |

Rules:

- Use `step-6` for large hero statements, `line-height: 1`, `letter-spacing: -0.02em`.
- Use bold 700 for headings and nav.
- Body copy stays large, plain, and readable at `step-0` with `line-height: 1.35`.
- Links are underlined with visible underline offset, not converted into subtle color-only links.

## Layout

- Max content width is `1200px`, centered with `padding-inline: var(--space-l)`.
- Header uses a baseline-aligned flex row, wraps instead of becoming a hamburger.
- Hero is a two-column flex row: copy on the left, monochrome illustration on the right.
- Hero image shrinks across desktop widths and hides below about `580px`.
- Sections stack vertically with generous `space-3xl` breathing room.
- Civic/status sections are centered and narrow in copy, then wide in data visualization.
- Sponsor or partner rows use simple two-column grids of logos/items.

Responsive behavior is deliberately simple: wrap, stack, hide the large hero illustration, keep the text navigation visible.

## Components

**Header**

Text logo at left, bold text links at right. Links use small padding and 5px radius; current/hover state is a 2px underline.

**Hero**

Huge black headline, plain-language subtitle, primary inverse button, secondary underlined link, optional hand-drawn oval around one word, and a black monochrome illustration with `mix-blend-mode: multiply`.

**Button**

Primary: black background, pastel text, 3px transparent/black border, 5px radius. Hover inverts to pastel background with black text. Secondary: underlined text link.

**Notice Banner**

Full-width grid with 1px black border. Left icon rail is black with pastel icon. Content side remains pastel.

**Status Map / Data Panel**

Large low-contrast map or panel on the active canvas. Use dot fills for unsupported/background states, hatch fills for next-up/prioritized states, and solid black for active/full support. Include a legend with counts.

**Footer**

Full-width black inverse footer. Text and form controls use the active canvas color. Optional slow small creature/object animation can sit above the footer, but do not copy the source snail.

## Depth, Borders & Shapes

Depth is almost flat. There are no extracted `box-shadow` values.

- Borders: 1px for banners/status panels; 3px for buttons and focus rings.
- Radius: 5px for buttons/links/forms; 4.5px for legend boxes; 100% for avatars or annotation loops.
- Do not add cards with large radius or shadows.
- Texture and illustration provide depth, not elevation.

## Motion & Interaction

- Link hover: underline, 2px thickness for nav/current states.
- Button hover: invert black/pastel colors.
- Focus: 3px solid black outline with 2px offset.
- Banner and legend interaction may fade/dim items with `opacity .2`.
- Footer motif can move very slowly: source snail used `animation: 300s linear -24s infinite`.
- Respect forced-colors mode using system color equivalents when possible.

## Responsive Behavior

- Header wraps but keeps text navigation visible.
- Hero image hides under about `580px`; do not replace it with a cramped tiny image.
- Hero headline remains massive and may occupy most of the first mobile viewport.
- Buttons wrap naturally; primary and secondary actions can sit on one line when width allows.
- Notice banners can keep the black icon rail; content wraps in the pastel field.
- Maps/data graphics can crop horizontally only when the core labels remain readable.

## Do's and Don'ts

Do:

- Use one pastel background as the whole page field.
- Keep black as the dominant contrast.
- Use large, human-readable type.
- Add speckles, hand annotation, and civic data marks.
- Make links visibly underlined.
- Keep language direct and supportive.

Don't:

- Turn the palette into a purple gradient or multi-color rainbow page.
- Use thin gray text, glassmorphism, neon, glow, or soft drop shadows.
- Hide navigation behind a hamburger by default.
- Use polished SaaS cards as the main layout.
- Copy the Namesake logo, passport image, sponsor logos, map data, or snail asset.

## Prompt Guide

Preserve: pastel single-color canvas, black ink, Atkinson-like soft type, speckles, inverse buttons, civic notice/status components, hand-drawn annotation, direct helpful copy.

Adapt: page content, active pastel color, illustration subject, map/list data, resource categories, footer motif.

Avoid: source content/assets, generic SaaS layout, glossy gradients, card-heavy dashboards, overdecorated illustration.

Default page type: accessible civic guide/resource homepage.

## Known Gaps

The source uses inline Astro font-face declarations and an interactive support map. This child skill captures the visual grammar and static HTML/CSS mechanics, not the full application logic.

Source screenshots were captured with Chrome headless. The skill does not copy proprietary raster assets such as the passport illustration, sponsor logos, or snail image.
