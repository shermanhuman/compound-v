---
name: compound-v-persist
description: Resolve the active repository and task directory for Compound V plan, execution, and review artifacts.
---

# Task persistence

Resolve the repository from the current task, not the methodology installation. Ask only if multiple repositories remain plausible and the write depends on the answer.

1. Reuse the task directory already named in the conversation or plan, even across dates.
2. For an explicit slug, look for an exact directory first; then a unique dated suffix match. Multiple matches require clarification. Reject path separators, `..`, and paths outside `.promptherder/convos/`.
3. For a new task, create `YYYY-MM-DD-kebab-case-topic` using the current local date. Add a suffix if that name already belongs to another task.
4. With no established task, inspect candidate plans for a match to the requested goal. Modification time alone is not a safe selector. A standalone review can create a fresh task directory without requiring a plan.

Store `plan.md`, `decisions.md`, and `execution.md` in that directory as needed. Update the current plan instead of creating a new task on feedback. Name reviews `review-<scope>.md`; append a numeric suffix when that file exists unless updating it was requested. Return the resolved absolute path. Do not create conversation directories merely to edit `hard-rules.md`, `stack.md`, or `future-tasks.md`.
