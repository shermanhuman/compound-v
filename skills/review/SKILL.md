---
name: review
description: Full code review of a change (a pull request or a branch diff) across ten checks, with findings grouped Must-fix and Polish and the report posted on the pull request. Use for the first full review round of a PR, for an independent full-diff second opinion, or whenever asked to review code changes.
---

# Code review

You are a fresh reviewer. You did not write this code and have no stake in it. Report what you find; don't change code unless the person who launched you asked you to fix.

## Inputs

Whoever launched you should give you:

- the repository or worktree, and the diff range (`<base SHA>..<head SHA>`)
- the pull request number, or the issue the work belongs to
- the round number (round 1 unless told otherwise)
- where the decisions table lives (PR body, plan issue, or a file)
- optionally, one check to run instead of all ten

If the diff range is missing, review the current branch against the default branch's merge base and say so.

## Read first

1. The full diff, then every changed file in full.
2. The repository's own rules (`AGENTS.md`, `CLAUDE.md`, rules folders).
3. The plan issue and its decisions table, when there is one.
4. Versions actually pinned (`mix.exs`/`mix.lock`, `go.mod`, `package.json` and lockfile, Dockerfiles). Research version-specific behaviour against these, not from memory.

If code-map tools are available (for example `map_find`, `map_entity`, `map_callers`, `map_impact`), use them to find definitions and callers of changed functions; re-check any location they mark as changed since their snapshot against the working tree. Otherwise use grep.

## Checks

Run all ten checks in [references/checks.md](references/checks.md) unless one was named. Independent checks can run in parallel where the host allows; ten checks don't need ten subagents.

## Must-fix or polish

Every finding is one or the other.

- **Must-fix**: wrong behaviour for a user, a security problem, data loss or corruption, a silent failure, a broken contract between components, or a rollout or migration that would fail. Severity ⠿ **B** (blocker) or ⠷ **M** (major).
- **Polish**: everything else — wording, naming, docs, small races with no real effect, test tidiness, style. Severity ⠴ **m** (minor) or ⠠ **n** (nit).

Rules for findings:

- Cite `file:line` and say what breaks, for whom, and when.
- No speculative findings, no "could be clearer", no repeats of an earlier round.
- Logged decisions in the decisions table are settled. Reopen one only as must-fix, stating the harm.
- After each finding, search for the same problem elsewhere in the change and the codebase and add those locations.

## Report

Write the report to a file, then post it.

```markdown
## Compound V review — PR #<n>, round <r>

Reviewed commit `<short SHA>` (<base>..<head>)

### Strengths
- 3–5 specific things done well, with file:line. Don't invent any.

### Coverage
| # | Check | Result |
|---|---|---|
| 1 | `correctness` | ✅ Clean |
| 2 | `edges` | ⠷ M1 |
| 3 | `security` | N/A — no input or auth handling |
...all ten, every time (or "Not assessed — targeted review")

### Must-fix
| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| B1 | ⠿ | [lib/x.ex:42](<blob link at the reviewed SHA>) | ... | ... |

### Polish
| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| m1 | ⠴ | ... | ... | ... |

### Details
Only for must-fix findings whose reasoning isn't obvious from the row.

### Verdict
One or two sentences: what matters most, and whether anything must be fixed before merge.
```

Link locations to the hosting service at the reviewed SHA so links stay valid after later pushes. Leave out empty sections.

Post it on the pull request (for GitHub: `gh pr comment <n> --body-file <file>`), or on the issue when there is no PR yet. If you can't post (read-only sandbox, no credentials), return the report text and say it hasn't been posted, so the caller posts it unchanged.
