---
name: compound-v-verify
description: Verify task outcomes and report accurate evidence before declaring implementation complete.
---

# Completion verification

Compare the result with the current request and accepted scope. Run the checks required by the repository and checks proportionate to the changed behavior. Use focused tests during iteration; run a full suite when required or justified by impact, not after every small step.

Inspect the diff for accidental changes, new warnings, temporary debug code, and missing migration or usage documentation. Do not remove unrelated TODOs, change unrelated warnings, or add cleanup outside scope.

Do not rerun unchanged successful checks without a reason. If a check cannot run because of missing tools, credentials, or an external service, identify it and report the limit. Never equate generated files, a successful build, or a suggested command with live host/model behavior.

Summarize what changed, checks actually executed and their results, and any remaining limitation. Scope the completion claim to what the evidence supports.
