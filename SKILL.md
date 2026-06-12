---
name: uigod
description: Creates or upgrades reusable web style-reference skills from user-provided design references such as URLs, screenshots, copied code, or written style notes. Use when the user wants to turn a refined website or UI style into a reusable Codex skill for future web generation.
---

# UIgod

UIgod turns design references into reusable web style-reference skills.

It does not primarily generate a website. Its job is to create or upgrade a child skill that lets future agents understand and reproduce one specific web style family with minimal drift.

## Use When

Use UIgod when the user wants to:

- turn a website, screenshot, or code fragment into a reusable style skill
- upgrade an existing style skill instead of starting from zero
- preserve a design language for future web work

## Inputs

Accept any mix of:

- reference URLs
- user-provided screenshots
- copied HTML, CSS, JSX, or component snippets
- textual descriptions of the desired style

Interpretation rule:

- one reference: preserve more of its specific character
- multiple references: extract shared traits and ignore one-off noise

## Core Workflow

### Phase A — Intake & Analysis

1. **Understand the style target** and the intended web use case.
2. **Extract CSS tokens from the reference** (see `docs/REFERENCE-ANALYSIS-GUIDE.md`):
   - For URL references: fetch the page's CSS and extract custom properties, font-face declarations, border-radius patterns, box-shadow values, border widths, background colors per section, and typography scale (clamp/px values).
   - For screenshot-only references: infer these values from the visual, but mark all as `[inferred]` in source-observations.md.
   - For code snippets: extract values directly from the provided code.
   - Document all extracted values in `references/source-observations.md` under a dedicated `## CSS Extraction` section.
3. **Cross-check extracted tokens** before proceeding:
   - Compare extracted CSS values against what the DESIGN.md will declare.
   - If only screenshots are available, note all uncertainties explicitly.
   - If a URL was provided but CSS was not fetched, do not proceed — fetch it first.

### Phase B — Skill Decision

4. **Inspect existing child skills** for a close match.
5. If a near match exists, propose upgrading it.
6. If the style is clearly different, propose creating a new child skill.
7. **Ask the user to confirm** the direction before editing the library.

### Phase C — Generation

8. **Generate or update the child skill** using the standard `DESIGN.md`-first skeleton.
   - Every token in DESIGN.md frontmatter must trace back to an extracted CSS value or be explicitly marked as synthesized.
   - Do not guess hex values, font stacks, or spacing units — use the extracted data.

### Phase D — Validation

9. **Run reference-accuracy validation** before accepting the skill:
   - Verify DESIGN.md tokens against the CSS extraction notes.
   - Confirm section background colors, border treatments, typography scale, and button styles match the reference.
   - If discrepancies are found (like the first studiobrot attempt), fix them before proceeding.
10. **Validate internal consistency**: confirm that `DESIGN.md`, `preview.html`, source evidence, and any confirmed applied examples all express the same style family.

## Child Skill Contract

Each child skill should represent one web style family and use this structure:

```text
child-skill-name/
├── DESIGN.md
├── README.md
├── SKILL.md
├── preview.html
├── references/
│   ├── source-observations.md
│   ├── source-screenshots-or-notes/
│   └── code-patterns/
└── examples/
    ├── README.md
    └── applied/
```

## File Boundaries

- `DESIGN.md`: canonical design truth, compatible with `awesome-design-md` style entries; declares the style's default representative page type
- `SKILL.md`: concise operational wrapper for agents
- `README.md`: human-facing summary and preview notes
- `references/source-observations.md`: provenance, extraction notes, and uncertainty
- `references/source-screenshots-or-notes/`: optional source screenshots, copied public notes, or user-provided evidence; this is evidence, not template material
- `references/code-patterns/`: reusable component and section snippets that show implementation mechanics; these are references, not validation examples
- `preview.html`: token specimen page (colors, typography, shapes, motifs) rendered with the style's own tokens; this is the primary first-pass visual validation surface
- `examples/applied/`: confirmed examples produced by using this child skill on new user requests; do not place source-site replicas here

Do not split the design core back into `style-notes.md`, `component-breakdown.md`, and `do-dont.md`.

## Authoring Priorities

- Style first, framework second.
- Web only for the first version.
- Prefer decomposed code references over one whole-page source dump.
- Prefer synthesized representative code over fake source reconstruction.
- Do not clone or replicate the source site as a child-skill example.
- Screenshots are helpful when supplied, but not required.
- Avoid vague "premium UI" language; name the specific visual behavior.
- During initial skill creation, prioritize `DESIGN.md`, `preview.html`, and source evidence before examples.
- Add `examples/applied/` only after the new skill has been used on a fresh prompt and the result is visually confirmed.
- If an example is needed, generate a new information architecture for the requested page type while preserving the extracted style.
- If the user does not specify an applied validation target, use a fictional personal portfolio at `examples/applied/portfolio/index.html`.
- The default portfolio should include hero, navigation, project cases, capability/workflow section, experience or notes, contact CTA, responsive behavior, and at least one style-defining motif.

## Required Output Quality

A generated child skill is ready only when another agent can:

- quickly understand the style family from `DESIGN.md`
- scan the palette, type system, and shapes through `preview.html`
- inspect source evidence without treating it as a template
- see how the style appears in code through code patterns and confirmed applied examples when available
- reuse the package for a new web page without re-reading the original reference
- avoid obvious drift using sharp do/don't guidance

**Reference-accuracy rule:** Every token in `DESIGN.md` (colors, font stacks, border radii, spacing, shadows) must be verifiable against the CSS extraction in `source-observations.md`. If a token was synthesized rather than extracted, it must be explicitly labeled. If the reference was a URL but CSS was not fetched and analyzed, the child skill is not ready.

## Reference Documents

Use these project docs when developing UIgod itself:

- `docs/PRD.md`
- `docs/DEV-PLAN.md`
- `docs/DESIGN-MD-SPEC.md`
- `docs/CHILD-SKILL-SKELETON.md`
- `docs/REFERENCE-ANALYSIS-GUIDE.md`
- `docs/REFACTOR-PLAN.md`
- `docs/QUALITY-CHECKLIST.md`
- `docs/MIGRATION-CHECKLIST.md`
