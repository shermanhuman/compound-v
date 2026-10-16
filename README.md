# Compound V

A plan-and-review methodology for Claude Code and Codex, packaged as a plugin.

- **Plans** get a one-sentence goal, a decisions table that becomes the job's decisions log, steps that each say how they're checked, rollout and rollback, and out-of-scope items with a home.
- **Open decisions get settled** one question at a time, most consequential first, with a recommendation each time and every answer written into the decisions table.
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
| `compound-v:interrogate` | Settle a plan's open decisions one question at a time, most consequential first, each answer recorded in the decisions table |
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

Deleting the herd alone leaves what Promptherder generated from it: the old always-on rule in `AGENTS.md` (which still points sessions at `/plan`, `/execute` and YOLO) and the old skill and rule folders under `.claude/` and `.agents/`, which Claude Code and Codex keep loading next to the plugin's skills. The files are untracked, so they also survive a `git pull`, and a newly tracked `AGENTS.md` can block one. Let Promptherder remove its own output, in each existing checkout, before pulling the change that retires it there:

1. Remove the herds: `rm -rf .promptherder/herds/compound-v` (or `.promptherder/herds` to retire Promptherder entirely).
2. Preview, then re-sync, so Promptherder deletes every file its manifest says it generated from them: `promptherder plan --update-lock`, then `promptherder --update-lock`.
3. If you're retiring Promptherder: delete the `AGENTS.md` and `CLAUDE.md` it leaves behind. If `AGENTS.md` has text above the `<!-- Auto-generated by promptherder -->` marker, that part is yours: keep it and delete from the marker line down.
4. Check: `find .claude/skills .claude/rules .agents -maxdepth 1 \( -name 'compound-v-*' -o -name 'workflow-*' -o -name rule-browser \) 2>/dev/null` prints nothing, and `git status --short --ignored` shows no leftover old skills. Promptherder leaves the emptied folders behind; `find .claude/skills .agents -type d -empty -delete` tidies them. Then pull and start a new session.

Without Promptherder installed, remove the `compound-v-*`, `workflow-*` and `rule-browser` folders under `.claude/skills/` and `.agents/skills/` by hand, and the generated part of `AGENTS.md`/`CLAUDE.md` as in step 3.

## Credits

Based on [obra/superpowers](https://github.com/obra/superpowers), with the [Antigravity adaptation](https://github.com/anthonylee991/gemini-superpowers-antigravity).

`interrogate` adapts the `grilling` skill from [mattpocock/skills](https://github.com/mattpocock/skills) at commit `49dd158` (MIT, Copyright (c) 2026 Matt Pocock): the decision tree, looking facts up instead of asking for them, and not acting until the user confirms. It differs by asking one decision at a time through the host's question tool and recording each answer in the plan's decisions table.

## License

MIT
