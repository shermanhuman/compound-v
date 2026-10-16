---
name: review-loop
description: Runs the review rounds for a pull request or a plan — who reviews when, how fixes are verified, when to stop, and how every round is recorded on the PR or issue. Use before opening a pull request, after pushing new commits to one, when asked to run or continue a review round, and after finishing a plan.
---

# Review loop

Every round uses a **fresh** reviewer (a new subagent or a new process, not a fork of yourself): a reviewer that has seen the code tends to accept its own earlier conclusions. Brief it with the inputs its skill lists and the facts you've already verified, so it doesn't re-derive them.

## Choosing the tier

Pick the tier from the diff before round 1, and say which one and why in the PR body and the first review comment. The user can ask for the full tier at any time.

**Light** covers prose only. The list is closed: anything not on it is full.

- Prose in READMEs, docs and the changelog that gives no instructions. An instruction is a fenced command, an inline command someone would run, or an imperative step, so a procedural section is full.
- Comment-only code changes, confirmed by `git diff -w` showing only comment lines.
- Typo and wording fixes in those same files. A string a user or agent sees at runtime (templates, messages, translations, site copy) is code, so it's full.
- Changes to the PR body only, marketplace or listing descriptions (not their sources), and settings that only switch plugins on or off.

**Full** covers everything else. That includes agent-instruction files (`AGENTS.md`, `CLAUDE.md`, rules, skills, hook text) of any size, and their rounds use the *instructions pass* in [checks.md](../review/references/checks.md) on those files in place of the ten code checks. A mixed diff is full, with each file reviewed by the checks that fit it: the code checks for code, the instructions pass for instruction files, and the light-pass items for prose.

The PR's own version-line bump (the version line in any manifest: `plugin.json`, `marketplace.json`, `mix.exs`, `go.mod`, `package.json`) doesn't change the tier, and neither does a change to a plugin or listing entry's `description` text in those files. Any other change in them does, and lockfile changes count as dependency changes: full.

**The light loop.** A fresh reviewer runs the *light pass* in [checks.md](../review/references/checks.md). Fix its polish and post fix notes; that's the whole loop, with no independent pass and no polish or quick-check cycle. A must-fix finding gets a `compound-v:followup` round on its fix, repeated while follow-ups find must-fix issues, as in the full tier's step 2. If a finding shows the diff wasn't prose-only, the PR moves to the full tier from there. Merging the default branch in, or a CI fix, needs no round unless it touches something on the full side.

## Pull requests

Open the pull request as a draft before round 1, so each round is posted on it as it lands, and mark it ready only after the final round has no must-fix findings.

Full tier:

1. **Round 1** — a fresh reviewer runs `compound-v:review` on the full diff against the default branch. If the user asked for a second opinion from another model, it runs `compound-v:review` too, in parallel; give it a prefix for its finding IDs (for example `A-M1`) so the two reports never share an ID.
2. **Fix** every must-fix finding (and that round's polish if it's cheap; leave the rest for the polish pass). Then a fresh reviewer runs `compound-v:followup` on the fix diff (`<last reviewed SHA>..HEAD`). Repeat while follow-ups find must-fix issues.
3. **Independent pass** — once a round has no must-fix findings, one full-diff pass by the configured second voice:
   - a different model when one is configured (the user's rules name it and how to run it), running `compound-v:review`;
   - otherwise the host's built-in review: in Claude Code, `/code-review high`, plus `/security-review` when the change touches authentication, user input, secrets or infrastructure; in Codex, `codex review`;
   - otherwise a fresh `compound-v:review` pass by yourself, re-reading the full diff from the start.

   Say on the PR which one ran, and why if it fell back. Its must-fix findings go back to step 2.
4. **Polish pass** — fix all open polish in one go, small fixes only (a redesign now is what makes the next round find new problems). Run the tests, then a quick `compound-v:followup` of only the polish diff. New polish it raises is noted, not fixed; a must-fix sends you back to step 2.

**Stop rule.** Keep going while each round's must-fix findings are new ground. When `compound-v:followup` reports **spinning** — a fix reversing an earlier fix or a logged decision, the same class of finding recurring, or the same lines churning — stop and bring the user the design question instead of patching again. As a cost guard, stop and report after six rounds on one PR regardless. The stop rule and the cost guard apply to both tiers.

A commit that only changes the version number needs no round of its own. Merging the default branch into the branch, or a CI fix, gets a `compound-v:followup` round.

## Before acting on any round

1. List every review that was requested: your subagents, a second-opinion model, built-in reviews, and any the user ran.
2. Wait for the ones still running — in the background, never a foreground polling loop.
3. Read everything posted on the pull request **and** the plan issue since you last read them — other reviewers post there too. On a pull request that means all three kinds of record, every page: conversation comments, review summaries and inline review comments. For GitHub:

   ```bash
   gh api --paginate repos/<owner>/<repo>/issues/<n>/comments
   gh api --paginate repos/<owner>/<repo>/pulls/<n>/reviews
   gh api --paginate repos/<owner>/<repo>/pulls/<n>/comments
   ```

   Without `--paginate` the API returns only the first 30 of each, and `gh pr view --comments` leaves out inline comments, so later findings go missing without any error.
4. Treat each finding as a hypothesis: find the line of code or the read-only query that would prove it wrong, then adopt, adapt or refute it with that evidence.
5. Fix or refute every valid must-fix finding (only the user may waive one).

## Record every round on the PR

- Each review is posted as a comment (the review skills do this; if a reviewer couldn't post, post its text unchanged and say whose it is).
- After addressing a round, post one fix-notes comment answering each finding by ID: the fix and its commit SHA, or the evidence for refuting it, or "noted" for polish left alone.
- When a round ran before a pull request existed (for example on a host that can't open one), post it when the PR opens; reviewers return their text until then. Finding IDs continue across rounds on one PR (round 2 starts after round 1's last number).
- Add decisions made during review to the decisions table in the PR body, with who and when.

## Plans

When a plan is finished, a fresh reviewer runs `compound-v:plan-review` (plus the second-opinion model when the user asks for one). Wait for every requested review, fold the findings in, post the review and a short "how each finding was handled" comment on the plan's issue, then ask for approval. If the host's plan mode can't write to the tracker, open the issue as the first step after approval and post both then. A plan review that finds must-fix issues gets one more `compound-v:plan-review` after the plan is revised.
