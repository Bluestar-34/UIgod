# UIgod Refactor Plan

## Goal

Complete the initial refactor from a fragmented note-based child-skill format to a `DESIGN.md`-led, agent-ready style library.

## Target State

The initial refactor is complete when UIgod has:

- one canonical child-skill contract
- clean boundaries between design truth and agent instructions
- at least one migrated template and one migrated live sample
- explicit migration and quality gates
- root docs that no longer describe the legacy three-file design split

## Version Control Guardrails

- Work on branch `codex/uigod-designmd-refactor`.
- Do not revert or stage unrelated changes outside `F:\Obsi-neuroBlue\05_项目\UIgod`.
- When staging or committing later, stage only `UIgod/...`.
- Keep migration changes grouped by intent: contract docs, child-skill migrations, validation assets.

## File Ownership Boundaries

- `DESIGN.md`: canonical design truth
- `SKILL.md`: operational wrapper for agents
- `README.md`: human-facing summary
- `preview.html`: quick local inspection surface
- `references/source-observations.md`: provenance and uncertainty record
- `references/source-screenshots-or-notes/`: optional source evidence, not template material
- `references/code-patterns/`: reusable fragments
- `examples/applied/`: confirmed transfer examples generated after using the skill

## Workstreams

### 1. Contract Normalization

Scope:

- root `SKILL.md`
- `docs/PRD.md`
- `docs/DECISIONS.md`
- `docs/DEV-PLAN.md`
- `docs/DESIGN-MD-SPEC.md`
- `docs/CHILD-SKILL-SKELETON.md`

Done means:

- all core docs describe the same child-skill structure
- no doc treats `style-notes.md`, `component-breakdown.md`, or `do-dont.md` as the canonical design core

### 2. Child-Skill Migration

Scope:

- `_template-web-style-skill`
- `lonely-blue-field-notes`

Done means:

- each package contains `DESIGN.md`, `README.md`, `SKILL.md`, `preview.html`, `references/source-observations.md`, and `examples/`
- legacy fragmented design-core files are removed

### 3. Validation Surfaces

Scope:

- local preview page
- optional preview image
- example fragments

Done means:

- the preview is nonblank and readable
- examples reflect the same style logic as `DESIGN.md`

### 4. Governance Layer

Scope:

- migration checklist
- quality checklist
- repo scan for legacy references

Done means:

- future child-skill migrations follow one repeatable checklist
- the repo has a clear acceptance bar for new entries

## Rollout Order

1. Lock the canonical contract in docs.
2. Migrate the template.
3. Migrate one live child skill.
4. Add governance checklists.
5. Sweep the repo for legacy references.
6. Verify the initial refactor against the new checklists.

## Quality Gates

The refactor should fail review if any of these are false:

- `DESIGN.md` is not the single design truth source
- `SKILL.md` repeats large parts of `DESIGN.md`
- preview and examples do not match the documented style
- provenance is missing or unclear
- the package reads like generic aesthetic prose instead of an actionable style system

## Current Status

- Contract normalization: in progress
- Child-skill migration: done for template and first live sample
- Validation surfaces: done for template and first live sample
- Governance layer: in progress

## After The Initial Refactor

The next layer of work should be:

- a searchable library index or catalog
- conventions for recording upgrades over time
- another child-skill migration to pressure-test generality
- lightweight match heuristics for upgrade-vs-new suggestions
