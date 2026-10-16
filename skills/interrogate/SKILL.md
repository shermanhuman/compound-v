---
name: interrogate
description: Settle every open decision in a plan, design or idea. Calls the evidence already makes go to the user as one pre-decided checklist; the rest are asked one decision at a time, most consequential first, with a recommendation each time. Every answer is recorded in the plan's decisions table. Use when the user asks to be grilled, interrogated or cross-examined, or to stress-test a plan before approving it.
---

# Interrogate

Settle every decision in the plan so nothing is silently assumed, without spending the user's time on calls the evidence already makes. You bring the facts, make the clear calls and put them in front of the user as a checklist. The user ticks the ones they accept and decides the rest one at a time.

## Map the decisions first

Read the plan, its decisions table and any issue it lives on. Build a decision tree: each open decision, and the decisions that hang off it.

- **Settled:** rows the user already decided (`accepted` or `rejected`, decided by the user). Never ask them again.
- **Open:** `ask` rows, choices the planner made on its own, and assumptions the plan relies on without saying so. Hunt for the last kind: defaults, limits, names, who can do what, what happens on failure, what ships first.
- **Facts are your job.** If a decision needs a fact from the code, the data, the docs or the environment, look it up (dispatch a subagent for anything broad) and put the result in the question. Never ask the user for something you can find yourself. If a fact is still out when its decision comes up, don't wait: that decision and the ones below it are blocked, so ask the next most consequential one that isn't, and come back when the fact is in.

Then sort the open decisions into three piles.

- **Mechanical:** version numbers, check commands and file layout. Record them as planner decisions and don't show them; the user can read the table.
- **Checklist:** consequential calls you'd make yourself and expect the user to wave through. Every test must hold:
  - the evidence fits in one line (code, data, docs, a row the user already decided, or an explicit user rule)
  - the alternatives are clearly worse, not close
  - it's cheap to reverse and touches little
  - it changes nothing the user sees: no product direction, names or wording, spend, security or privacy, and nothing hard to undo
  - it conflicts with no user decision
  - everything it depends on is settled, or is on the checklist ahead of it

  An `ask` row qualifies only when a fact looked up since the plan was written makes it clear-cut.
- **Queue:** everything else, asked one at a time.

When in doubt, queue it. Record the checklist calls in the decisions table as `accepted`, decided by the planner, before you send the checklist, so the list survives lost context.

## Keep the gaps short

The user waits between questions, and you can't work while a question is open. Do the slow work before asking, not after the answer.

- **Gather every fact up front.** While building the map, look up the facts all the open decisions need, in one parallel batch. Then no question has to wait on a lookup.
- **Build the checklist and the first queue question in the same pass.** The checklist's answers lead straight into the queue.
- **Prepare the next question before sending this one.** Know which decision comes next for each likely answer, and have its facts and options ready.
- **Record and ask in one step.** After an answer, make the plan edits and send the next question in the same response, not as two separate responses.

## Present the checklist

When the host's question tool has a multi-select mode, the checklist is the first thing the user sees. Don't send a map message first; the first question's text carries the count, because text written before a question is easy to miss.

- **Layout.** One multi-select question per group of two to four related decisions (same step or area), parents before children, most consequential group first, and up to four questions per call; another call takes anything past sixteen. The tool needs at least two options per question, so split a group of five 3 + 2, fold a lone item into the nearest group, and ask a one-item checklist as a single-choice question (accept it, or ask me about it).
  - **Header:** the area, in twelve characters or fewer ("Storage", "Rollout").
  - **Question text:** the area and the count, then: "Tick each decision you accept as made. Anything unticked is asked on its own next. Type under Other to correct one." The first question also carries the map in one line: "N open: M here, K asked one at a time after."
