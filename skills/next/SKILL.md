---
name: next
description: Pick the best next project from the user's open GitHub issues and offer to start planning it. With no argument it looks at the repositories this session has touched; "all" covers every organisation the user belongs to plus their own account; a repository or topic narrows it. Use when the user runs /compound-v:next or asks what to work on next or what's open in a repository or area.
argument-hint: "[all | repo | topic]"
---

# Next

Recommend one project with reasons, name two or three runners-up, then offer to start. The user wants a pick, not a survey, so never print a table of every issue.

## Scope

`$ARGUMENTS` is empty, `all`, a repository or a topic.

- **Empty:** the repositories this session has touched, judged from what you've seen in this conversation: the working directory's repository, worktrees you used, repositories you edited, and ones whose pull requests or issues you handled. Say which ones you used. If the session hasn't touched any, use `all` and say so.
- **`all`:** every open issue in each organisation the user belongs to plus their own account (`gh api user/orgs --jq '.[].login'` and `gh api user --jq .login`), including issues other people filed. Skip any owner the user's rules exclude.
- **A repository:** match it against repository names in the `all` scope, partial names included (`admin` finds `acme-admin`). Ask if two match. Rank that repository's issues, and still check other repositories for work a release there depends on.
- **Anything else is a topic** (billing, search, secrets, …): within the `all` scope, keep the issues that are about it by meaning, not exact word, and say which ones matched.

## Read

Run `gh` the way the user's rules say, for example through a tool manager. Keep output compact: titles and counts, never whole bodies.

1. **Open issues**, one line each with checklist progress. Use one `--owner` per owner in scope, or `--repo` for the touched repositories. Rank on labels and milestones only when the repositories actually use them.

   ```bash
   gh search issues --state open --limit 200 --sort updated <--owner X ... | --repo O/R ...> \
     --json repository,number,title,updatedAt,createdAt,commentsCount,body \
     --jq '.[] | "\(.repository.nameWithOwner) #\(.number) | \(.title) | upd \(.updatedAt[0:10]) cre \(.createdAt[0:10]) | c\(.commentsCount) | todo \((.body // "") | [scan("(?m)^\\s*[-*] \\[ \\]")] | length) done \((.body // "") | [scan("(?m)^\\s*[-*] \\[[xX]\\]")] | length) | \((.body // "")[0:160] | gsub("\\s+"; " "))"'
   ```

2. **Open pull requests** in the same scope. A repository with an open pull request of the user's finishes it before anything new starts there.

   ```bash
   gh search prs --state open <same scope flags> \
     --json repository,number,title,isDraft,author --jq '.[] | "\(.repository.nameWithOwner) #\(.number) draft=\(.isDraft) by=\(.author.login) \(.title)"'
   ```

   For each of the user's: `gh pr view <n> -R <owner>/<repo> --json mergeable,mergeStateStatus,statusCheckRollup` says whether it's blocked.

3. **The shortlist only** (the five or six issues still in the running):
   - the body and last comment, because progress on a plan issue often lives in its comments, not in ticked boxes: `gh issue view <n> -R <owner>/<repo> --json body,comments --jq '.body, .comments[-1].body'`
   - the pull requests that reference it: `gh api repos/<owner>/<repo>/issues/<n>/timeline --jq '.[] | select(.event=="cross-referenced") | .source.issue | "\(.repository.full_name) #\(.number) pr=\(.pull_request != null) merged=\(.pull_request.merged_at != null) \(.state)"'`

4. **The user's priorities** that the host already loaded: their rules, and any project or goal notes in memory. Don't go looking for more.

## Rank

Use judgment, in this order, with each criterion breaking ties left by the one above. Don't compute scores.

1. **Finish what's in flight.** If the user has an open pull request in a repository that's a draft, red, conflicting or behind, it's the pick for that repository. One that's ready and green goes under *Needs you* ("merge #n"), and new work in that repository waits behind it. Someone else's pull request doesn't block the user's; say it's there.
2. **Half-done releases:** a plan or issue where part has shipped and a counterpart (another repository, a rollout step) is still open.
3. **Blocked on the user:** a decision, spending, or a secret only they hold is never the pick. Give it one line naming the decision.
4. **Impact:** what end users of the software see, then production safety and security, then developer tooling and CI, then housekeeping. The user's own priorities, when their rules or notes state them, refine this.
5. **Batch within a repository.** Small leftovers (follow-up checklist items, flaky tests, alert noise) ride along with the pick as one release; name them.
6. **Size:** a pick fits one session unless the user asked for a big one. Say when a candidate is a multi-week plan.
7. **Stale:** an issue untouched for six months or more, or a plan whose releases all shipped, is a candidate for closing, not a pick.

## Answer

Under 25 lines, plain text, no tables:

```text
Next: <repo> — <one-line project>
Why now: <two or three sentences: state, impact, what blocks what>
Release: <issues and items folded in, by number; the open PR to finish first, if any>
Needs you: <decisions or inputs, or "nothing">

Runners-up:
- <repo> #n — <one line, and why it lost>

Housekeeping: <issues that look done or stale, "close?">
```

Then ask through the host's question tool, repeating that context inside the question, since the widget hides the text above it. The options: start the pick in plan mode, take a runner-up, or widen the scope. On start, enter plan mode, use the `compound-v:plan` format, and make the issue the plan's home. Without a question tool, ask in one plain sentence. The pick itself creates nothing and closes nothing.
