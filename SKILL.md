---
name: frontend-project-map
description: Generate and maintain a 9-diagram frontend project map from real source code. Use when analyzing or onboarding a frontend repository, creating architecture docs, reviewing module dependencies, tracing routes/auth/state/API flows, preparing refactors, or updating AI coding context with docs/architecture diagrams. Do not use for backend-only analysis or visual mockup generation.
---

# Frontend Project Map Skill

Use this skill to turn an unfamiliar frontend repository into a verified architecture map. Work from real source evidence first, then generate maintainable Mermaid/Markdown/SVG artifacts under `docs/architecture/`.

## Operating principles

- Verify before visualizing. Read source files, config files, lockfiles, and documentation before drawing.
- Prefer text-first diagrams. Generate Mermaid `.mmd` files before rendered `.svg` files so the output can be reviewed and versioned.
- Cite source paths inside notes. Every important node or edge should be traceable to a file path, function, hook, route, model, or dependency declaration.
- Mark uncertainty explicitly. Use `待确认` when code evidence is incomplete.
- Keep diagrams readable. Split by domain when a graph becomes crowded.
- Update AI context. After generating the map, add or propose entries for `CLAUDE.md`, `AGENTS.md`, `.cursor/rules/`, or equivalent project rules.

## Required workflow

1. Scan the repository.
   - Read `package.json`, lockfiles, README, build config, route config, source directories, state management files, services/API files, type files, env examples, CI/CD, Docker files, and docs.
   - Identify framework, routing, state management, UI library, request client, auth/permission approach, build tool, and deployment hints.

2. Create `docs/architecture/00-index.md`.
   - Include project overview, diagram index, key findings, risks, and next steps.

3. Generate the nine diagrams in this order unless the user asks for a narrower scope:
   1. Frontend architecture map
   2. Module dependency map
   3. Route flow map
   4. Auth guard decision map
   5. Data model map
   6. Interaction sequence map for one core feature
   7. State machine map for one core component/page
   8. External dependency map
   9. Component lifecycle map for one risky or frequently changed component

4. Produce risk and findings summaries.
   - Create or update `docs/architecture/findings.md` and `docs/architecture/risks.md`.

5. Update project AI context.
   - Add a concise architecture map reference block to `CLAUDE.md`, `AGENTS.md`, or `.cursor/rules/frontend-project-map.mdc` when appropriate.
   - If you cannot modify files, output the exact block the user can paste.

## Diagram specifications

### 1. Frontend architecture map

Use for global orientation. Read app entry, pages/routes, layouts, components, stores/models/contexts, services/API, utils, build config, and README.

Output:
- `docs/architecture/01-frontend-architecture.mmd`
- `docs/architecture/01-frontend-architecture.svg`

Show these layers:
- UI/component layer
- Router layer
- Store/Context/Model layer
- Service/API layer
- Infrastructure/build/deploy layer

Each module must include a short responsibility and evidence path. Keep infrastructure smaller than core layers.

### 2. Module dependency map

Use for impact analysis and refactoring. Scan internal imports and path aliases.

Output:
- `docs/architecture/02-module-deps.mmd`
- `docs/architecture/02-module-deps.svg`

Rules:
- Normalize aliases from `tsconfig.json`, `jsconfig.json`, Vite, Webpack, Umi, Next, or equivalent config.
- Group nodes to 10-20 meaningful modules.
- Compute or reason about inbound/outbound dependencies.
- Highlight cycles, high in-degree modules, high out-degree modules, and leaf modules.
- Flag bottom-layer modules that depend on business pages as dependency inversion risks.

### 3. Route flow map

Use to explain page topology and navigation.

Output:
- `docs/architecture/03-route-flow.mmd`
- `docs/architecture/03-route-flow.svg`

Include route paths, layouts, nested routes, redirects, dynamic params, 403/404/login/home pages, and guards. Label navigation type when known: declarative link, programmatic navigation, redirect, default route, or guard redirect.

### 4. Auth guard decision map

Use for permission debugging and security review.

Output:
- `docs/architecture/04-auth-guard.mmd`
- `docs/architecture/04-auth-guard.svg`

Trace from page access through login status, token validity, user initialization, roles, route/page permission, button permission, pass, `/login`, `/403`, `/404`, or error route. Read files like `access.ts`, `auth.ts`, `permission.ts`, router guards, request interceptors, user models/stores, and service calls. Do not invent roles or permission keys.

### 5. Data model map

Use to understand where data is defined, changed, and consumed.

Output:
- `docs/architecture/05-data-model.mmd`
- `docs/architecture/05-data-model.svg`

Inspect stores, models, contexts, Redux slices, Zustand stores, Pinia/Vuex modules, hooks, service return types, and TypeScript types/interfaces. Show state fields, types, actions/reducers/mutations, async effects/thunks, derived data, and consuming pages/components. Highlight global models such as user/auth/app/settings/permission.

### 6. Interaction sequence map

Use to trace a core feature end-to-end.

Output pattern:
- `docs/architecture/06-sequence-[feature].mmd`
- `docs/architecture/06-sequence-[feature].svg`

Choose the feature with the user when possible. Good defaults: login, registration, permission initialization, file upload, list search, form submit, order creation, import/export, dashboard load.

Trace user action → UI event → validation/parameter building → API call → store/model/context update → route transition → view render → success/failure handling. Each step must include component/function/hook and source path.

### 7. State machine map

Use to flatten interaction states and find missing branches.