- **Each option is one decision, already made.** The label is the choice itself in five words or fewer, not "Accept …". Multi-select has no per-option preview, so the description carries everything the user needs, in about fifty words:
  - *Decided:* what.
  - *Because:* the one-line evidence.
  - *Instead of:* the nearest alternative, and why it's worse.
  - *Undo:* what reversing costs.
  - *Depends on:* the earlier item, when there is one.
- **Reading the answer:**
  - Ticked items are accepted. Unticked items join the queue, and so does everything ticked that depended on one. Nothing ticked queues everything (if the tool refuses an empty answer, "none" under Other does the same).
  - Text under Other that names an item and a different choice is a correction: record the user's choice as its own `accepted` row and yours as `rejected`. When it's unclear which item it means, queue that item with the text as its context.
  - A steering phrase under Other ("all", "none", "ask me each one") steers, as in *When the user steers*. Item numbers or labels alone ("not 3", "drop the shim") mean those items are unticked.
  - Any other text under Other that isn't about an item is a new request. Add it to the plan as a decision decided by the user, and say so in your next message.
- **This is the only batch.** The queue never batches, because a batch gets skimmed. The checklist can be skimmed safely: an unticked item costs one question, not a wrong decision.
- **Without multi-select** (a tool limited to a few single-choice questions, a non-interactive run, or no question tool at all): send the checklist as a numbered plain-text list with the same five fields per item, ending "Reply 'all' to accept these, or the numbers to ask about one at a time." Use the host's question tool, where it has one, for the queue.

An empty checklist goes straight to the queue, and the first queue question carries the map line. An empty queue after the checklist means you're finished.

## Ask the queue one decision at a time

Take the queued decision that the most other decisions depend on. Its answer can settle or remove the ones below it.

- **Use the host's question tool** when it has one. Put the full context inside the question: the situation, what's at stake, and any fact you looked up. In each option, say what happens and what it costs, with longer detail in a per-option preview where the host supports one. Put your recommendation first and mark it. Text written before the question is easy to miss, so don't rely on it.
- **Without a question tool**, ask in plain text: a short heading, the context, the options with their costs, and your recommendation, worded so that "yes" accepts it.
- One decision per question. The checklist was the batch, and only for calls the evidence already made.
- Plain formatting. No emoji.

## After each answer

1. Record it straight away in the plan's decisions table: verdict `accepted` or `rejected`, why (in the user's words when they gave a reason), decided by the user, with the date. When the user picks an option other than your recommendation, add it as its own `accepted` row.
   - For the checklist, do it in one edit, from the same resolved answer that builds the queue. Each ticked item becomes `accepted`, decided by "user (checklist)" with the date, unless it went back to the queue because something it depends on was unticked. Every queued item, unticked or re-queued, becomes `ask`, keeping its why, decided "—".
   - Update the plan's issue too when there is one. A long session then survives lost context, and nobody asks the same thing twice.
2. Change any step, risk or assumption the answer affects.
3. Redraw the tree: drop decisions the answer made moot, add the ones it opened, and pick the next most consequential decision. After the checklist, the first queue question goes in the same response as the edits.

## When the user steers

- **"None":** nothing on the checklist is accepted; queue every item.
- **"Accept the rest":** take your recommendation for every remaining decision, record each as decided by the user with the note "accepted the recommendation", and list them back in one message. On the checklist, "all" under Other ticks everything.
- **"Ask me each one":** skip the checklist, queue everything, and set the planner's checklist rows back to `ask`.
- **"Let's just talk":** stop using the question tool and continue in prose until they're ready to resume.
- **"Summarize first":** give a synopsis of where things stand before the next question.
- **A question about a question:** when the user stops to ask something (what it costs, how others do it), find the facts, then ask the same decision again with the answer inside the question's context. Text written before a question is easy to miss.
- **An answer that conflicts with an earlier one:** point out the conflict and ask which stands. Don't quietly overwrite either.

## Finish

The session is done when no decision is left open. Summarize what was decided and what changed in the plan, then stop. Don't start implementing until the user confirms the plan as it now stands, through the host's plan approval when there is one.
