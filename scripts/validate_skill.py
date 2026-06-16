#!/usr/bin/env python3
"""Validate a skill package for basic marketplace readiness."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE.txt",
    "agents/openai.yaml",
    "references/diagram-prompts.md",
    "references/quality-checklist.md",
]
FORBIDDEN_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must end with ---")
    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value
    return data, body


def validate(root: Path) -> None:
    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.is_file():
            fail(f"Missing required file: {rel}")

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(skill_text)

    allowed = {"name", "description"}
    extra = set(frontmatter) - allowed
    if extra:
        fail(f"SKILL.md frontmatter must only contain name and description, found: {sorted(extra)}")

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not name:
        fail("Missing frontmatter field: name")
    if not NAME_RE.match(name):
        fail("Skill name must be lowercase kebab-case")
    if not description:
        fail("Missing frontmatter field: description")
    if len(description) < 80:
        fail("Description is too short; include triggers and boundaries")
    if len(description) > 900:
        fail("Description is too long; keep it concise for progressive disclosure")
    if len(body.splitlines()) > 500:
        fail("SKILL.md body exceeds 500 lines; move details into references/")

    combined_text = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in root.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "dist" not in path.parts
        and path.suffix in {".md", ".yaml", ".yml", ".py", ".txt"}
    )
    for pattern in FORBIDDEN_PATTERNS:
        if pattern.search(combined_text):
            fail(f"Potential secret matched pattern: {pattern.pattern}")

    print(f"OK: {name} is valid")


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.is_dir():
        fail(f"Not a directory: {root}")
    validate(root)


if __name__ == "__main__":
    main()
