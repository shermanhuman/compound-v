---
name: compound-v-execute
description: Carry out an authorized implementation or approved plan, verify the result, and fix relevant defects.
---

# Execution

Apply only while implementing the current task. Resolve the active plan with `compound-v-persist` if the task uses one. An explicit request to execute a named plan authorizes its implementation. A direct implementation request does not require a preexisting plan file or a special command.

For a named plan, verify it exists and matches the requested task before changing its status to approved. Read relevant project rules and actual version pins. Use `.promptherder/stack.md` as context; do not edit generated host files.

Group independent reads and work with `compound-v-parallel`. Use `compound-v-tdd` where tests add meaningful protection. Verify each meaningful batch and record evidence in the active task's `execution.md` when maintaining task artifacts. On a failure, diagnose and fix it with `compound-v-debug` before dependent work continues. If the plan needs a correction within existing scope, update and continue; ask only for material new scope or missing authorization.

Review the result using `compound-v-review`. Since implementation was requested, fix relevant defects without another generic FIX confirmation. Defer optional unrelated cleanup. Run the required final checks using `compound-v-verify`; summarize changes, verification, and unresolved limitations. Provide manual smoke-test steps only for checks that need user involvement. Never imply a suggested test was run.
