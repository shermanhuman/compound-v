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
   - **Clear calls:** the evidence fits in one line, the alternatives are clearly worse, it's cheap to undo, it touches nothing the user sees (product direction, names, wording, spend, security, privacy), it conflicts with no user decision, and what it depends on is settled. An `ask` row qualifies only when a fact found since makes it clear-cut. These go on the packet's "decided unless you object" list.
   - **Decisions:** everything else. When in doubt, it's a decision.
4. **Make each decision concrete.**
   - **The question** in one sentence, and what it changes.
   - **Show, don't tell.** Put the thing itself in front of the user: the mock or screenshot, the diagram, the diff or config, example output under each option, the numbers. Describe only what can't be shown.
   - **Options** lettered A, B, C, each with what happens and what it costs. Recommendation first, marked. The last option is always **More discussion**, for when the packet didn't give the user enough to decide.
   - **Links between decisions:** when one answer changes another decision, say how ("if 2B, skip 5") instead of holding the second one back.
5. **Record before sending.** Clear calls go in the table as `accepted` (planner), packet decisions as `ask`. A packet sent as plain text or a page is also posted on the plan's issue, so a reply like `2B` can still be read after lost context.

## Present it once

The packet has a top (the goal, the plan in a few lines, the count such as "6 decisions, 9 decided unless you object", a link to the full plan), the decisions numbered from 1 in order of consequence, the clear calls numbered on from there with one line of evidence each, and how to answer: "Reply `ok` to take every recommendation, or only your changes: `2B, 5C, 7: <note>`, `4: more` for more discussion, `12: no` to object to a clear call."

Pick one surface and send everything on it:

- **Plain text** by default: the packet in Markdown, with mocks and diagrams as code blocks or links to rendered files.
- **A page** when the packet has visuals text can't carry, or is too long for chat: an artifact or published page where the host has one, otherwise a local HTML file written outside the working tree, its path given to the user. Answers come back in chat unless the page can deliver them.
- **The question tool** only when the whole packet fits in a single call: the goal and count in the first question's text, every decision as a question with previews for what each option shows, and the clear calls as one multi-select "tick any you object to" question. Nothing the user needs may sit only in text before the widget; the user doesn't read it. Never spread one packet across several calls.

## After the answers

1. **Resolve first, then record, in one edit.**
   - A decision the reply doesn't mention takes its recommendation, recorded as decided by "user (accepted the recommendation)". `ok` does this for all of them.
   - Before applying a default, check its links against the answers: a decision a chosen option makes moot is recorded `rejected` with "not applicable after 2B"; one whose condition is still open stays `ask`. Clear calls get the same check.
   - A chosen letter is `accepted`, decided by the user, dated, with their reason when they gave one; an option other than your recommendation gets its own `accepted` row.
   - These stay `ask` and join the follow-up: More discussion, an objection to a clear call, a note with no letter, and any answer that conflicts with an earlier one.
   - Update the plan's issue too, then change the steps, risks and assumptions the answers affect.
2. **One follow-up packet** for everything still open and any decision the answers opened that nobody could have foreseen, built the same way and showing the missing information. If a More discussion reply didn't say what was missing, first ask in one plain-text message what's missing for all of them. Never fall back to one question at a time.
3. **Log rough edges** only where the user's rules name a home for them; with no home, list them in your final summary. One line each: the skill, the kind, the decision, and what was missing. Kinds: `more-discussion` (the packet didn't present what the user needed), `foreseeable-follow-up` (a follow-up asked something the first packet could have), `override-knowable` (the user overrode a recommendation for a reason the research could have found).

If the user asks to talk instead, talk it through in prose until they want the packet again.

## Finish

The session is done when nothing is open. Summarize what was decided and what changed in the plan, then stop. Don't start implementing until the user approves the plan as it now stands, through the host's plan approval when there is one.
