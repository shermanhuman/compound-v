---
name: compound-v-tdd
description: Apply tests-first discipline and choose valuable, proportionate coverage when implementing features, fixing bugs, refactoring, or reviewing tests.
---

# TDD Skill

**Announce at start:** "Using TDD: checking coverage for [behavior]."

## When to use this skill

- new features that can be unit tested
- bug fixes (add or strengthen regression coverage when it closes a gap)
- refactors (confirm existing coverage protects the behavior before changing it)
- test reviews (assess the policy below; review alone does not authorize edits)

## Test value and cost

- **Distinct failure:** identify what a test would catch and check existing coverage first. Reuse or strengthen an existing test when it already exercises that contract. When claiming existing coverage, name its file and test and explain which failure it detects or which behavior it preserves during a refactor. If you cannot identify that evidence, treat the coverage as a gap. Trivial edits do not need a new test merely to record that code changed.
- **Cheapest sufficient layer:** put rule combinations in pure/domain tests, database semantics and races in integration tests, and permissions, wiring and presentation contracts at their relevant boundaries. Keep representative end-to-end checks; do not repeat the whole rule matrix through every layer without a distinct risk.
- **Proportionate fixtures:** create only data the assertion needs. Full catalogs, seeds and backfills need an integration purpose. Preserve real positive and negative examples so smaller fixtures do not make assertions vacuously pass.
- **Observable behavior:** avoid assertions that mirror implementation or match source wording unless the structure itself is a required contract. Where safe, consolidate repeated setup while preserving distinct assertions and state isolation.
- **Runtime is maintenance cost:** measure expensive cases and substantial additions. Use repository-specific commands and budgets; do not invent universal timeouts or silently exclude coverage to meet a speed target. Preserve required security, isolation, equivalent behavior across supported implementations, and recovery contracts.
- **No test bureaucracy:** no new test-count or coverage-percentage target, or per-test justification document, by default. Explain material coverage tradeoffs and costly additions in the normal plan or review.

## Research

Before writing tests, do research **in parallel** (invoke multiple tool calls in the same response):

- Search the web for the project's testing framework best practices and latest patterns (scope to `stack.md` versions).
- Search the web for assertion styles and testing utilities available in the framework.

## Rules

- Prefer **red -> green -> refactor**.
- If tests are hard, still add **verification**: minimal repro script, integration test, or clear manual steps.
- Keep tests focused: one behavior per test where possible.
- Name tests by behavior, not implementation details.

## Process

1. Define the behavior change (what should be true after).
2. Check whether an existing test captures it. Add or adjust coverage for a real gap (make the regression fail first if practical).
3. Implement the minimal change to pass.
4. Refactor if needed (keep passing).
5. Run fast and affected tests during iteration, plus relevant linters **in parallel** where independent. A fast subset does not prove the edited feature is covered. Before final completion or PR submission, follow the full-validation requirements in `compound-v-verify` and the repository.

## Output requirements

When you change code, include:

- what coverage you reused, added or changed, with file and test names
- how to run them
- what they prove

## Bite-sized granularity

When a new test is needed, keep the feedback steps small:

1. Write the failing test — step
2. Run it to confirm it fails — step
3. Implement the minimal code to make it pass — step
4. Run tests to confirm they pass — step
5. Commit when the task includes committing — a separate step, not required after every test.

Don't combine these. Each step is independently verifiable.

Use existing framework conventions. Follow `compound-v-verify` for validation scope, including documentation-only and other low-impact changes.
