# Review: prompt-refactor

## Strengths

- Consistent blockquote prompts across all 3 workflows (plan, execute, review)
- Clean domain short names table in review skill — easy to scan, memorable
- YOLO cascade well-documented in compound-v.md — each level clearly defined
- Short-names-first rule is both in hard-rules.md AND compound-v.md — can't be missed
- Hard-rules.md check properly wired into correctness domain AND plan research phase AND execute context files

## Findings

⠴ **m1**: `compound-v.md:11` — Pipeline description said "approval gate" implying separate step. **Fixed:** Changed to "/execute approval".

⠠ **n1**: `execute.md:54-57` — Response option list items outside blockquote. Cosmetic only. Not fixed.

⠠ **n2**: Plan skill filesystem tree section is example content, not template. Working as intended.

## Verdict

Ready to merge? **Yes** — m1 was fixed. Nits are cosmetic, no action needed.

## Files modified

| File                                | Change                                                                                   |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| `rules/compound-v.md`               | + output formatting, severity indicators, decision prompts, short-names-first, YOLO mode |
| `skills/compound-v-plan/SKILL.md`   | + visual anchors, TDD sequencing, YAGNI/DRY checks, parallel research, hard-rules read   |
| `skills/compound-v-review/SKILL.md` | Full overhaul: 10 domains, domain targeting, findings-first, version-specific research   |
| `skills/compound-v-tdd/SKILL.md`    | + explicit parallel research directive                                                   |
| `skills/compound-v-debug/SKILL.md`  | + explicit parallel research directive                                                   |
| `workflows/plan.md`                 | /execute approval, DECLINE option, blockquote prompts                                    |
| `workflows/execute.md`              | Findings-first finish, YOLO mode, hard-rules context, blockquote prompts                 |
| `workflows/review.md`               | Domain targeting, YOLO mode support                                                      |
| `.promptherder/hard-rules.md`       | Blockquote prompts rule, short-names-first rule                                          |
