---
name: compound-v-verify
description: Mandatory checklist before claiming a task is done. Ensures verification, clean code, and accurate reporting. Use before saying "done" or "complete".
---

# Verification Before Completion

Before reporting a task as done, run through this checklist.

## When to use this skill

- before telling the user a task is complete
- before moving to the next plan step
- before writing a review or execution summary

## The checklist

1. **Requirements** — Re-read the task description. Confirm all requirements are met and no details or edge cases were missed.
2. **Tests** — During iteration, run the repository's fast checks and affected tests; a fast subset does not prove the edited feature is covered. Before final completion of code changes or PR submission, run the full repository suite and required checks. Reuse successful results when subsequent changes do not invalidate them; do not rerun the whole suite at every batch checkpoint or for a final prose-only edit. For documentation-only or similarly low-impact changes, use appropriate direct validation plus required repository checks instead of manufacturing a test. Report what ran, what was reused, and any relevant untested scope.
3. **Code cleanliness** — Remove temporary debug prints, commented-out code, and placeholder TODOs introduced by this task; do not sweep unrelated work.
4. **Warnings** — Check for and resolve linter warnings, compiler warnings, and deprecation notices.
5. **Verification commands** — Run the exact verification commands from the plan step. Confirm expected output.
6. **Documentation** — Update relevant docs if you changed behavior, APIs, CLI flags, or configuration.

## Statement of completion

When you announce completion, include:

- What you did (1-2 lines)
- How you verified it (exact commands + results)

Example: "Step 3 complete. Added auth middleware to `lib/auth/plug.ex`. Verified: `mix test test/auth/` — 8 tests, 0 failures."

## Never

- Say "done" without running verification commands
- Skip the checklist because "it's simple"
- Move to step N+1 if step N is not verified

When a required check cannot run, report the exact command and blocker and scope the completion claim accordingly. Never claim that an unrun smoke test or generated host file proves runtime behavior.
