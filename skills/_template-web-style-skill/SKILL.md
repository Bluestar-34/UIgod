---
name: template-web-style-skill
description: Reusable template for a generated web style-reference child skill with a DESIGN.md core. Use as a starting point when UIgod creates a child skill from website, screenshot, code, or written style references.
---

# Template Web Style Skill

Replace this template with the specific style family name and description.

This child skill helps agents understand and reproduce one coherent web style family. It is not a rigid page generator.

## Use When

Use this skill when the user asks for a website or web interface in this specific style family.

Default representative page type: replace with the page type this style expresses best; generate it when the user does not specify one.

## Read First

1. `DESIGN.md` for the style system
2. `references/source-observations.md` for extraction notes
3. `references/code-patterns/` for reusable snippets
4. `preview.html` for a quick visual scan
5. `examples/index.html` for transfer proof

## Style Priority

Preserve the style's visual grammar before choosing a framework.

Start from the `Signature Moves` section in `DESIGN.md`; a strong output should visibly preserve most of those moves.

If a project has an existing framework, translate the examples into that framework while keeping the style logic intact.

## Output Expectations

Generated web work should feel native to this style family without copying one exact reference page.

When consulting examples, study visual decisions, spacing, component behavior, and interaction density. Do not copy page structure unless the user explicitly asks to reproduce that exact structure.
