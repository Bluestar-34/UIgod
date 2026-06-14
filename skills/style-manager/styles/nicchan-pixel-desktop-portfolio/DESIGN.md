---
version: alpha
name: nicchan-pixel-desktop-portfolio
description: "Accessible pixel desktop portfolio style derived from nicchan.me. Purple dusk pixel-art wallpaper, fixed icon dock, bottom taskbar, draggable-window cards, W95-style typography, hard 3px borders, inset UI shadows, lavender/teal/magenta accents, light and dark color-scheme support."

colors:
  wallpaper: "#716eba"
  violet-darkest: "#17162b"
  violet: "#2c2b4b"
  violet-lighter: "#4f4d7e"
  lavender: "#a3a3c7"
  lavender-lighter: "#c6c6dc"
  teal: "#9ddacb"
  teal-lighter: "#c1edc7"
  teal-darker: "#52a2a7"
  magenta: "#a75293"
  magenta-lighter: "#cb96cc"
  mauve-lighter: "#c6b0c6"
  mauve-lightest: "#eee7ee"
  gray: "#bdb6c4"
  gray-lighter: "#d7dde1"
  gray-darker: "#878894"
  off-white: "#fafafa"
  white: "#ffffff"
  black: "#000000"

typography:
  pixel:
    fontFamily: "\"W95fa\", \"Seravek Fallback\", \"Gill Sans Nova Fallback\", \"Ubuntu Fallback\", \"Calibri Fallback\", \"Liberation Sans Fallback\", source-sans-pro, sans-serif"
    fontSize: "16px"
    lineHeight: 1.6
    fontWeight: 400
  accent:
    fontFamily: "\"Sysfont\", \"Seravek Fallback\", \"Gill Sans Nova Fallback\", \"Ubuntu Fallback\", \"Calibri Fallback\", \"Liberation Sans Fallback\", source-sans-pro, sans-serif"
    fontSize: "clamp(2.5rem, 7vw + 1rem, 4.5rem)"
    lineHeight: 1
    fontWeight: 400
  code:
    fontFamily: "\"Departure Mono\", monospace"
    fontSize: "1rem"
    lineHeight: 1.5

rounded:
  none: "0"

spacing:
  border: ".1875rem"
  window: ".5rem"
  page-inline: "5%"
  text-padding: "calc(var(--border-thickness) * 2) calc(var(--border-thickness) * 3)"
  xs: "clamp(.75rem, .4891rem + 1.3043vi, 1.5rem)"
  s: "clamp(1rem, .6522rem + 1.7391vi, 2rem)"
  m: "clamp(1.5rem, .9783rem + 2.6087vi, 3rem)"
  l: "clamp(2rem, 1.3043rem + 3.4783vi, 4rem)"

components:
  window:
    border: ".1875rem solid #000"
    background: "#ffffff"
    text: "#2c2b4b"
    header: "linear-gradient(to right, #a3a3c7, #9ddacb)"
  button:
    border: ".1875rem solid #4f4d7e"
    background: "#d7dde1"
    shadow: "inset -3px -3px #878894, inset 3px 3px #ffffff"
    hoverBackground: "#c6b0c6"
  taskbar:
    background: "#bdb6c4"
    borderTop: ".1875rem solid #4f4d7e"
---

## Overview

Nic Chan's site expresses a desktop operating system as an accessible personal portfolio. The page is not merely retro: it is a functional pixel desktop with fixed navigation icons, draggable-looking windows, a bottom taskbar, view-transition-aware UI, light/dark/system settings, and crisp pixel imagery over a purple evening wallpaper.

Default representative page type: independent developer, designer, or creative-technologist portfolio.

Use this style when the experience should feel like a personal computer workspace: approachable, technical, playful, accessible, and highly navigable.

## Use Cases

- Independent developer/designer portfolio
- Small studio homepage
- Personal blog or notes index
- Creative-technologist project archive
- Playful documentation microsite

Best for content that can be grouped into desktop-like windows: introduction, selected work, notes, services, contact, settings.

## Signature Moves

