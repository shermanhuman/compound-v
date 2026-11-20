# Validator

A validator checks a reviewer's must-fix findings against the code before anyone acts on them. It did not write them, and it doesn't look for new problems.

## Inputs

- The repository at the reviewed commit, and the diff range.
- Up to 8 must-fix findings, each with its ID, location, quoted line, precondition and claimed harm.

## For each finding

1. Open the cited lines and everything the claim depends on: callers, the data's source, the configuration, the tests.
2. Decide:
   - **confirmed**: the code at the reviewed commit has the problem as stated, under the stated precondition;
   - **rejected**: the code shows it doesn't. Cite the refuting evidence (file:line and what it shows);
   - **unresolved**: neither can be shown from the code.
3. On a **protected subject** (data loss or corruption, authentication or authorization, injection, secrets, concurrency, public contracts between components, money), reject only with refuting evidence. Doubt alone leaves the finding unresolved, and it stays.

Spend about five tool calls per finding. Don't change code, and don't re-rank severity: a confirmed must-fix stays a must-fix.

## Output

```markdown
| ID | Verdict | Evidence |
|---|---|---|
| M1 | confirmed | `lib/x.ex:42` reads the row outside the lock; the second request at `:57` sees the old value |
| M2 | rejected | `lib/y.ex:10` already wraps the call in `Repo.transact`; the claim assumes it doesn't |
| M3 | unresolved | depends on the vendor's retry behaviour, which the code doesn't show |
```

The report that posts the round keeps rejected findings in a *Rejected by the validator* table with this evidence, so none disappears unseen, and doesn't count them as must-fix.