Output pattern:
- `docs/architecture/07-state-[component].mmd`
- `docs/architecture/07-state-[component].svg`

Good targets: login form, upload component, search form, multistep form, payment button, async list page, modal editor, captcha component.

Show only states supported by code or clear logic: idle, inputting, validating, loading, success, error, retry, disabled, expired, cancelled, unmounted. Label transitions with triggering events, methods, conditions, and paths. Add suggested test cases for missing branches.

### 8. External dependency map

Use before upgrades, dependency replacement, or deployment review.

Output:
- `docs/architecture/08-external-deps.mmd`
- `docs/architecture/08-external-deps.svg`

Group dependencies into:
- Core framework and heavy dependencies
- Middleware and infrastructure
- External APIs and third-party services

Read `package.json`, lockfiles, `.env*`, README, Docker, CI/CD, service/API code, monitoring/analytics config. Include version, purpose, coupling level, replacement risk, and upgrade risk.

### 9. Component lifecycle map

Use for async bugs, memory leaks, repeated requests, and cleanup review.

Output pattern:
- `docs/architecture/09-lifecycle-[component].mmd`
- `docs/architecture/09-lifecycle-[component].svg`

Good targets: dashboard page, list page, upload component, WebSocket component, chart component, rich editor, map component, video player, frequently changed container.

Map mount/init, prop update, state update, effects/watchers, async requests, lazy/Suspense, error handling, cleanup, and unmount. Adapt terms to framework: React hooks, Vue lifecycle/watch, Angular lifecycle, Svelte effects. Flag missing cleanup, un-cancelled requests, stale subscriptions, timers, repeated requests, or wrong dependency arrays.

## Visual style guidance

Use this when rendering SVGs or asking a model to generate visual layout:

- Canvas background: `#F8FAFC`.
- Primary text: `#0F172A`.
- Module titles: 11-12px, bold.
- Descriptions: 9px, regular, low-saturation dark color.
- Avoid fixed card widths; size cards by content.
- Use rounded outer containers at 8px and inner cards at 6px.
- Highlight cycles with red bold dashed lines.
- Highlight high-risk modules with orange or red borders.
- Highlight `待确认` items with yellow dashed boxes.
- Keep infrastructure in a smaller corner block.

## Required index template

Create `docs/architecture/00-index.md` with this structure:

```markdown
# Frontend Project Architecture Map

## Project overview

- Project name:
- Framework:
- Build tool:
- Routing:
- State management:
- UI library:
- API/request layer:
- Auth/permission:
- Deployment/CI:
- Analysis date:

## Diagram index

| No. | Diagram | File | Purpose |
|---|---|---|---|
| 01 | Frontend architecture | ./01-frontend-architecture.svg | Global layers |
| 02 | Module dependencies | ./02-module-deps.svg | Internal dependencies and cycles |
| 03 | Route flow | ./03-route-flow.svg | Page topology and navigation |
| 04 | Auth guard | ./04-auth-guard.svg | Permission decisions |
| 05 | Data model | ./05-data-model.svg | Data ownership and consumers |
| 06 | Interaction sequence | ./06-sequence-[feature].svg | Core feature execution chain |
| 07 | State machine | ./07-state-[component].svg | Interaction states and missing branches |
| 08 | External dependencies | ./08-external-deps.svg | Upgrade and service risks |
| 09 | Component lifecycle | ./09-lifecycle-[component].svg | Effects, async, cleanup |

## Key findings

1.
2.
3.

## Risks

1.
2.
3.

## Next steps

1.
2.
3.
```

## AI context block template

Add this block to the project's AI rules file when the map is ready:

```markdown
# Frontend Project Map Context

This repository has architecture map artifacts under `docs/architecture/`. Before code changes, bug analysis, feature work, or refactoring, inspect the relevant diagrams and update them when the change affects routing, auth, state management, API/service flows, dependencies, or component lifecycle behavior.

Primary entry:
- `docs/architecture/00-index.md`

Core diagrams:
- `docs/architecture/01-frontend-architecture.svg`
- `docs/architecture/02-module-deps.svg`
- `docs/architecture/03-route-flow.svg`
- `docs/architecture/04-auth-guard.svg`
- `docs/architecture/05-data-model.svg`
- `docs/architecture/06-sequence-[feature].svg`
- `docs/architecture/07-state-[component].svg`
- `docs/architecture/08-external-deps.svg`
- `docs/architecture/09-lifecycle-[component].svg`

Rules:
- Treat source code as authoritative when diagrams disagree.
- Update diagrams after architecture-affecting changes.
- Do impact analysis before editing high in-degree modules.
- Do not invent routes, roles, APIs, stores, or dependencies.
```

## Completion checklist

Finish with a concise checklist:

- [ ] Repository scanned
- [ ] `00-index.md` created or updated
- [ ] Frontend architecture map created
- [ ] Module dependency map created
- [ ] Route flow map created
- [ ] Auth guard map created
- [ ] Data model map created
- [ ] Interaction sequence map created
- [ ] State machine map created
- [ ] External dependency map created
- [ ] Component lifecycle map created
- [ ] `findings.md` created or updated
- [ ] `risks.md` created or updated
- [ ] AI context file created or update proposed

## Failure handling

- If the repository is too large, start with the main application package and document the scope.
- If rendering SVGs is unavailable, still produce valid Mermaid files and explain how to render them.
- If route/auth/state code is generated or hidden, document the generated source and mark uncertain edges.
- If no frontend framework is detected, stop and explain that this skill is intended for frontend repositories.
