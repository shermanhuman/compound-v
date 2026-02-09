---
description: Runs a review pass with severity levels (Blocker/Major/Minor/Nit). Supports check targeting and YOLO mode.
---

// turbo-all

# Review

Invoke the `compound-v-review` skill and follow it exactly.

## Workflow-specific protocol

### Slug resolution

1. If the user provided a kebab-case slug (e.g. `/review fix-this`), use it.
2. If invoked as part of `/execute` (within an execution flow), use the plan's slug. Overwriting `review.md` is correct here.
3. Otherwise, this is a **standalone review**. Generate a new slug from the review scope (e.g. `review-last-commit`, `review-auth-module`). Do NOT reuse a slug from a previous standalone review.

### Check targeting

If the user specified a check short name (e.g. `/review security`, `/review edges`), pass it to the review skill. Run only that check.

If the user specified `YOLO` (e.g. `/review YOLO`), pass that mode to the review skill.

Both can be combined with a slug: `/review fix-this security`, `/review fix-this YOLO`.

### Persist (mandatory)

Write the review to `.promptherder/convos/<slug>/review.md`.
Confirm it exists by listing `.promptherder/convos/<slug>/`.

Do not implement changes in this workflow unless `YOLO` mode is active.
