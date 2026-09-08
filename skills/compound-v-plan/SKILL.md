---
name: compound-v-plan
description: Plan substantial changes or an explicitly requested design; preserve the distinction between plan-only work and authorized implementation.
---

# Planning

First identify the requested outcome and authorization. An explicit plan-only request ends with a plan. An implementation request permits planning and then implementation without asking the user to repeat authorization. These planning instructions end when the task moves to execution.

Read relevant code, project instructions, and actual runtime/lockfile versions. Use `.promptherder/stack.md` as recorded context, but flag differences from current manifests; legacy `.agents/rules/stack.md` and `.agent/rules/stack.md` are read-only migration sources. Research current or uncertain APIs using available tools and official version-matched documentation. Batch independent reads when supported. Do not demand a web search for every obvious local edit.

Ask only for missing information that changes the outcome or blocks a dependent action. Continue independent work while waiting. Describe key alternatives, tradeoffs, assumptions, and decisions briefly; do not publish private reasoning transcripts.

For a durable multi-step plan, use `compound-v-persist` and write `plan.md` with goal, scope, status, changed files, ordered/dependent steps, relevant verification, and material risks. Record concise decision rationales in `decisions.md` when useful. Scale detail to the task; do not force filesystem trees or minute-by-minute steps for small changes.

Treat `future-tasks.md` as optional deferred ideas, not accepted requirements. Include an idea only when the current request covers it. Save newly deferred work when requested; otherwise mention it only if useful.

For plan-only work, present the reviewable plan and stop. A later "implement", "proceed", or explicit execute invocation advances to execution; do not retain the prior plan-only prohibition. If implementation was already requested, continue using `compound-v-execute`. A full-pipeline/YOLO request is handled by `compound-v-pipeline`.
