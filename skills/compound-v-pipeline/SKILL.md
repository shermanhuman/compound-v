---
name: compound-v-pipeline
description: Run planning, implementation, verification, and review when the user requests the full task or an autonomous YOLO pipeline.
---

# Authorized pipeline

Confirm the task includes implementation. An explicit plan-only request stays in planning even if autonomy is requested for research. If the request is ambiguous between a plan and a full pipeline, clarify that choice before implementation.

Use `compound-v-plan` to establish the scoped plan, then `compound-v-execute` to implement, verify, review, and fix relevant findings. Invoke these callable helper skills directly; do not attempt to automatically invoke manual-only `workflow-*` entry points.

Carry the same repository, task slug, plan path, scope, and authorization across phases. Planning restrictions expire on the authorized transition to execution. Review-only restrictions do not override a request to fix. After compaction, reread the current task artifacts and user authorization rather than guessing the phase.

YOLO reduces unnecessary interaction. It does not authorize unrelated work, external publishing, sending messages, merging, or bypassing host permissions. End with the concrete result, checks run, and any remaining blocker.
