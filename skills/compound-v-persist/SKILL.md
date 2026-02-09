---
name: compound-v-persist
description: Resolves target repository and storage location for conversation artifacts. Guarantees organized, time-sorted history.
---

# Persist

Use this skill BEFORE writing any artifact to `.promptherder/`.

## 0. Resolve Target Repository

When multiple repositories are open in the workspace, all `.promptherder/` paths target the **repository the user is working in**, not the methodology source repo. Infer the target from the user's active document or recent conversation context. If the active document is outside all repositories, use recent conversation context (which files were read/written). If still ambiguous, ask which repository before writing.

## 1. Determine the Slug

The "slug" is the folder name in `.promptherder/convos/`. It MUST follow the format:  
`YYYY-MM-DD-kebab-case-topic`

**Logic flow:**

1. **Explicit Override:** Did the user provide a specific slug? -> Use it. If the slug does not start with `YYYY-MM-DD-`, prepend today's date.
2. **New Topic Signal:**
   - Writing `plan.md`?
   - Writing `ideas.md` (brainstorming)?
     -> **CREATE NEW**: Generate a short, descriptive kebab-case slug based on the goal.
3. **Continuation Signal:**
   - Writing `review-*.md`?
   - Writing `debug.md`?
   - Writing `task.md`?
     -> **REUSE LATEST**: Find the most recently modified folder in `.promptherder/convos/`.
     - _Exception:_ If no folders exist, treat as New Topic.
     - _Exception:_ If the latest folder has no `plan.md`, treat as New Topic.

## 2. Check & Create Directory

1. Construct path: `.promptherder/convos/<YYYY-MM-DD>-<slug>/`
2. Ensure the directory exists.
   - If creating new, use the **Current Local Time** for the date prefix.
   - If reusing, use the existing folder name (even if date differs).

## 3. Return Path

Return the full absolute path for the file to be written (e.g., `.../2024-01-01-fix-login/plan.md`).
