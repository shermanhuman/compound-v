# Compound V

An AI coding methodology for people who'd rather ship than babysit.

You type `/plan`, approve what looks good, and come back to working code. The agent researches best practices, executes in parallel, reviews its own work, and only bugs you when it genuinely can't decide something on its own.

## Where it came from

Compound V is a fork of [obra/superpowers](https://github.com/obra/superpowers) — a fantastic set of prompts that brought structure and discipline to AI coding. We love Superpowers. We use a lot of the same ideas: TDD, systematic debugging, verify before you declare victory.

Where we diverge is philosophy. Superpowers is about **control** — subagents, gated checkpoints, human approval at each step. That's great when you want to supervise closely. Compound V is about **results with minimal effort** — the agent does its homework, makes its own decisions where it can, and gives you one plan to approve instead of twenty micro-decisions. You stay in the loop, but the loop is smaller.

## Install

```bash
go install github.com/shermanhuman/promptherder/cmd/promptherder@latest
promptherder pull https://github.com/shermanhuman/compound-v
promptherder
```

That's it. Your agents now have Compound V loaded. Works with VS Code Copilot (`.github/`) and Antigravity (`.agent/`).

---

## The Pipeline

Five slash commands. That's the whole interface.

### `/plan` — "figure this out for me"

You describe what you want. The agent reads your codebase, searches the web for best practices scoped to your exact stack versions, evaluates multiple approaches internally, kills the bad ideas itself, and hands you a single confident plan.

The magic: it tracks every idea it considered — accepted, rejected, or deferred — in a `decisions.md` file. You can audit them any time with `SHOW DECISIONS`. Ideas that are good but out of scope get offered as future tasks instead of cluttering the current plan.

**Example:**

```
You: /plan add rate limiting to the API

Agent: I'm using the planning skill to work through this.

        Researching: reading routes, checking stack.md for Go 1.23 / Chi v5,
        searching for Chi middleware patterns, reading future-tasks.md...

# Plan: add-rate-limiting

> **Status**: draft

## Goal

Add per-IP rate limiting to all public API routes.

### 1. Add rate limiter middleware
- **Files:** `internal/middleware/ratelimit.go`
- **Change:**
  - Test: TestRateLimiterRejects429AfterLimit
  - Code: Token bucket middleware using golang.org/x/time/rate
- **Verify:** `go test ./internal/middleware/...`

### 2. Wire into router
- **Files:** `cmd/server/routes.go`
- **Change:**
  - Test: TestPublicRoutesHaveRateLimiter
  - Code: Add middleware to public route group
- **Verify:** `go test ./cmd/server/...`

## Risks & mitigations
- Risk: shared state across goroutines → use sync.Map for per-IP limiters

## Rollback plan
Remove middleware from route group, delete ratelimit.go.

**Ideas I'd defer to future tasks:**
- Redis-backed rate limiting for multi-instance deployments
- Per-endpoint rate limit configuration

> Add these to future-tasks.md? yes / no

> Run /execute add-rate-limiting to proceed, SHOW DECISIONS to audit,
> DECLINE to reject, or give feedback.
```

You say `/execute add-rate-limiting` and go get coffee.

---

### `/execute` — "go build it"

Running `/execute` IS the approval. The agent reads the plan, groups independent steps into parallel batches, searches the web for latest docs before each batch, and works through everything with verification after each step.

If something breaks mid-way, it automatically switches to the debug skill — reproduce, isolate, hypothesize, fix, add a regression test. If the plan itself turns out to be wrong, it stops and asks before going off-script.

When it's done, it automatically runs a full `/review`.

**YOLO mode:** `/execute YOLO` — executes the plan, auto-reviews, auto-fixes every finding, and gives you a summary. Zero interaction.

---

### `/review` — "tear this apart"

This is where Compound V gets fun. The agent splits the review into **10 independent checks**, each focused on its own problem domain:

| # | Check | What it looks for |
|---|-------|-------------------|
| 1 | `correctness` | Does the code actually do what the plan said? |
| 2 | `edges` | Nil, empty, zero, max, off-by-one, race conditions |
| 3 | `security` | Hardcoded secrets, unsanitized input, CVEs, auth gaps |
| 4 | `perf` | N+1 queries, unbounded loops, missing timeouts |
| 5 | `tests` | Coverage gaps, flaky tests, happy-path-only assertions |
| 6 | `design` | Single responsibility, naming, idiomatic patterns |
| 7 | `dry` | Duplicated logic, copy-paste with minor variations |
| 8 | `yagni` | Abstractions nobody asked for, premature optimization |
| 9 | `logging` | Silent failures, missing context, leaked PII in logs |
| 10 | `docs` | Outdated comments, missing API docs, stale READMEs |

Each check runs concurrently. Each one searches the web for version-specific gotchas scoped to your `stack.md`. Findings get severity-graded with braille dot indicators:

```
| ID | Sev | Location         | Issue                           |
|----|-----|------------------|---------------------------------|
| B1 | ⠿   | auth.go:42       | JWT secret loaded from env without fallback |
| M1 | ⠷   | ratelimit.go:18  | sync.Map never pruned — memory leak under load |
| m1 | ⠴   | routes.go:7      | Unused import                   |

> FIX to fix ⠿⠷, FIX ALL to fix everything, SKIP to move on, or give feedback.
```

After finding issues, it also **scans the rest of the codebase** for similar patterns — so you don't fix one instance while three others lurk elsewhere.

You can also run a single check: `/review security` or `/review perf`.

**YOLO mode:** `/review YOLO` — auto-fixes everything from blockers down to nits. Outputs a summary.

---

### `/idea` — "save this for later"

Dead simple. You have a thought mid-session that's not in scope? Type `/idea redis-backed rate limiting for multi-instance` and it appends a checklist item to `.promptherder/future-tasks.md` with a date stamp. No ceremony. Next time you `/plan`, the agent reads that file and considers whether any deferred ideas are relevant.

```
You: /idea add OpenTelemetry tracing to all HTTP handlers

Agent: Added to future tasks.
       - [ ] add OpenTelemetry tracing to all HTTP handlers _(added: 2026-01-15)_
```

---

### `/rule` — "always do this"

Same energy as `/idea`, but for project-wide rules that the AI must follow in every session. Type `/rule never use eval` and it gets appended to `.promptherder/hard-rules.md`. Every workflow reads that file. Every review checks against it.

```
You: /rule all API routes require authentication

Agent: Added hard rule.
       - all API routes require authentication
```

Now `/review` will flag any unprotected route as a blocker. `/plan` will include auth in every new endpoint. It's like a linter rule, but for your AI.

---

## YOLO Mode

The `YOLO` flag cascades through the pipeline. It's for when you trust the process and just want results:

| Command | What happens |
|---|---|
| `/review YOLO` | Auto-fix all findings (⠿→⠠). Output summary. |
| `/execute YOLO` | Execute plan, auto-review, auto-fix. Zero interaction. |
| `/plan YOLO` | Full pipeline: plan → execute → review → fix. You literally just describe what you want and walk away. |

---

## State Files

Compound V keeps its memory in `.promptherder/`. This is what makes it more than a set of prompts — it's a system that learns your project.

| File | What it does |
|---|---|
| `hard-rules.md` | Project rules the AI always follows. Added by `/rule`. |
| `future-tasks.md` | Ideas parked for later. Added by `/idea` or during `/plan`. |
| `convos/<slug>/plan.md` | The approved plan for a task. |
| `convos/<slug>/decisions.md` | Every idea considered — accepted, rejected, deferred. |
| `convos/<slug>/execution.md` | Step-by-step execution log with verification results. |
| `convos/<slug>/review-*.md` | Review findings and resolutions. |

### stack.md

Create `.agent/rules/stack.md` (or `.github/rules/stack.md`) to pin your versions:

```markdown
# Stack

- Go 1.23
- Chi v5.2
- PostgreSQL 16
- Node 22 (for frontend tooling)
```

Every workflow reads this file. Web searches get scoped to these exact versions. Reviews check for version-specific gotchas. Plans use version-appropriate patterns. It's the single source of truth for "what are we building with."

---

## .gitignore tip

The state files in `.promptherder/convos/` are useful for continuity but can be noisy in PRs. Add this to your `.gitignore`:

```
# promptherder conversation state (keep rules and future-tasks)
.promptherder/convos/
```

Keep `hard-rules.md` and `future-tasks.md` tracked — they're valuable project knowledge. The conversation artifacts are ephemeral.

Also add the agent target directories if you don't want generated files in your repo:

```
.agent/
.github/copilot-instructions.md
```

---

## What's Included

| Type | Contents |
|---|---|
| **Workflows** | `/plan`, `/execute`, `/review`, `/idea`, `/rule` |
| **Skills** | Planning, TDD, code review, debugging, parallel execution, verification, persistence |
| **Rules** | Core methodology, output formatting, browser testing |

## Credits

- [obra/superpowers](https://github.com/obra/superpowers) — the original methodology that started it all
- [anthonylee991/gemini-superpowers-antigravity](https://github.com/anthonylee991/gemini-superpowers-antigravity) — Antigravity adaptation

## License

MIT License — Copyright (c) 2026 Sherman Boyd
