---
description: Plan a requested task; stop for plan-only requests or follow an explicitly authorized full pipeline.
---

# Plan

For explicit plan-only work, use `compound-v-plan` and stop after presenting the plan. Explain how to continue with the native execute entry point or an ordinary request to implement; do not require an exact command string. Feedback updates the same plan. SHOW DECISIONS displays concise recorded decision rationales. DECLINE marks the plan declined.

If the user explicitly requests the full pipeline (including `/plan YOLO` as legacy shorthand), use `compound-v-pipeline` instead. Do not apply plan-only stopping rules after that authorized transition.
