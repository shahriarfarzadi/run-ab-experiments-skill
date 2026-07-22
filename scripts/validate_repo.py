#!/usr/bin/env python3
"""Dependency-free structural validation for the repository and skill."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "run-ab-experiments"
SKILL_FILE = SKILL / "SKILL.md"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
LINK_PATTERN = re.compile(r"\]\(([^)]+)\)")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"error: {message}")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    require(lines and lines[0] == "---", "SKILL.md must start with YAML frontmatter")
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise SystemExit("error: SKILL.md frontmatter is not closed") from error

    fields: dict[str, str] = {}
    for line in lines[1:closing]:
        match = re.fullmatch(r"([A-Za-z0-9_-]+):\s*(.+)", line)
        require(match is not None, f"unsupported frontmatter line: {line!r}")
        key, value = match.groups()
        require(key not in fields, f"duplicate frontmatter field: {key}")
        fields[key] = value.strip().strip('"\'')
    return fields


def validate_frontmatter() -> None:
    text = SKILL_FILE.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    require(set(fields) == {"name", "description"},
            "frontmatter must contain only name and description")
    name = fields["name"]
    description = fields["description"]
    require(NAME_PATTERN.fullmatch(name) is not None, "invalid skill name")
    require(name == SKILL.name, "skill name must match its directory")
    require(40 <= len(description) <= 1536,
            "description must be 40 to 1,536 characters")
    require(len(text.splitlines()) < 500, "SKILL.md must stay below 500 lines")


def validate_links() -> None:
    for markdown in SKILL.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (markdown.parent / target).resolve()
            require(resolved.is_relative_to(SKILL.resolve()),
                    f"link escapes skill directory: {markdown}: {raw_target}")
            require(resolved.exists(),
                    f"broken link in {markdown.relative_to(ROOT)}: {raw_target}")


def validate_repository() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "VERSION",
        ROOT / "install.sh",
        SKILL / "agents" / "openai.yaml",
        SKILL / "scripts" / "ab_math.py",
        SKILL / "references" / "discovery-question-bank.md",
        SKILL / "references" / "experiment-design.md",
        SKILL / "references" / "analysis-and-trust.md",
        SKILL / "references" / "lifecycle-and-source-map.md",
    ]
    for path in required:
        require(path.is_file(), f"required file is missing: {path.relative_to(ROOT)}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    require(VERSION_PATTERN.fullmatch(version) is not None, "VERSION is not SemVer")
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    require(f"version: {version}" in citation, "CITATION.cff version is stale")

    forbidden_suffixes = {".pdf", ".epub"}
    forbidden = [
        path.relative_to(ROOT)
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in forbidden_suffixes
    ]
    require(not forbidden, f"source-book files must not be included: {forbidden}")

    marker_pattern = re.compile(r"\b(?:TO" + "DO|FIX" + "ME|T" + "BD)\b", re.I)
    placeholders: list[Path] = []
    for path in SKILL.rglob("*"):
        if path.is_file():
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if marker_pattern.search(text):
                placeholders.append(path.relative_to(ROOT))
    require(not placeholders, f"placeholder markers remain: {placeholders}")

    calculator = SKILL / "scripts" / "ab_math.py"
    compile(calculator.read_text(encoding="utf-8"), str(calculator), "exec")


def main() -> None:
    validate_repository()
    validate_frontmatter()
    validate_links()
    print("Repository contract passed.")


if __name__ == "__main__":
    main()
