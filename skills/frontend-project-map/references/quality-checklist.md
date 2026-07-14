# Skill Quality Checklist

Use this checklist before publishing a release package.

## Required package files

- [ ] `SKILL.md` exists at package root.
- [ ] `SKILL.md` has YAML frontmatter with only `name` and `description`.
- [ ] `name` is lowercase kebab-case.
- [ ] `description` is concise, trigger-oriented, and includes boundaries.
- [ ] `README.md` explains purpose, structure, validation, and packaging.
- [ ] `LICENSE.txt` exists.
- [ ] `agents/openai.yaml` exists with display metadata.
- [ ] No secrets or private environment values are included.

## Instruction quality

- [ ] The skill says when and how to use it.
- [ ] It follows progressive disclosure: core workflow in `SKILL.md`, longer references in `references/`.
- [ ] It gives deterministic output paths.
- [ ] It requires source-grounded evidence.
- [ ] It includes failure handling.
- [ ] It avoids unsafe instructions such as hiding behavior, exfiltrating data, or bypassing review.

## Diagram output quality

- [ ] Mermaid source files are created before SVGs.
- [ ] Important nodes/edges reference source paths.
- [ ] Uncertain claims are marked `待确认`.
- [ ] Large diagrams are split instead of made unreadable.
- [ ] Findings and risks are summarized.
- [ ] AI context rules are updated or proposed.

## Release quality

- [ ] `python scripts/validate_skill.py .` passes.
- [ ] `python scripts/build_dist.py .` creates `dist/frontend-project-map-skill.zip`.
- [ ] GitHub Actions uploads the dist artifact.
- [ ] Version tag releases attach the zip artifact.
