# Compound V

A plan-and-review method for Claude Code and Codex, packaged as a plugin. Work is planned with a decisions log, checked by reviewers who haven't seen it before, and merged by a person, one release per pull request. Most of it exists because something specific went wrong without it; each step below says what.

## The workflow

1. **Pick the work.** `/compound-v:next` reads your open issues and pull requests and recommends one project, with reasons and runners-up. It finishes in-flight work before starting new work, never picks something only you can unblock, and folds small leftovers into the same release. With no argument it looks at the repositories this session has touched; `all` covers every organisation you belong to and your own account; a repository or topic narrows it.
2. **Plan** in the host's plan mode with `compound-v:plan`: a one-sentence goal, a decisions table (`# · Idea · Verdict · Why · Decided`), steps that each say how they're checked, rollout and rollback. Rejected ideas stay in the table, so nobody proposes them again, and reviewers treat decided rows as settled. Every plan gets an issue (plan in the body, reviews as comments), so a long job survives a lost context.
3. **Plan review** by a fresh reviewer (`compound-v:plan-review`) before you're asked to approve. It checks the plan's claims against the code and data. The trap it exists for is a confident "X is unused" or "this already works" that nobody verified.
4. **Interrogate** (`compound-v:interrogate`) settles what's left. The calls the evidence already makes come to you as one pre-decided checklist (tick what you accept), and the rest are asked one at a time with the full context inside the question, because text written above a question widget goes unread.
5. **Build in a worktree** on a branch from a fresh fetch. The main checkout may hold someone else's work or a running dev server.
6. **Review loop** (`compound-v:review-loop`) at the tier the diff needs:
   - *Full:* round 1 runs ten checks on the whole diff, follow-ups review only each fix, then an independent full-diff pass by a second voice, then one polish pass.
   - *Light* (prose-only diffs): one focused pass that checks every claim against reality and sweeps the repository for text the change made stale.

   Agent-instruction files (`AGENTS.md`, rules, skills, hooks) get the full tier with an *instructions* pass instead of the code checks.

   Why it's built this way:
   - **Fresh reviewers each round:** a reviewer that has seen the code tends to accept its own earlier conclusions.
   - **Every page of all three comment endpoints:** unpaginated reads stop at 30, and `gh pr view --comments` leaves out inline comments, so findings disappear without an error.
   - **The stop rule:** fixes that undo fixes, the same finding coming back, or the same lines churning mean patching won't converge, so the design question goes to you.
   - **Findings are hypotheses:** a wrong premise adopted unchecked spreads.
7. **You merge, and a merge is a release.** The agent never merges or pushes to the default branch. Pull requests stay drafts until the last review round has no must-fix findings.
8. **Follow-ups go to issues:** a real piece of work gets its own issue, and small leftovers go in one "Follow-ups from #N" checklist. Never a local list, because local notes made unfinished work look finished.
9. **Issue and PR references are links.** A Stop hook (`hooks/check-links.py`) sends a reply back once when it names an issue or PR, such as `#12`, `repo#12` or `PR 12`, outside a markdown link, a URL or code. Run, build and job numbers like `run #512` are left alone; a rare false match costs one rewrite. A reminder at session start wasn't enough: over a long session it stopped being followed.

## Install

Claude Code:

```bash
claude plugin marketplace add shermanhuman/compound-v
claude plugin install compound-v@compound-v
```

Then start a new session, or run `/reload-plugins` in an open one. Inside a session, `/plugin` opens the same thing as a panel.

Codex:

```bash
codex plugin marketplace add shermanhuman/compound-v
codex plugin add compound-v@compound-v
```

Then start a new session and open `/hooks` to trust the Compound V hook. Codex skips plugin hooks until you do, and without the hook the skills still work, but plans and pull requests aren't steered to them.

