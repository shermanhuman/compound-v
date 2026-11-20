# Preferred patterns

The reviewer checks every code change against these, at the level marked. **Required**: a violation is a must-fix, under the evidence rule (quote the line, state the precondition). **Recommended**: a violation is polish. Stack-specific forms live in the user's own rules; apply them where they exist. The list applies to code changes only, not to prose or instruction files.

Flag a pattern only where the change introduces or newly exposes the problem, and skip anything that doesn't apply (a one-off local script needs no idempotency key).

## Durability

| # | Pattern | Level | What a violation looks like |
|---|---|---|---|
| D1 | **Safe migrations.** Each migration works with the release already running: add before you remove (a release apart), set a lock timeout, build indexes concurrently, add constraints unvalidated then validate, never edit an applied migration | Required | A column dropped in the same change as the code that stops reading it; a plain index on a large table; an edited migration file that has already run |
| D2 | **A timeout on every external call**, shorter than its caller's deadline | Required | An HTTP, database or RPC call relying on a library default, or with none |
| D3 | **Stable idempotency keys** on outbound side effects (charges, messages, emails, CRM writes), built from durable state; where the vendor has none, record the external ID first and look it up before re-creating | Required | A key generated per attempt; a retried create with no key |
| D4 | **Jobs, consumers and scripts are safe to run twice**, including after stopping halfway | Required | A job that inserts or sends without checking what an earlier attempt did |
| D5 | **Resend after an unknown outcome only when replay is idempotent.** After a timeout that may have succeeded, replay only an operation that is idempotent, naturally or under the same still-valid idempotency key (the provider returns the first result); otherwise reconcile before acting again | Required | Resending a call with no idempotency protection after an ambiguous failure |
| D6 | **Webhooks: verify the raw body, store the receipt under a unique event ID and enqueue the work in one transaction, answer fast**, and never depend on delivery order | Required | Business logic or outbound calls inside the request; dedupe by read-then-insert; verifying re-encoded JSON |
| D7 | **No external call inside a database transaction.** Enqueue the effect as a job in the same transaction instead | Required | A send, HTTP call, process spawn or broadcast inside a transaction block |
| D8 | **Retry only what's retryable** (timeouts, connection errors, 408/429/5xx), with backoff and jitter, capped, in one layer; a 429 waits for `Retry-After` | Required | Retries stacked across layers; a fixed sleep loop; retrying non-retryable 4xx responses |
| D9 | **Uniqueness in the database**: a unique index (partial where needed), with the conflict handled | Required | An existence check followed by an insert |
| D10 | **Job uniqueness that fits**: the keys, period and states that define a duplicate are explicit, and jobs that must not collapse don't share a key | Recommended | A bare `unique: true`; one key shared by different kinds of work |
| D11 | **Guard concurrent read-modify-write**: atomic updates, a row lock inside a transaction, or optimistic locking; claim work with skip-locked; one lock order; re-check state after locking | Required | Read, compute, write back with nothing in between |
| D12 | **Fail loudly.** Every failure is returned, retried within a limit, or logged, counted and alerted; a job never reports success after a failure | Required | `rescue _ -> :ok`; a discarded error value; a catch-all that logs at debug |
| D13 | **Resumable, batched backfills**, outside the schema migration, sized by work, resumable from a cursor | Required | An unbatched update inside a migration; a backfill that restarts from the beginning |
| D14 | **Graceful shutdown**: stop taking work, drain requests, then cancel workers, within a budget shorter than the platform's grace period | Recommended | Cancelling workers before draining; no shutdown path |
| D15 | **Probes check the right thing**: liveness the process only, readiness the required dependencies | Recommended | A liveness check that queries the database or a vendor |
| D16 | **Bounded queues and fan-out**, each with a defined behaviour when full | Recommended | A task or goroutine spawned per request or per item with no limit |
| D17 | **Degrade instead of failing** when an optional dependency fails; only required dependencies affect readiness | Recommended | A page that errors because a side panel's vendor is down |
| D18 | **Validate at trust boundaries**, including generated config: parse into typed shapes, reject unknown or oversized input, cap request bodies | Required | Unbounded body reads; atoms or types built from input; unchecked casts of external JSON |
| D19 | **Fail fast on configuration**: required settings are checked at boot; a blank value isn't "configured" | Required | A missing secret discovered on the first request |
| D20 | **Structured logs with correlation IDs**, carried across services and into job metadata | Recommended | Data interpolated into log strings; a request ID dropped at a service boundary |
| D21 | **Rate limits that hold across nodes**, throttled at the source, honouring `Retry-After` | Recommended | Limiter state owned by a request process |
| D22 | **Kill switches for risky paths**: a flag that defaults off and can be turned off without a deploy | Recommended | A risky new path that can only be stopped by a rollback |
| D23 | **Money, time and constraints in the data**: integer minor units or decimals for money, UTC timestamps with time zone, half-open ranges, integrity constraints in the database | Required | Money as a float; naive timestamps for events; a rule enforced only in code |
| D24 | **Monotonic clocks for durations**; order by database sequences, not client timestamps | Recommended | Wall-clock arithmetic for timeouts; last-write-wins on a client `updated_at` |

Circuit breakers and sagas are not checked: behind a job queue, per-vendor queues and pausing them already do the breaker's work, and a single transaction beats a saga inside one database.

## Structure

| # | Rule | Level |
|---|---|---|
| S1 | **One place for each fact (DRY).** Duplicated knowledge (a rule, constant or schema in two places) is the finding, not similar-looking lines | Required |
| S2 | **The simplest design that meets the requirement (KISS).** A more complex design names the requirement that needs it | Required |
| S3 | **Nothing for requirements nobody stated (YAGNI).** No option without a caller; no abstraction with one implementation, except at a boundary S7 allows | Required |
| S4 | One responsibility per module, context or package; the web layer holds no business rules | Recommended |
| S5 | Talk only to direct collaborators: one context doesn't query another's tables; it calls its public functions | Recommended |
| S6 | High cohesion, low coupling: no dependency cycles between contexts or packages | Recommended |
| S7 | Abstract only at boundaries (external services, test doubles) | Recommended |
| S8 | Small interfaces defined by the code that uses them; implementations keep the whole contract, error shapes included | Recommended |
| S9 | A closed set until a second case is real; no hidden inheritance through macros or embedding | Recommended |

A structure finding marked required still needs the evidence rule: name the duplicated fact and both places, the requirement the extra complexity lacks, or the unused option, with the lines.
