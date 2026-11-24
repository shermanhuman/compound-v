# Rough-edge kinds

A rough edge is a moment where the workflow cost the user more than it should have. Log one only where the user's rules name a home for the log; with no home, list them in your final summary. One entry each, first line exactly:

`rough-edge: <skill or rule> · <kind> · <link to the plan, PR, issue or session>`

then a line or two on what was missing or went wrong. Log it when it happens, not at the end.

Kinds:
- `more-discussion`: a decision packet didn't give the user enough to decide.
- `foreseeable-follow-up`: a follow-up packet asked something the first one could have.
- `override-knowable`: the user overrode a recommendation for a reason research could have found.
- `correction`: the user corrected you.
- `manual-step`: the user did by hand what a skill or rule should have covered.
- `missed-trigger`: a skill didn't run when it should have, or ran when it shouldn't.
- `escape`: a problem reached staging, a release or production that a review or check should have caught.
- `stuck`: work stopped after failed rounds.
- `other`.

Steps the rules reserve for the user (merging, signing in, guarded production actions) aren't rough edges.
