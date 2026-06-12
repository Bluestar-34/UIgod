#!/usr/bin/env python3
"""Validate a UIgod child skill against the lean contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_PATHS = [
    "SKILL.md",
    "DESIGN.md",
    "preview.html",
    "references/source-observations.md",
    "references/code-patterns",
    "examples/index.html",
]

DESIGN_SECTIONS = [
    "Overview",
    "Use Cases",
    "Signature Moves",
    "Colors",
    "Typography",
    "Layout",
    "Components",
    "Depth, Borders & Shapes",
    "Motion & Interaction",
    "Responsive Behavior",
    "Do's and Don'ts",
    "Prompt Guide",
    "Known Gaps",
]

OBSERVATION_SECTIONS = [
    "Sources",
    "Capture Method",
    "CSS Files",
    "Theme Detection",
    "Extracted Tokens",
    "Signature Moves",
    "Extracted vs Inferred vs Synthesized",
]

PLACEHOLDER_RE = re.compile(r'\b(?:Replace this|TODO|TBD|\[STYLE LABEL\])\b', re.I)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def markdown_headers(text: str) -> set[str]:
    return {match.group(1).strip() for match in re.finditer(r'^##\s+(.+?)\s*$', text, re.M)}


def check_html(path: Path) -> bool:
    text = read_text(path).lower()
    return "<html" in text and "</html>" in text


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a UIgod child skill folder.")
    parser.add_argument("skill_dir", help="Path to child skill folder")
    parser.add_argument("--allow-template", action="store_true", help="Allow placeholders and missing transfer example in the template skill")
    args = parser.parse_args()

    root = Path(args.skill_dir)
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        print(f"FAIL: missing folder {root}")
        return 2

    for rel in REQUIRED_PATHS:
        path = root / rel
        if not path.exists():
            if args.allow_template and rel == "examples/index.html":
                warnings.append("template has no examples/index.html yet")
                continue
            errors.append(f"missing required path: {rel}")

    skill_md = root / "SKILL.md"
    design_md = root / "DESIGN.md"
    observations_md = root / "references/source-observations.md"
    preview_html = root / "preview.html"
    example_html = root / "examples/index.html"

    if skill_md.exists():
        text = read_text(skill_md)
        if not has_frontmatter(text):
            errors.append("SKILL.md missing YAML frontmatter")
        if "DESIGN.md" not in text:
            warnings.append("SKILL.md does not mention DESIGN.md")
        if "source-observations.md" not in text:
            warnings.append("SKILL.md does not mention source-observations.md")
        if PLACEHOLDER_RE.search(text) and not args.allow_template:
            errors.append("SKILL.md still contains placeholders")

    if design_md.exists():
        text = read_text(design_md)
        if not has_frontmatter(text):
            errors.append("DESIGN.md missing YAML frontmatter")
        headers = markdown_headers(text)
        for section in DESIGN_SECTIONS:
            if section not in headers:
                errors.append(f"DESIGN.md missing section: {section}")
        if PLACEHOLDER_RE.search(text) and not args.allow_template:
            errors.append("DESIGN.md still contains placeholders")

    if observations_md.exists():
        text = read_text(observations_md)
        headers = markdown_headers(text)
        for section in OBSERVATION_SECTIONS:
            if section not in headers:
                warnings.append(f"source-observations.md missing section: {section}")
        if PLACEHOLDER_RE.search(text) and not args.allow_template:
            errors.append("source-observations.md still contains placeholders")

    for html_path, label in [(preview_html, "preview.html"), (example_html, "examples/index.html")]:
        if html_path.exists() and not check_html(html_path):
            errors.append(f"{label} does not look like a complete HTML document")

    if (root / "examples/applied").exists():
        errors.append("old examples/applied structure exists; use examples/index.html")

    if list(root.glob("*.zip")):
        warnings.append("zip file found inside child skill; package only when explicitly requested")

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"FAIL: {error}")

    if errors:
        return 1
    print(f"PASS: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
