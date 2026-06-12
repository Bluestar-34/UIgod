# UIgod MOC

## Goal

UIgod is a style-oriented meta-skill project.

It does not primarily generate websites.

Its first job is to read user-supplied design references and produce or upgrade a reusable child skill that captures a specific web style family.

## Docs

- [SKILL.md](SKILL.md): draft UIgod meta-skill instructions
- [docs/PRD.md](docs/PRD.md): product requirements and scope
- [docs/DEV-PLAN.md](docs/DEV-PLAN.md): development phases and implementation prep
- [docs/REFACTOR-PLAN.md](docs/REFACTOR-PLAN.md): concrete initial-refactor rollout plan
- [docs/QUALITY-CHECKLIST.md](docs/QUALITY-CHECKLIST.md): child-skill acceptance gate
- [docs/MIGRATION-CHECKLIST.md](docs/MIGRATION-CHECKLIST.md): old-to-new migration checklist
- [docs/DESIGN-MD-SPEC.md](docs/DESIGN-MD-SPEC.md): canonical `DESIGN.md` contract
- [docs/CHILD-SKILL-SKELETON.md](docs/CHILD-SKILL-SKELETON.md): required shape of generated child skills
- [docs/DECISIONS.md](docs/DECISIONS.md): current product decisions and rationale

## Workspace

- `inputs/`: user-supplied URLs, notes, screenshots, copied snippets
- `outputs/`: generated child skill drafts and review artifacts
- `skills/`: finalized or in-progress child skills, each led by `DESIGN.md`
- `skills/_template-web-style-skill/`: copyable child-skill starter package
- `skills/lonely-blue-field-notes/`: first live child-skill trial based on `neurohack.blue`
- `tools/`: optional helper scripts and utilities
- `prototypes/`: experiments before they become stable skill behavior

## Current Focus

1. Define UIgod as a web-style child-skill generator.
2. Normalize child skills around a canonical `DESIGN.md`.
3. Keep `DESIGN.md`, `SKILL.md`, preview, provenance, and examples sharply separated.
4. Validate the workflow with a live reference site and a working example output.
