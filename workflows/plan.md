---
description: Plan a requested task; stop for plan-only requests or follow an explicitly authorized full pipeline.
---

# Plan

For explicit plan-only work, use `compound-v-plan` and stop after presenting the plan. Explain how to continue with the native execute entry point or an ordinary request to implement; do not require an exact command string. Feedback updates the same plan. SHOW DECISIONS displays concise recorded decision rationales. DECLINE marks the plan declined.

If the user explicitly requests the full pipeline (including `/plan YOLO` as legacy shorthand), use `compound-v-pipeline` instead. Do not apply plan-only stopping rules after that authorized transition.

## Required artifacts and response

Resolve the active task with `compound-v-persist`. Write `plan.md` and `decisions.md` in `.promptherder/convos/<slug>/`, using the planning skill’s full template. Feedback edits those same artifacts. For plan-only work, finish with one continuation menu:

> Run the native execute workflow with `<slug>` or ask me to implement; SHOW DECISIONS to audit, DECLINE to reject, or give feedback.

_Task: `<slug>`_

Offer to save worthwhile deferred ideas to `future-tasks.md`; append only after the user requests or confirms that persistence. Do not present a continuation approval menu during an already-authorized full pipeline.
