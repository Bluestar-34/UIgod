---
name: lonely-blue-field-notes
description: Guides web design toward a dark editorial technical-journal style with warm serif headlines, monospaced metadata, split profile-and-manifest layouts, signal-color accents, stream-like content lists, and an optional Signal Brutalist variant with stronger blue/green/ember marks and richer matte background elements. Use when the user wants a personal site, technical blog, research journal, security writeup hub, reflective creator web presence, or asks for a more individual, brutalist, expressive, blue-green-red field-notes visual system.
---

# Lonely Blue Field Notes

This child skill captures a dark editorial web style derived from a personal technical writing site.

It is designed for web work that should feel like private field notes rather than a polished SaaS dashboard or a loud cyberpunk landing page.

Default representative page type: a personal technical journal homepage (profile rail + manifesto + ranked writing stream). When the user does not specify a page type, generate this one.

It has two intensity modes:

- **Calm Field Notes**: the default; restrained, quiet, sparse, cinematic.
- **Signal Brutalist**: use when the user asks for more individuality, stronger blue/green/red, more background elements, 野兽派, brutalist, experimental, or less "polite" pages.

## Use When

Use this skill for:

- personal technical blogs
- security writeup hubs
- AI experiment journals
- reflective creator homepages
- research notebooks with strong visual atmosphere
- expressive slides or pages that need a personal, signal-heavy, editorial-brutalist mood

## Read First

- `DESIGN.md` for the canonical design system
- `references/signal-brutalist-backgrounds.md` when stronger background elements, blue/green/ember signals, or a brutalist variant is requested
- `references/source-observations.md` for the reference-site extraction notes
- `references/code-patterns/` for reusable fragments
- `examples/index.html` for the transfer example
- `preview.html` for a quick token scan

## Style Priority

Preserve the emotional mix:

- solitary
- technically literate
- low-noise by default; higher signal density only in Signal Brutalist mode
- warm against dark
- editorial rather than product-marketing

For Signal Brutalist mode, keep the authored field-note soul but increase the graphic pressure:

- matte off-black surfaces, not pure black
- visible blue / green / ember structural marks
- hard slabs, register ticks, vertical bars, torn-paper strips, grain, and archival frame lines
- asymmetric layouts with one large quiet void and one active signal edge
- no cheap neon glow, rainbow gradient, generic grid wallpaper, or cyberpunk dashboard clichés

Framework choice comes after the style logic is understood.

The original reference is an Astro site, but the bundled examples are framework-neutral HTML and CSS so they can be translated into another stack.

Use `DESIGN.md` as the single design truth source. Treat this file as the operational wrapper around it.

## Expected Output

A strong result should feel like a composed technical journal:

- serif headlines carry gravity
- monospaced metadata keeps the system precise
- warm text sits on nearly black paper
- blue, green, ember, and gold signals appear as restrained accents
- lists behave like editorial streams, not grid-heavy marketing cards

In Signal Brutalist mode, a strong result should feel more authored and physical:

- background has multiple deliberate layers: matte paper, grain, slab geometry, edge registers, and 1-3 signal bars
- blue / green / ember are clearly visible but used as structural ink, not glow effects
- small text uses tilted, stamped, or boxed treatments sparingly so it feels like field labels rather than filler
- white/light pages may be warmer and more graphic; dark pages must stay clean, flat, and expensive

## Guardrails

- Keep the serif / mono / calm sans hierarchy intact.
- Keep the first-screen rail-versus-manifest split legible.
- Prefer rails, ranked lists, and thin borders over card-heavy layouts.
- Preserve signal colors as editorial marks; even in Signal Brutalist mode, do not turn the style into bright cyber UI.
- Do not use ugly multi-color CSS gradients or generic grid backgrounds on dark pages. Prefer matte SVG/background layers, hard-edge slabs, low-alpha grain, and precise signal bars.
