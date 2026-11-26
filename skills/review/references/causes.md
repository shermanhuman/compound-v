# Causes

Every must-fix finding, in a code review, a follow-up or a plan review, names its cause in a `Cause` cell: `<class> · <the specific cause in a few words>`, for example `two-owners · plan text parsed by the server and by the page`. The class comes from the table below, and this file is its only list; the other skills cite it.

The class is for counting. The specific cause is what a follow-up matches: two findings share a cause when one fix would have prevented both. Two findings of the same class with different causes are not a recurrence.

Rows marked **trap** are the design traps: a plan lists them in its *Traps* table, and a plan reviewer checks each one against the plan with evidence (`compound-v:plan-review`, check 4). Rows marked **proof** are about how a change is proved: plan-review check 6 and review check 5 cite them.

The examples come from a review of about 2,000 must-fix findings on real pull requests and plans.

| Class | Kind | What it is | The question it asks | Example |
|---|---|---|---|---|
| `two-owners` | trap | One fact kept in two places that must stay in step, and they drift: two parsers of one format, a cache and its source, a rule written in two languages, docs and the constants they describe. **Our own copy of an outside tool's or API's behaviour counts too**: hand-written shell or SQL parsing, an assumed API shape and a stub built on it. | Can one side own it, and the other read from it (or run the real tool)? | The server guessed where the page's Markdown renderer put a plan's steps; each fix covered one more shape and broke another. |
| `merged-facts` | trap | Two facts that only looked the same were merged, deduplicated or simplified into one, hiding one of them. | Are these the same fact, or the same text? What fixture shows them differing? | "Read 5 min ago" shown once for two windows that were read at different times. |
| `concurrency` | trap | Two writers, a retry, a late response or an out-of-order event: races, lost updates, double sends, idempotency. | Who else writes this, twice, at once or out of order? | A draft saved after its ask was answered overwrote the answer. |
| `silent-failure` | trap | An error swallowed, a fallback that hides a failure, a job that reports success after failing, a check that quietly does nothing. | When this fails, who finds out, and how? | A parser failure returned an empty preview instead of an error. |
| `wrong-default` | trap | A bad default, flag, path or setting, or behaviour that changes for an existing user or caller without saying so. | What does an existing user or caller see the day this ships? | Copying production settings to staging left a release switch on. |
| `release-path` | trap | Migration, deploy, rollback or production hazards: what runs between steps, who else drives production, and whether rollback is real. | What runs in production between each step, and who else changes it? | A release script and a GitOps controller's auto-sync both drove production, so the script reported green while the controller rolled it back. |
| `overbuilt` | trap | More complex than the problem needs, or a simpler option the plan missed. | What is the simplest thing that meets the stated need? | A goal of less complexity reviewed through 22 reports of new machinery. |
| `many-sites-proof` | proof | A change that touches many places (a migration, rename or swap) done site by site and proved by banning old spellings, so each round finds a variant. | Is the outcome checked (rendered output, live state), not the spelling? | A source test banned one spelling of hand-built markup; each round found another. |
| `vacuous-check` | proof | A test or check that can't fail, or that passes when the fact it guards is gone. | Was it shown failing once? | A count asserted on an empty fixture. |
| `edge-input` | | An input shape, empty or null, boundary, time zone or ordering not handled. | | |
| `logic` | | A plain logic bug that fits no other class. | | |
| `spec-drift` | | The change doesn't do what the plan, the restatement or the issue says. | | |
| `security` | | Escaping, authorization, secrets, injection, loosened permissions. | | |
| `performance` | | Correct, but slow or memory-hungry at real size or under hostile input. | | |
| `doc-accuracy` | | Prose, a PR body, docs or skill text that is wrong or contradicts itself. | | |
| `ui-visual` | | Layout, rendering or accessibility problems seen on screen. | | |
| `ambiguous-instruction` | | An agent-facing rule that can be read two ways. | | |
