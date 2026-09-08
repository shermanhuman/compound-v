---
activation: always
---

# Compound V

Use the Compound V workflows and skills below.

## Pipeline

1. `/plan` — autonomous planning with `/execute` approval
2. `/execute` — parallel-by-default execution with checkpointing
3. `/review` — severity-graded review pass
4. `/idea` — add to future tasks (lightweight, any time)
5. `/rule` — add a hard rule to the always-on prompt
6. `/stack` — scan project versions, compare to best practices, update `stack.md`

## Skills (auto-activated)

- `compound-v-plan` — autonomous planning methodology
- `compound-v-review` — severity-graded review with 10 parallel checks
- `compound-v-tdd` — tests-first discipline
- `compound-v-debug` — systematic debugging
- `compound-v-parallel` — parallel execution reasoning
- `compound-v-verify` — verification before completion
- `compound-v-persist` — resolves conversation slugs and paths
- `compound-v-execute` — callable execution, batch checkpoints, and final review
- `compound-v-pipeline` — carries authorization through plan, execute, and review

## Manual rules

- `browser.md` — browser-based UI testing (manual trigger)

## Output formatting

All workflows and skills must follow these formatting rules:

### Structure

- **H1** for titles, **H2** for sections, **H3** for subsections
- `---` dividers between major sections
- Tables for structured data (findings, decisions, comparisons)
- Ordered lists for sequential steps. Unordered lists when order doesn't matter.

- **Bold** for key terms and action verbs.
- `Inline code` for anything the user might copy: commands, paths, filenames, flags, slugs
- _Italic_ for caveats, assumptions, and metadata.
- Blockquotes (`>`) for prompting the user — questions, decisions, and action menus. Not for informational text.

### Severity indicators (braille dot patterns)

- `⠿` **Blocker** — wrong behavior, security issue, data loss, broken build
- `⠷` **Major** — likely bug, missing edge case, poor reliability
- `⠴` **Minor** — style, clarity, small maintainability issue
- `⠠` **Nit** — optional polish

Finding IDs are mandatory in reviews: `⠿ **B1**`, `⠷ **M2**`, `⠴ **m3**`, `⠠ **n1**`

### Decision prompts

- **After plan:** `> Run /execute <slug> to proceed, SHOW DECISIONS to audit, DECLINE to reject, or give feedback.`
- **After review findings:** `> FIX to fix ⠿⠷, FIX ALL to fix everything, SKIP to move on, or give feedback.`
- **Deferred ideas:** `> Add these to future-tasks.md? yes / no`

Task slugs go on the next line in italics: _Task: `<slug>`_

### Short names first

Lead with the short name in backticks, then its description: `edges` — boundary conditions and error handling; `perf` — performance pitfalls; `YOLO` — full autonomous mode.

### YOLO mode

`YOLO` (all caps) cascades through the pipeline:

- `/review YOLO` — Auto-fix ALL findings (⠿→⠠) without asking. Output summary.
- `/execute YOLO` — Execute, auto-review, auto-fix all findings. No interaction.
- `/plan YOLO` — Full pipeline: plan → execute → review → fix. Zero interaction.

Always summarize what was built, found, and fixed.

## Native host execution

Promptherder 1.x installs native `workflow-<name>` entry points: `$workflow-plan` in Codex and `/workflow-plan` in Claude Code, likewise execute/review/idea/rule/stack. A configured prefix precedes `workflow-`. Short `/plan` names above describe the workflow vocabulary, not guaranteed installed aliases.

Keep the formats, finding IDs, and action vocabulary above. Grugg can shorten prose without removing required sections, evidence, or technical qualifications. Full-pipeline authorization invokes `compound-v-pipeline` and its callable `compound-v-execute` helper; do not automatically call a manual-only entry point. Plan-only instructions expire when execution is authorized. Existing implementation/fix authorization does not require another generic approval menu. YOLO fixes all in-scope findings, including minor/nit findings, but does not authorize unrelated work, merging, publication, or bypassing host permissions.
