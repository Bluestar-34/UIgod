# UIgod MOC

## Goal

UIgod is an agent-invoked style extraction meta-skill.

It should be discovered from natural user requests and run by the AI agent, not operated as a manual checklist.

Its first job is to read user-supplied design references and produce or upgrade a reusable child skill that captures a specific web style family.

## Core Files

- [SKILL.md](SKILL.md): agent trigger metadata and execution protocol
- [agents/openai.yaml](agents/openai.yaml): UI metadata and implicit invocation policy
- [docs/CONTRACT.md](docs/CONTRACT.md): child-skill shape, `DESIGN.md` contract, and acceptance gate
- [docs/REFERENCE-ANALYSIS-GUIDE.md](docs/REFERENCE-ANALYSIS-GUIDE.md): compact extraction guide for URLs, screenshots, code, and briefs

## Workspace

- `inputs/`: user-supplied URLs, notes, screenshots, copied snippets
- `skills/`: finalized or in-progress child skills, each led by `DESIGN.md`
- `skills/_template-web-style-skill/`: copyable child-skill starter package
- `tools/extract_style_evidence.py`: URL/local HTML evidence collector for CSS/token extraction
- `tools/validate_child_skill.py`: contract validator for generated child skills
- `skills/lonely-blue-field-notes/`: first live child-skill trial based on `neurohack.blue`
- `prototypes/`: experiments before they become stable skill behavior

## Current Focus

1. Keep UIgod valid as an automatically invokable Codex skill.
2. Normalize child skills around a compact `DESIGN.md`-first contract.
3. Keep `DESIGN.md`, `SKILL.md`, preview, provenance, and examples sharply separated.
4. Validate the workflow with a live reference site and a working example output.
