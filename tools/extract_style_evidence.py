#!/usr/bin/env python3
"""Collect first-pass style evidence from a URL or local HTML file.

This helper is intentionally small and dependency-free. It does not replace
visual judgement; it prevents the common UIgod failures: missed CSS files,
unresolved theme evidence, and invented tokens.
"""

from __future__ import annotations

import argparse
import html.parser
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path


CSS_URL_RE = re.compile(r'url\(\s*[\'"]?([^\'")]+)[\'"]?\s*\)', re.I)
VAR_RE = re.compile(r'(--[-_a-zA-Z0-9]+)\s*:\s*([^;{}]+);')
FONT_FACE_RE = re.compile(r'@font-face\s*{([^{}]+)}', re.I | re.S)
FONT_FAMILY_RE = re.compile(r'font-family\s*:\s*([^;{}]+);', re.I)
COLOR_RE = re.compile(
    r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]+\)|hsla?\([^)]+\)|'
    r'\b(?:black|white|transparent|currentColor)\b'
)
VALUE_PATTERNS = {
    "font-size": re.compile(r'font-size\s*:\s*([^;{}]+);', re.I),
    "font-weight": re.compile(r'font-weight\s*:\s*([^;{}]+);', re.I),
    "line-height": re.compile(r'line-height\s*:\s*([^;{}]+);', re.I),
    "letter-spacing": re.compile(r'letter-spacing\s*:\s*([^;{}]+);', re.I),
    "border": re.compile(r'\bborder(?:-[a-z-]+)?\s*:\s*([^;{}]+);', re.I),
    "border-radius": re.compile(r'border-radius\s*:\s*([^;{}]+);', re.I),
    "box-shadow": re.compile(r'box-shadow\s*:\s*([^;{}]+);', re.I),
    "transition": re.compile(r'transition(?:-[a-z-]+)?\s*:\s*([^;{}]+);', re.I),
    "animation": re.compile(r'animation(?:-[a-z-]+)?\s*:\s*([^;{}]+);', re.I),
}
MEDIA_RE = re.compile(r'@media\s+([^{]+){', re.I)
THEME_HINT_RE = re.compile(r'\b(?:dark|light|theme|color-scheme|prefers-color-scheme)\b', re.I)


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.css_links: list[str] = []
        self.asset_links: list[str] = []
        self.body_attrs: dict[str, str] = {}
        self.html_attrs: dict[str, str] = {}
        self.meta: list[dict[str, str]] = []
        self.svg_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k.lower(): v or "" for k, v in attrs}
        if tag == "html":
            self.html_attrs = attr
        elif tag == "body":
            self.body_attrs = attr
        elif tag == "link":
            href = attr.get("href", "")
            rel = attr.get("rel", "")
            if href and ("stylesheet" in rel.lower() or ".css" in href):
                self.css_links.append(href)
        elif tag == "meta":
            self.meta.append(attr)
        elif tag == "img":
            src = attr.get("src", "")
            if src:
                self.asset_links.append(src)
        elif tag == "svg":
            self.svg_count += 1


def is_url(value: str) -> bool:
    return urllib.parse.urlparse(value).scheme in {"http", "https"}


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "UIgodStyleExtractor/1.0 (+https://local)",
            "Accept": "text/html, text/css, */*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def read_source(source: str) -> tuple[str, str]:
    if is_url(source):
        return fetch_text(source), source
    path = Path(source)
    return path.read_text(encoding="utf-8", errors="replace"), path.resolve().as_uri()


def read_file_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = Path(urllib.request.url2pathname(parsed.path))
    return path.read_text(encoding="utf-8", errors="replace")


def local_css_fallbacks(source_path: Path, href: str) -> list[Path]:
    parent = source_path.resolve().parent
    parsed_path = urllib.parse.unquote(urllib.parse.urlparse(href).path)
    candidates: list[Path] = []
    if parsed_path:
        raw = Path(parsed_path.lstrip("/"))
        candidates.append(parent / raw)
        candidates.append(parent / raw.name)
        stem = raw.stem.split(".")[0]
        if stem:
            candidates.extend(parent.glob(f"{stem}*.css"))
    candidates.extend(parent.glob("*.css"))

    unique: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen or not resolved.exists() or resolved.suffix.lower() != ".css":
            continue
        seen.add(resolved)
        unique.append(resolved)
    return unique


