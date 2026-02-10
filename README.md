# Compound V

An AI coding methodology that gets things done with minimal human effort.

## Philosophy: Superpowers vs Compound V

[Superpowers](https://github.com/obra/superpowers) is about **control** — subagents are spawned for each task, two-stage reviews gate progress, worktrees isolate branches, and checkpoints require human approval. It's a rigorous process that keeps the AI on rails.

Compound V is about **results** — the agent researches before acting, executes in parallel batches, and only surfaces decisions that genuinely need human input. You describe what you want, approve a plan, and come back when it's done.

| | Superpowers | Compound V |
|---|---|---|
| Execution | Subagent per task | Parallel tool calls |
| Reviews | Two-stage gating | Severity-graded, batch at end |
| Research | Training data only | Web search before every step |
| Checkpoints | After each task | After each batch |
| Human effort | High (gate each task) | Low (approve plan, review result) |

Both share the same core values: TDD, systematic over ad-hoc, verify before declaring success.

## Install

```bash
# Install promptherder
go install github.com/shermanhuman/promptherder/cmd/promptherder@latest

# Pull this herd
promptherder pull https://github.com/shermanhuman/compound-v

# Sync to agents
promptherder
```

## What's Included

| Type | Purpose |
|---|---|
| **Workflows** | `/plan`, `/execute`, `/review`, `/idea`, `/rule` |
| **Skills** | Planning, review, TDD, debugging, parallel execution, verification |
| **Rules** | Core methodology, output formatting, browser testing |

## Usage

1. **`/plan`** — Describe what you want. The agent researches, evaluates options, and presents a plan.
2. **`/execute`** — Approve the plan. The agent works through it in parallel batches.
3. **`/review`** — Get a severity-graded code review with 10 parallel checks.

## License

MIT License — Copyright (c) 2026 Sherman Boyd
