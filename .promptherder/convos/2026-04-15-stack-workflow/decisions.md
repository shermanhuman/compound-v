# Decisions: /stack Workflow

| #   | Idea | Verdict  | Pros | Cons | Rationale |
| --- | ---- | -------- | ---- | ---- | --------- |
| 1   | New `/stack` workflow in compound-v | accepted | Consistent with `/idea`, `/rule` pattern. Lightweight, one-file. | Adds to workflow count | This IS the feature. |
| 2   | Scan lockfiles for actual versions (mix.exs, package.json, go.mod, Gemfile, pyproject.toml, etc.) | accepted | Auto-discovers versions without human memory | May miss some ecosystems | Cover the top 8-10 package managers. Add note for manual entries. |
| 3   | Web search for latest stable + recommended versions | accepted | Lets user see if they're behind | Web search can be slow/noisy | Scoped to discovered technologies. Don't search for everything. |
| 4   | Output comparison table: actual vs stack.md vs recommended | accepted | Actionable at a glance | Requires all three data sources | This is the core value proposition of the command. |
| 5   | Prompt user to supply changes, then write stack.md | accepted | User stays in control | Requires one more turn | Matches `/rule` pattern: present, confirm, write. |
| 6   | Location: `.agent/rules/stack.md` | accepted | Matches existing pattern from compound-v README | Could also be `.github/rules/` | README already documents `.agent/rules/stack.md` as canonical. |
| 7   | Make plan skill read stack.md at the very start of Phase 2 | rejected | Superseded by decision 11 | — | This was wrong — plan skill reads stack.md in the *same parallel batch* as web searches. Decision 11 fixes this properly by splitting into Phase 2a (sequential read) → Phase 2b (parallel research). |
| 8   | Add `/stack` to the compound-v.md rule file's pipeline list | accepted | Users discover commands from the rule file | Minor edit | Necessary for discoverability. |
| 9   | Update README.md to document `/stack` | accepted | Users need to know it exists | Minor edit | Standard for new workflows. |
| 10  | Auto-detect ecosystem from directory contents, not just presence of lockfiles | accepted | Works even if lockfiles aren't checked in | Slightly more complex scanning | Check for both lockfiles AND source indicators (e.g. `.ex` files → Elixir). |
| 11  | Move stack.md read to Phase 2a in plan skill (before parallel research) | accepted | Web searches can scope to exact versions. Currently both happen in same parallel batch — agent may fire generic searches before file reads complete. | Adds one sequential step | Small latency cost (~200ms for local read) is worth version-scoped searches. |
| 12  | Nudge user to run `/stack` when no stack.md found during planning | accepted | Discoverability — user learns the command exists. Non-blocking. | Could be annoying if repeated | One-line suggestion, not a gate. Agent continues planning regardless. |
| 13  | Purge `structure.md` references from plan skill | accepted | Dead code — no one has ever created one. Agent scans the codebase anyway. | Loses a theoretical feature | YAGNI. If needed later, add a `/structure` command (future task). |
