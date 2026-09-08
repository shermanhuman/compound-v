---
name: compound-v-execute
description: Execute an authorized plan in dependency-aware batches, checkpoint verification, and finish with review and smoke-test instructions.
---

# Execute Plan

Invoke skills as needed during execution: `compound-v-tdd`, `compound-v-debug`, `compound-v-parallel`, `compound-v-verify`.

**Announce at start:** "Executing plan: `<slug>`. [1-2 line summary of the plan]."

## Workflow-specific protocol

### Slug resolution

Invoke the `compound-v-persist` skill to resolve the target `<slug>` folder.

- If the user provided a slug (e.g. `/execute fix-this`), pass it to the skill.
- A named plan must already exist in the resolved folder. For a direct implementation request, first record the scoped plan using `compound-v-plan`, then continue under the existing authorization.

### Preconditions (do not skip)

1. The plan must exist at `.promptherder/convos/<slug>/plan.md`.
2. Update status to `approved` in plan.md when execution is authorized by the workflow invocation or the user’s implementation request.

If an explicitly named plan does not exist, resolve that mismatch before execution. Do not require a separate user command to plan an already-authorized implementation task.

### Context files (read before starting)

- `.promptherder/convos/<slug>/plan.md` — the approved plan.
- `.promptherder/hard-rules.md` — project-level rules that must always be followed.

### Load stack context (sequential — before execution)

Read `.promptherder/stack.md` first, then legacy `.agents/rules/stack.md` or `.agent/rules/stack.md`. Compare against actual pins. These versions scope all web searches during execution.

If none exists, print: _"No `stack.md` found. Run `/stack` to pin your versions — this improves web search accuracy."_ Then continue.

### Execution loop

1. Analyze step dependencies (use `compound-v-parallel`). Group independent steps into batches.
2. **Before each batch**, use the available web-search tool for latest docs on libraries/APIs about to be used. Scope to `stack.md` versions.
3. Run independent steps concurrently using supported tools. Coordinate shared files/state and use subagents only when authorized.
4. After each batch: run verification, append results to `.promptherder/convos/<slug>/execution.md`.
5. If verification fails: stop, switch to `compound-v-debug`. Do not continue until fixed.
6. If the plan is wrong, correct it before dependent work. Ask only when a material change exceeds the existing scope or authorization.

### Finish (required)

**Normal mode:**

1. Run `compound-v-review`. Keep its required output format. Implementation already authorizes fixing relevant defects; do not insert a generic FIX approval stop. Do not duplicate its report.
2. After fixes (if any), provide a manual smoke test:
   - List exact commands to test the happy path end-to-end
   - List edge cases worth testing manually
   - Show expected output for each command
3. Let the review skill write the collision-safe review report once; append execution results to `execution.md`.
4. Confirm artifacts exist by listing `.promptherder/convos/<slug>/`.

**`YOLO` mode:**

1. Run `compound-v-review` in YOLO mode. It handles auto-fixing.
2. Output summary: what was built, what was found, what was fixed.
3. Let the review skill write the collision-safe review report once; append execution results to `execution.md`.
4. Confirm artifacts.

Stop after completing the finish step.
