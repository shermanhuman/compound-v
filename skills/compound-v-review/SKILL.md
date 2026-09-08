---
name: compound-v-review
description: Review a requested change for actionable defects; distinguish review-only work from already-authorized fixes.
---

# Review

Establish the repository, diff/base, and requested checks. A targeted review runs the requested check; other checks are unassessed, not "clean". A general review considers relevant checks from [the check reference](references/checks.md). Load that reference only for the review.

Read changed code in context and the accepted requirements. Use a plan if one belongs to this task; standalone reviews do not require one. Consult current official documentation for uncertain or version-sensitive claims. Concurrency is optional and follows `compound-v-parallel` and host authorization.

Report concrete findings in severity order: B1 blocker, M1 major, m1 minor, n1 nit. Include a location, triggering condition, impact, and a useful correction. Preserve uncertainty and distinguish verified defects from questions. Summarize actual coverage and relevant test results; do not add mandatory praise, empty tables, or findings merely to fill categories. Grugg may tighten wording but does not replace these IDs or remove evidence.

For review-only requests, report findings without modifying code. Offer a fix action only when there are findings needing new authorization. "FIX", "FIX ALL", or an ordinary request to fix is authorization; it does not require YOLO. During authorized implementation or an explicit review-and-fix request, fix relevant defects and verify them without asking again. Clarify ambiguous findings individually while continuing independent authorized fixes.

When maintaining task artifacts, use `compound-v-persist` and write a uniquely named `review-<scope>.md` once. Include assessment and evidence, not a conversational action menu. The calling workflow should not overwrite that report with a second summary. End the review phase when the task moves on.
