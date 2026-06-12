# UIgod PRD

## 1. Product Positioning

UIgod is a style-reference meta-skill for web design work.

It accepts design references such as URLs, screenshots, copied code fragments, and textual style descriptions, then produces either:

- an upgraded existing child skill, or
- a brand-new child skill

The child skill is not a rigid page generator. It is a reusable style reference package that helps other agents understand and recreate a specific web design family with high fidelity.

## 2. Problem

Today, strong visual references are often trapped inside:

- a single website the user likes
- a screenshot with no source code
- scattered notes about typography, layout, and tone
- one-off prompts that cannot be reused later

This makes good design direction fragile. Each new generation starts from scratch and style quality drifts quickly.

## 3. Product Goal

Turn one-off design inspiration into a reusable child skill that preserves a specific web style family and can guide future website or web app generation.

## 4. Non-Goals

UIgod v1 does not aim to:

- become a universal website builder
- support all surfaces at once such as mobile, dashboard, deck, and native app
- require a strict intermediate manifest before child-skill generation
- force child skills to follow a rigid page-generation workflow
- depend on screenshot tooling to be available in every agent
- require full original website source code

## 5. First Release Scope

The first release is limited to web pages and web interfaces.

Child skills produced by UIgod should:

- represent one style family only
- focus on web output only
- provide style understanding rather than fixed page recipes
- include decomposed code references
- remain useful even when the user provides only a screenshot

## 6. Core Users

### 6.1 Builder-Designer

Someone who sees strong design references online and wants to turn them into reusable creative infrastructure.

### 6.2 Agent Operator

Someone who wants future agents to generate work in a recognizable style without restating the same visual guidance every time.

## 7. Inputs

UIgod should accept any combination of the following:

- one or more reference URLs
- one or more user-provided screenshots
- copied HTML, CSS, JSX, or component snippets
- plain-text design direction from the user

Input count is decided by the user.

Interpretation rule:

- single reference: preserve more of that reference's specific character
- multiple references: extract shared traits and reduce one-off noise

## 8. Core Output

UIgod outputs a child skill package.

That child skill should act as a style reference system for other agents, not a locked template engine.

The child skill should help other agents understand:

- what makes the style distinctive
- which layout patterns belong to the style
- which component constructions feel native to the style
- which code expressions best represent the style
- which moves would break the style

## 9. Child Skill Product Principles

### 9.1 Style First

The child skill is led by style understanding, not framework dogma.

### 9.2 Single Style Family

Each child skill captures one coherent style family only.

### 9.3 Web Only for v1

Do not mix mobile, native app, deck, and dashboard concerns into the first version unless the project scope changes.

### 9.4 Decomposed Code Reference Over Monolithic Source

The child skill should primarily provide decomposed, synthesized reference code, such as:

- nav
- hero
- section systems
- card or list systems
- form patterns
- footer or closing blocks
- type, spacing, and color implementation details

### 9.5 Synthesized Over Literal Reconstruction

Because original source is usually unavailable, the child skill should synthesize representative code patterns instead of pretending to reproduce the exact source.

### 9.6 Screenshot Optional, Not Required

If the user provides screenshots, they improve understanding.

If screenshot support is unavailable, the system must still work from URLs, code snippets, and text.

## 10. Primary Workflow

### 10.1 Intake

Collect user references and normalize the request.

### 10.2 Match Existing Child Skills

Before generating a new child skill, UIgod should check whether the reference appears close to an existing skill in the local library.

### 10.3 Upgrade vs New

If the reference is close enough to an existing skill, UIgod should prefer upgrading that skill.

If the difference is large enough, UIgod should propose creating a new one.

Before either action, UIgod should confirm the direction with the user.

### 10.4 Generate Child Skill Package

Produce a reusable child skill with a unified structure and high-quality style references.

## 11. Functional Requirements

### FR-1 Reference Intake

UIgod must accept URL, screenshot, copied code, and text description as valid inputs.

### FR-2 Reference Count Flexibility

UIgod must support both single-reference and multi-reference sessions.

### FR-3 Existing Skill Matching

