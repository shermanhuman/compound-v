---
name: review-loop
description: Runs the review rounds for a pull request or a plan — who reviews when, how fixes are verified, the opt-in persona mode, when to stop, and how every round is recorded on the PR or issue. Use before opening a pull request, after pushing new commits to one, when asked to run or continue a review round, and after finishing a plan.
---

# Review loop

Reviewers never come from the session that wrote the code (a new subagent or process, never a fork of yourself): a reviewer that has seen how the code was written tends to accept it. Brief each with the inputs its skill lists and the facts you've already verified, so it doesn't re-derive them. A brief for guard work (a gate, a guard, permissions) states the threat model. In the persona mode, one review session per pull request keeps the reviewers' context across rounds; its final pass is always fresh.

## Choosing the tier

Pick the tier from the diff before round 1, and say which one and why in the PR body and the first review comment. The user can ask for the full tier at any time. When a decision changes what gates a PR (what it ships, its tier, whether it waits on another change), re-plan that PR's review then and say so on the PR; don't leave it waiting on the old plan.

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
2. **Fix and follow up:** fix every must-fix finding, then the second voice runs `compound-v:followup` on the fix diff (`<last reviewed SHA>..<this round's pinned SHA>`), as the full tier's step 3 says, repeated while follow-ups find must-fix issues. Then the full tier's **polish pass** (step 4). There is no separate second-voice round: round 1 already had two voices.

**The light loop.** A fresh reviewer runs the *light pass* in [checks.md](../review/references/checks.md). Fix its polish and post fix notes; that's the whole loop, with no second voice and no polish or quick-check cycle. A must-fix finding gets a `compound-v:followup` round on its fix, repeated while follow-ups find must-fix issues. If a finding shows the diff wasn't prose-only, the PR moves to the instructions or full tier from there. Merging the default branch in, or a CI fix, needs no round unless it touches something outside the light list.

## Before any round: the author's check

Before asking for any review, check your own work, since a reviewer's round costs far more than these do:
- every factual claim in the change has a source you checked (the PR description or fix notes say where; not the changed text itself);
- every test it adds has been run, and every command it recommends has been tried as far as is safe: read-only commands run, anything that changes something outside your worktree (a deploy, delete, uninstall, publish) only with `--help` or `--dry-run`;
- every rule restated from another document is cited instead;
- when a reviewer left a reproduction or fuzz script on an earlier round, rerun it against the fix.

## Reviews don't block

While a review runs, keep working: on the next step, or on another goal. **Pin each round to a commit:** push, record the head SHA, and give it to every reviewer, who reads that snapshot (`git show <sha>:<path>`, or a worktree at it), never your live worktree, so your edits during the round can't change what they read. Start both voices together, and fix the first report's findings while the other finishes, except any fix a known question for the user touches. Only must-fix findings earn another round. Between rounds, fix only must-fix findings: polish waits for the polish pass, and the fix notes answer it "held for the polish pass" (the light loop, which has no polish pass, fixes its polish as it goes). A polish fix gets no re-review unless it changes behaviour: for code, what it does; for instruction files, what an agent following them would do.

## Before acting on any round

1. List every review that was requested: your subagents, a second-opinion model, built-in reviews, and any the user ran.
2. Don't block on the ones still running: take each report through steps 3 to 7 as it lands, and keep working in between. Questions for the user from any report are held until every report is in, then sent as one packet (step 5); the round's follow-up starts after the answers are applied. When a later report raises a question, recheck the fixes already made against it, and revert or hold any it touches. Post the round's fix notes after the last report. Wait in the background, never in a foreground polling loop.
3. Read everything posted on the pull request **and** the plan's home (a plan store the user's rules name, or the plan's issue) since you last read them — other reviewers post there too. On a pull request that means all three kinds of record, every page: conversation comments, review summaries and inline review comments. For GitHub:

   ```bash
   gh api --paginate repos/<owner>/<repo>/issues/<n>/comments
   gh api --paginate repos/<owner>/<repo>/pulls/<n>/reviews
   gh api --paginate repos/<owner>/<repo>/pulls/<n>/comments
   ```

   Without `--paginate` the API returns only the first 30 of each, and `gh pr view --comments` leaves out inline comments, so later findings go missing without any error.
4. Treat each finding as a hypothesis: find the line of code or the read-only query that would prove it wrong, then adopt, adapt or refute it with that evidence.
5. Findings under *Questions for the user* aren't patched, in any tier: send them in one decision packet per round (`compound-v:interrogate`'s *Present it once*), hold the fixes they touch until the answers come, and record each answer where the decisions live.
6. **Before fixing,** compare each of this round's must-fix causes, and any recurring polish's, with every earlier one on the pull request, the second voice's included (`compound-v:followup`'s *Recurrence*). A match means the step-back comes first (*Stop rule*). Record the comparison in the fix notes as the cause ledger.
7. Fix or refute every valid must-fix finding (only the user may waive one).

## Pull requests

Open the pull request as a draft before round 1, so each round is posted on it as it lands, and mark it ready only after the final round has no must-fix findings.

Full tier:

