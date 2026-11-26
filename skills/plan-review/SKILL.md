---
name: plan-review
description: Critical review of an implementation plan before it is approved — checks its factual claims against the code and data, its scope, design traps, rollout and proof, and ends with approve / approve with changes / rework. Use whenever a plan is finished and before asking for approval, or when asked to review a plan.
---

# Plan review

You are a fresh reviewer at high effort. Read-only: don't change code, checkouts, data or the plan. Your job is to find what would make this plan fail or mislead, and to confirm what holds.

## Inputs

- the plan (in a plan store the user's rules name, an issue, a file, or both), the revision under review, and its decisions; a reviewer that can't reach the store gets them in the brief
- the request it answers, if separate from the plan
- the repositories involved, and any research or evidence the plan was built from
- earlier reviews of this plan, if any (check their findings stayed fixed)

Read code from the default branch (`git fetch`, then `git show origin/<default>:<path>`) unless the plan is about a branch; working trees may hold someone else's changes.

## Check

1. **Claims hold.** Every `file:line`, count, quoted behaviour, "this already works" and "X is unused" claim — verify it against the code. Where the plan relies on production data or performance, check it with read-only queries when you have access; keep them light. Mark each claim verified or refuted, with evidence. If code-map tools are available (`map_find`, `map_entity`, `map_callers`, `map_impact`), use them for where things are defined and who calls them, and re-check any location they mark as changed since their snapshot against the code you're reviewing; otherwise grep.
2. **Scope.** The plan delivers the stated goal and the request, nothing important is silently dropped, and nothing extra crept in. Deferred items have a home (an issue), not just a mention; a deferred part of the goal or the request is a stage (check 4).
3. **Decisions.** Accepted and rejected rows are settled (the goal's own, and rows the plan cites by ID; a match from another goal is not); reopen one only as must-fix, stating the harm. The exception is a staging row the user didn't decide (check 4). Flag open `ask` rows the plan proceeds without.
4. **Design traps.** Before you read the plan's own *Traps* table, fill in yours: one row per **trap** in [causes.md](../review/references/causes.md). Each row says whether the trap applies here, where (a plan section, step or `file:line`), and the evidence: what you searched (the functions, the grep, the data you looked at). "Doesn't apply" says what was searched, not a reason. Then compare with the plan's table. Every disagreement, and every instance the plan didn't list, is a finding. A stage that nothing forces is polish, even where the decisions table accepts it, unless the user decided that row; the planner removes it or records what forces it (see `compound-v:plan`'s *Deliver the goal whole*).
5. **Rollout.** Step order, what's broken between steps, migrations and their order relative to deploys, version bumps, one PR per repository unless a recorded reason forces a stage, and whether rollback is real. Don't ask for a stage unless you name the risk that forces it.
6. **Proof.** Each step's check can actually fail, and is shown failing once (`vacuous-check` in [causes.md](../review/references/causes.md)). A change that touches many places is proved by its outcome (the rendered output, the live state), not by banning old spellings (`many-sites-proof`). Tests sit at the right layer (see `compound-v:testing`); user-facing changes have an end-to-end check; success is measurable.
7. **Deliverables.** The *Design* section has what the plan's goal type requires (`compound-v:plan`): for a Change and above, a diagram or a `No diagram:` line with its reason, user stories with acceptance tests, functions and interfaces, and the *Traps* table; for a Feature and above, the further parts the plan skill lists. Each part is specific to this plan. A required part that's missing or empty is must-fix; a suggested one is polish. Plans approved before this check existed are exempt.

## Must-fix or polish

- **Must-fix** (⠿ **B** blocker, ⠷ **M** major): the plan as written would produce wrong behaviour, a security problem, data loss, a silent failure, a broken contract between components, or a rollout that fails; or a load-bearing claim is false; or a required deliverable is missing (check 7). Each names its `Cause` from [causes.md](../review/references/causes.md), as in `compound-v:review`.
- **Polish** (⠴ **m** minor, ⠠ **n** nit): everything else.

No speculative findings, no "could be clearer". A reviewer's suggestion is a hypothesis too: give the evidence for each finding so the author can test it.

## Report

```markdown
## Plan review: <plan title>

### Strengths
- 3–5 claims you verified, each with its evidence.

### Traps
| Trap | Applies? | Where | What was searched | The plan's row agrees? |
|---|---|---|---|---|

### Must-fix
| ID | Sev | Section | Issue | Cause | Fix |
|---|---|---|---|---|---|

### Polish
| ID | Sev | Section | Issue | Fix |
|---|---|---|---|---|

### Details
Only for must-fix findings whose reasoning isn't obvious from the row.

### Verdict
approve / approve with changes / rework — in one or two sentences.
```

Write it outside the repository and post it in the plan's home: to a plan store the user's rules name, as a review of the revision you read; otherwise as a comment on the plan's issue (for GitHub: `gh issue comment <n> --body-file <file>`). If you can't post (a plan mode that can't write, a sandbox), return the text and say it hasn't been posted.
