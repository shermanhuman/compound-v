---
name: compound-v-review
description: Reviews changes for correctness, edge cases, style, security, and maintainability with severity levels. 10 parallel checks with version-specific research. Use before finalizing changes.
---

# Review Skill

Act as a senior engineer performing a thorough code review.

**Announce at start:** "Running review pass on [scope]."

## When to use this skill

- before delivering final code changes
- after implementing a planned set of steps
- before merging or shipping

## Check targeting

User can run a single check by short name: `/review security`, `/review edges`, `/review perf`.
If no check specified, run all 10.

| #   | Check                       | Short name    |
| --- | --------------------------- | ------------- |
| 1   | Correctness                 | `correctness` |
| 2   | Edge cases & error handling | `edges`       |
| 3   | Security                    | `security`    |
| 4   | Performance                 | `perf`        |
| 5   | Tests                       | `tests`       |
| 6   | Design & maintainability    | `design`      |
| 7   | DRY                         | `dry`         |
| 8   | YAGNI & overengineering     | `yagni`       |
| 9   | Logging & observability     | `logging`     |
| 10  | Documentation               | `docs`        |

## Load stack context (sequential — before research)

Read `.promptherder/stack.md` for recorded versions, falling back to legacy `.agents/rules/stack.md` or `.agent/rules/stack.md`; compare with actual project pins. If none exists, infer versions from `go.mod`, `mix.exs`, `package.json`, or equivalent. These versions scope all subsequent web searches.

If `stack.md` is missing from all locations and no versions can be inferred, print: _"No `stack.md` found. Run `/stack` to pin your versions — this improves web search accuracy."_ Then continue.

## Research before reviewing

Do all research **in parallel** (invoke multiple tool calls in the same response):

1. Use `git diff` against the pre-implementation baseline for the review scope.
2. Read all changed files in parallel to build full context.
3. Search the web for version-specific docs, gotchas, and best practices scoped to `stack.md` versions.
4. Read `.promptherder/hard-rules.md` if it exists.
5. Read the current task’s plan and future-tasks file if present. A standalone review does not require a plan; do not invent one or select an unrelated task.

## Review checks

Read [the ten-check reference](references/checks.md) for the requested review. Run all ten for a general review; run the named check for targeted review. Execute independent checks concurrently where tools and authorization allow; otherwise perform them locally. Ten checks does not require ten subagents.

## Output format

Keep the review **scannable**. The user should grasp the full picture in 10 seconds from the table, then drill into details only where needed.

### 1. Strengths (3-5 items max)

Highlight what's well done. Be specific with file:line references. Don't list everything good — pick the top 3-5.

---

### 2. Check coverage

**Always include this table.** Every check must appear — no silent omissions.

```
| # | Check | Result |
|---|-------|--------|
| 1 | `correctness` | ✅ Clean |
| 2 | `edges` | ⠷ M1 |
| 3 | `security` | N/A — no auth or input handling |
| ... | ... | ... |
```

Mark each check: `✅ Clean` (performed, no issues), finding IDs, `N/A — reason`, or `Not assessed — targeted review`. Never label an unperformed check clean.

---

### 3. Findings

**Always start with a summary table.** This is the scannable overview:

```
| ID | Sev | Location | Issue |
|----|-----|----------|-------|
| B1 | ⠿ | file.go:42 | Brief description |
| M1 | ⠷ | auth.go:15 | Brief description |
| m1 | ⠴ | utils.go:8 | Brief description |
```

Detail a finding ONLY if the fix is non-obvious or the reasoning is nuanced. If someone can understand the issue and fix from the table row alone, do NOT expand it below.

```
⠷ **M1**: auth.go:15 — Why this matters (1-2 lines)
  Fix: specific remediation.
```

Finding IDs: `⠿ **B1**` (blocker), `⠷ **M1**` (major), `⠴ **m1**` (minor), `⠠ **n1**` (nit).

---

### 3b. Codebase scan for similar issues

**After identifying any finding**, search the codebase for similar issues in the same class:

- Same anti-pattern in other files?
- Related code that might have the same bug?
- Copy-pasted code that shares the flaw?

Use `rg`/search to find other occurrences. Add them to the findings table if found. This prevents fixing one instance while leaving others broken.

---

### 4. Persistence (before verdict)

Write review to `.promptherder/convos/<slug>/review-<description>.md`.

- `<description>` should match the review scope (e.g. `review-login-fix.md`, `review-security.md`).
- Do not overwrite previous reviews unless explicitly requested.

The persisted file contains strengths, check coverage, findings table, details, and assessment — but NOT the action menu. The menu is conversational, not archival.

**Overwrite guard:** (Managed by `compound-v-persist` skill usage + dynamic filename)

Confirm the file exists by listing `.promptherder/convos/<slug>/`.

---

### 5. Verdict

State your assessment in 1-2 sentences (what you found, what matters most). When fixes remain and are not already authorized, present the action menu:

> FIX to fix ⠿⠷ (blockers + majors), FIX ALL to fix everything, SKIP to move on without fixes, or give feedback.

_Task: `<slug>`_

**When needed, the action menu appears exactly ONCE, at the very end of the response.** It comes AFTER persistence. Do not repeat it after file operations or any other step.

Clarify findings whose correction depends on missing input; continue independent authorized fixes.

---

## Fix triage (when user approves)

- FIX ALL → Fix in severity order (⠿ → ⠷ → ⠴ → ⠠), test after each.
- FIX → Fix ⠿ blockers and ⠷ majors. Note ⠴⠠ for later.
- SKIP → Confirm artifacts, move on.
- Feedback → Discuss, then fix agreed items.

**`YOLO` mode:**

Skip the action menu. Keep the required review report and auto-fix ALL findings (⠿ → ⠷ → ⠴ → ⠠). Output summary of what was fixed.

## Authorization and lifecycle

Keep the strengths, coverage, findings, persistence, and verdict structure above; never invent praise or findings to fill a count. For review-only work, report first and offer the action menu when fixes remain. FIX, FIX ALL, and ordinary requests to fix are valid authorization; YOLO is not required. When fixes were already requested or this review finishes an implementation task, perform those fixes without another generic approval stop. YOLO fixes every in-scope severity, including minor/nit findings. Out-of-scope ideas remain deferred.

Use `compound-v-persist` for the active slug and collision-safe report filename. Write the report once; wrappers do not replace it with a second summary. Review-only constraints end when the user authorizes fixes or advances to another phase.
