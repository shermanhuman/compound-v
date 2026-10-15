---
name: followup
description: Follow-up review of only the fixes made since the last review round — confirms each earlier finding is fixed, finds what the fixes broke, and checks for spinning (flip-flops, recurring problems, churn). Use for review rounds 2 and later on a pull request, and for the quick check after the polish pass.
---

# Follow-up review

You are a fresh reviewer for a later round. Review **only** what changed since the last reviewed commit, not the whole change again.

## Inputs

- the repository or worktree, and the fix range (`<last reviewed SHA>..<head SHA>`)
- the pull request number and this round's number
- where the decisions table lives
- whether this is a normal follow-up round or the quick check after the polish pass

## Read first

1. Every earlier review comment and fix-notes comment on the pull request (for GitHub: `gh pr view <n> --comments`, or `gh api repos/<owner>/<repo>/issues/<n>/comments`).
2. The decisions table.
3. The fix diff, then the changed files in full where the diff alone doesn't show the effect.

## For each earlier finding

| ID | Was | Now |
|---|---|---|
| M1 | ⠷ missing timeout on sync call | ✅ fixed in `abc1234` |
| m2 | ⠴ log wording | ⏭ refuted with evidence — accepted |
| B1 | ⠿ race on retry | ❌ not fixed: ... |

## New issues the fixes caused

Same Must-fix / Polish rules, severities and table as the `review` skill. In the quick check after the polish pass, list new polish as noted, not to fix; only must-fix findings count.

## Spinning check

Before reporting, compare this round with the earlier ones and flag:

- **Flip-flop**: a fix that reverses an earlier fix, or contradicts a logged decision.
- **Recurrence**: the same class of must-fix finding showing up again in a new place.
- **Churn**: the same lines rewritten round after round.

Any of these means more patching won't converge. Report it under **Spinning** with the rounds and commits involved, and recommend stopping for a design decision instead of another fix.

## Report

```markdown
## Compound V follow-up — PR #<n>, round <r>

Reviewed fixes `<last SHA>..<head SHA>`

### Earlier findings
(table above)

### New findings
Must-fix and Polish tables, or "None".

### Spinning
"None", or what's recurring and the design question it raises.

### Verdict
One or two sentences.
```

Post it on the pull request like the `review` skill does; if you can't post, return the text and say so.
