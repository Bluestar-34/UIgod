# UIgod

UIgod is one of the two default installed coordinator skills for this repository.

It turns website URLs, screenshots, copied HTML/CSS, and style briefs into managed style packages. Install UIgod together with `style-manager`; generated styles stay under `skills/style-manager/styles/` and keep nested `SKILL.md` files for style-level recognition.

## What This Skill Does

1. Captures source evidence from a reference.
2. Extracts CSS tokens, theme state, typography, shape, layout, interaction, and asset facts.
3. Distills the evidence into a portable `DESIGN.md`.
4. Creates a managed `skills/style-manager/styles/<style-name>/` package with `SKILL.md`, `preview.html`, `references/`, and `examples/index.html`.
5. Validates the child skill with the bundled contract checker.

## Bundled Files

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Main agent instructions |
| [docs/CONTRACT.md](docs/CONTRACT.md) | Required child-skill contract |
| [docs/REFERENCE-ANALYSIS-GUIDE.md](docs/REFERENCE-ANALYSIS-GUIDE.md) | Evidence extraction protocol |
| [tools/extract_style_evidence.py](tools/extract_style_evidence.py) | URL/local HTML evidence extractor |
| [tools/validate_child_skill.py](tools/validate_child_skill.py) | Child-skill validator |
| [templates/web-style-skill/](templates/web-style-skill/) | Starter resource for generated managed styles |

## Default Boundary

- Install: `skills/uigod/` and `skills/style-manager/`
- Generate: `skills/style-manager/styles/<style-name>/`
- Allow nested recognition: generated managed styles keep `SKILL.md`

This keeps the active skill list small while preserving a reusable style library beside UIgod.
