---
name: style-manager
description: Lists, selects, and applies UIgod-managed web, image and video style packages without installing each style as a separate Codex skill. Use when the user asks to list available styles, choose a saved UI style, use the style library, apply a specific managed style, or generate a web page with a preferred/default style.
---

# Style Manager

Style Manager is the visible entry point for the bundled UIgod style library.

It keeps individual style packages inside `styles/<style-name>/` so users get one catalog entry point while agents can still discover nested style skills. Each managed style is agent-readable through `DESIGN.md`, `SKILL.md`, source notes, code patterns, previews, and examples.

## Quick Start

When the user asks to list or choose a style, run:

```bash
python skills/style-manager/tools/list_styles.py
```

When the user asks to build or restyle something with a managed style:

1. Select the style.
2. Read `styles/<style-name>/DESIGN.md`.
3. Read `styles/<style-name>/SKILL.md`.
4. Consult `references/source-observations.md` and `references/code-patterns/` only when implementation detail is needed.
5. Build fresh content in that style. Do not clone the original reference site.

## Selection Rules

- If the user names a style, use that style.
- If the user asks to choose, list styles with short descriptions and wait for their choice.
- If the user gives a project brief but no style choice, infer the best match from the brief.
- If there is no useful signal, use `preferences.json` when present.
- If no user preference exists, use the default from `preferences.example.json`.

Use the helper for non-interactive selection:

```bash
python skills/style-manager/tools/list_styles.py --choose --prefer "portfolio dark editorial"
```

## Preference File

Optional user preferences live at `skills/style-manager/preferences.json`.

Use `preferences.example.json` as the schema. Preferences are hints, not hard rules. A direct user style choice always wins.

## Managed Style Package

Each managed style uses this structure:

```text
styles/<style-name>/
+-- SKILL.md
+-- DESIGN.md
+-- preview.html
+-- references/
|   +-- source-observations.md
|   +-- code-patterns/
+-- examples/
    +-- index.html
```

Nested `SKILL.md` files are intentional: they let agents recognize specific styles directly when nested skill scanning is enabled. `style-manager` remains the human-friendly list/selection layer.

## Output Behavior

When listing styles, show:

- style id
- human name
- one-sentence style summary
- preview/example path when available

When applying a style, briefly name the selected style and why it fits before building.

## Video and prompt library

In the full repo, read ../../catalog.json for media, aliases and verification status. Match an explicit Chinese alias such as 灰度思维 to neuroblue-halftone-motion. If catalog.json is unavailable in a two-skill installation, list styles/ and read the selected style.json and DESIGN.md. Do not choose a web-only style as an already verified video style.

Apply the style to the latest user script; preserve visual and motion grammar while changing content. Video defaults: narration, at least one minute, actual t=0 first-frame approval before full production, no HyperFrames. Avoid decorative small labels, HUD and Unicode arrow decorations in the library frontend. Read the style's Known Gaps; sample-verified is not user-approved full production.

## Imported references and user curation

In the full repository, catalog.json includes collections/ external-reference entries beyond styles/. Read prompt_file for the original prompt and preserve author, source and prompt_partial. Do not apply the full style-package contract to an imported reference or claim it was visually validated. curation.json records only user-picked favorites; default browsing is all. A favorite is a preference, not a verification status.