1. Purple pixel-art wallpaper fills the viewport behind all UI.
2. Fixed left desktop-icon navigation remains visible across breakpoints.
3. Bottom taskbar frames the page like an operating system shell.
4. Content lives in square bordered windows with gradient title bars and small window controls.
5. W95fa/Sysfont/Departure Mono typography creates a pixel operating-system voice.
6. Three-pixel borders and inset bevel shadows replace soft elevation.
7. Lavender, teal, magenta, gray, and violet tokens drive both light and dark themes.
8. Accessibility controls, visible focus rings, and reduced-motion respect are treated as part of the style.

## Colors

The visual field is a violet-blue pixel-art wallpaper. UI surfaces sit on top as bright white or dark violet windows, with lavender and teal header gradients.

| Token | Value | Use |
|---|---:|---|
| wallpaper | #716eba | base behind pixel-art scene |
| violet-darkest | #17162b | page title, outlines, strong text |
| violet | #2c2b4b | primary text, dark window background |
| violet-lighter | #4f4d7e | borders, card text |
| lavender | #a3a3c7 | window header start, tags |
| teal | #9ddacb | window header end |
| teal-lighter | #c1edc7 | light highlight panels |
| magenta | #a75293 | underlines, small accent icon blocks |
| magenta-lighter | #cb96cc | focus/list highlights |
| mauve-lighter | #c6b0c6 | button hover |
| mauve-lightest | #eee7ee | nav label background |
| gray | #bdb6c4 | taskbar/footer |
| gray-lighter | #d7dde1 | button and card fill |
| gray-darker | #878894 | recessed shadow |
| off-white | #fafafa | code or box fill |
| white | #ffffff | window fill and highlight |
| black | #000000 | hard outer window borders |

Dark mode keeps the same wallpaper and swaps the window system: windows become #2c2b4b, text becomes #c6c6dc, nav labels become #2c2b4b with white text, and header gradients shift from magenta-darker to teal-darkest.

## Typography

The default typeface is W95fa. The title/accent face is Sysfont. Code uses Departure Mono. All three are custom web fonts on the source; use them when available, otherwise use the fallback stack declared in the frontmatter.

Rules:

- Keep body text pixelated unless the user asks for an antialiased accessibility setting.
- Use Sysfont for page titles, legends, and large labels.
- Do not substitute smooth modern UI fonts as the default; the pixel font is a defining feature.
- Preserve generous line-height: source body is 16px with 1.6 line-height, window bodies reach 24px text on wide screens.
- Main title: `clamp(2.5rem, 7vw + 1rem, 4.5rem)`, line-height 1, transparent gradient fill plus drop-shadow.

## Layout

The layout behaves like a desktop:

- Fixed left navigation column of pixel icons and small text labels.
- Main content padded by `--header-width` (`5rem`, then `6rem` on wide landscape).
- Bottom taskbar fixed to the viewport when there is enough height.
- Page content is a grid of independent window regions.
- On wide landscape, windows can appear as positioned panels rather than a simple vertical stack.
- On mobile, the navigation remains a left icon strip and windows stack vertically to the right.

The wallpaper must cover the entire viewport with `background-size: cover` and `background-position: center`. It should be crisp, illustrated, and recognizably pixel-art, not a smooth gradient.

## Depth, Borders & Shapes

Depth is created through classic inset UI shadows, not soft shadows.

- Buttons/cards use `inset -3px -3px #878894, inset 3px 3px #ffffff`.
- Hover/pressed state reverses the perceived bevel and translates by `translate3d(1px, 1px, 0)`.
- Windows do not use drop shadows; they rely on thick black borders and header structure.
- Focus states use double outlines: a solid violet outline plus a dotted white outline.

Everything is squared off. Border radius is `0`.

The source uses a conic-gradient mask on bordered UI to keep corners pixel-crisp. If that is too heavy for a target project, use ordinary square borders, but never round the corners.

Primary shape rules:

