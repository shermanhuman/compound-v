---
name: testing
description: Decide what is worth testing and at which layer — proportionate coverage, cheapest sufficient layer, small fixtures, runtime as a cost. Use when writing or changing tests, planning a change's proof, or reviewing test coverage.
---

# What's worth testing

- **Distinct failure.** Name what a test would catch, and check existing coverage first. Reuse or strengthen an existing test when it already exercises that contract. When you claim existing coverage, name its file and test and say which failure it detects or which behaviour it preserves during a refactor; if you can't, treat it as a gap. A trivial edit doesn't need a new test just to record that code changed.
- **Cheapest sufficient layer.** Rule combinations go in pure or domain tests; database semantics and races in integration tests; permissions, wiring and presentation contracts at their boundaries. Keep representative end-to-end checks; don't repeat the whole rule matrix through every layer without a distinct risk.
- **Proportionate fixtures.** Create only the data the assertion needs. Full catalogs, seeds and backfills need an integration purpose. Keep real positive and negative examples, so a smaller fixture doesn't make an assertion pass vacuously.
- **Observable behaviour.** Avoid assertions that mirror the implementation or match source wording, unless that structure is itself a required contract. Where safe, share repeated setup while keeping distinct assertions and state isolation.
- **Runtime is maintenance cost.** Measure expensive cases and substantial additions. Use the repository's own commands and time budgets; don't invent universal timeouts, and don't silently drop coverage to meet a speed target. Keep required security, isolation, equivalent behaviour across supported implementations, and recovery contracts.
- **No test bureaucracy.** No test-count or coverage-percentage targets and no per-test justification documents by default. Explain material coverage trade-offs and costly additions in the plan or the review.

When you change code, say which coverage you reused, added or changed (file and test names), how to run it, and what it proves. A fast subset during iteration is fine; it doesn't prove the feature is covered — run what the repository requires before calling the work done.
