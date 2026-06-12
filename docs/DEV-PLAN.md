# UIgod Development Plan

## 1. Immediate Objective

Stabilize UIgod as a working `DESIGN.md`-led style-skill generator for web work.

The initial refactor is about locking:

- scope
- output contract
- documentation boundaries
- migration rules
- validation gates

## 2. Project Structure

```text
UIgod/
├── MOC.md
├── SKILL.md
├── docs/
│   ├── PRD.md
│   ├── DEV-PLAN.md
│   ├── DECISIONS.md
│   ├── DESIGN-MD-SPEC.md
│   ├── CHILD-SKILL-SKELETON.md
│   ├── REFACTOR-PLAN.md
│   ├── QUALITY-CHECKLIST.md
│   └── MIGRATION-CHECKLIST.md
├── inputs/
├── skills/
├── skills/
├── tools/
└── prototypes/
```

## 3. Phase Plan

### Phase 0 - Project Lock

Completed:

- create project workspace
- write PRD
- define child-skill contract

### Phase 1 - Root Skill Normalization

Completed:

- create the root `UIgod/SKILL.md`
- define intake and upgrade-vs-new behavior
- align the root skill with the `DESIGN.md`-first child-skill contract

### Phase 2 - Child Skill Template

Completed:

- define the canonical child-skill skeleton
- migrate `_template-web-style-skill`
- define file boundaries for `DESIGN.md`, `SKILL.md`, preview, examples, and provenance

### Phase 3 - Live Sample Migration

Completed:

- migrate `lonely-blue-field-notes`
- create a working `preview.html`
- generate a visual preview asset for validation
- confirm that design system, examples, and preview stay coherent

### Phase 4 - Governance Layer

Current phase:

- add migration and quality checklists
- rewrite remaining root docs that still describe the legacy three-file design split
- define the completion bar for the initial refactor

### Phase 5 - Library Expansion

Next:

- add a lightweight library index or catalog
- define how upgrades record what changed
- test the contract on a second visually different style family
- tighten match heuristics for upgrade-vs-new decisions

## 4. First Implementation Backlog

### P0 - Completed

- Define the canonical `DESIGN.md`-led child-skill skeleton
- Migrate the template child skill
- Migrate `lonely-blue-field-notes` to the new structure

### P1 - Current

- Tighten the `DESIGN.md` spec until another agent can use it without the original reference
- Add quality and migration checklists
- Remove legacy structure references from root docs
- Confirm the root skill contract matches the migrated child skills

### P2 - Next

- Add an initial library convention inside `skills/`
- Define how upgraded child skills record what changed
- Add lightweight tooling only if repeated manual work becomes painful
- Test the new contract against another sample style family

## 5. Development Rules

- Keep UIgod focused on web only until the first workflow is stable.
- Prefer canonical `DESIGN.md` over fragmented design notes.
- Prefer concise high-signal guidance over vague aesthetic prose.
- Prefer decomposed code examples over giant whole-page dumps.
- Treat screenshots as optional inputs, not mandatory infrastructure.
- Prefer synthesized style translation over pretending to clone exact source.
- Ask the user before upgrading an existing child skill or creating a new one.

## 6. Initial Refactor Exit Criteria

- [x] Workspace folder created
- [x] PRD written
- [x] Child-skill skeleton defined
- [x] UIgod root skill draft created
- [x] First child-skill template package created
- [x] First live reference-to-skill trial completed
- [x] Canonical `DESIGN.md` contract documented
- [x] Root docs fully purged of the legacy three-file design split
- [x] Migration and quality checklists added
- [x] Initial refactor verified by repo scan

## 7. After The Initial Refactor

The next useful implementation step is to make the child-skill library easier to search and maintain:

- add a small catalog or index
- formalize upgrade history conventions
- validate the contract on another style family
