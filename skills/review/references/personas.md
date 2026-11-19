# Review personas

Each persona runs a slice of the checks in [checks.md](checks.md) on the review bundle. The review session picks every persona whose trigger the diff (or a later fix diff) matches. Depth says how hard the persona works: **deep** personas get the most capable model and effort the user's rules name, **standard** ones a cheaper setting. Where the rules name neither, all personas run at the session's own setting.

| Persona | Checks | Also looks for | Runs when the diff touches | Depth |
|---|---|---|---|---|
| `correctness` | 1 `correctness`, 2 `edges`, 9 `logging` | Silent failures: an error swallowed, a fallback that hides a failure, a job that stops retrying without telling anyone | Any code | deep |
| `security` | 3 `security` | Loosened permissions, roles or allowlists; secrets in code, logs or errors | Authentication, authorization, payments, personal data, user input, webhooks, infrastructure, CI, hooks | deep |
| `api` | contracts between components | Breaking changes to routes, payloads, public functions or events; versioning; error shapes; drift from the approved design in the decisions table | Routes, controllers, handlers, public modules, event or message formats, code-map route facts | deep |
| `schema` | 4 `perf` | Reversible, backward-compatible migrations (expand, then contract); constraints and indexes in the database; locking; N+1 queries; resumable batched backfills; data integrity | Migrations, schema definitions, queries, seeds | deep |
| `design` | 6 `design`, 7 `dry`, 8 `yagni` | The preferred patterns in [patterns.md](patterns.md) | Any code | standard |
| `tests` | 5 `tests` | Whether the tests would fail if the change were wrong, at the cheapest layer that proves it (`compound-v:testing`); flaky constructs | Any code, with or without test changes | standard |
| `ops` | runtime and rollout | Deploy order, configuration and secrets, resource limits, probes, graceful shutdown, rollback, observability, staging kept apart from production | Infrastructure, Dockerfiles, CI, deploy and migration scripts, runtime configuration | standard |
| `ui` | user-facing behaviour | Match with the chosen design, accessibility, empty, loading and error states, layout at small and large sizes, copy. Looks at the running app when the host can run it | Templates, components, styles, client code, user-facing strings | standard |
| `instructions` | the instructions pass | | Agent-instruction files, as the review loop's instructions tier lists them | deep |
| `docs` | 10 `docs`, the light pass | | READMEs, docs, changelogs, comments | standard |

A persona reports findings only in its own area. A problem it notices elsewhere goes in one line under *Outside my area*, for the persona that owns it.
