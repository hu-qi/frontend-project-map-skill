#!/usr/bin/env python3
"""Build a zip package for the frontend-project-map skill."""

from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path

PACKAGE_NAME = "frontend-project-map-skill"
EXCLUDE_DIRS = {".git", "dist", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo", ".DS_Store"}
INCLUDE_TOP_LEVEL = {
    "SKILL.md",
    "agents",
    "references",
}


def should_include(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return False
    if path.name in EXCLUDE_SUFFIXES:
        return False
    if rel.parts[0] not in INCLUDE_TOP_LEVEL:
        return False
    return path.is_file()


def build(root: Path) -> Path:
    skill_root = root / "skills" / "frontend-project-map"
    dist = root / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir(parents=True, exist_ok=True)

    zip_path = dist / f"{PACKAGE_NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_root.rglob("*")):
            if should_include(path, skill_root):
                arcname = path.relative_to(skill_root).as_posix()
                zf.write(path, arcname)
        for rel in ("README.md", "LICENSE.txt"):
            source = root / rel
            if source.is_file():
                zf.write(source, rel)

    print(f"Built {zip_path}")
    return zip_path


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not (root / "skills" / "frontend-project-map" / "SKILL.md").is_file():
        raise SystemExit("ERROR: nested skill SKILL.md not found")
    build(root)


if __name__ == "__main__":
    main()
