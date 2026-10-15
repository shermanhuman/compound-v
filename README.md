# Compound V

A plan-and-review methodology for Claude Code and Codex, packaged as a plugin.

- **Plans** get a one-sentence goal, a decisions table that becomes the job's decisions log, steps that each say how they're checked, rollout and rollback, and out-of-scope items with a home.
- **Every plan is reviewed** by a fresh reviewer before you're asked to approve it: claims checked against the code and data, scope, design traps, rollout, proof.
- **Code review** runs ten checks (correctness, edges, security, perf, tests, design, dry, yagni, logging, docs), sorts findings into Must-fix and Polish, and posts the report on the pull request.
- **Follow-up rounds** review only the fixes, confirm each earlier finding, and stop the loop when it starts spinning: fixes that undo earlier fixes, the same problem recurring, the same lines churning.
- **The review loop** sequences it all — full review, follow-ups, one independent full-diff pass by a second model or the host's built-in review, a single polish pass — and records every round on the PR.

## Install

Claude Code:

```text
/plugin marketplace add shermanhuman/compound-v
/plugin install compound-v@compound-v
```

Codex:

```bash
codex plugin marketplace add shermanhuman/compound-v
codex plugin add compound-v@compound-v
```

The same marketplace also lists [Grugg](https://github.com/shermanhuman/grugg) (terse mode, opt-in) and the author's personal [Oh](https://github.com/shermanhuman/oh) plugins.

**Codex hooks.** Compound V's always-on rules arrive through a session-start hook. Codex skips plugin hooks until you trust them: open `/hooks` once and trust the Compound V hook. Without that, the skills still work but plans and PRs won't be steered to them automatically.

**Updating.** Installed copies change when the plugin's version does. In Claude Code, turn on auto-update for this marketplace in `/plugin`, or run `claude plugin update compound-v@compound-v`. In Codex, run `codex plugin marketplace upgrade compound-v`.

## Skills

| Skill | Use |
|---|---|
| `compound-v:plan` | Format and habits for any implementation plan, including in plan mode |
| `compound-v:plan-review` | Fresh, critical review of a finished plan; verdict approve / approve with changes / rework |
| `compound-v:review` | Ten-check review of a full diff; Must-fix / Polish; posted on the PR |
| `compound-v:followup` | Review of only the fixes since the last round, with the spinning check |
| `compound-v:review-loop` | Who reviews when, when to stop, how rounds are recorded |
| `compound-v:testing` | What's worth testing and at which layer |

In Claude Code, invoke a skill as `/compound-v:review`; in Codex, as `$compound-v:review`. Both hosts also load them on their own when a task matches.

## Choosing the second voice

The loop's independent pass uses "a different model when one is configured". Name it in your own rules (`AGENTS.md`, `CLAUDE.md`, or a personal plugin) along with the command to run it, for example a Codex model via `codex exec` for a Claude user, or Claude via `claude -p` for a Codex user. Without one, the loop uses the host's built-in review, and failing that a fresh full pass.

## Severity

| Group | Severity | Meaning |
|---|---|---|
| Must-fix | ⠿ B blocker, ⠷ M major | wrong behaviour, security, data loss, silent failure, broken contract between components, failing rollout or migration |
| Polish | ⠴ m minor, ⠠ n nit | everything else |

Only must-fix findings earn another round.

## Upgrading from 1.x

1.x was a [Promptherder](https://github.com/shermanhuman/promptherder) herd with `/workflow-plan`, `/workflow-execute`, YOLO and `.promptherder/convos/`. 2.0 drops all of that: plan in the host's own plan mode, and reviews live on the PR or issue.

Deleting the herd alone leaves what Promptherder generated from it: the old always-on rule in `AGENTS.md` (which still points sessions at `/plan`, `/execute` and YOLO) and the old skill and rule folders under `.claude/` and `.agents/`, which Claude Code and Codex keep loading next to the plugin's skills. The files are untracked, so they also survive a `git pull`, and a newly tracked `AGENTS.md` can block one. In each existing checkout, before pulling the change that retires Promptherder there:

1. Install the plugin as above, or update an existing install so the marketplace clone has the script: `claude plugin marketplace update compound-v` (or let the marketplace auto-update). In Codex, `codex plugin marketplace upgrade compound-v` puts it under `~/.codex/plugins/cache/compound-v/compound-v/<version>/scripts/`.
2. Preview: `python3 -I ~/.claude/plugins/marketplaces/compound-v/scripts/cleanup_generated.py <checkout>` (from a clone of this repository, `scripts/cleanup_generated.py`). It prints every path it would remove and anything it leaves for you.
3. Remove: the same command with `--apply`. It removes only untracked files with evidence that Promptherder generated them: its manifest lists them (from git history if the manifest is already gone), they carry Promptherder's marker, or a herd source of the same name exists. Tracked files, `.claude/settings*.json`, `.claude/worktrees/` and anything without that evidence are kept, and it stops if git can't read the checkout. If `AGENTS.md` is left for you, the text above Promptherder's marker is yours: keep it and delete from the marker line down.
4. Pull, then check: `git status --short --ignored` shows nothing under `.claude/skills/`, `.claude/rules/` (apart from tracked rules) or `.agents/`. Start a new session.

## Credits

Based on [obra/superpowers](https://github.com/obra/superpowers), with the [Antigravity adaptation](https://github.com/anthonylee991/gemini-superpowers-antigravity).

## License

MIT