- Outer window border: 3px solid black.
- UI button/card border: 3px solid violet-lighter.
- Footer/taskbar top border: 3px solid violet-lighter.
- Dashed dividers use 3px text-accent lines.
- Pixel images use `image-rendering: crisp-edges` and `image-rendering: pixelated`.

## Components

**Desktop Nav**

Vertical icon list fixed to the left. Each item has a 16-bit/pixel icon above a tiny label. Labels sit on mauve-lightest in light mode and violet in dark mode. Icons should be symbolic and low-resolution.

**Window**

Use a `.window` shell with a header and body. Header uses the lavender-to-teal gradient, a text title, and two square controls: minimize and maximize. Body uses white or dark violet depending on theme and contains normal content.

**Taskbar**

A fixed bottom bar with the current page, open window buttons, arrow controls, and settings button. It should look functional, not decorative.

**Button**

Classic raised system button. Use hard border, inset bevel, and 1px pressed translation. Text can be simple arrow copy like `Open case ->`.

**List/Card**

Cards are gray-lighter panels with violet border and bevel. Use them for post lists, case studies, notes, or file rows. Keep content dense and scannable.

**Pixel Art Motif**

Include at least one of: pixel portrait, small 16x16 icons, pixel skyline wallpaper, sparkles, or a dithered scene. Use crisp image rendering.

## Motion & Interaction

- Button hover/active/pressed: `translate3d(1px, 1px, 0)` plus inverted inset bevel.
- Window controls imply minimize/maximize actions even when examples are static.
- Taskbar window buttons may scroll horizontally.
- Reduced-motion settings are part of the style and should be respected.
- Focus states are intentionally visible and should not be softened.

## Do's and Don'ts

Do:

- Build an actual desktop metaphor with nav icons, windows, and a taskbar.
- Keep the palette anchored in violet/lavender/teal/magenta.
- Use 3px hard borders and inset bevels.
- Provide visible focus states and settings/accessibility affordances.
- Stack windows cleanly on narrow screens.
- Use pixel art or CSS pixel patterns as a primary visual asset.

Don't:

- Turn this into generic "retro gaming" neon UI.
- Use rounded cards, glassmorphism, blur, or soft shadows.
- Replace the taskbar/window controls with modern pill tabs.
- Use smooth gradients as the main background.
- Hide navigation inside a hamburger menu on mobile.
- Copy Nic Chan's content, portrait, client logos, or exact page structure.

## Responsive Behavior

Below desktop width, windows stack in source order with `translate: 0`. The left icon rail remains visible and compact. The taskbar can become horizontally scrollable and may cover content, so examples should leave bottom padding.

Wide landscape:

- `--header-width: 6rem`
- `--window-spacing: 0`
- main area can hold overlapping or offset windows
- active/maximized windows can take the full layout

Mobile:

- keep a narrow icon rail
- use single-column windows
- reduce window body font size to avoid overflow
- keep controls tappable at roughly 40px square

## Prompt Guide

When applying this style to a new site:

1. Choose a desktop metaphor that fits the content: portfolio windows, app panels, logbook windows, file list, terminal note.
2. Generate a distinct pixel-art wallpaper or CSS pixel scene for the domain.
3. Place 3-5 primary content windows, not dozens of cards.
4. Give every action a system-button treatment.
5. Add one accessibility/settings area if the site has user preferences.
6. Verify the mobile layout: icon rail, windows, and taskbar must not obscure important text.

Preserve: pixel wallpaper, left icon rail, bottom taskbar, square windows, inset bevels, W95/Sysfont typography, lavender-teal-magenta palette.

Adapt: content, icon subjects, wallpaper scene, window count, page type.

Avoid: source content, source portrait/logos, rounded cards, glass blur, SaaS gradients, generic arcade neon.

## Known Gaps

The source uses Astro/Svelte islands, view transitions, Cloudinary images, user preference persistence, Tinylytics, and draggable/minimizable window behavior. This package captures the visual grammar and HTML/CSS implementation patterns, not the full application logic.

The source wallpaper and portrait are brand-specific assets. New builds should use their own pixel art or synthesized CSS patterns.
