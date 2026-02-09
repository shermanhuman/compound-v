# Review: compound-v v0.8.0

## Strengths

1. **Excellent content density** — Every file is tight and imperative. No fluff. Skills like `compound-v-review` pack detailed, actionable criteria into each of the 10 checks without becoming bloated.
2. **Consistent structure** — All skills follow the same pattern: YAML frontmatter → title → "when to use" → instructions → output format. Every workflow has the same slug resolution → protocol → persistence structure.
3. **DRY workflow pattern** — Workflows are thin links that delegate to skills (`compound-v-plan`, `compound-v-review`) and add only workflow-specific protocol (slug resolution, persistence, response handling). This avoids duplicating skill logic in workflows.
4. **Severity indicators** — The braille dot patterns (`⠿⠷⠴⠠`) are a clever, accessible, no-color-needed severity encoding. Well-documented in the rules file.
5. **YOLO cascade** — The escalation from `/review YOLO` → `/execute YOLO` → `/plan YOLO` is well-defined and consistent across all three workflow files.

---

## Findings

| ID  | Sev | Location                      | Issue                                                                                               |
| --- | --- | ----------------------------- | --------------------------------------------------------------------------------------------------- |
| M1  | ⠷   | `README.md:28-44`             | Structure tree is outdated — missing `idea.md`, `rule.md` in workflows and `skills/README.md`       |
| M2  | ⠷   | `rules/browser.md`            | Placeholder content — single sentence provides no actual guidance                                   |
| M3  | ⠷   | `hard-rules.md:9-10`          | Hard rules duplicate text already in `rules/compound-v.md:54,60-67` verbatim                        |
| m1  | ⠴   | `skills/compound-v-parallel/` | Has both `SKILL.md` and `ANTIGRAVITY.md` that are near-duplicates                                   |
| m2  | ⠴   | `compound-v-plan/SKILL.md:36` | References `.agent/rules/stack.md` but review skill references just `stack.md` — inconsistent paths |
| m3  | ⠴   | `workflows/review.md`         | Missing `// turbo-all` annotation — present in all other workflows                                  |
| m4  | ⠴   | `rules/compound-v.md:28`      | `@browser.md` prefix convention undocumented                                                        |
| n1  | ⠠   | `herd.json`                   | Missing optional metadata fields (description, author, repository)                                  |
| n2  | ⠠   | `skills/README.md:30`         | References `internal/app/copilot.go` from the promptherder repo — confusing in context              |
| n3  | ⠠   | `workflows/execute.md:5`      | `// turbo-all` position convention undocumented                                                     |

---

### Detail

⠷ **M1**: `README.md:28-44` — Structure tree shows only 3 workflows but the repo has 5 (+ `idea.md`, `rule.md`). The `skills/` tree omits `README.md`.
Fix: Update the tree to reflect the actual filesystem.

⠷ **M2**: `rules/browser.md` — Single sentence "Use `browser_subagent` to test." provides no guidance on when, how, or what to verify with browser testing.
Fix: Flesh out with real browser testing guidance or remove and drop the reference from `compound-v.md:28`.

⠷ **M3**: `hard-rules.md:9-10` — Both rules (blockquote decision points, short-names-first) are already stated in `rules/compound-v.md` which has `trigger: always_on`.
Fix: Remove duplicated entries from `hard-rules.md`.

⠴ **m1**: `ANTIGRAVITY.md` adds an "Execution pattern" section not in `SKILL.md`, but the rest is copy-pasted. Creates maintenance divergence.
Fix: Merge the unique content into `SKILL.md` and delete `ANTIGRAVITY.md`, or document why a separate variant is needed.

⠴ **m2**: Path inconsistency — plan skill says `.agent/rules/stack.md`, review skill says just `stack.md`.
Fix: Standardize on the full relative path everywhere.

---

## Assessment

The methodology is tight and well-structured. Three majors are content accuracy issues (outdated tree, placeholder rule, duplicated hard rules), not design flaws. Minors are consistency papercuts. No blockers.