def safe_name(url_or_path: str, index: int) -> str:
    parsed = urllib.parse.urlparse(url_or_path)
    name = Path(parsed.path).name or f"style-{index}.css"
    name = re.sub(r'[^-_.a-zA-Z0-9]+', "-", name)
    if not name.endswith(".css"):
        name = f"{name}.css"
    return f"{index:02d}-{name}"


def top_values(pattern: re.Pattern[str], text: str, limit: int = 24) -> list[tuple[str, int]]:
    values = [m.group(1).strip() for m in pattern.finditer(text)]
    return Counter(values).most_common(limit)


def resolve_var(name: str, variables: dict[str, str], seen: set[str] | None = None) -> str:
    seen = seen or set()
    if name in seen:
        return variables.get(name, "")
    seen.add(name)
    value = variables.get(name, "")
    nested = re.search(r'var\(\s*(--[-_a-zA-Z0-9]+)', value)
    if nested:
        literal = resolve_var(nested.group(1), variables, seen)
        if literal:
            return literal
    return value


def extract_css_summary(css_text: str) -> dict[str, object]:
    variables = {name: value.strip() for name, value in VAR_RE.findall(css_text)}
    resolved = {name: resolve_var(name, variables) for name in variables}
    font_faces = []
    for block in FONT_FACE_RE.findall(css_text):
        family = FONT_FAMILY_RE.search(block)
        font_faces.append(family.group(1).strip().strip('"\'') if family else block[:80].strip())

    summary: dict[str, object] = {
        "custom_property_count": len(variables),
        "custom_properties_sample": dict(list(resolved.items())[:80]),
        "font_faces": sorted(set(font_faces)),
        "font_families": top_values(FONT_FAMILY_RE, css_text, 30),
        "colors": Counter(COLOR_RE.findall(css_text)).most_common(60),
        "media_queries": Counter(m.group(1).strip() for m in MEDIA_RE.finditer(css_text)).most_common(20),
        "theme_hints": [line.strip()[:220] for line in css_text.splitlines() if THEME_HINT_RE.search(line)][:80],
    }
    for label, pattern in VALUE_PATTERNS.items():
        summary[label] = top_values(pattern, css_text, 30)
    return summary


