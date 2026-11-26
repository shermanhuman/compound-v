---
name: pull-requests
description: The procedure for a pull request where every PR is a release — which PR is yours, the worktree, testing the way CI does, end-to-end checks that are shown to fail once, the draft, the description, keeping it mergeable and green, and cleaning up after the merge. Use before opening a PR, when pushing more commits to one, when a PR has conflicts or failing checks, before saying a PR is ready to merge, when returning to a session with open PRs, and after a PR merges.
---

# Pull requests

A pull request is a release: one per repository, and a person merges it. Reviews run through `compound-v:review-loop`; the version bump is `compound-v:release`. Run `gh` and other tools the way the user's rules say.

## Which PR is yours

- Yours is the one whose branch you (this session or this batch of work) created. In a new session, a PR is yours when the user points you to it or you're continuing its branch; otherwise ask once.
- Before opening one, list the open PRs. If yours is open, push to its branch and update its description instead of opening another. Before each push, check it's still open; if it merged, start a new branch from the freshly fetched default branch.
- Another session's open PR doesn't block yours. Whichever merges second merges the default branch into its own branch and takes the next version.
- Several repositories in one release: give the titles a common prefix so they read as one release.

## Before opening a PR

1. **Work in a git worktree,** on a new branch from the freshly fetched default branch, without tracking it:

   ```bash
   git fetch
   git worktree add --no-track -b <branch> <path> origin/<default-branch>
   ```

   The main checkout may hold someone else's work or a running server; read there, but don't change it. Keep one worktree per batch of work, merge the default branch in when it moves (merge, never rebase: posted commit SHAs must stay valid), and remove the worktree after the merge. After deleting a folder, stage explicit paths rather than `git add -A`, and check `git diff --cached --summary` for gitlinks (mode 160000) before committing.
2. **Test the way CI does:** read the CI workflow first, its `services:` (databases, caches) included, and start the same ones before a local suite; then run every suite and configuration CI runs, the formatter check, and a warnings-as-errors build where the language has one. A failure that also fails on the default branch is shown failing there, not assumed.
3. **Check user-facing changes end to end,** with the repository's end-to-end setup, a scenario for each change. For each key check, show once that it can fail: break what it checks, watch it fail, restore it. A check that has never failed may not be checking anything. Without an end-to-end setup, say so in the PR and describe the manual check you ran.
4. **Open a draft, then review.** Open the PR as a draft once local tests pass, so each review round is posted on it as it lands, and run `compound-v:review-loop`. Carry the plan's decisions (or the decision record the user's rules name) where reviewers read them. Remove debug output and stray TODOs first.
5. **Bump the version last** (`compound-v:release`), once the work is tested and reviewed, taking the number from the PR's base.

## The description

Describe the final change, its migrations and rollout, and the checks you actually ran, with their exact commands and results (suites, end-to-end scenarios, review rounds), never just "tests pass". Write it to a file of your own and pass it with `--body-file`.

## Keeping it mergeable and green

Until it merges, the PR's state is yours:
- **After every push,** watch its checks in the background; fix what fails, push, and watch again. Checks can take a few seconds to register after a push. A check that's red by design on a draft (a version check before the bump lands last) waits for the bump; everything else gets fixed. Don't call a PR ready while a check is red or running.
- **Before calling it ready,** and when you come back to a session with open PRs, look at its state, mergeability and checks. Conflicting means merge the default branch in now. A green result on a branch that's behind can be stale, because checks don't rerun when the base moves.
- **When the base moves,** merge the default branch in, re-apply your bump at the same level on top of the base's new version (two PRs setting the same version merge cleanly and still fail a version check), run the affected checks, push, and watch again.
- **Ready means mergeable now:** the final review round has no must-fix findings, the bump has landed, the base is the default branch, and it's up to date and green. When it stops qualifying, put it back to draft before fixing it. A PR stacked on another PR's branch stays a draft until that one merges and it's retargeted.
- **A failure that isn't yours** (flaky, or failing on the default branch) is shown failing on the default branch, with the run link, before you say so. Fix flakiness rather than re-running until green.
- Tell the user what you found and fixed. When several PRs are ready at once, give the merge order.

## Merging

The user merges. Creating branches, pushing feature branches, and creating or updating PRs are yours. Never merge, never push to the default branch, never force-push, and never route around a refusal: when a PR is ready, hand the user the merge.

## After the merge

Clean up yourself:
- Confirm the branch is in the default branch, then delete it locally and on the remote, and remove its worktree and scratch trees. Never delete the default branch.
- Close the issues it finished, with a comment linking the PR; say which related issues stay open and why.
- For a plugin, update its installs wherever the user's rules say they live, and confirm the versions.
