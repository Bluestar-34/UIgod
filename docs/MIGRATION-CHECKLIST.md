# UIgod Migration Checklist

Use this when upgrading an older child skill into the `DESIGN.md`-first contract.

## Legacy To New Mapping

- merge `references/style-notes.md` into `DESIGN.md`
- merge `references/component-breakdown.md` into `DESIGN.md` and `examples/`
- merge `references/do-dont.md` into `DESIGN.md`
- keep provenance in `references/source-observations.md`
- add `references/source-screenshots-or-notes/` for optional source evidence
- add `README.md`
- add `preview.html` as a token and motif specimen page from `DESIGN.md`
- preserve or improve reusable snippets under `references/code-patterns/`
- add `examples/README.md`
- move only confirmed transfer outputs into `examples/applied/`
- remove the legacy fragmented design-core files after consolidation

## Migration Steps

1. Read the old child skill and identify the true style family.
2. Consolidate the design core into `DESIGN.md`.
3. Rewrite `SKILL.md` so it becomes an operational wrapper instead of a parallel design doc.
4. Add or refresh `README.md`.
5. Add or refresh `references/source-observations.md`.
6. Add or refresh `references/source-screenshots-or-notes/`.
7. Add or refresh `preview.html`.
8. Check that examples still match the new design contract and do not clone the source site.
9. Delete obsolete legacy design-core files.
10. Run the [QUALITY-CHECKLIST.md](QUALITY-CHECKLIST.md).

## Current Migration Status

- [x] `skills/_template-web-style-skill`
- [x] `skills/lonely-blue-field-notes`

## Review Notes

- Migration is not complete until root docs also describe the new contract correctly.
- If a child skill cannot express the style well in `DESIGN.md`, refine the contract before migrating more entries.
