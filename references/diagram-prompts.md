# Diagram Prompt Reference

Use these prompts when the main `SKILL.md` asks for a specific diagram. Always adapt paths and framework terms to the target repository.

## Frontend architecture map

```text
Analyze the frontend repository from real source files and draw a layered architecture map.

Layers:
- UI/component layer
- Router layer
- Store/Context/Model layer
- Service/API layer
- Infrastructure/build/deploy layer

For each node include name, responsibility, and evidence path. Do not invent modules. Mark uncertain nodes as 待确认.

Output Mermaid and SVG under docs/architecture/.
```

## Module dependency map

```text
Scan internal imports and configured path aliases. Build a module dependency graph with 10-20 grouped nodes. Highlight cycles, high in-degree modules, high out-degree modules, leaf modules, and dependency inversion risks. Include a short dependency statistics summary.
```

## Route flow map

```text
Read route config and navigation calls. Draw route nodes, layouts, nested routes, redirects, dynamic params, special pages, and guard redirects. Label links as declarative, programmatic, redirect, default route, or guard redirect when evidence exists.
```

## Auth guard decision map

```text
Trace page access through login status, token validity, user initialization, roles, page permissions, button permissions, and final pass or redirect. Include source files and method names. Do not invent roles or permission keys.
```

## Data model map

```text
Inspect stores, models, contexts, slices, hooks, service return types, and TypeScript definitions. Show state fields, types, actions, async effects, derived data, and consuming pages/components.
```

## Interaction sequence map

```text
For the selected feature, trace user action to UI event, validation, API call, state update, route transition, view render, success handling, and failure handling. Every step must name the component/function/hook and evidence path.
```

## State machine map

```text
For the selected component or page, extract all interaction states and transitions from code. Include only states supported by code or clear logic. Label transitions with events, methods, conditions, and paths. Add missing branch test suggestions.
```

## External dependency map

```text
Analyze package metadata, lockfiles, env examples, README, Docker/CI, and service code. Group external dependencies into core framework/heavy dependencies, infrastructure/middleware, and third-party services. Include version, purpose, coupling, and risk.
```

## Component lifecycle map

```text
For the selected component, map mount/init, prop update, state update, effects/watchers, async requests, lazy loading, error handling, cleanup, and unmount. Flag missing cleanup, un-cancelled requests, stale subscriptions, timers, repeated requests, and dependency mistakes.
```
