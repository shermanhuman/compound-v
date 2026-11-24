---
name: interrogate
description: Settle every open decision in a plan, design or idea in one round trip, and hand the user a task they must do themselves. Look up every fact first, then put the plan and every open decision in front of the user at once as one decision packet, with options shown rather than described and a recommendation pre-filled, and record the answers. Use before a plan's approval when it has open decisions, when the user asks to be grilled, interrogated or to stress-test a plan, or before asking the user to do a step themselves.
---

# Interrogate

Settle every decision in the plan in one round trip. The user's time is the scarce resource: do all the research before asking, then ask everything at once. Never drip questions one after another. (A goal's intent is the one exception: it's settled in conversation, one question at a time, before planning; see `compound-v:plan`'s *Intent first*.)

## Build the packet

1. **Map the decisions.** Read the plan, its decisions and its home (`compound-v:plan`'s *The plan's home*). Where the user's rules name a decision store, search it too:
   - **Settled:** an `accepted` or `rejected` row that is the goal's own or that the plan cites by ID. Never ask it again.
   - **Decided before:** a match from another goal. Put it in the packet as a clear call ("decided before in <ID>: …"), never drop the question silently, and never treat it as settled.
   - **Open:** `ask` rows, choices the planner made alone, and assumptions the plan relies on without saying so (defaults, limits, names, who can do what, what happens on failure, what ships first). Check the confirmed defaults, where the user's rules or the store keep them, before asking.
2. **Find every fact first.** Look up what each decision needs from the code, data, docs and environment, in one parallel batch, with subagents for anything broad. Never ask the user for a fact you can find.
3. **Sort.**
   - **Mechanical** (versions, file layout, check commands): record it, don't show it.
   - **Clear calls:** the evidence fits in one line, the alternatives are clearly worse, it's cheap to undo, it touches nothing the user sees (product direction, names, wording, spend, security, privacy), it conflicts with no user decision, and what it depends on is settled. An `ask` row qualifies only when a fact found since makes it clear-cut. These go on the packet's "decided unless you object" list.
   - **Decisions:** everything else. When in doubt, it's a decision. Mark each **critical** (the plan can't be right without it, or its answer can't be undone) or **optional** (it carries your default, the user may skip it, and work proceeds on the default). Critical ones come first.
4. **Make each decision concrete.**
   - **The question, then its context, then the options.** The question in one sentence (on a board, the title). Before the options, two or three lines of context: what's happening, why it needs the user now, and what the answer unblocks. One screen per decision: the question, the context, the thing shown and the options stay open; fold the rest.
   - **Show, don't tell.** Put the thing itself in front of the user: the mock or screenshot, the diagram, the diff or config, example output under each option, the numbers (as a chart, and a table whose columns say what they measure). Describe only what can't be shown.
   - **Options** lettered A, B, C, each with what happens and what it costs. **Each option stands on its own:** its label names what it means in full, never "those four" or "as above"; when it stands for a list, show the list as a table. Recommendation first, marked, with a one-line reason. The last option is always **More discussion**, for when the packet didn't give the user enough to decide.
   - **Links between decisions:** when one answer changes another decision, say how ("if 2B, skip 5") instead of holding the second one back.
5. **Record before sending.** Clear calls are recorded `accepted` (planner) and packet decisions `ask`, in the decision store where the rules name one, otherwise the plan's decisions table. The packet's link and text also go on the plan's home, so a reply like `2B` can still be read after lost context.

## Present it once

The packet has:
- **a top:** the goal, the plan in a few lines, the count (such as "2 critical and 4 optional decisions, 9 decided unless you object"), and a link to the full plan;
- **the decisions,** numbered from 1, critical first and then optional, each in order of consequence;
- **the clear calls,** numbered on from there, with one line of evidence each;
- **how to answer:** "Reply `ok` to take every recommendation, or only your changes: `2B, 5C, 7: <note>`, `4: more` for more discussion, `12: no` to object to a clear call."

Put the packet where the user will see it, never only in the chat, in the first of these that exists:

- **A board the user's rules name,** with an item schema command: run the schema command first. The packet is one group of items, so the agent is told once, when the last is answered:
  - each decision is an item, with its options and their mockups as blocks;
  - one more item carries the packet's top and the clear calls, decided-before matches included, with two options: accept them all, or object (the note names which).

  Accepting an item from its line takes its recommendation, so an optional item costs one click; the group completes only when every item is answered. Read the answers structurally from the board.
