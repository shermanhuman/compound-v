Compound V is installed. In every session:

- **Plans.** Write implementation plans in the `compound-v:plan` format, including in plan mode. Before asking for approval, have a fresh reviewer run `compound-v:plan-review` and fold its findings in. When the project uses an issue tracker, every plan gets an issue: the plan in the body, reviews as comments.
- **Reviews.** Changes headed for a pull request go through `compound-v:review-loop`, at the tier it picks (light for prose-only diffs, full for everything else), on a draft PR opened before the first round, and after every later push. Reviews and fix notes are posted on the PR or issue, not kept in local files.
- **Deferred work** goes to the issue tracker: its own issue for a real piece of work, one "Follow-ups from #N" checklist issue for small leftovers. Never a local list.
- **Questions to the user.** Multiple choice when the host has a question tool, with the full context inside the question itself; one question at a time when answers depend on each other.
