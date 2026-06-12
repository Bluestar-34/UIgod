# UIgod DESIGN.md Spec

## Goal

UIgod child skills should use `DESIGN.md` as the canonical design system document.

The structure should stay compatible with the `awesome-design-md` style of entry so a child skill can be read both as:

- a standalone design system document
- the design core inside a richer agent-ready package

## Compatibility Position

UIgod borrows these strengths from `awesome-design-md`:

- one canonical design document per style
- stable section order
- explicit tokens and component guidance

UIgod adds a surrounding execution package:

- `SKILL.md` for agent usage
- `preview.html` for visual inspection
- `references/source-observations.md` for provenance
- `references/source-screenshots-or-notes/` for optional source evidence
- `references/code-patterns/` for reusable code evidence
- `examples/` for confirmed applied outputs

## Required Structure

Each child skill should contain:

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

## DESIGN.md Rules

### 1. Frontmatter

Include:

- `version`
- `name`
- `description`
- structured tokens for colors, typography, rounded, spacing
- component token entries when relevant

### 2. Required Sections

Every `DESIGN.md` should include these headings in this order:

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`
9. `## Responsive Behavior`
10. `## Iteration Guide`
11. `## Known Gaps`

Keep empty filler out. If a section is light, keep it brief but still present.

## File Boundaries

### DESIGN.md

Holds the canonical style truth.

Do not duplicate the whole document into `SKILL.md`.

### README.md

Holds a short human-facing explanation:

- what this style is
- where it came from
- what files matter
- how to preview it

### SKILL.md

Holds the agent usage layer:

- trigger conditions
- when to use the style
- which files to read first
- what to preserve while generating

### source-observations.md

Holds the extraction trail and uncertainty notes.

### source-screenshots-or-notes/

Holds optional source evidence such as screenshots, user-supplied notes, captured page text, URL/date records, and viewport notes. It is evidence, not a template.

### references/code-patterns/

Holds synthesized component and section snippets that demonstrate implementation mechanics.

These files are references, not validation examples and not page templates.

### examples/

Holds confirmed applied examples only. Applied examples are produced after using the child skill on a new prompt and confirming the result.

### preview.html

A token specimen page: color swatches, type specimens, and shape samples rendered from the `DESIGN.md` tokens with the style's own fonts and colors.

During initial skill creation, `preview.html` is the primary visual proof that the design tokens and motifs were captured.

`preview.html` should behave more like a `getdesign.md` design-system scan than a miniature page build.

### examples/applied/

Applied examples are optional at initial creation and become required only when publishing a validated use case.

They must be generated with the child skill on a fresh site/app request.

They must not clone the source site. They should demonstrate transfer: same style family, new information architecture.

Default applied validation page:

- Use `examples/applied/portfolio/index.html` when the user does not specify another target.
- Make the content fictional, realistic, and clearly different from the source site.
- Stress-test hero, navigation, project cards, capability/workflow sections, experience or notes, CTA, responsive behavior, and one style-defining motif.

## Quality Bar

A child skill is migration-complete only when:

- `DESIGN.md` can be read on its own and still explain the style well
- `DESIGN.md` declares the default representative page type for the style
- `SKILL.md` is shorter and more operational than `DESIGN.md`
- `preview.html` shows token specimens that match `DESIGN.md`
- source notes explain what was observed versus synthesized
- another agent can reproduce the style direction without reopening the original source reference
- confirmed applied examples, when present, demonstrate style transfer rather than source replication