- **A decision page the user's rules name.**
- **An artifact or published page,** where the host has one.
- **A local HTML file,** written outside the working tree. The chat carries only the link.

In plan mode, while writes are blocked, open decisions go in the plan's decisions table as `ask` rows rather than the chat or the question tool, and are posted as the packet as soon as plan mode ends.

Answers are collected on the page when it can deliver them back to the session; otherwise the user replies in chat in the answer format above. Only when no page can be shown at all, or the user asks for it in chat, send the packet as plain text in one message. Never spread a packet across several messages or question-tool calls. Once its link is out, don't change the packet: put anything new in a follow-up.

## After the answers

1. **Resolve first, then record, in one edit.**
   - An optional decision the reply doesn't mention takes its recommendation, recorded as decided by "user (accepted the recommendation)". `ok` does this for every decision. A critical decision that a partial reply skips stays `ask` and joins the follow-up.
   - Before applying a default, check its links against the answers. A decision a chosen option makes moot is recorded `rejected` with "not applicable after 2B"; one whose condition is still open stays `ask`. Clear calls get the same check.
   - A chosen letter is `accepted`, decided by the user, dated, with their reason when they gave one. An option other than your recommendation gets its own `accepted` row.
   - A note with no letter that settles the decision ("7: neither, keep the current name") is the user's own option, recorded `accepted`.
   - These stay or go back to `ask` and join the follow-up: More discussion, an objection to a clear call, a note that asks something or leaves the choice open, and any answer that conflicts with an earlier one.
   - Record in the decision store when the rules name one (its decide command is the only way to change a row there; never edit a rendered table), otherwise in the plan's table. Update the plan's home, then change the steps, risks and assumptions the answers affect.
2. **One follow-up packet** for everything still open and any decision the answers opened that nobody could have foreseen, built the same way and showing the missing information. If a More discussion reply didn't say what was missing, first ask once what's missing for all of them, where the user picked More discussion (on the board, as a decision whose options are the likely gaps). Never fall back to one question at a time.
3. **Log rough edges** as [references/rough-edges.md](references/rough-edges.md) says: `more-discussion`, `foreseeable-follow-up` and `override-knowable` come from packets.

If the user asks to talk instead, talk it through in prose until they want the packet again.

## Tasks for the human

Sometimes the user has to do a step themselves. Each task spends their attention, so **push back on yourself first:**
1. **Is there a way in?** A CLI, an API, an MCP server, or a setting that makes the step unnecessary. Look before you ask.
2. **Is it really theirs?** Only for one of these reasons, which you name on the task:
   - it's a step the user's rules reserve for them;
   - it needs their own sign-in, identity or second factor;
   - it spends money;
   - it's physical;
   - the service offers no way for an agent to do it.
3. **Make their part as small as it can be.** Prepare everything around it: the exact command, the values to enter, the link with every ID filled in.

Post it where the user's rules put tasks (a board's task item), else under a **Needs the user** heading on the work's issue, and give the user its link. In this shape:

```
### Sign in to the cloud CLI   ~1 min · unblocks <what>
**Why it's yours:** needs your sign-in (the credentials expired).
**Tried:** `<command>` → "<the error>".

1. In a terminal, run:
   `<the exact command>`
2. Approve in the browser window that opens.
   You should see: "<what success looks like>"

**I'll check it myself:** `<the check>` succeeds.
**Ready on my side:** <what's prepared>. **Then I'll:** <the next step>.
```

Every link goes to the exact page, every command is ready to paste, and every step says what the user should see. A step waiting on the user doesn't stop the work: keep going on what can move. Run your check before carrying on, and say on the task if it failed. A task the user does often is a candidate for automation; log it as a `manual-step` rough edge.

## Finish

The session is done when nothing is open. Summarize what was decided and what changed in the plan, then stop. Don't start implementing until the user approves the plan as it now stands. Where the rules name a plan store, that approval is the store's approval item for the revision; when the user approves in chat or plan mode, post the approval item and wait for its answer. Otherwise it's the host's plan approval, when there is one.
