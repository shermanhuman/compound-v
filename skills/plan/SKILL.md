---
name: plan
description: Use when the user gives you a new goal, before planning, and whenever you write or revise a plan, including in the host's plan mode. Covers the intent conversation and restatement, goal types, checks before planning, the plan format, and critical and optional questions.
---

# Plans

Use this inside whatever planning mode the host has: settle intent, research (read the code, check the data, check the docs for the versions actually pinned), then write the plan.

## Intent first

Before planning a new goal, settle what the user wants, in conversation:
1. **Look first.** Read what already answers it: the code, the issues, past decisions (where the user's rules name a plan or decision store, search its plans and decisions too). Never ask what you could find out.
2. **One question at a time,** each with your best guess, so "yes" is a full answer (on a board, one ask with every question and your guess for each). Ask only questions whose answer changes what gets built.
3. **About five at most.** Past that, say what's still unclear instead of asking more. "Enough, plan it" ends the conversation.
4. **Restate the goal** in this shape:
   - the goal in one sentence;
   - who it's for;
   - why now, and what not doing it costs;
   - **done when**, measurable, which becomes the acceptance tests;
   - **not doing**;
   - the goal type, and an ETA from past work of the same type and size, or "no history yet" when there's none to measure;
   - your assumptions.

   Then ask "Shall I start planning?", unless the user already said to plan.

The restatement goes at the top of the plan in its home (*The plan's home*; for a patch, its PR description), above the plan, and stays there when the plan is revised. It is the goal's anchor. Re-read it before each review round and before calling the work done; reviewers check the work against it. A request that already says what's wanted and what done looks like (a clear bug report, most patches) skips the questions and the closing ask: post the restatement and start.

## Goal types

| Type | Examples | Plan | *Design* section (beyond goal, scope, non-goals and how it's tested) |
|---|---|---|---|
| **Patch** | a bug fix, a copy change, a small config change | a short note: goal, how it's tested, steps | none |
| **Change** | a small enhancement, a refactor, an internal tool | the plan's sections, kept short | a diagram, user stories, functions and interfaces, traps; mockups when it touches a screen |
| **Feature** | new user-facing capability, a new integration | the full plan | the Change parts, plus a sequence diagram of the main flow, the data model or API spec, and what's logged and measured to learn how it's used; suggested: quality targets, cross-cutting concerns, alternatives considered |
| **Product** | a new app or service | feature depth | plus context and container views, and operations |

A patch touches no schema, dependency files, auth, money paths or public API, and changes under about 150 lines. Work that outgrows that is reclassified, and you say so.

## Before you write it

These cost the user nothing, so do them before any technical question or plan packet:
- **Look for something that already exists:** a library, a feature of a tool already in use, or an earlier attempt in the repository.
- **Spike instead of asking.** When a technical unknown would change the plan, run a short, time-boxed experiment.
- **Pre-mortem.** "It failed a month from now; why?" Put only the top risk in the plan, with what the plan does about it.
- **Who else it touches:** other repositories, users, operations, data. When the change removes a fallback, find out who relied on it.
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

   Verdicts are `accepted`, `rejected` or `ask`. The table is the decisions log for the whole job: reviewers treat accepted and rejected rows as settled, it carries into the pull request body, and decisions made during review rounds are added as new rows with who and when. Every row's `#` is unique and never reused.

   Where the user's rules name a decision store, the store holds the decisions: posting the plan records its rows, each with an ID. After that a decision changes only through the store's decide command, never by editing the table, and the plan shows the store's rows.
4. **Design** — what the goal-types table asks for, under these headings (a Patch has none):
   - `### Diagram`: a Mermaid diagram of every component that reads or writes the data the change touches, and the flow between them, or a `No diagram:` line with the reason. Two components reading one format, or a cache beside its source, show up here.
   - `### User stories`: who does what and what they see, each with an acceptance test that can fail. The restatement's *done when* isn't a substitute: it says what is true at the end, while a story walks one person through one path, edge cases included.
   - `### Functions and interfaces`: each new or changed function, route, table, message or instruction section, with its shape (signature, columns, payload) and the one fact it owns. A fact two entries claim is a design problem to settle now.
   - `### Traps`: one row per trap in `compound-v:review`'s [causes.md](../review/references/causes.md): whether it applies, where, and how the plan handles it. Plan review fills in its own table and compares.
   - For a Feature and above, the further parts the goal-types table lists, each under its own heading. Quality targets are measurable non-functional goals. Cross-cutting concerns are security, privacy and observability, with how the design handles each. Alternatives considered are other designs that would reach the goal, including buying or reusing, and why not.
5. **Steps** — under `### Steps`, each starting with its name in bold, saying what changes (files, by pattern rather than listing every file) and **how it's checked** in one `*Check:*` line, with a check that can actually fail. In a plan store, write them as a numbered list (`1. **Name.** …`), which the store ticks; anywhere else (an issue, a file), as task items (`- [ ] **Name.** …`), converted to the numbered list when the plan moves into a store. Reuse existing code where it exists and name it.
6. **Happy path** — for user-facing changes, a numbered walkthrough of what the user sees afterwards. It becomes the "where to look" list at the end.
7. **Risks, rollout and rollback** — what could go wrong, the order things ship in (migrations relative to deploys, which repository first), and how to undo each step.
8. **Assumptions** — anything inferred rather than confirmed, so it can be corrected.
9. **Out of scope** — each deferred item with its home: its own issue for real work, or one "Follow-ups from #N" checklist issue for small leftovers.

## Asking questions

Ask only what the code, the data, the decision record or a sensible default can't answer. Intent is a conversation (above); technical questions come all at once, as one packet after the research (`compound-v:interrogate`'s *Present it once*), never one after another, in two lists:
- **Critical:** what the plan can't be right without, and anything whose answer can't be undone (data deleted, a message sent, money spent, a public API released). These are answered before work starts.
- **Optional:** each with your default and its reason. The user can skip them all, and you proceed on the defaults.

A plan with no critical questions that the user's rules don't require approval for (bugs and upkeep usually go ahead) needs no packet. A question that comes up mid-work gets the same test: if its answer is cheap to undo, record your default in the plan's home (a patch's PR) and keep going; otherwise, and always when it can't be undone, ask, and carry on with the work it doesn't touch. Where the user's rules name a board, the question goes there, not the chat; in plan mode it waits in the decisions table as an `ask` row until plan mode ends (`compound-v:interrogate`).

`compound-v:interrogate` is the procedure: use it whenever a plan has open decisions before approval, or the user asks to stress-test one.

## The plan's home

A patch's short note goes in its pull request's description, with no issue of its own and no plan review; the PR's review covers it. Anything bigger has a home, so a long job survives a lost context:
- **A plan store the user's rules name:** the restatement, the plan and every revision, the steps, the decisions and the reviews live there, and approval is the store's approval item for a revision. The work's issue keeps the restatement and a link to the plan. If the store is unreachable, say so and keep working in the issue, marked "not yet in the plan store": the plan, decisions, reviews and ticks. Check the store again at the next step, and move them in once it's back; never let that fail silently.
- **Otherwise an issue,** when the project uses an issue tracker: the plan in the body, reviews as comments, the approved revision written back to the body, and the steps as a checklist ticked off as they land.

Run `compound-v:plan-review` with a fresh reviewer and fold its findings in before asking for approval.

## Carrying it out

- Build on a feature branch, in a separate worktree, from a fresh fetch of the default branch. The main checkout may hold someone else's work or a running server.
- Stop dependent work when a step's check fails; fix the cause before moving on.
- Tick each step as it lands, in the plan's home.
- A revision during the build goes on without a new approval unless it changes the restatement or a decision the user made. Then ask for approval of that revision, with the changed decision shown, hold the work it touches, and carry on with the rest.
- When reality disagrees with the plan, revise it in its home instead of drifting from it quietly.
- Finish by saying where to see it working: the preview or command, what to look at, and the edge cases worth trying.
