---
description: Review changes, optionally target a check, and fix only when the task includes authorization to fix.
---

# Review

Use `compound-v-review`. Pass the active task, requested check, and whether fixes were requested. Reuse an execution task when called from implementation. A standalone review may create its own task context. YOLO or an ordinary review-and-fix request authorizes in-scope fixes. Let the skill persist the review once.
