---
name: lonely-blue-field-notes
description: Guides web design toward a dark editorial technical-journal style with warm serif headlines, monospaced metadata, split profile-and-manifest layouts, signal-color accents, and stream-like content lists. Use when the user wants a personal site, technical blog, research journal, security writeup hub, or reflective creator web presence that feels intimate, rigorous, and quietly cinematic.
---

# Lonely Blue Field Notes

This child skill captures a dark editorial web style derived from a personal technical writing site.

It is designed for web work that should feel like private field notes rather than a polished SaaS dashboard or a loud cyberpunk landing page.

Default representative page type: a personal technical journal homepage (profile rail + manifesto + ranked writing stream). When the user does not specify a page type, generate this one.

## Use When

Use this skill for:

- personal technical blogs
- security writeup hubs
- AI experiment journals
- reflective creator homepages
- research notebooks with strong visual atmosphere

## Read First

- `DESIGN.md` for the canonical design system
- `references/source-observations.md` for the reference-site extraction notes
- `references/code-patterns/` for reusable fragments
- `examples/applied/` for confirmed transfer examples
- `preview.html` for a quick token scan

## Style Priority

Preserve the emotional mix:

- solitary
- technically literate
- low-noise
- warm against dark
- editorial rather than product-marketing

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

## Guardrails

- Keep the serif / mono / calm sans hierarchy intact.
- Keep the first-screen rail-versus-manifest split legible.
- Prefer rails, ranked lists, and thin borders over card-heavy layouts.
- Preserve sparse signal colors; do not turn the style into bright cyber UI.
