#!/usr/bin/env python3
"""List and choose UIgod managed style packages."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "styles"
PREFERENCES = ROOT / "preferences.json"
PREFERENCES_EXAMPLE = ROOT / "preferences.example.json"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def first_overview(text: str) -> str:
    match = re.search(r"^## Overview\s*(.+?)(?:^## |\Z)", text, re.M | re.S)
    if not match:
        return ""
    for line in match.group(1).splitlines():
        line = line.strip()
        if line and not line.startswith("-"):
            return re.sub(r"\s+", " ", line)
    return ""


def load_preferences() -> dict:
    for path in (PREFERENCES, PREFERENCES_EXAMPLE):
        if path.exists():
            return json.loads(read_text(path))
    return {}


def style_info(path: Path) -> dict[str, str]:
    design = path / "DESIGN.md"
    text = read_text(design)
    fm = frontmatter(text)
    preview = ""
    for rel in ("examples/preview.png", "preview.png", "examples/preview-mobile.png"):
        if (path / rel).exists():
            preview = str(path.relative_to(ROOT) / rel).replace("\\", "/")
            break
    description = fm.get("description") or first_overview(text)
    return {
        "id": path.name,
        "name": fm.get("name") or path.name,
        "description": description,
        "preview": preview,
        "path": str(path.relative_to(ROOT)).replace("\\", "/"),
    }


def list_styles() -> list[dict[str, str]]:
    repo=ROOT.parents[1]
    if (repo/'catalog.json').exists():
        catalog=json.loads(read_text(repo/'catalog.json'))
        featured=json.loads(read_text(repo/'curation.json'))['featured_ids']
        entries=[e for e in catalog['entries'] if not e.get('hidden')]
        entries.sort(key=lambda e:(0 if e['id'] in featured else 1,featured.index(e['id']) if e['id'] in featured else -datetime.fromisoformat(e['added_at']).timestamp(),e['id']))
        return [{'id':e['id'],'name':e.get('display_name',e['name']),'description':e['summary'],'preview':e.get('preview_url') or e['path']+'/'+e['deliverables']['preview'],'path':e['path'],'media':e['media'],'content_type':e['content_type'],'kind':e['kind'],'status':e['status'],'featured':e['id'] in featured} for e in entries]
    if not STYLES_DIR.exists():
        return []
    styles = []
    for path in sorted(STYLES_DIR.iterdir(), key=lambda p: p.name):
        if path.is_dir() and (path / "DESIGN.md").exists():
            styles.append(style_info(path))
    return styles


def score_style(style: dict[str, str], prefer: str, preferences: dict) -> int:
    haystack = " ".join([style["id"], style["name"], style["description"]]).lower()
    score = 0
    for term in re.findall(r"[\w-]+", prefer.lower()):
        if term and term in haystack:
            score += 4
    for term in preferences.get("likes", []):
        if str(term).lower() in haystack:
            score += 1
    for term in preferences.get("avoid", []):
        if str(term).lower() in haystack:
            score -= 2
    if style["id"] == preferences.get("default_style"):
        score += 1
    return score


def choose_style(styles: list[dict[str, str]], prefer: str, preferences: dict) -> dict[str, str] | None:
    if not styles:
        return None
    if prefer:
        return max(styles, key=lambda style: score_style(style, prefer, preferences))
    default_style = preferences.get("default_style")
    for style in styles:
        if style["id"] == default_style:
            return style
    return styles[0]


def markdown_table(styles: list[dict[str, str]]) -> str:
    lines = ["| Style | Name | Summary | Preview |", "|---|---|---|---|"]
    for style in styles:
        summary = style["description"]
        if len(summary) > 160:
            summary = summary[:157].rsplit(" ", 1)[0].rstrip(" ,.;:") + "..."
        lines.append(
            f"| `{style['id']}` | {style['name']} | {summary} | {style['preview']} |"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="List or choose managed UIgod styles.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of Markdown.")
    parser.add_argument("--choose", action="store_true", help="Output one selected style.")
    parser.add_argument("--prefer", default="", help="Brief or preference text used for selection.")
    parser.add_argument('--media',default='',help='video, web, image or interactive')
    parser.add_argument('--search',default='',help='Search names, summaries and IDs')
    parser.add_argument('--featured',action='store_true',help='Only public maintainer picks')
    parser.add_argument('--limit',type=int,default=30,help='Maximum listed entries; 0 lists all')
    args = parser.parse_args()

    preferences = load_preferences()
    styles = list_styles()
    styles=[s for s in styles if (not args.media or args.media in s.get('media',[])) and (not args.featured or s.get('featured')) and (not args.search or args.search.lower() in ' '.join([s['id'],s['name'],s['description']]).lower())]

    if args.choose:
        selected = choose_style([s for s in styles if s.get('kind','style-package')=='style-package'], args.prefer, preferences)
        if args.json:
            print(json.dumps(selected or {}, ensure_ascii=False, indent=2))
        elif selected:
            print(f"{selected['id']} - {selected['description']}")
        else:
            print("No managed styles found.")
        return 0 if selected else 1

    if args.limit>0:styles=styles[:args.limit]
    if args.json:
        print(json.dumps(styles, ensure_ascii=False, indent=2))
    else:
        print(markdown_table(styles) if styles else "No managed styles found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
