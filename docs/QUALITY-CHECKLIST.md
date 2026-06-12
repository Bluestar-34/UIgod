# UIgod Quality Checklist

Use this checklist before treating a child skill as ready.

## 1. Package Completeness

- [ ] `DESIGN.md` exists
- [ ] `README.md` exists
- [ ] `SKILL.md` exists
- [ ] `preview.html` exists
- [ ] `references/source-observations.md` exists
- [ ] `references/source-screenshots-or-notes/` exists, even if it only contains a README
- [ ] `references/code-patterns/` contains representative fragments when code snippets are available
- [ ] `examples/README.md` explains that applied examples are post-validation artifacts
- [ ] `examples/applied/` contains confirmed examples only when they have been generated and visually accepted

## 2. Boundary Integrity

- [ ] `DESIGN.md` is the canonical design truth
- [ ] `SKILL.md` stays operational and shorter than `DESIGN.md`
- [ ] `README.md` stays human-facing instead of duplicating the full design system
- [ ] provenance notes stay in `references/source-observations.md`
- [ ] the package does not fall back to `style-notes.md`, `component-breakdown.md`, or `do-dont.md` as the core design contract

## 3. Reference Accuracy (CSS-Level)

This section is **mandatory when a URL was provided as reference**. It verifies that the child skill's tokens actually match the source CSS.

- [ ] CSS extraction was performed per `docs/REFERENCE-ANALYSIS-GUIDE.md` (Section 1)
- [ ] extracted CSS custom properties, font faces, border-radius, box-shadow, border-width values are documented in `source-observations.md`
- [ ] section background colors are mapped and documented (✓ = every section mapped)
- [ ] typography scale (all font-size declarations including clamp values) is documented
- [ ] interactive behaviors (hover, transitions, cursors) are documented
- [ ] DESIGN.md frontmatter tokens (colors, typography, rounded, spacing) match the extracted CSS values; or discrepancies are explicitly noted as synthesized
- [ ] every DESIGN.md token can be traced back to a CSS extraction note or explicitly marked as synthesized
- [ ] if any token was approximated (screenshot-only input), it is marked `[inferred]` in source-observations.md

## 4. Style Specificity

- [ ] the style reads as one coherent family
- [ ] typography, color, spacing, and layout behavior are concrete rather than generic
- [ ] do/don't guidance is sharp enough to prevent obvious drift
- [ ] the document could still guide a build when the only original input was a screenshot

## 5. Code Usefulness

- [ ] examples are synthesized and representative rather than fake source reconstruction
- [ ] code patterns are reusable in a fresh project
- [ ] no example clones or reconstructs the source site
- [ ] applied examples, if present, use fresh information architecture for the requested site type
- [ ] when no validation target was specified, the applied example is `examples/applied/portfolio/index.html`
- [ ] the default portfolio stress-tests hero, nav, project cases, capability/workflow section, experience or notes, contact CTA, responsiveness, and one style-defining motif
- [ ] applied examples feel like the same family as the code patterns
- [ ] future agents can use examples as style evidence without treating them as page templates

## 6. Preview Validation

- [ ] `preview.html` opens locally over `file://` without extra setup
- [ ] the token specimens (colors, typography, shapes) match `DESIGN.md` exactly
- [ ] specimens are rendered with the style's own fonts, colors, and radii
- [ ] the preview focuses on design tokens and motifs, not source-site page reconstruction
- [ ] the preview may link to confirmed applied examples when present

## 7. Provenance Honesty

- [ ] source references are listed clearly
- [ ] observed behavior is separated from inferred behavior
- [ ] known uncertainty is acknowledged
- [ ] source screenshots or notes are stored as evidence, not used as example templates

## 8. Acceptance Test

- [ ] another agent could generate a fresh web page in this style without reopening the original reference site
- [ ] `preview.html` verifies source-style capture at token and motif level
- [ ] a separate transfer test verifies generation on a different topic, defaulting to a fictional personal portfolio, before adding an applied example