UIgod should review existing child skills before deciding whether to create a new one.

### FR-4 User Confirmation

UIgod must ask the user to confirm when it wants to upgrade an existing child skill or create a new one.

### FR-5 Child Skill Scope Control

UIgod must keep each child skill constrained to one style family.

### FR-6 Web-Limited Output

UIgod v1 must produce child skills aimed at web work only.

### FR-7 Code-Centric Reference Package

UIgod must include code references as a required part of each child skill.

### FR-8 Decomposed Reference Structure

UIgod should prefer decomposed component and section examples over a single large page dump.

### FR-9 Screenshot Independence

UIgod must not fail purely because screenshot capability is unavailable.

### FR-10 Synthesized Style Translation

UIgod should synthesize representative code and guidance even when exact source code is unavailable.

## 12. Child Skill Deliverable Contract

Each generated child skill should follow one shared structure.

The first stable contract is:

- `DESIGN.md`
- `README.md`
- `SKILL.md`
- `preview.html`
- `references/source-observations.md`
- `references/source-screenshots-or-notes/`
- `examples/README.md`
- `references/code-patterns/`
- `examples/applied/`

Boundary rules:

- `DESIGN.md` is the canonical design truth and should remain compatible with `awesome-design-md` style entries.
- `SKILL.md` is the operational wrapper for agents and should stay shorter than `DESIGN.md`.
- `README.md` is a short human-facing summary.
- `preview.html` is the local visual inspection surface.
- `references/source-observations.md` records what was observed, what was synthesized, and what remains uncertain.
- `references/source-screenshots-or-notes/` stores optional source evidence and must not be treated as template material.
- `references/code-patterns/` stores reusable component and section snippets.
- `examples/applied/` stores confirmed examples generated by using the child skill on new prompts.

Optional:

- `assets/user-supplied/`
- `preview.png`

## 13. Quality Requirements

### QR-1 Distinctiveness

The child skill should feel tied to a specific design family, not generic "high-end UI" language.

### QR-2 Transferability

Another agent should be able to apply the child skill to a new website request without needing the original references again.

### QR-3 Restraint

The child skill should not overfit to one exact page layout if the user's intent is broader than that layout.

### QR-4 Code Usefulness

Reference code should be short, representative, and reusable.

### QR-5 Style Boundaries

The child skill should clearly explain what belongs and what does not belong to the style family.

### QR-6 Boundary Cleanliness

`DESIGN.md` and `SKILL.md` should have cleanly separated responsibilities so the design core is not scattered across multiple files.

### QR-7 Inspectability

Another agent should be able to inspect the style through both code examples and a quick preview surface without needing the original reference page.

### QR-8 Applied Transfer

The initial child skill should prioritize `DESIGN.md`, `preview.html`, and source evidence.

Applied examples are added after the child skill has generated a fresh page for a new prompt and that output has been visually confirmed.

Applied examples must not imitate or reconstruct the source site. They should preserve style while using the information architecture appropriate to the requested site type.

If the user does not specify a validation target, the default applied example should be a fictional personal portfolio at `examples/applied/portfolio/index.html`.

## 14. Out of Scope for Now

These may matter later, but they are not the current development priority:

- a formal style index implementation
- fully automated similarity scoring
- heavy extraction scripts
- non-web child skills
- automatic screenshot capture pipeline
- fully deterministic skill compilation

## 15. Success Criteria

UIgod v1 is successful when:

- a user can provide one or more design references
- UIgod can decide whether to upgrade an existing child skill or create a new one
- the choice is confirmed with the user
- the produced child skill represents one clear web style family
- the child skill includes decomposed code references
- `preview.html` demonstrates source-style capture at token and motif level
- confirmed applied examples demonstrate style transfer when present
- another agent can use that child skill as a strong style guide for a new web generation task

## 16. Open Questions

- How should existing child skills be indexed and surfaced during matching?
- How much source-site implementation detail is worth preserving when style-first synthesis conflicts with technical fidelity?
- When should UIgod create optional helper scripts, given that scripting support may vary across agents?
