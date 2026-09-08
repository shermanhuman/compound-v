---
name: compound-v-debug
description: Diagnose failing tests, errors, and incorrect behavior using evidence before changing the implementation.
---

# Debugging

Capture the observed failure, expected behavior, affected inputs, and environment. Reproduce safely, then inspect the relevant path and form a small set of evidence-based hypotheses. Use logs, tracing, focused tests, or a minimal reproduction to distinguish them.

Check version-matched documentation or known issues when the behavior is uncertain or external. Batch independent investigation where supported. Do not force web research or a fixed number of hypotheses for an obvious local defect.

Fix the root cause within the requested scope. Add meaningful regression protection where practical and rerun the failing case plus relevant required checks. Remove temporary instrumentation introduced by this investigation; preserve intentional diagnostics. Report the cause, correction, and verification without claiming an unrun check passed.
