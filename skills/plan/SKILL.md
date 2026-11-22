---
name: plan
description: How a goal becomes a plan — the intent conversation (one question at a time, then a restatement), goal types, checks to run before planning, and the plan format (one-sentence goal, decisions table, checked steps, rollout and rollback, out-of-scope items with homes), plus critical and optional questions and carrying the plan through execution. Use when the user gives you a new goal, before planning, and whenever you write or revise a plan, including in the host's plan mode.
---

# Plans

Use this inside whatever planning mode the host has: settle intent, research (read the code, check the data, check the docs for the versions actually pinned), then write the plan.

## Intent first

Before planning a new goal, settle what the user wants, in conversation:
1. **Look first.** Read what already answers it: the code, the issues, past decisions. Never ask what you could find out.
2. **One question at a time,** each with your best guess, so "yes" is a full answer. Ask only questions whose answer changes what gets built.
3. **About five at most.** Past that, say what's still unclear instead of asking more. "Enough, plan it" ends the conversation.
4. **Restate the goal** in this shape:
   - the goal in one sentence;
   - who it's for;
   - why now, and what not doing it costs;
   - **done when**, measurable, which becomes the acceptance tests;
   - **not doing**;
   - the goal type, and an ETA from past work of the same type and size;
   - your assumptions.

   Then ask "Shall I start planning?"

The restatement goes at the top of the plan's issue (*The plan's home*), above the plan, and stays there when the plan is revised. It is the goal's anchor. Re-read it at every checkpoint; reviewers check the work against it. A request that already says what's wanted and what done looks like (a clear bug report, most patches) skips the questions and the closing ask: post the restatement and start.

## Goal types

| Type | Examples | Plan | Plan deliverables, beyond goal, scope, non-goals and how it's tested |
|---|---|---|---|
| **Patch** | a bug fix, a copy change, a small config change | a short note | none |
| **Change** | a small enhancement, a refactor, an internal tool | a short plan | user stories with acceptance tests; a diagram, mockups, API spec or ER diagram when it touches those |
| **Feature** | new user-facing capability, a new integration | the full plan | all of those that apply, plus what's logged and measured to learn how it's used |
| **Product** | a new app or service | feature depth | plus architecture and operations |

A patch touches no schema, dependency files, auth, money paths or public API, and changes under about 150 lines. Work that outgrows that is reclassified, and you say so.

## Before you write it

These cost the user nothing, so do them before asking anything:
- **Look for something that already exists:** a library, a feature of a tool already in use, or an earlier attempt in the repository.
- **Spike instead of asking.** When a technical unknown would change the plan, run a short, time-boxed experiment.
- **Pre-mortem.** "It failed a month from now; why?" Put only the top risk in the plan, with what the plan does about it.
- **Who else it touches:** other repositories, users, operations, data.
- **Sort decisions by reversibility.** What's cheap to undo gets a default; what can't be undone is a critical question.

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

Ask only what the code, the data or a sensible default can't answer. Intent is a conversation (above); technical questions come all at once, as one packet on a web page after the research, never one after another, in two lists:
- **Critical:** what the plan can't be right without, and anything whose answer can't be undone. These are answered before work starts.
- **Optional:** each with your default and its reason. The user can skip them all, and you proceed on the defaults.

A plan with no critical questions and no approval needed goes ahead without a packet. A question that comes up mid-work gets the same test: if its answer is cheap to undo, record your default where the user will see it and keep going; otherwise it waits.

`compound-v:interrogate` is the procedure: use it whenever a plan has open decisions before approval, or the user asks to stress-test one.

## The plan's home

When the project uses an issue tracker, every plan gets an issue: the plan in the body, reviews as comments, the approved revision written back to the body, and the steps as a checklist ticked off as they land. Run `compound-v:plan-review` with a fresh reviewer and fold its findings in before asking for approval.

## Carrying it out

- Build on a feature branch, in a separate worktree, from a fresh fetch of the default branch. The main checkout may hold someone else's work or a running server.
- Stop dependent work when a step's check fails; fix the cause before moving on.
- When reality disagrees with the plan, update the plan and the issue instead of drifting from them quietly.
- Finish by saying where to see it working: the preview or command, what to look at, and the edge cases worth trying.