def write_markdown(
    out_dir: Path,
    source: str,
    source_base: str,
    parser: LinkParser,
    css_records: list[dict[str, object]],
    combined_summary: dict[str, object],
) -> None:
    lines: list[str] = []
    lines.append("# Style Evidence")
    lines.append("")
    lines.append("## Source")
    lines.append(f"- Input: `{source}`")
    lines.append(f"- Base: `{source_base}`")
    lines.append("")
    lines.append("## Markup Theme Hints")
    lines.append(f"- html attrs: `{json.dumps(parser.html_attrs, ensure_ascii=False)}`")
    lines.append(f"- body attrs: `{json.dumps(parser.body_attrs, ensure_ascii=False)}`")
    color_scheme = [
        meta for meta in parser.meta
        if meta.get("name", "").lower() in {"color-scheme", "theme-color"}
    ]
    lines.append(f"- meta color hints: `{json.dumps(color_scheme, ensure_ascii=False)}`")
    lines.append(f"- inline SVG count: {parser.svg_count}")
    lines.append("")
    lines.append("## CSS Files")
    lines.append("| File | Size | Source |")
    lines.append("| --- | ---: | --- |")
    for record in sorted(css_records, key=lambda item: int(item["size"]), reverse=True):
        lines.append(f"| `{record['file']}` | {record['size']} | `{record['url']}` |")
    lines.append("")
    lines.append("## Extracted Token Leads")
    lines.append("")
    lines.append("### Custom Properties Sample")
    props = combined_summary.get("custom_properties_sample", {})
    if isinstance(props, dict):
        for key, value in list(props.items())[:80]:
            lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("### Fonts")
    for family in combined_summary.get("font_faces", []):
        lines.append(f"- @font-face: `{family}`")
    for value, count in combined_summary.get("font_families", []):
        lines.append(f"- font-family `{value}` ({count})")
    lines.append("")
    lines.append("### Colors")
    for value, count in combined_summary.get("colors", []):
        lines.append(f"- `{value}` ({count})")
    lines.append("")
    for label in [
        "font-size",
        "font-weight",
        "line-height",
        "letter-spacing",
        "border",
        "border-radius",
        "box-shadow",
        "transition",
        "animation",
    ]:
        lines.append(f"### {label}")
        for value, count in combined_summary.get(label, []):
            lines.append(f"- `{value}` ({count})")
        lines.append("")
    lines.append("### Media Queries")
    for value, count in combined_summary.get("media_queries", []):
        lines.append(f"- `{value}` ({count})")
    lines.append("")
    lines.append("### Theme Hint Lines")
    for value in combined_summary.get("theme_hints", []):
        lines.append(f"- `{value}`")
    lines.append("")
    lines.append("## Asset Leads")
    for asset in parser.asset_links[:80]:
        lines.append(f"- `{urllib.parse.urljoin(source_base, asset)}`")
    lines.append("")
    lines.append("## Next Manual Pass")
    lines.append("- Decide default theme from markup, screenshot, and CSS.")
    lines.append("- Convert token leads into role-based tokens.")
    lines.append("- Identify 5-8 signature moves.")
    lines.append("- Mark extracted, inferred, and synthesized values separately.")
    (out_dir / "evidence.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    argp = argparse.ArgumentParser(description="Extract first-pass UIgod style evidence.")
    argp.add_argument("source", help="URL or local HTML file")
    argp.add_argument("--out", default="style-evidence", help="Output directory")
    args = argp.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    html_text, base = read_source(args.source)
    source_path = None if is_url(args.source) else Path(args.source)
    (out_dir / "source.html").write_text(html_text, encoding="utf-8")

    parser = LinkParser()
    parser.feed(html_text)

    css_records: list[dict[str, object]] = []
    combined_css: list[str] = []

    for index, href in enumerate(dict.fromkeys(parser.css_links), start=1):
        css_url = urllib.parse.urljoin(base, href)
        try:
            css_text = fetch_text(css_url) if is_url(css_url) else read_file_url(css_url)
        except Exception as exc:  # noqa: BLE001 - evidence tool should keep going
            if source_path is not None:
                fallbacks = local_css_fallbacks(source_path, href)
                if fallbacks:
                    fallback = fallbacks[0]
                    css_text = fallback.read_text(encoding="utf-8", errors="replace")
                    css_url = fallback.resolve().as_uri()
                    file_name = safe_name(str(fallback), index)
                    (out_dir / file_name).write_text(css_text, encoding="utf-8")
                    css_records.append({
                        "file": file_name,
                        "size": len(css_text.encode("utf-8")),
                        "url": css_url,
                        "note": f"local fallback for {href}",
                    })
                    combined_css.append(f"/* {css_url} */\n{css_text}")
                    continue
            css_records.append({"file": "(fetch failed)", "size": 0, "url": css_url, "error": str(exc)})
            continue
        file_name = safe_name(css_url, index)
        (out_dir / file_name).write_text(css_text, encoding="utf-8")
        css_records.append({"file": file_name, "size": len(css_text.encode("utf-8")), "url": css_url})
        combined_css.append(f"/* {css_url} */\n{css_text}")

        for asset_url in CSS_URL_RE.findall(css_text):
            if asset_url.startswith("data:"):
                continue
            parser.asset_links.append(urllib.parse.urljoin(css_url, asset_url))

    combined_text = "\n\n".join(combined_css)
    (out_dir / "combined.css").write_text(combined_text, encoding="utf-8")
    summary = extract_css_summary(combined_text)
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(out_dir, args.source, base, parser, css_records, summary)

    css_count = len([record for record in css_records if int(record["size"]) > 0])
    print(f"Saved evidence to {out_dir}")
    print(f"CSS files fetched: {css_count}")
    if css_records:
        largest = max(css_records, key=lambda record: int(record["size"]))
        print(f"Largest CSS: {largest['file']} ({largest['size']} bytes)")
    return 0 if css_count or not parser.css_links else 2


if __name__ == "__main__":
    sys.exit(main())
