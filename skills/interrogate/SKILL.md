---
name: interrogate
description: Settle every open decision in a plan, design or idea in one round trip. Look up every fact first, then put the plan and every open decision in front of the user at once as one decision packet, with options shown rather than described and a recommendation pre-filled, and record the answers in the plan's decisions table. Use before a plan's approval when it has open decisions, or when the user asks to be grilled, interrogated or to stress-test a plan.
---

# Interrogate

Settle every decision in the plan in one round trip. The user's time is the scarce resource: do all the research before asking, then ask everything at once. Never drip questions one after another.

## Build the packet

1. **Map the decisions.** Read the plan, its decisions table and any issue it lives on. Rows the user already decided (`accepted` or `rejected`) are settled; never ask them again. Open: `ask` rows, choices the planner made alone, and assumptions the plan relies on without saying so (defaults, limits, names, who can do what, what happens on failure, what ships first).
2. **Find every fact first.** Look up what each decision needs from the code, data, docs and environment, in one parallel batch, with subagents for anything broad. Never ask the user for a fact you can find.
3. **Sort.**
   - **Mechanical** (versions, file layout, check commands): record in the table, don't show.
   - **Clear calls:** the evidence fits in one line, the alternatives are clearly worse, it's cheap to undo, and it touches nothing the user sees (product direction, names, wording, spend, security, privacy). These go on the packet's "decided unless you object" list.
   - **Decisions:** everything else. When in doubt, it's a decision.
4. **Make each decision concrete.**
   - **The question** in one sentence, and what it changes.
   - **Show, don't tell.** Put the thing itself in front of the user: the mock or screenshot, the diagram, the diff or config, example output under each option, the numbers. Describe only what can't be shown.
   - **Options** lettered A, B, C, each with what happens and what it costs. Recommendation first, marked. The last option is always **More discussion**, for when the packet didn't give the user enough to decide.
   - **Links between decisions:** when one answer changes another decision, say how ("if 2B, skip 5") instead of holding the second one back.
5. **Record before sending.** Clear calls go in the table as `accepted` (planner); packet decisions as `ask`. The packet then survives lost context.

## Present it once

Everything goes out together, in one message or on one page:

- **Top:** the goal, the plan in a few lines, the count ("6 decisions, 9 decided unless you object") and a link to the full plan.
- **Decisions**, most consequential first.
- **Decided unless you object:** one line each, with its evidence.
- **How to answer:** "Reply `ok` to take every recommendation, or only your changes: `2B, 5C, 7: <note>`, or `4: more` for more discussion."

Use the richest surface the host offers:

- **A page** when the host can show one (an artifact, a published page, a local HTML file the user opens): best for mocks, diagrams and long packets. Collect the answers on the page when it can.
- **The question tool** only when the whole packet fits in a single call, every decision at once, with previews for what each option shows. Never spread one packet across several calls.
- **Plain text** otherwise: the same packet in Markdown, with mocks and diagrams as code blocks or links to rendered files.

## After the answers

1. Record every answer in one edit: `accepted` or `rejected`, why (in the user's words when they gave a reason), decided by the user, dated. `ok` takes every recommendation; record those as decided by "user (accepted the recommendation)". An option other than your recommendation gets its own `accepted` row. Update the plan's issue too.
2. Change the steps, risks and assumptions the answers affect.
3. If the answers ask for more discussion, open decisions nobody could have foreseen, conflict with an earlier answer, or ask a question about a question, send **one follow-up packet** with all of them, built the same way, showing the missing information. Never fall back to one question at a time.
4. **Log rough edges** where the user's rules say they go (otherwise as a comment on the plan's issue), one line each: the skill, the kind, the decision, and what was missing. Kinds: `more-discussion` (the packet didn't present what the user needed), `foreseeable-follow-up` (a follow-up packet asked something the first one could have), `override-knowable` (the user overrode a recommendation for a reason the research could have found).

If the user asks to talk instead, talk it through in prose until they want the packet again.

## Finish

The session is done when nothing is open. Summarize what was decided and what changed in the plan, then stop. Don't start implementing until the user approves the plan as it now stands, through the host's plan approval when there is one.
