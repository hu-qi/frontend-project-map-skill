# Frontend Project Map Skill

A reusable Agent Skill for generating a verified 9-diagram frontend project map from real source code.

## What it does

This skill helps an AI coding agent analyze a frontend repository and produce maintainable architecture artifacts under `docs/architecture/`:

1. Frontend architecture map
2. Module dependency map
3. Route flow map
4. Auth guard decision map
5. Data model map
6. Interaction sequence map
7. State machine map
8. External dependency map
9. Component lifecycle map

The skill emphasizes source-grounded analysis, text-first Mermaid diagrams, risk summaries, and AI-context updates for follow-up coding work.

## Skill package structure

```text
frontend-project-map-skill/
  SKILL.md
  README.md
  LICENSE.txt
  agents/openai.yaml
  references/
    diagram-prompts.md
    quality-checklist.md
  scripts/
    validate_skill.py
    build_dist.py
  .github/workflows/
    package.yml
```

## Local validation

```bash
python scripts/validate_skill.py .
```

## Local packaging

```bash
python scripts/build_dist.py .
```

The package will be created at:

```text
dist/frontend-project-map-skill.zip
```

## GitHub Actions packaging

Every push and pull request runs `.github/workflows/package.yml` to:

1. Validate `SKILL.md` frontmatter and required marketplace files.
2. Build `dist/frontend-project-map-skill.zip`.
3. Upload the zip as a workflow artifact.

Tag pushes like `v1.0.0` additionally create a GitHub Release and attach the zip.

## Notes for maintainers

- Keep `SKILL.md` focused and under about 500 lines.
- Put longer reusable prompts and review rubrics in `references/`.
- Do not add secrets, tokens, private repository details, or environment values to the package.
