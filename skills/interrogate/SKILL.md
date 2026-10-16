---
name: interrogate
description: Settle every open decision in a plan, design or idea by questioning the user one decision at a time, most consequential first, with a recommendation each time and every answer recorded in the plan's decisions table. Use when the user asks to be grilled, interrogated or cross-examined, or to stress-test a plan before approving it.
---

# Interrogate

Question the user until every decision in the plan is settled and nothing is silently assumed. You bring the facts and a recommendation; the user makes the decisions.

## Map the decisions first

Read the plan, its decisions table and any issue it lives on. Build a decision tree: each open decision, and the decisions that hang off it.

- **Settled:** rows the user already decided (`accepted` or `rejected`, decided by the user). Never ask them again.
- **Open:** `ask` rows, choices the planner made on its own, and assumptions the plan relies on without saying so. Hunt for the last kind: defaults, limits, names, who can do what, what happens on failure, what ships first.
- **Facts are your job.** If a decision needs a fact from the code, the data, the docs or the environment, look it up (dispatch a subagent for anything broad) and put the result in the question. Never ask the user for something you can find yourself. Don't wait on a lookup: while it runs, that decision and the ones below it are blocked, so ask the next most consequential decision that isn't, and come back when the fact is in.

Send the user the map: how many decisions are open, the order you'll take them in, and which ones may disappear depending on early answers. Where the host has a question tool, send it as a question whose options are start, accept the rest, summarize first, and let's just talk. Otherwise send it as its own message and wait for the go-ahead.

## Keep the gaps short

The user waits between questions, and you can't work while a question is open. Do the slow work before asking, not after the answer.

- **Gather every fact up front.** While building the map, look up the facts all the open decisions need, in one parallel batch. Then no question has to wait on a lookup.
- **Prepare the next question before sending this one.** Know which decision comes next for each likely answer, and have its facts and options ready.
- **Record and ask in one step.** After an answer, make the plan edits and send the next question in the same response, not one after the other.

## Ask one decision at a time

Take the open decision that the most other decisions depend on. Its answer can settle or remove the ones below it.

- **Use the host's question tool** when it has one. Put the full context inside the question: the situation, what's at stake, and any fact you looked up. In each option, say what happens and what it costs, with longer detail in a per-option preview where the host supports one. Put your recommendation first and mark it. Text written before the question is easy to miss, so don't rely on it.
- **Without a question tool**, ask in plain text: a short heading, the context, the options with their costs, and your recommendation, worded so that "yes" accepts it.
- One decision per question. Don't batch, even when several look independent; a batch gets skimmed.
- Plain formatting. No emoji.

## After each answer

1. Record it straight away in the plan's decisions table: verdict `accepted` or `rejected`, why (in the user's words when they gave a reason), decided by the user, with the date. When the user picks an option other than your recommendation, add it as its own `accepted` row. Update the plan's issue too when there is one. A long session then survives lost context, and nobody asks the same thing twice.
2. Change any step, risk or assumption the answer affects.
3. Redraw the tree: drop decisions the answer made moot, add the ones it opened, and pick the next most consequential decision.

## When the user steers

- **"Accept the rest":** take your recommendation for every remaining decision, record each as decided by the user with the note "accepted the recommendation", and list them back in one message.
- **"Let's just talk":** stop using the question tool and continue in prose until they're ready to resume.
- **"Summarize first":** give a synopsis of where things stand before the next question.
- **A question about a question:** when the user stops to ask something (what it costs, how others do it), find the facts, then ask the same decision again with the answer inside the question's context. Text written before a question is easy to miss.
- **An answer that conflicts with an earlier one:** point out the conflict and ask which stands. Don't quietly overwrite either.

## Finish

The session is done when no decision is left open. Summarize what was decided and what changed in the plan, then stop. Don't start implementing until the user confirms the plan as it now stands, through the host's plan approval when there is one.
