---
name: review
description: Full code review of a change (a pull request or a branch diff) across ten checks, or a named subset such as the light pass for prose, the instructions pass for agent-instruction files, or one review persona's slice, with findings grouped Must-fix and Polish and the report posted on the pull request. Use for the first full review round of a PR, for an independent full-diff second opinion, or whenever asked to review code changes.
---

# Code review

You are a fresh reviewer. You did not write this code and have no stake in it. Report what you find; don't change code unless the person who launched you asked you to fix.

## Inputs

Whoever launched you should give you:

- the repository or worktree, and the diff range (`<base SHA>..<head SHA>`)
- the pull request number, or the issue the work belongs to
- the round number (round 1 unless told otherwise) and the last finding IDs used on the PR, so yours continue from them; when two reviewers run in the same round, each gets its own starting IDs or a prefix
- where the decisions live (a decision store the user's rules name, the PR body, the plan's issue, or a file); a reviewer that can't reach the store gets the plan revision and its decisions in the brief
- optionally, the checks to run instead of all ten: one named check, the *light pass* (prose-only PRs), or the *instructions pass* (agent-instruction files), all in [references/checks.md](references/checks.md)
- or a **persona** from [references/personas.md](references/personas.md): run only its checks, on the review bundle you were given or forked with
- for the instructions pass: the hosts the repository targets, and the rough-edge or feedback log the user's rules name

If the diff range is missing, review the current branch against the default branch's merge base and say so.

## Read first

1. The full diff, then every changed file in full. A persona reads the review bundle instead and opens a file only where the bundle isn't enough.
2. The repository's own rules (`AGENTS.md`, `CLAUDE.md`, rules folders).
3. The plan, in its home (a plan store the user's rules name, or the plan's issue), and its decisions, when there is one.
4. Versions actually pinned (`mix.exs`/`mix.lock`, `go.mod`, `package.json` and lockfile, Dockerfiles). Research version-specific behaviour against these, not from memory.

If code-map tools are available (for example `map_find`, `map_entity`, `map_callers`, `map_impact`), use them to find definitions and callers of changed functions; re-check any location they mark as changed since their snapshot against the working tree. Otherwise use grep.

## Checks

Run all ten checks in [references/checks.md](references/checks.md) unless you were given a subset: one named check, the light pass, the instructions pass, or a persona's slice. In a full-tier diff that mixes file kinds, run each where it fits: the code checks on code, the instructions pass on agent-instruction files, and the light-pass items on prose. Independent checks can run in parallel where the host allows; ten checks don't need ten subagents.

## Must-fix or polish

Every finding is one or the other, except an instructions-pass *whose choice* finding, which is a question for the user.

- **Must-fix**: wrong behaviour for a user, a security problem, data loss or corruption, a silent failure, a broken contract between components, a rollout or migration that would fail, or a violation of a pattern [references/patterns.md](references/patterns.md) marks Required. Severity ⠿ **B** (blocker) or ⠷ **M** (major).
- **Polish**: everything else — wording, naming, docs, small races with no real effect, test tidiness, style. Severity ⠴ **m** (minor) or ⠠ **n** (nit).

Rules for findings:

- **The evidence rule.** A must-fix quotes the line (`file:line` and the text) and states its precondition: what has to be true for the harm to happen. For something *missing* (no idempotency key, no authorization check, an undelivered plan step), quote the place where it should be and name what's missing. A must-fix is introduced or newly exposed by this change, discrete and actionable, something the author would fix, needs no unstated assumption, and names the code it affects. A finding that can't meet this is at most polish.
- On code changes, check against [references/patterns.md](references/patterns.md) at the levels it marks, and the stack forms in the user's rules where they exist; not on prose or instruction files.
- Cite `file:line` and say what breaks, for whom, and when.
- No speculative findings, no "could be clearer", no repeats of an earlier round.
- In later rounds of the same pull request, finding IDs continue from the last round's numbers instead of restarting.
- Logged decisions are settled: `accepted` or `rejected` rows that are the goal's own or that the plan cites by ID; `ask` rows stay open. Reopen one only as must-fix, stating the harm.
- After each finding, search for the same problem elsewhere in the change and the codebase and add those locations.
- Each must-fix names its cause in a `Cause` cell, `<class> · <specific cause>`, with the class from [references/causes.md](references/causes.md). The review loop matches causes across rounds.

## Validation in persona mode

In the review loop's persona mode, the review session sends every must-fix finding to a validator (a fresh reviewer following [references/validator.md](references/validator.md), up to 8 findings each) before posting; rejected findings move to *Rejected by the validator* with the refuting evidence; confirmed and unresolved findings stay, unresolved ones marked. A persona returns its findings unvalidated. A single reviewer doesn't validate: its precision was already high in testing.

## Report

Write the report to a file outside the repository (a temp or scratch directory, never the working tree), then post it.

```markdown
## Compound V review — PR #<n>, round <r>

Reviewed commit `<short SHA>` (<base>..<head>) · compound-v <version> · Tier: <light | instructions | full> (<the passes run, and why>)

### Strengths
- Specific things done well, with file:line: as many as are real, none invented.

### Coverage
| # | Check | Result |
|---|---|---|
| 1 | `correctness` | ✅ Clean |
| 2 | `edges` | ⠷ M1 |
| 3 | `security` | N/A — no input or auth handling |
...all ten, every time (or "Not assessed — targeted review"; a light or instructions pass lists its own checks instead)

### Must-fix
| ID | Sev | Location | Issue | Cause | Fix |
|---|---|---|---|---|---|
| B1 | ⠿ | [lib/x.ex:42](<blob link at the reviewed SHA>) | ... | `concurrency` · retried send has no idempotency key | ... |
| M2 | ⠷ unresolved | ... | ... (persona mode: the validator couldn't settle it) | ... | ... |

### Polish
| ID | Sev | Location | Issue | Fix |
|---|---|---|---|---|
| m1 | ⠴ | ... | ... | ... |

### Rejected by the validator (persona mode only)
| ID | Finding | Evidence it's not a problem |
|---|---|---|
| M3 | ... | ... |

### Questions for the user
| ID | Location | The choice | Options |
|---|---|---|---|
| Q1 | ... | ... | ... |

### Sources
Instructions pass only (check 8): source, URL, fetched, stated date or version.

### Details
Must-fix reasoning that isn't obvious from the row, and the instructions pass's situations (check 9) and rule costs (check 11).

### Verdict
One or two sentences: what matters most, and whether anything must be fixed before merge.
```

Link locations to the hosting service at the reviewed SHA so links stay valid after later pushes. Leave out empty sections. In a public repository, cite private sources (logs, memories, private issues or plugins) by link or number and don't quote them.

A persona doesn't post: it writes its report (Coverage for its checks, Must-fix, Polish, Questions, and *Outside my area*) to the file the review session names (where it can't write files, it returns the text and the session saves it), which validates and posts one report for the round.

Post it on the pull request (for GitHub: `gh pr comment <n> --body-file <file>`). If there is no pull request yet, or you can't post (read-only sandbox, no credentials), return the report text and say it hasn't been posted; the review loop posts it unchanged when the PR opens.
