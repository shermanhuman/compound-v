---
name: followup
description: Follow-up review of only the fixes made since the last review round — confirms each earlier finding is fixed, finds what the fixes broke, and checks for spinning (flip-flops, recurring problems, churn). Use for review rounds 2 and later on a pull request, and for the quick check after the polish pass.
---

# Follow-up review

You are the reviewer for a later round: fresh, or a review persona forked from the pull request's review session. Review **only** what changed since the last reviewed commit, not the whole change again, and read the replies to earlier findings.

- **Don't re-raise a rejected finding** (one the validator rejected, or one whose refutation an earlier follow-up accepted) unless the diff under review (the fix diff, or the whole PR in a final pass) changed the code the rejection cited. The author's word alone doesn't make a finding rejected.
- **Never lower the depth** an earlier round used.
- If the fix range only merges the default branch and the pull request's own lines are unchanged (`git diff <last reviewed SHA>..HEAD` restricted to the PR's files is empty), keep the earlier result and say so instead of reviewing again.
- The evidence rule applies as in `compound-v:review`, and validation in persona mode.

## Inputs

- the repository or worktree, and the fix range (`<last reviewed SHA>..<head SHA>`)
- the pull request number and this round's number
- where the decisions live (a decision store the user's rules name, the PR body, or the plan's issue); a reviewer that can't reach the store gets the decisions, earlier reviews and fix notes in the brief
- whether this is a normal follow-up round or the quick check after the polish pass
- for a persona: its name in [personas.md](../review/references/personas.md). Check its own earlier findings and what the fixes broke in its area; it writes its report to the file the review session names (where it can't write files, it returns the text and the session saves it) instead of posting

## Read first

1. Every earlier review and fix-notes record on the pull request (a persona forked from the review session already has them, and reads only what's new since) — all three kinds of record, every page: conversation comments, review summaries and inline review comments. For GitHub:

   ```bash
   gh api --paginate repos/<owner>/<repo>/issues/<n>/comments
   gh api --paginate repos/<owner>/<repo>/pulls/<n>/reviews
   gh api --paginate repos/<owner>/<repo>/pulls/<n>/comments
   ```

   Without `--paginate` the API returns only the first 30 of each, and `gh pr view --comments` leaves out inline comments, so later findings go missing without any error.
2. The decisions.
3. The fix diff, then the changed files in full where the diff alone doesn't show the effect.

## For each earlier finding

| ID | Was | Now |
|---|---|---|
| M1 | ⠷ missing timeout on sync call | ✅ fixed in `abc1234` |
| m2 | ⠴ log wording | ⏭ refuted with evidence — accepted |
| B1 | ⠿ race on retry | ❌ not fixed: ... |

## New issues the fixes caused

Same Must-fix rules, severities and table as the `compound-v:review` skill, each must-fix with its `Cause` ([causes.md](../review/references/causes.md)). When the fix diff adds a new call to a library or outside API, or changes a pinned version, research it as `compound-v:review`'s 🔍 checks do and list the sources in a *Sources* section. In a normal follow-up round, raise no new polish: it waits for the polish pass. The exception is a polish finding that recurs in a new place; report it with its `Cause`, since a recurring polish finding is usually a design trap. A fix that adds a choice the user hasn't decided (a surface, default, name or something they'll be asked) goes under *Questions for the user*, as in that skill. Finding IDs continue across rounds on one pull request: if round 1 ended at M2 and m3, this round starts at M3 and m4, so fix notes never confuse two findings. In the quick check after the polish pass, list new polish as noted, not to fix; only must-fix findings count.

## Spinning check

Before reporting, compare this round's causes (must-fix, and any recurring polish), and the author's cause ledger in the fix notes, with every earlier round's, the second voice's included, and flag:

- **Flip-flop**: a fix that reverses an earlier fix, or contradicts a logged decision.
- **Recurrence**: a must-fix, or a polish finding recurring in a new place, whose specific cause matches an earlier finding's: one fix would have prevented both. The same class with a different cause isn't a recurrence; note it.
- **Churn**: the same lines rewritten round after round (the review loop's *Stop rule* gives the instructions tier's threshold).

Any of these means more patching won't converge: the author steps back (`compound-v:review-loop`'s stop rule).

## Step-back check

When the author posted a step-back since the last round, check it by its outcome:
- **a design change, built**: it names the cause and the findings that share it, and the fix diff removes the cause rather than patching one more instance;
- **a design change, held** for the user's answer: the ask is posted, and the work it touches is unchanged;
- **a sweep**: your own search for sibling sites matches the author's list, and the outcome proof exists and can fail;
- **not the same cause**: the evidence holds, for example a fix that would have prevented one finding and not the other.

A step-back that fails a check is a must-fix.

## Report

```markdown
## Compound V follow-up — PR #<n>, round <r>

Reviewed fixes `<last SHA>..<head SHA>`

### Earlier findings
(table above)

### New findings
Must-fix, Polish and Questions for the user tables, or "None".

### Step-back
Only when the author posted one: each check above, passed or failed.

### Spinning
The first line is exactly `None`, or one kind word (`flip-flop`, `recurrence` or `churn`), then ` — ` and what's spinning, with the findings and commits involved. Notes go after it, under a `Noted:` line. A recurrence, flip-flop or churn that a passed step-back already covers is `None`, with a `Noted:` line; when two kinds apply, name the one the step-back should start from and note the other.

### Verdict
One or two sentences.
```

Write it outside the repository (a temp or scratch directory) and post it on the pull request like `compound-v:review` does. If there is no pull request yet, or you can't post, return the text and say so; the review loop posts it.
