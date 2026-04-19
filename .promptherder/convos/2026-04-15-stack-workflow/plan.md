# Plan: `/stack` Workflow

> **Status**: approved

## Goal

Add a `/stack` workflow to compound-v that auto-discovers project versions, compares them to stack.md and recommended best practices, and lets the user update stack.md interactively.

---

## Plan

### 1. Create `/stack` workflow

- **Files:** `workflows/stack.md`
- **Change:** New workflow file following `/idea` and `/rule` patterns (lightweight, one-file, `// turbo-all`). Steps:
  1. **Read** existing `.agent/rules/stack.md` if it exists
  2. **Scan** the project for version indicators — lockfiles, manifests, source-file patterns. Supported ecosystems:
     - `mix.exs` / `mix.lock` → Elixir + Erlang/OTP
     - `package.json` / `package-lock.json` → Node.js + npm deps
     - `go.mod` → Go + module deps
     - `Gemfile` / `Gemfile.lock` → Ruby
     - `pyproject.toml` / `requirements.txt` / `Pipfile` → Python
     - `Cargo.toml` → Rust
     - `pom.xml` / `build.gradle` → Java
     - `docker-compose.yml` / `Dockerfile` → infrastructure (PostgreSQL, Redis, etc.)
     - `.tool-versions` / `mise.toml` → mise/asdf version manager pins
  3. **Search the web** for each discovered technology: latest stable version + recommended production version
  4. **Output** a comparison table:
     ```
     | Technology | Actual (code) | stack.md | Latest Stable | Recommended | Notes |
     |------------|--------------|----------|---------------|-------------|-------|
     | Elixir     | 1.16.2       | 1.16     | 1.17.1        | 1.17        | Major available |
     | PostgreSQL | 16           | —        | 17.2          | 16 or 17    | LTS is fine |
     ```
  5. **Prompt** the user: which changes to apply? (Can accept all, pick specific rows, or add manual entries)
  6. **Write** `.agent/rules/stack.md` with the final selections, preserving any manual entries that weren't auto-detected
- **Verify:** `cat workflows/stack.md` — confirm it follows `/idea` and `/rule` pattern

### 2. Register `/stack` in `compound-v.md` rule

- **Files:** `rules/compound-v.md`
- **Change:** Add `/stack` to the Pipeline section (line ~15) with one-line description
- **Verify:** `grep stack rules/compound-v.md`

### 3. Document `/stack` in README

- **Files:** `README.md`
- **Change:** Add `/stack` to the workflow list table and a brief section near the existing `stack.md` documentation (around line 189)
- **Verify:** `grep -A3 '/stack' README.md`

### 4. Fix plan skill phase ordering + purge `structure.md`

- **Files:** `skills/compound-v-plan/SKILL.md`
- **Change:**
  - **Remove** all references to `.agent/rules/structure.md` (dead code — no one uses it, agent scans the codebase anyway)
  - **Split** Phase 2 into two sub-phases:
    - **Phase 2a (sequential):** Read `.agent/rules/stack.md`. If missing, print: _"No `stack.md` found. Run `/stack` to pin your versions — this improves web search accuracy."_ Then continue.
    - **Phase 2b (parallel):** All web searches (now version-scoped), project file reads, `future-tasks.md`, `hard-rules.md`.
- **Verify:** `grep -c structure skills/compound-v-plan/SKILL.md` — should be 0
- **Verify:** `grep -B2 -A8 'Phase 2' skills/compound-v-plan/SKILL.md`

---

## What this builds

### Happy path

1. User runs `/stack` in a project
2. Agent reads existing `stack.md` (if any), scans lockfiles/manifests, discovers Elixir 1.16, Phoenix 1.7, PostgreSQL 16
3. Agent searches web for latest stable versions of each
4. Agent prints comparison table showing actual vs stack.md vs latest
5. User says "update Elixir to 1.17, keep PostgreSQL at 16, add Redis 7"
6. Agent writes `.agent/rules/stack.md` with the selections
7. All future `/plan`, `/execute`, `/review` commands scope web searches to those versions

### Filesystem tree

```
compound-v/
├── skills/
│   └── compound-v-plan/
│       └── SKILL.md       ← MODIFIED (phase ordering)
├── workflows/
│   ├── execute.md
│   ├── idea.md
│   ├── plan.md
│   ├── review.md
│   ├── rule.md
│   └── stack.md          ← NEW
├── rules/
│   └── compound-v.md     ← MODIFIED (add /stack to pipeline)
└── README.md              ← MODIFIED (document /stack)
```

---

## Risks & mitigations

- **Web search noise** → Scope searches to "latest stable version [technology] 2026" not "[technology] best version". Parse official sources.
- **Lockfile format changes** → Workflow describes WHAT to look for, not exact parsing. The LLM handles format naturally.
- **Missing ecosystems** → Workflow explicitly says "scan for common indicators" and includes a fallback: "list any technologies you detect that don't match the above patterns."

## Rollback plan

`git revert` — three files touched, all additive. No breaking changes to existing workflows.

---

## References

- Full plan: `.promptherder/convos/2026-04-15-stack-workflow/plan.md`
- Decisions: `.promptherder/convos/2026-04-15-stack-workflow/decisions.md`
