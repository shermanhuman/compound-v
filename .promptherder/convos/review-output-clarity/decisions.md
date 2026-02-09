# Decisions: review-output-clarity

| #   | Idea                                               | Verdict  | Pros                                                                      | Cons                     | Rationale                                                  |
| --- | -------------------------------------------------- | -------- | ------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------- |
| 1   | Add check coverage table to output format          | accepted | Makes all 10 checks visible; LLMs comply better with explicit templates   | Adds ~12 lines to output | Research confirms explicit checklists improve compliance   |
| 2   | Strengthen "skip details" with imperative language | accepted | Current phrasing is advisory; binary test gives LLM a clear decision rule | None                     | Small change, high impact                                  |
| 3   | Add bad-example anti-pattern for re-detailing      | rejected | Anti-patterns are effective teaching tools                                | Adds bulk                | Positive rule is sufficient if clear                       |
| 4   | Move persistence before verdict in output format   | accepted | Eliminates double action menu structurally                                | None                     | Root cause: persistence after verdict → menu appears twice |