1. **Round 1** — a fresh reviewer runs `compound-v:review` on the full diff against the default branch, with live web access as the instructions loop says (the 🔍 checks research). If the user asked for the second voice at round 1 too, it runs `compound-v:review` in parallel; give it a prefix for its finding IDs (for example `A-M1`) so the two reports never share an ID.
2. **Round 2** — the second voice runs `compound-v:review` on the full diff, with its own ID prefix, in parallel with a fresh `compound-v:followup` of round 1's fixes (when round 1 found must-fix; otherwise the second voice runs alone). The second voice is:
   - a different model when one is configured (the user's rules name it and how to run it);
   - otherwise the host's built-in review: in Claude Code, `/code-review high`, plus `/security-review` when the change touches authentication, user input, secrets or infrastructure; in Codex, `codex review`;
   - otherwise a fresh `compound-v:review` pass by yourself, re-reading the full diff from the start.

   Say on the PR which one ran, and why if it fell back. If it already ran at round 1, round 2 is its follow-up of round 1's fixes alone, and if round 1 found nothing, review ends there.
3. **Fix and follow up** — fix every must-fix finding. Then a fresh run of the second voice's model runs `compound-v:followup` on the fix diff (`<last reviewed SHA>..<this round's pinned SHA>`). A built-in review, your own pass, or a second voice that has become unavailable can't follow up; then a fresh reviewer does, at no lower model and effort than round 1, and the PR says so. Repeat while follow-ups find must-fix issues.
4. **Polish pass** — fix all open polish in one go, small fixes only (a redesign now is what makes the next round find new problems). Run the tests. Only if a polish fix changed behaviour, run a quick `compound-v:followup` of that diff; new polish it raises is noted, not fixed, and a must-fix sends you back to step 3.

**Who reviews each round, at a glance:**

| Case | Round 1 | Round 2 | Round 3 and later | Review stops when |
|---|---|---|---|---|
| Full tier, round 1 found must-fix | a fresh reviewer | a fresh follow-up of the fixes, and the second voice's full review | the second voice's follow-ups, while must-fix remain | a round from round 2 on finds no must-fix (then the polish pass), or the stop rule |
| Full tier, round 1 clean | a fresh reviewer | the second voice's full review | the second voice's follow-ups | the same |
| Second voice asked for at round 1 | both | the second voice's follow-up, if round 1 found must-fix | the same | round 1 clean, or a later round finds no must-fix; or the stop rule |
| Instructions tier | both voices | the second voice's follow-up, if round 1 found must-fix | the same | round 1 clean, or a later round finds no must-fix; or the stop rule |
| Persona mode | the personas | persona follow-ups, and the second voice's full review | persona and second-voice follow-ups | no must-fix open, then the final pass (persona step 5), or the stop rule |
| No second voice configured | a fresh reviewer | a fresh follow-up of any fixes, and the host's built-in review (or your own fresh pass) | fresh follow-ups, at no lower model and effort than round 1 | as the full tier |
| Light tier | the light pass, its polish fixed | a follow-up only for a must-fix | the same | the light pass finds no must-fix, or a follow-up finds none |

**Persona mode** runs when the user's rules switch it on, typically for high-consequence changes (the production boundary, data handling, money, authentication), where finding more is worth several times the cost. Its entry gate: a diff that touches none of the deep areas (`security`, `api`, `schema`, `instructions`; `correctness`, `design` and `tests` run on any code and don't count) and is under the size limit the user's rules set gets the single-reviewer loop above instead. With no size limit set, only the deep-area test applies.


1. **Read once.** A fresh review session builds one bundle for the pull request, written to a file: the diff hunks with enough surrounding lines to follow them (whole files only where hunks aren't enough), code-map facts for the changed functions when a map covers the repository (callers, callees, routes, schema), the git history and earlier review comments on the touched lines, the repository's rules and the decisions table. It leaves out generated, vendored and lock files, and lists them. It then picks every persona in [personas.md](../review/references/personas.md) whose trigger the diff matches, and the round comment says which and why. It runs where the session keeps a transcript and can be resumed, and names itself and every reviewer `<repo>#<n> r<round> <role>` in their first prompt, so cost can be measured.
2. **Personas in parallel.** Each persona runs `compound-v:review` with its persona name, all at once, and writes its report to a file; queue any the host or the plan's limits can't start yet, never drop them. Where the host can fork a subagent, fork the personas from the review session, so the bundle is read once and reused from cache; personas the user's rules put on a different model fork from a second review session that read the same bundle. Without forking, start every persona's brief with the identical bundle file and put its persona last; start one first and the rest once its first response has begun, or none of them reads the bundle from cache.
3. **Validate and post.** The review session reads every persona's report file (so the next round's forks inherit them), merges findings on the same lines and issue (the more specific persona keeps it), hands each *Outside my area* line to the persona that owns that area (resuming it, or checking the line itself if that persona didn't run), and sends the must-fix findings to validators as the review skill says. It posts one round report with each persona's coverage and sources, the confirmed and unresolved findings (unresolved ones marked) and *Rejected by the validator*, plus the round's wall time and, where the host reports it, tokens per persona.
4. **Round 2 and later.** Round 2 always has the second voice's full-diff review, as the full tier's step 2 says, alone when round 1 found nothing. Fix every must-fix finding. Then the personas with must-fix findings run `compound-v:followup` on the fix diff (`<last reviewed SHA>..<this round's pinned SHA>`), forked again from the same review session (resume it where the host can), so they know what they asked for. A persona with nothing open goes quiet; a later fix diff that matches its trigger wakes it for a follow-up on that diff. Validate and post as in step 3, dropping repeats of rejected findings as `compound-v:followup` defines them, and repeat while follow-ups find must-fix issues. Launch follow-ups at the same model and effort as round 1: never lower. From then on the second voice follows up each fix diff beside the personas; its report is posted as its own and validated as in step 3.
5. **Final pass** — once the second voice has reviewed the full diff and no must-fix is open, a fresh review session and fresh personas (every persona the pull request used) review the full diff. Validate as in step 3, and drop repeats of rejected findings as `compound-v:followup` defines them. While rounds remain under the cap, its must-fix findings go back to step 4, to the persona that owns the area, and the final pass runs again (the *Stop rule* says how the cap treats it).
6. **Polish pass** — fix all open polish in one go, small fixes only (a redesign now is what makes the next round find new problems). Run the tests. Only if a polish fix changed behaviour, run a quick `compound-v:followup` of that diff; new polish it raises is noted, not fixed, and a must-fix sends you back to step 4.

Where the host can't run subagents in parallel, run the personas one after another in the same order; the steps don't change.

**Stop rule.** Keep going while each round's must-fix findings are new ground. In persona mode, all the personas of one round, and the second voice beside them, count as one round.

**Step back** before patching again when a must-fix, or a polish finding recurring in a new place, shares its cause with an earlier finding on the pull request (one fix would have prevented both; `compound-v:followup`'s *Recurrence*), when a fix reverses an earlier fix or a logged decision, or when the same lines churn (in the instructions tier, one line or clause rewritten in three rounds). Post a step-back note naming the suspected shared cause and the findings involved, with one of three outcomes:
- **a design change** that removes the cause. Build it yourself when it stays inside the plan's decisions; when it changes a decision the user made, or the scope, ask the user and hold the work it touches;
- **a sweep**: every sibling site of the cause, listed, fixed and proved by the outcome, not by banning a spelling;
- **not the same cause**, with the evidence.

The next follow-up checks the step-back (`compound-v:followup`'s *Step-back check*).

Rounds per PR are capped by the goal's type (`compound-v:plan`): patch 3, change 3, feature and product 4. A round is everyone who reviews in it: both voices of a round, all of a persona round, a follow-up. The quick check after the polish pass and persona mode's final pass confirm, so they don't count; a must-fix either finds once the rounds used have reached the cap goes to the user. Reaching the cap with nothing open ends review: finish the remaining steps without another round. A PR with no goal type takes the change cap. The user's rules may lift the cap, and the six-round guard with it, for a kind of PR. At the cap with must-fix findings still open, or after three rounds whose fixes didn't hold, stop and bring it to the user; a step-back due at that point is posted first, so the user sees the cause. As a cost guard, stop and report after six rounds on one PR regardless. The stop rule and the cost guard apply to every tier.

A commit that only changes the version number needs no round of its own. Merging the default branch into the branch, or a CI fix, gets a `compound-v:followup` round, which keeps the earlier result when the PR's own lines didn't change.

## Record every round on the PR

- Each review is posted as a comment, naming the plugin version and, in persona mode, the mode (the review skills do this; if a reviewer couldn't post, post its text unchanged and say whose it is).
- After addressing a round, post one fix-notes comment answering each finding by ID: the fix and its commit SHA, or the evidence for refuting it, or "held for the polish pass" for polish (after the polish pass: the fix, or "left: needs more than a small fix", with an issue if it's real work); for a question, the user's answer and its decisions row.
- When a round ran before a pull request existed (for example on a host that can't open one), post it when the PR opens; reviewers return their text until then. Finding IDs continue across rounds on one PR (round 2 starts after round 1's last number).
- Add decisions made during review where the decisions live (the decision store the user's rules name, else the decisions table in the PR body), with who and when.

## Plans

When a plan beyond a patch is finished (a patch's note goes in its PR and gets no plan review), a fresh reviewer runs `compound-v:plan-review` (plus the second-opinion model when the user asks for one). Wait for every requested review, fold the findings in, post the review and a short "how each finding was handled" note in the plan's home (the plan store the user's rules name, attached to the revision reviewed, or the plan's issue), then ask for approval. If the host's plan mode can't write: with a plan store, leave the restricted mode first (where only the user can, ask them to), then post the revision, the review, the note on how each finding was handled and the approval item, and wait for its answer before building; without one, post both as the first step after the host's approval. A plan review that finds must-fix issues gets one more `compound-v:plan-review` after the plan is revised. The step-back applies to plans too: when a plan review's must-fix shares its cause with an earlier round's, rewrite the approach it comes from instead of patching the row again.
