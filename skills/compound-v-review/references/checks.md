# Review check reference

Choose applicable checks from the requested scope. Findings need a concrete trigger, consequence, and location; do not invent defects to fill a checklist.

- `correctness`: compare with the requested behavior and accepted plan. Deferred ideas are not requirements. Trace changed branches and contracts.
- `edges`: empty/missing input, boundaries, resource lifecycle, partial failure, and concurrency. Recommend bounded retries only for retryable operations with safe idempotency.
- `security`: inspect relevant authorization, input handling, secret exposure, and dependency advisories. Use current primary sources when making security claims. Do not turn every review into an unrelated full audit.
- `perf`: look for demonstrated or credible regressions, unbounded work, N+1 queries, and missing limits on remote operations. Do not require pagination for ordinary local file reads or speculative caching.
- `tests`: run relevant required checks; assess whether tests assert meaningful behavior and handle important failure paths. Report unrun checks.
- `design`: assess existing conventions, clear responsibilities, and coupling. Do not impose a pattern solely because it is newer.
- `dry`: identify duplicated knowledge that would drift together. Extract only when a shared abstraction improves the code; no fixed occurrence count is decisive.
- `yagni`: distinguish public entry points and supported extension contracts from unused speculative code. Check callers before recommending removal.
- `logging`: retain actionable context without secrets. Handle errors at the right layer instead of requiring every layer to log the same error.
- `docs`: check user-facing behavior, migration notes, and misleading examples. Documentation changes should describe the delivered result.

Search for similar defects when a discovered issue gives a concrete reason to suspect them, keeping remediation within scope.
