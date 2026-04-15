---
description: Scan project for versions, compare to stack.md and latest recommended, update interactively. Use any time.
---

// turbo-all

# Stack

Discover project versions, compare them to `stack.md` and current best practices, and update `.agent/rules/stack.md` interactively.

**What this does:** Creates or updates `stack.md` — the single source of truth for pinned versions across all compound-v workflows. Every `/plan`, `/execute`, and `/review` scopes web searches to these versions.

## Steps

1. **Read** `.agent/rules/stack.md` if it exists. Note its contents for the comparison table.

2. **Scan** the project for version indicators. Check for these files and extract version data:

   | File | Technologies |
   |------|-------------|
   | `mix.exs` / `mix.lock` | Elixir, Erlang/OTP, Hex deps |
   | `package.json` / `package-lock.json` | Node.js, npm/yarn deps |
   | `go.mod` | Go, module deps |
   | `Gemfile` / `Gemfile.lock` | Ruby, gem deps |
   | `pyproject.toml` / `requirements.txt` / `Pipfile` | Python, pip deps |
   | `Cargo.toml` | Rust, crate deps |
   | `pom.xml` / `build.gradle` | Java, Maven/Gradle deps |
   | `docker-compose.yml` / `Dockerfile` | Infrastructure (PostgreSQL, Redis, etc.) |
   | `.tool-versions` / `mise.toml` | mise/asdf version manager pins |

   Also check for source-file indicators if no lockfile exists (e.g. `.ex` files → Elixir, `.go` files → Go). List any technologies detected that don't match the table above.

   Focus on **primary technologies** — the language, framework, database, and key infrastructure. Don't list every transitive npm dependency.

3. **Search the web** for each discovered technology (in parallel):
   - Latest stable release version
   - Recommended production version (sometimes differs from bleeding edge)
   - Any notable version-specific advisories or migration considerations

4. **Output** a comparison table:

   ```
   | Technology | Actual (code) | stack.md | Latest Stable | Recommended | Notes |
   |------------|--------------|----------|---------------|-------------|-------|
   | Elixir     | 1.16.2       | 1.16     | 1.17.1        | 1.17        | Major available |
   | Phoenix    | 1.7.14       | —        | 1.7.14        | 1.7         | Current |
   | PostgreSQL | 16           | 16       | 17.2          | 16 or 17    | LTS is fine |
   ```

   Mark rows where actual version differs from stack.md with ⚠️.
   Mark rows where actual version is more than one major behind latest with 🔴.

5. **Prompt** the user:

   > Review the table above. You can:
   > - **ACCEPT** — write stack.md with the Actual versions as-is
   > - **UPDATE** — tell me which rows to change (e.g. "bump Elixir to 1.17, add Redis 7")
   > - **SKIP** — don't write anything

6. **Write** `.agent/rules/stack.md` with the final selections. Use this format:

   ```markdown
   # Stack

   - Elixir 1.17
   - Phoenix 1.7
   - PostgreSQL 16
   - Node 22 (for frontend tooling)
   ```

   Preserve any manual entries from the existing `stack.md` that weren't auto-detected. Keep it a flat bullet list — no categories, no explanations. Just technology + version.

7. **Confirm:** "Stack updated. All `/plan`, `/execute`, and `/review` commands will now scope to these versions."

That's it. No planning, no approval workflow. Scan, compare, prompt, write.
