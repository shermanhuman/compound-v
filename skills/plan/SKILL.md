---
name: plan
description: The format and habits for an implementation plan — one-sentence goal, decisions table, checked steps, rollout and rollback, out-of-scope items with homes — plus how to ask the user questions and how to carry the plan through execution. Use whenever you write or revise a plan, including in the host's plan mode.
---

# Plans

This is a format, not a workflow: use it inside whatever planning mode the host has. Research first (read the code, check the data, check the docs for the versions actually pinned), then write the plan.

## Before you present it

Cut what doesn't earn its place: duplicated steps, anything there "just in case", anything more complex than the problem needs. Put each idea you rejected in the decisions table with the reason, so nobody re-proposes it.

## Deliver the goal whole

A plan delivers its goal whole: one plan, built to done, one pull request per repository. Each stage costs another plan, another review loop and another wait on the user.

Split the work into stages (phases, waves, a pilot, a first version and then the rest) only when the user asks or something forces it, such as a migration that must ship before the code that uses it, and record why in the decisions table.

"Lower risk" or "learn first" isn't a reason on its own; name the specific risk a single delivery would run. Moving part of the goal to Out of scope is a stage too.

## Sections

1. **Goal** — one sentence that defines success.
2. **Context** — why this change, what prompted it, what the outcome should be.
3. **Decisions** — every choice made while planning:

   | # | Idea | Verdict | Why | Decided |
   |---|---|---|---|---|
   | 1 | Store facts in a table, not a JSON column | accepted | atomic upserts; JSON read-modify-write lost a concurrent save | user, 2026-10-14 |
   | 2 | Add a "did you mean" index | rejected | four misspelt searches in 395; not worth a nightly job | planner, 2026-10-14 |
   | 3 | Keep the old column for one release | ask | needs the user's call on rollback window | — |

   Verdicts are `accepted`, `rejected` or `ask`. The table is the decisions log for the whole job: reviewers treat accepted and rejected rows as settled, it carries into the pull request body, and decisions made during review rounds are added as new rows with who and when.
4. **Steps** — each says what changes (files, by pattern rather than listing every file) and **how it's checked**, with a check that can actually fail. Reuse existing code where it exists and name it.
5. **Happy path** — for user-facing changes, a numbered walkthrough of what the user sees afterwards. It becomes the "where to look" list at the end.
6. **Risks, rollout and rollback** — what could go wrong, the order things ship in (migrations relative to deploys, which repository first), and how to undo each step.
7. **Assumptions** — anything inferred rather than confirmed, so it can be corrected.
8. **Out of scope** — each deferred item with its home: its own issue for real work, or one "Follow-ups from #N" checklist issue for small leftovers.

## Asking questions

Ask only what the code, the data or a sensible default can't answer, and ask it all at once, as one packet on a web page after the research, never one question after another.

`compound-v:interrogate` is the procedure: use it whenever a plan has open decisions before approval, or the user asks to stress-test one.

## The plan's home

When the project uses an issue tracker, every plan gets an issue: the plan in the body, reviews as comments, the approved revision written back to the body, and the steps as a checklist ticked off as they land. Run `compound-v:plan-review` with a fresh reviewer and fold its findings in before asking for approval.

## Carrying it out

- Build on a feature branch, in a separate worktree, from a fresh fetch of the default branch. The main checkout may hold someone else's work or a running server.
- Stop dependent work when a step's check fails; fix the cause before moving on.
- When reality disagrees with the plan, update the plan and the issue instead of drifting from them quietly.
- Finish by saying where to see it working: the preview or command, what to look at, and the edge cases worth trying.
