---
description: Autonomous planning workflow. Researches, reasons, and presents a plan with minimal back-and-forth. Respects the user's time.
---

// turbo-all

# Plan

## Task

Plan the task described by the user in their message above.

## Rules

- DO NOT edit code during this workflow.
- You may read files to understand context.
- Never write to `stack.md` or `structure.md` without showing proposed changes and getting explicit user approval.
- **Minimize round-trips.** Do your own thinking. Don't ask the user to hold your hand.
- **YAGNI ruthlessly.** Kill ideas yourself before presenting them.

## Phase 1: Establish the goal

Determine the **desired end result** — the single sentence that defines success.

- If the user stated a clear goal, use it.
- If the goal is ambiguous, ask ONE question: "What's the desired end result?" and STOP. Do not proceed until you have a goal.
- Do NOT ask multiple clarifying questions. Infer what you can and note assumptions.

## Phase 2: Research (autonomous — no user interaction)

Do all of this in parallel, silently:

1. Resolve a task slug:
   - If the user provided a kebab-case slug (e.g. `/plan fix-auth`), use it.
   - If continuing a previous task, check `.promptherder/convos/` for a matching folder.
   - Otherwise, generate a short kebab-case name (2-4 words) from the task description.

2. Read `.agent/rules/stack.md` and `.agent/rules/structure.md` if they exist.

3. `search_web` for best practices, alternatives, and pitfalls. Scope queries to versions in `stack.md`.

4. `view_file_outline` on relevant project files.

5. Read `.promptherder/future-tasks.md` if it exists — check if any deferred ideas are relevant.

## Phase 3: Think (autonomous — no user interaction)

Build your internal reasoning. For each approach you consider:

- **Idea**: what is it?
- **Pros**: why it's good
- **Cons**: why it's risky or complex
- **Verdict**: accept / reject / ask (need user input)

Apply these filters yourself:

- YAGNI — is this the simplest approach?
- Does it solve the actual problem or a hypothetical one?
- What are the risks? Are they manageable?
- Are there rollback options?

**Reject bad ideas yourself.** Only surface ideas with verdict `ask` to the user.

### Persist decisions

Write the full decisions table to `.promptherder/convos/<slug>/decisions.md`:

```markdown
# Decisions: <title>

| #   | Idea | Verdict  | Pros | Cons | Rationale |
| --- | ---- | -------- | ---- | ---- | --------- |
| 1   | ...  | accepted | ...  | ...  | ...       |
| 2   | ...  | rejected | ...  | ...  | ...       |
| 3   | ...  | ask      | ...  | ...  | ...       |
```

Update this file whenever decisions change (feedback, re-planning, etc.).

## Phase 4: Present the plan

Write the plan to `.promptherder/convos/<slug>/plan.md` and present it to the user in a single response:

```markdown
# Plan: <title>

> `/plan` · **Status**: draft · `.promptherder/convos/<slug>/plan.md`

## Goal

<one sentence>

## Plan

1. Step name
   - Files: `path/to/file`
   - Change: what changes (1-2 bullets)
   - Verify: command to verify

## Risks & mitigations

- Risk → mitigation

## Rollback plan

<how to undo>
```

### Asking for input

After the plan, present **batch questions** — all the decisions you need input on, in one block:

```
**I need your input on:**

1. <question> — I recommend (A) because ...
   - (A) option
   - (B) option
2. <question>
   - (A) ...
   - (B) ...
```

If you have no questions (the path is clear), skip this section.

### Approval prompt

Always end with:

> **Reply APPROVED to proceed, reply SHOW DECISIONS to audit my reasoning, or give feedback.**
> Task: `<slug>`

## Handling responses

### If APPROVED

- Update status to `approved` in plan.md.
- Reply: **"Plan approved. Run `/execute` to begin. Task: `<slug>`"**
- Do NOT implement.

### If SHOW DECISIONS

- Print the contents of `.promptherder/convos/<slug>/decisions.md` (the full decisions table with all ideas, including rejected ones).
- After showing, re-prompt: **"Reply APPROVED, give feedback, or answer the open questions above."**

### If feedback

- Incorporate feedback, re-research if needed, update plan.
- Present the updated plan (same format as Phase 4).
- Don't apologize excessively. Just fix it and re-present.

### If answers to questions

- Process answers, update plan accordingly.
- Present the updated plan.

## Deferred ideas

If you identify ideas with future value that don't belong in this plan, list them when presenting the plan:

```
**Ideas I'd defer to future tasks:**
- <idea> — <brief rationale>
- <idea> — <brief rationale>

Should I add these to `future-tasks.md`?
```

**Only append to `.promptherder/future-tasks.md` after the user confirms.** Format:

```markdown
- [ ] <idea> — <brief rationale> _(from: <slug>, <date>)_
```

Do NOT put deferred items in the plan file.
