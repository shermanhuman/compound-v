---
name: plan-review
description: Critical review of an implementation plan before it is approved — checks its factual claims against the code and data, its scope, design traps, rollout and proof, and ends with approve / approve with changes / rework. Use whenever a plan is finished and before asking for approval, or when asked to review a plan.
---

# Plan review

You are a fresh reviewer at high effort. Read-only: don't change code, checkouts, data or the plan. Your job is to find what would make this plan fail or mislead, and to confirm what holds.

## Inputs

- the plan (an issue, a file, or both) and its decisions table
- the request it answers, if separate from the plan
- the repositories involved, and any research or evidence the plan was built from
- earlier reviews of this plan, if any (check their findings stayed fixed)

Read code from the default branch (`git fetch`, then `git show origin/<default>:<path>`) unless the plan is about a branch; working trees may hold someone else's changes.

## Check

1. **Claims hold.** Every `file:line`, count, quoted behaviour, "this already works" and "X is unused" claim — verify it against the code. Where the plan relies on production data or performance, check it with read-only queries when you have access; keep them light. Mark each claim verified or refuted, with evidence. If code-map tools are available (`map_find`, `map_entity`, `map_callers`, `map_impact`), use them for where things are defined and who calls them, and re-check any location they mark as changed since their snapshot against the code you're reviewing; otherwise grep.
2. **Scope.** The plan delivers the stated goal and the request, nothing important is silently dropped, and nothing extra crept in. Deferred items have a home (an issue), not just a mention.
3. **Decisions.** Accepted and rejected rows in the decisions table are settled; reopen one only as must-fix, stating the harm. Flag open `ask` rows the plan proceeds without.
4. **Design traps.** Silent failures, wrong defaults, behaviour that changes for existing users without saying so, a simpler option the plan missed, building more than the problem needs.
5. **Rollout.** Step order, what's broken between steps, migrations and their order relative to deploys, version bumps, one PR per repository where that's the rule, and whether rollback is real.
6. **Proof.** Each step's check can actually fail; tests sit at the right layer (see `compound-v:testing`); user-facing changes have an end-to-end check; success is measurable.

## Must-fix or polish

- **Must-fix** (⠿ **B** blocker, ⠷ **M** major): the plan as written would produce wrong behaviour, a security problem, data loss, a silent failure, a broken contract between components, or a rollout that fails — or a load-bearing claim is false.
- **Polish** (⠴ **m** minor, ⠠ **n** nit): everything else.

No speculative findings, no "could be clearer". A reviewer's suggestion is a hypothesis too: give the evidence for each finding so the author can test it.

## Report

```markdown
## Plan review: <plan title>

### Strengths
- 3–5 claims you verified, each with its evidence.

### Must-fix
| ID | Sev | Section | Issue | Fix |
|---|---|---|---|---|

### Polish
| ID | Sev | Section | Issue | Fix |
|---|---|---|---|---|

### Details
Only for must-fix findings whose reasoning isn't obvious from the row.

### Verdict
approve / approve with changes / rework — in one or two sentences.
```

Write it outside the repository and post it as a comment on the plan's issue (for GitHub: `gh issue comment <n> --body-file <file>`). If the issue doesn't exist yet (a plan mode that can't write), or you can't post, return the text and say it hasn't been posted; it goes on the issue when the issue is opened.
