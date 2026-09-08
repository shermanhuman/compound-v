---
activation: always
---
# Compound V

Use the methodology in proportion to the task. User instructions and existing authorization determine scope; a skill does not create a new approval requirement or override host policy.

- Planning: `compound-v-plan`. An explicit plan-only request stops after presenting the plan. A request to implement includes permission to plan internally and continue.
- Execution: `compound-v-execute`, with debugging, testing, and verification helpers as needed.
- Review: `compound-v-review`. Report findings for review-only requests; fix them when the user has already requested fixes or implementation.
- Full pipeline: `compound-v-pipeline`. `YOLO` requests autonomous progress within the stated task, not unrelated changes, merging, deployment, publishing, or bypassing tool permissions.
- Persistent task artifacts: `compound-v-persist`; use the active task, not an unrelated recent folder.

Promptherder 1.x exports workflow entry points as `workflow-plan`, `workflow-execute`, `workflow-review`, `workflow-idea`, `workflow-rule`, and `workflow-stack`. In Codex invoke `$workflow-plan`; in Claude Code invoke `/workflow-plan`. Legacy `/plan` and similar names are shorthand in older discussions, not guaranteed installed aliases. If configured, the command prefix precedes `workflow-`.

Keep ordinary replies concise and follow the user's requested format. Use tables only when comparison helps. For substantive reviews use stable finding IDs: B1 blocker, M1 major, m1 minor, n1 nit. Optional braille severity symbols may accompany readable labels. Grugg may shorten commentary but must preserve evidence, uncertainty, finding IDs, and required artifact formats. Use named helpers when installed; if selection omits a helper, follow the applicable procedure locally without inventing unavailable tools. Do not load every skill for an unrelated request.
