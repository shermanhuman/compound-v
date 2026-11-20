---
name: review-loop
description: Runs the review rounds for a pull request or a plan — who reviews when, how fixes are verified, the opt-in persona mode, when to stop, and how every round is recorded on the PR or issue. Use before opening a pull request, after pushing new commits to one, when asked to run or continue a review round, and after finishing a plan.
---

# Review loop

Reviewers never come from the session that wrote the code (a new subagent or process, never a fork of yourself): a reviewer that has seen how the code was written tends to accept it. Brief each with the inputs its skill lists and the facts you've already verified, so it doesn't re-derive them. In the persona mode, one review session per pull request keeps the reviewers' context across rounds; its final pass is always fresh.

## Choosing the tier

Pick the tier from the diff before round 1, and say which one and why in the PR body and the first review comment. The user can ask for the full tier at any time.

**Light** covers prose only. The list is closed: anything not on it is instructions or full.

- Prose in READMEs, docs and the changelog that gives no instructions. An instruction is a fenced command, an inline command someone would run, or an imperative step, so a procedural section is full.
- Comment-only code changes, confirmed by `git diff -w` showing only comment lines.
- Typo and wording fixes in those same files. A string a user or agent sees at runtime (templates, messages, translations, site copy) is code, so it's full.
- Changes to the PR body only, marketplace or listing descriptions (not their sources), and settings that only switch plugins on or off.

**Instructions** covers a diff of agent-instruction files only (`AGENTS.md`, `CLAUDE.md`, rules, skills and their references, subagent definitions and commands, hook text and the hook output generated from it), plus the manifest and README lines that describe them. Its rounds use the *instructions pass* in [checks.md](../review/references/checks.md).

**Full** covers everything else. A mixed diff is full, with each file reviewed by the checks that fit it: the code checks for code, the instructions pass for instruction files, and the light-pass items for prose.

The PR's own version-line bump (the version line in any manifest: `plugin.json`, `marketplace.json`, `mix.exs`, `go.mod`, `package.json`) doesn't change the tier, and neither does a change to a plugin or listing entry's `description` text in those files. Any other change in them does, and lockfile changes count as dependency changes: full.

**The instructions loop.**

0. **Audit first** where the host has an instruction audit (in Claude Code, `/doctor prompt-audit <path>`, run in a headless session such as `claude -p "/doctor prompt-audit <path>"`, one file or directory per run): fix its mechanical findings (wrong references, contradictions, dated wording) before round 1; its choices join round 1's packet for the user.
1. **Round 1, two voices:** a fresh reviewer and the second voice (the configured different model, or else a second fresh reviewer) each run the instructions pass on the full diff, in parallel, with prefixed finding IDs. Each does the current-practice check itself, so it needs live web access (a Codex reviewer: `-c web_search="live"`), and its brief carries what its sandbox can't reach, such as the user's rough-edge log. If a voice returns check 8 Not assessed, rerun it with live access, or say on the PR that only one reading was made.
2. **Fix and follow up:** fix every must-fix finding, then a fresh reviewer runs `compound-v:followup` on the fix diff (`<last reviewed SHA>..HEAD`), repeated while follow-ups find must-fix issues. Then the full tier's **polish pass** (step 4). There is no separate independent pass: round 1 already had two voices.

**The light loop.** A fresh reviewer runs the *light pass* in [checks.md](../review/references/checks.md). Fix its polish and post fix notes; that's the whole loop, with no independent pass and no polish or quick-check cycle. A must-fix finding gets a `compound-v:followup` round on its fix, repeated while follow-ups find must-fix issues. If a finding shows the diff wasn't prose-only, the PR moves to the instructions or full tier from there. Merging the default branch in, or a CI fix, needs no round unless it touches something outside the light list.

## Pull requests

Open the pull request as a draft before round 1, so each round is posted on it as it lands, and mark it ready only after the final round has no must-fix findings.

Full tier:

1. **Round 1** — a fresh reviewer runs `compound-v:review` on the full diff against the default branch. If the user asked for a second opinion from another model, it runs `compound-v:review` too, in parallel; give it a prefix for its finding IDs (for example `A-M1`) so the two reports never share an ID.
2. **Fix** every must-fix finding (and that round's polish if it's cheap; leave the rest for the polish pass). Then a fresh reviewer, on the same model and effort as round 1, runs `compound-v:followup` on the fix diff (`<last reviewed SHA>..HEAD`). Repeat while follow-ups find must-fix issues.
3. **Independent pass** — once a round has no must-fix findings, one full-diff pass by the configured second voice:
   - a different model when one is configured (the user's rules name it and how to run it), running `compound-v:review`;
   - otherwise the host's built-in review: in Claude Code, `/code-review high`, plus `/security-review` when the change touches authentication, user input, secrets or infrastructure; in Codex, `codex review`;
   - otherwise a fresh `compound-v:review` pass by yourself, re-reading the full diff from the start.

   Say on the PR which one ran, and why if it fell back. Its must-fix findings go back to step 2.
4. **Polish pass** — fix all open polish in one go, small fixes only (a redesign now is what makes the next round find new problems). Run the tests, then a quick `compound-v:followup` of only the polish diff. New polish it raises is noted, not fixed; a must-fix sends you back to step 2.

**Persona mode** runs when the user's rules switch it on, typically for high-consequence changes (the production boundary, data handling, money, authentication), where finding more is worth several times the cost. Its entry gate: a diff that touches none of the deep areas (`security`, `api`, `schema`, `instructions`; `correctness`, `design` and `tests` run on any code and don't count) and is under the size limit the user's rules set gets the single-reviewer loop above instead. With no size limit set, only the deep-area test applies.