The same marketplace lists [Grugg](https://github.com/shermanhuman/grugg) (terse mode, opt-in), [Cartographer](https://github.com/shermanhuman/cartographer) (a code map over MCP that the review skills use when it's installed; it runs the `cartographer` binary from PATH, or fetches it with mise) and the author's personal [Oh](https://github.com/shermanhuman/oh) plugins. Install them the same way, by name.

## Updating

Installed copies change only when a plugin's version does.

- **Claude Code:** turn on auto-update for this marketplace in `/plugin` (it's off by default for third-party marketplaces), or run `claude plugin update compound-v@compound-v`. Updates apply at the next session, or after `/reload-plugins`. `claude plugin marketplace update` only refreshes the listing; it doesn't update installed plugins.
- **Codex:** run `codex plugin add compound-v@compound-v` to fetch the new version. If `/hooks` asks, trust the hook again.

## Switching a plugin on per repository

For a plugin only some repositories need (a framework's skills, an API's reference), install it once at user scope, switch it off in your user settings, and switch it on in each repository that wants it:

- **Claude Code:** `"<plugin>@compound-v": false` under `enabledPlugins` in `~/.claude/settings.json`, and `true` in the repository's committed `.claude/settings.json`. Worktrees of the repository follow it.
- **Codex:** `enabled = false` under `[plugins."<plugin>@compound-v"]` in `~/.codex/config.toml`, and `enabled = true` in the repository's committed `.codex/config.toml`. Codex reads that file only once the project path itself is trusted; a trusted parent folder doesn't count.

Sessions that span several repositories (started from a parent folder) don't pick up any one repository's settings. Switch a plugin on at user scope instead when you want it there.

## Skills

| Skill | Use |
|---|---|
| `compound-v:next` | Recommend the next project from open issues and pull requests, then offer to plan it |
| `compound-v:plan` | Format and habits for any implementation plan, including in plan mode |
| `compound-v:interrogate` | Settle a plan's open decisions: the clear calls confirmed in one checklist, the rest asked one at a time, every answer in the decisions table |
| `compound-v:plan-review` | Fresh, critical review of a finished plan; verdict approve / approve with changes / rework |
| `compound-v:review` | Review of a full diff: ten code checks, or the light or instructions pass; Must-fix / Polish; posted on the PR |
| `compound-v:followup` | Review of only the fixes since the last round, with the spinning check |
| `compound-v:review-loop` | Which tier, who reviews when, when to stop, how rounds are recorded |
| `compound-v:testing` | What's worth testing and at which layer |

In Claude Code, invoke a skill as `/compound-v:next`; in Codex, as `$compound-v:next`. Both hosts also load skills on their own when a task matches.

## Choosing the second voice

The full tier's independent pass uses "a different model when one is configured". Name it in your own rules (`AGENTS.md`, `CLAUDE.md`, or a personal plugin) along with the command to run it, for example a Codex model via `codex exec` for a Claude user, or Claude via `claude -p` for a Codex user. Without one, the loop uses the host's built-in review, and failing that a fresh full pass.

## Severity

| Group | Severity | Meaning |
|---|---|---|
| Must-fix | ⠿ B blocker, ⠷ M major | wrong behaviour, security, data loss, silent failure, broken contract between components, failing rollout or migration |
| Polish | ⠴ m minor, ⠠ n nit | everything else |

Only must-fix findings earn another round.

## Gotchas for adopters

It assumes GitHub with the `gh` CLI (the review skills post with `gh pr comment` and read with `gh api --paginate`), Claude Code or Codex, and an issue tracker.

- **Cost.** A full loop is three to five fresh reviewer runs per pull request: round 1 and the independent pass read the whole diff and the changed files, and follow-ups read the fixes. In a six-pull-request sample, adding the hosts' built-in reviews on top of the rubric review multiplied input tokens about tenfold (median about 2.6M per rubric review). The light tier exists for prose.
- **Versions drive updates.** Installed copies stay on the cached version until `version` in `plugin.json` changes, so every change ships with a bump.
- **Codex hook trust.** Codex skips a plugin's hooks until you trust them in `/hooks`, and it ties trust to the hook's contents, so an update that changes a hook can ask again (documented by Codex; not yet observed here).
- **Codex updates.** `codex plugin marketplace upgrade` refreshes the marketplace snapshot; once it reported "already up to date" and kept the old plugin. `codex plugin add <plugin>@compound-v` re-fetches. It also sets that plugin's `enabled = true` in `~/.codex/config.toml`, so check per-repository plugins you'd switched off.
- **Project-only enabling doesn't install.** A repository's settings can switch a plugin on, but it must already be installed at user scope.
- **Cloud and remote sessions load no plugins** (documented for Claude Code; unverified for Codex). Put the rules that must always hold (who merges, what a pull request means, version bumps) in each repository's `AGENTS.md` too.
- **The link check needs `python3` on PATH and a POSIX shell** (on Windows, Git Bash, which Claude Code uses for hooks when installed). Without them, every reply goes through unchecked; any failure to start the check lets the reply through rather than sending it back. Codex passes the same Stop fields, so the check should read its reply from `last_assistant_message` there (unverified for Codex), and changing `hooks/hooks.json` can ask for hook trust again.
- **One marketplace per plugin.** Adding the same plugin from two marketplaces loads it twice, and only one copy's hooks run (documented for Claude Code).
- **Plugin MCP servers in Codex** don't get `${CLAUDE_PLUGIN_ROOT}` expanded and start in the session's folder (seen in testing with Codex 0.162). Use a command on PATH.
- **A `codex exec` run with `-s read-only`** can't post comments or call MCP tools. Post its report yourself, unchanged.
- **Codex's question tool** (`request_user_input`) is single-choice, takes one to three short questions, and works in Plan mode only by default. Interrogate falls back to a numbered text checklist there.
- **The second voice needs configuring** in your own rules, or the independent pass uses the host's built-in review.
- **Open sessions keep the old version** after an update until they restart or run `/reload-plugins`.

## Upgrading from 1.x

1.x was a [Promptherder](https://github.com/shermanhuman/promptherder) herd. To move an existing checkout to the plugin, follow [docs/upgrading-from-1x.md](docs/upgrading-from-1x.md).

## Credits

Based on [obra/superpowers](https://github.com/obra/superpowers), with the [Antigravity adaptation](https://github.com/anthonylee991/gemini-superpowers-antigravity).

`interrogate` adapts the `grilling` skill from [mattpocock/skills](https://github.com/mattpocock/skills) at commit `49dd158` (MIT, Copyright (c) 2026 Matt Pocock): the decision tree, looking facts up instead of asking for them, and not acting until the user confirms. It differs by confirming clear calls in one checklist, asking the rest one decision at a time through the host's question tool, and recording each answer in the plan's decisions table.

## License

MIT
