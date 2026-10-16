# compound-v

A Claude Code and Codex plugin (skills in `skills/`, the always-on hook in `hooks/`) and the marketplace that lists it with the Grugg, Oh and Cartographer plugins (`.claude-plugin/marketplace.json`).

- **Merging is a human task.** Never merge a branch, squash-merge a PR, or push to the default branch. Create branches, push feature branches and open PRs; when work is ready, ask the user to merge.
- **Pull requests start as drafts.** Open the draft (`mise exec -- gh pr create --draft`) before the review loop, not after it as `compound-v:review-loop`'s pre-PR rounds assume; post each round on it as it lands; mark it ready (`mise exec -- gh pr ready`) only after the loop's final round passes with no must-fix findings. A plugin's version bump still lands last, so Version Bump Check stays red on the draft until then.
- Every PR bumps `version` in `.claude-plugin/plugin.json` (CI checks it): patch for fixes and wording, minor for new skills or behaviour, major for breaking changes. Without a bump, installed copies never update.
- After editing `hooks/always-on.md`, run `python3 scripts/build-hooks.py` and commit `hooks/session-start.json` too (CI checks they match).
- Validate before a PR: `claude plugin validate .` and `python3 scripts/build-hooks.py --check`.
- Skills stay generic: no product, company, model or person names. Personal choices belong in the user's own rules (for example the Oh plugin).
