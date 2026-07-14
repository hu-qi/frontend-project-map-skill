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
    "README.md",
    "LICENSE.txt",
    "agents",
    "references",
    "scripts",
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
    dist = root / "dist"
    if dist.exists():
        shutil.rmtree(dist)
    dist.mkdir(parents=True, exist_ok=True)

    zip_path = dist / f"{PACKAGE_NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(root.rglob("*")):
            if should_include(path, root):
                arcname = path.relative_to(root).as_posix()
                zf.write(path, arcname)

    print(f"Built {zip_path}")
    return zip_path


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not (root / "SKILL.md").is_file():
        raise SystemExit("ERROR: SKILL.md not found at package root")
    build(root)


if __name__ == "__main__":
    main()