1. **Read once.** A fresh review session builds one bundle for the pull request, written to a file: the diff hunks with enough surrounding lines to follow them (whole files only where hunks aren't enough), code-map facts for the changed functions when a map covers the repository (callers, callees, routes, schema), the git history and earlier review comments on the touched lines, the repository's rules and the decisions table. It leaves out generated, vendored and lock files, and lists them. It then picks every persona in [personas.md](../review/references/personas.md) whose trigger the diff matches, and the round comment says which and why. It runs where the session keeps a transcript and can be resumed, and names itself and every reviewer `<repo>#<n> r<round> <role>` in their first prompt, so cost can be measured.
2. **Personas in parallel.** Each persona runs `compound-v:review` with its persona name, all at once, and writes its report to a file; queue any the host or the plan's limits can't start yet, never drop them. Where the host can fork a subagent, fork the personas from the review session, so the bundle is read once and reused from cache; personas the user's rules put on a different model fork from a second review session that read the same bundle. Without forking, start every persona's brief with the identical bundle file and put its persona last; start one first and the rest once its first response has begun, or none of them reads the bundle from cache.
3. **Validate and post.** The review session reads every persona's report file (so the next round's forks inherit them), merges findings on the same lines and issue (the more specific persona keeps it), hands each *Outside my area* line to the persona that owns that area (resuming it, or checking the line itself if that persona didn't run), and sends the must-fix findings to validators as the review skill says. It posts one round report with each persona's coverage, the confirmed and unresolved findings (unresolved ones marked) and *Rejected by the validator*, plus the round's wall time and, where the host reports it, tokens per persona.
4. **Fix and follow up.** Fix every must-fix finding (and cheap polish). Then the personas with must-fix findings run `compound-v:followup` on the fix diff (`<last reviewed SHA>..HEAD`), forked again from the same review session (resume it where the host can), so they know what they asked for. A persona with nothing open goes quiet; a later fix diff that matches its trigger wakes it for a follow-up on that diff. Validate and post as in step 3, dropping repeats of rejected findings as `compound-v:followup` defines them, and repeat while follow-ups find must-fix issues. Launch follow-ups at the same model and effort as round 1: never lower.
5. **Final pass** — once no persona has a must-fix open: a fresh review session and fresh personas (every persona the pull request used) review the full diff, plus one full-diff `compound-v:review` by the configured second voice:
   - a different model when one is configured (the user's rules name it and how to run it);
   - otherwise the host's built-in review: in Claude Code, `/code-review high`, plus `/security-review` when the change touches authentication, user input, secrets or infrastructure; in Codex, `codex review`;
   - otherwise a fresh `compound-v:review` pass by yourself, re-reading the full diff from the start.

   Say on the PR which second voice ran, and why if it fell back. Validate as in step 3, and drop repeats of rejected findings as `compound-v:followup` defines them. Must-fix findings go back to step 4, to the persona that owns the area.
6. **Polish pass** — fix all open polish in one go, small fixes only (a redesign now is what makes the next round find new problems). Run the tests, then a quick `compound-v:followup` of only the polish diff. New polish it raises is noted, not fixed; a must-fix sends you back to step 4.

Where the host can't run subagents in parallel, run the personas one after another in the same order; the steps don't change.

**Stop rule.** Keep going while each round's must-fix findings are new ground. In persona mode, all the personas of one round count as one round, and the final pass as one more. When `compound-v:followup` reports **spinning** — a fix reversing an earlier fix or a logged decision, the same class of finding recurring, or the same lines churning (in the instructions tier, one line or clause rewritten in three rounds) — stop and bring the user the design question instead of patching again. As a cost guard, stop and report after six rounds on one PR regardless. The stop rule and the cost guard apply to every tier.

A commit that only changes the version number needs no round of its own. Merging the default branch into the branch, or a CI fix, gets a `compound-v:followup` round, which keeps the earlier result when the PR's own lines didn't change.

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
5. Findings under *Questions for the user* aren't patched, in any tier: send them in one decision packet before fixing this round's findings, and record each answer in the decisions table.
6. Fix or refute every valid must-fix finding (only the user may waive one).

## Record every round on the PR

- Each review is posted as a comment, naming the plugin version and, in persona mode, the mode (the review skills do this; if a reviewer couldn't post, post its text unchanged and say whose it is).
- After addressing a round, post one fix-notes comment answering each finding by ID: the fix and its commit SHA, or the evidence for refuting it, or "noted" for polish left alone; for a question, the user's answer and its decisions row.
- When a round ran before a pull request existed (for example on a host that can't open one), post it when the PR opens; reviewers return their text until then. Finding IDs continue across rounds on one PR (round 2 starts after round 1's last number).
- Add decisions made during review to the decisions table in the PR body, with who and when.

## Plans

When a plan is finished, a fresh reviewer runs `compound-v:plan-review` (plus the second-opinion model when the user asks for one). Wait for every requested review, fold the findings in, post the review and a short "how each finding was handled" comment on the plan's issue, then ask for approval. If the host's plan mode can't write to the tracker, open the issue as the first step after approval and post both then. A plan review that finds must-fix issues gets one more `compound-v:plan-review` after the plan is revised.
