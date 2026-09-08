# Compound V

A Promptherder herd for scoped planning, execution, review, and persistent task context. Version 1.0.0 aligns with Promptherder 1.x native skill compilation.

## Install

```bash
promptherder install codex claude
promptherder pull compound-v
promptherder plan
promptherder
```

Use the feature build of Promptherder 1.0.0 until that release is published. Existing locked installs must review herd updates with `plan --update-lock` and apply with `--update-lock`.

## Entry points

| Task | Codex | Claude Code |
|---|---|---|
| Plan | `$workflow-plan` | `/workflow-plan` |
| Execute | `$workflow-execute` | `/workflow-execute` |
| Review | `$workflow-review` | `/workflow-review` |
| Save an idea | `$workflow-idea` | `/workflow-idea` |
| Add a rule | `$workflow-rule` | `/workflow-rule` |
| Record versions | `$workflow-stack` | `/workflow-stack` |

Pass the task or slug after the invocation. A configured command prefix precedes `workflow-`. Legacy `/plan` and similar short aliases are not installed by the native compiler.

Plan-only requests stop at the plan. A later implementation request continues the same task. Full implementation or YOLO requests use callable helpers through planning, execution, review, and fixes without artificial approval stops. Authorization stays limited to the requested task and host permissions.

Conversation artifacts live under `.promptherder/convos/<date-topic>/`. Project rules live in `.promptherder/hard-rules.md`; observed versions in `.promptherder/stack.md`; deferred ideas in `.promptherder/future-tasks.md`. Source rules require synchronization and host reload to appear in future instruction contexts. Generated host files are not authoring locations.

When installed, Grugg supplies its explicit terse default; Compound V retains review finding IDs and evidence. Oh supplies environment and release guidance. Neither a style skill nor a version bump expands the task into publishing, merging, or deployment.

## Validation

Compiler fixtures validate dependency closure, native discovery, and resource copying. File validation cannot establish actual model adherence; test plan-only, approved execution, review-and-fix, and phase transitions in the installed host before making behavioral claims.

## Credits

Based on [obra/superpowers](https://github.com/obra/superpowers), with the [Antigravity adaptation](https://github.com/anthonylee991/gemini-superpowers-antigravity).

## Required methodology

Keep the structured plan and decisions table, happy-path walkthrough, affected-files tree, risks/rollback, and verification steps. Execute independent work in batches, research APIs against recorded/actual versions, checkpoint each batch, and stop dependent work on failures. General reviews cover all ten named checks and include strengths, coverage, severity-graded findings, persisted results, and one appropriate action menu. Run the full test suite before final completion of code changes and provide manual smoke-test commands. Detailed checklists remain in the skills and their referenced documents; native host support does not make them optional.

## Workflow examples

In Claude Code, `/workflow-plan add rate limiting to the API` writes the plan and decisions, including test → code → verify steps, happy path, affected files, risks, and rollback. `SHOW DECISIONS` displays the decision summaries. `/workflow-execute <slug>` advances that plan; an ordinary “implement that plan” request does too. Codex uses the same names with `$` instead of `/`.

`/workflow-review security` targets the security check. A general review runs `correctness`, `edges`, `security`, `perf`, `tests`, `design`, `dry`, `yagni`, `logging`, and `docs`. It produces a coverage table and findings with `⠿ B1`, `⠷ M1`, `⠴ m1`, and `⠠ n1` IDs. For review-only work with findings, `FIX` authorizes blockers/majors and `FIX ALL` authorizes every severity; already-authorized fixes proceed directly.

`/workflow-plan YOLO <task>` runs plan → execute → review → fix, including minor/nit findings within scope. `/workflow-idea add OpenTelemetry tracing` saves a dated checklist item. `/workflow-rule all API routes require authentication` appends the rule and synchronizes configured targets. `/workflow-stack` compares actual pins, recorded versions, and current recommendations; proposed upgrades stay separate from installed versions.

## Persistent files

| Source | Purpose |
|---|---|
| `.promptherder/hard-rules.md` | Explicit project rules; track in Git |
| `.promptherder/stack.md` | Observed versions and separately recorded upgrade proposals |
| `.promptherder/future-tasks.md` | Confirmed deferred ideas; track in Git |
| `.promptherder/convos/<slug>/plan.md` | Current scoped plan |
| `.promptherder/convos/<slug>/decisions.md` | Accepted/rejected/ask decision summaries and rationale |
| `.promptherder/convos/<slug>/execution.md` | Batch checkpoints and verification |
| `.promptherder/convos/<slug>/review-*.md` | Collision-safe review reports |

Add `.promptherder/convos/` to `.gitignore` if task artifacts would make PRs noisy. Keep authored rules and stack inventory tracked. Do not blanket-ignore host directories containing hand-maintained skills or settings.
