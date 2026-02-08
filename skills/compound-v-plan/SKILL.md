---
name: compound-v-plan
description: Autonomous planning with internal reasoning. Researches, evaluates ideas, presents a plan. Minimizes user round-trips. Use before making non-trivial changes.
---

# Planning Skill

## When to use this skill

- any multi-file change
- any change that impacts behavior, data, auth, billing, or production workflows
- any debugging that needs systematic isolation
- any design decision with multiple viable approaches

## Core pattern: think first, ask smart

Planning is **LLM-driven**, not turn-by-turn. The LLM should:

1. **Understand the goal** — what does success look like?
2. **Research autonomously** — read code, search web, understand constraints
3. **Reason internally** — evaluate approaches, apply YAGNI, reject bad ideas
4. **Present a plan** — one response with the plan, batch questions, and approval prompt

### Anti-patterns (don't do these)

- ❌ Asking the user to ACCEPT/REJECT individual ideas one at a time
- ❌ Showing an ideas table before you've done your own thinking
- ❌ Asking clarifying questions you could answer by reading the code
- ❌ Multiple rounds of "does this look right?" on sections of the plan
- ❌ Deferring the goal statement to a later phase

### Good patterns

- ✅ Research first, then present a confident plan
- ✅ Batch all questions into one block at the end
- ✅ Offer SHOW DECISIONS audit on demand (not by default)
- ✅ Kill bad ideas yourself with rationale (visible in audit)
- ✅ State assumptions explicitly so the user can correct them

## Internal reasoning format

When evaluating approaches, use this structure internally:

| #   | Idea | Verdict  | Pros | Cons | Rationale |
| --- | ---- | -------- | ---- | ---- | --------- |
| 1   | ...  | accepted | ...  | ...  | ...       |
| 2   | ...  | rejected | ...  | ...  | ...       |
| 3   | ...  | ask      | ...  | ...  | ...       |

**Verdicts:**

- `accepted` — you're confident this is right. Include in plan.
- `rejected` — you've killed it. Available in SHOW DECISIONS audit.
- `ask` — you genuinely can't decide without user input. Surface as a batch question.

## Investigation techniques

When researching:

- `search_web` for patterns, pitfalls, best practices (scope to versions in `stack.md`)
- Apply first-principles thinking — does this solve the actual problem?
- Challenge with YAGNI — is this the simplest approach?
- Build user stories for UX-facing ideas
- Check `.promptherder/future-tasks.md` for relevant deferred ideas

## Planning rules

- Steps should be **small** (2–10 minutes each).
- Every step must include **verification**.
- Prefer **incremental deliverables** (avoid "big bang" edits).
- Identify **rollback** and **risk controls** early.
- Group independent steps for **parallel execution** where possible.
- Never write to `stack.md` or `structure.md` without user approval.
- State the **goal** first. Everything else flows from it.

## Plan step format

```
1. Step name
   - Files: `path/to/file.ext`, `...`
   - Change: (1–2 bullets)
   - Verify: (exact commands or checks)
```
