# Compound V

A Promptherder herd for scoped planning, execution, review, and persistent task context. Version 1.0.0 aligns with Promptherder 1.x native skill compilation.

## Install

```bash
promptherder install codex claude
promptherder pull compound-v
promptherder plan
promptherder
```

Use the feature build of Promptherder 1.0.0 until that release is published. Existing locked installs must review herd updates with `plan --update-lock` and apply with `--update-lock`.

## Entry points

| Task | Codex | Claude Code |
|---|---|---|
| Plan | `$workflow-plan` | `/workflow-plan` |
| Execute | `$workflow-execute` | `/workflow-execute` |
| Review | `$workflow-review` | `/workflow-review` |
| Save an idea | `$workflow-idea` | `/workflow-idea` |
| Add a rule | `$workflow-rule` | `/workflow-rule` |
| Record versions | `$workflow-stack` | `/workflow-stack` |

Pass the task or slug after the invocation. A configured command prefix precedes `workflow-`. Legacy `/plan` and similar short aliases are not installed by the native compiler.

Plan-only requests stop at the plan. A later implementation request continues the same task. Full implementation or YOLO requests use callable helpers through planning, execution, review, and fixes without artificial approval stops. Authorization stays limited to the requested task and host permissions.

Conversation artifacts live under `.promptherder/convos/<date-topic>/`. Project rules live in `.promptherder/hard-rules.md`; observed versions in `.promptherder/stack.md`; deferred ideas in `.promptherder/future-tasks.md`. Source rules require synchronization and host reload to appear in future instruction contexts. Generated host files are not authoring locations.

Grugg controls optional conversation style; Compound V retains review finding IDs and evidence. Oh supplies environment and release guidance. Neither a style skill nor a version bump expands the task into publishing, merging, or deployment.

## Validation

Compiler fixtures validate dependency closure, native discovery, and resource copying. File validation cannot establish actual model adherence; test plan-only, approved execution, review-and-fix, and phase transitions in the installed host before making behavioral claims.

## Credits

Based on [obra/superpowers](https://github.com/obra/superpowers), with the [Antigravity adaptation](https://github.com/anthonylee991/gemini-superpowers-antigravity).
