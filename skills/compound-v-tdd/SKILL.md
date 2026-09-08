---
name: compound-v-tdd
description: Use regression tests and tests-first development for behavior changes where automated tests provide meaningful protection.
---

# Tests and implementation

Use existing tests and project conventions. For a reproducible bug or new behavior, prefer a focused failing test, the smallest correct implementation, and refactoring with tests passing. Verify that the test fails for the intended reason.

Test observable outcomes, especially important error paths. Do not add tests that only match prose, duplicate implementation details, or create more maintenance than protection for a reversible low-impact edit. Use a deterministic example, existing checker, or direct inspection when that is more appropriate.

Run relevant tests and required repository checks. Reuse successful verification unless subsequent changes or new evidence invalidates it. Do not require a commit per test or invent a global testing style. State what was tested and what remains unverified.
