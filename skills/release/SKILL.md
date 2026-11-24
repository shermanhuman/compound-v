---
name: release
description: Prepares a version bump from the repository's actual version source (plugin.json, mix.exs, Cargo.toml, go.mod, VERSION, tags) and publishes a release only when asked. Use when bumping a version, preparing a PR's version change, or when the user asks to tag, release or publish.
---

# Version and release

A **bump** changes the version and the docs that quote it; it doesn't publish. A **release** follows the repository's own release mechanism for that version. Run tools the way the user's rules say.

## Find the version source

Look at plugin manifests (`.claude-plugin/plugin.json`, and each plugin's in a multi-plugin repository), `VERSION`, `mix.exs`, `Cargo.toml`, package metadata, build scripts, tags and `.github/workflows/`. Several files describing one product is normal; ask only when there are genuinely separate products and the target is unclear.

- **Plugins:** `version` in each changed plugin's manifest. Installed copies update only when it changes, and a version check usually requires it to be strictly greater than the base's.
- **Elixir:** the application version in `mix.exs` or the source it reads.
- **Rust:** `[package]` version, or `[workspace.package]` when members inherit it; check each affected member. Update internal path-dependency requirements first, then refresh `Cargo.lock` and commit it too. `rust-version` is the toolchain floor, not the product version.
- **Go:** `go.mod`'s `go` line isn't the product version. Use `VERSION` when there is one; with tag-only versioning, record the intended version in the PR instead of tagging.

Use the requested level; otherwise patch for fixes and docs, minor for compatible features, major for breaking changes, subject to the project's pre-1.0 policy. With no version source at all, don't bump, and say so. Compare with the PR's base so one PR carries one bump, and don't reset a larger intentional bump.

## Prepare

1. Check the branch, the PR's base and the current version. Keep unrelated edits; a dirty tree is normal during feature work.
2. Bump last, after the work is tested and reviewed (`compound-v:pull-requests`). A version already raised enough over the base is sufficient.
3. Edit the authoritative source and its required copies.
4. Validate: the repository's tests and configured checks; for a plugin, its manifest validation and skill links. Report a check that couldn't run as a blocker, never as passed.

## Publish when asked

Read the release automation before tagging: some repositories tag from `VERSION` after a merge, others publish on a pushed tag. Never add a second trigger.

1. Verify the exact reviewed commit, the version, the checks, and that the tag doesn't exist yet.
2. For a tag-driven release, tag that commit and push only the tag. Pushing the default branch and merging are the user's.
3. Follow the release workflow for that tag and commit, not just the newest run, and confirm the published artifact.

A bump or tag doesn't authorize a production rollout, a secret rotation or a database migration; those follow the user's rules.

## Summary

| Field | Value |
|---|---|
| Project / type | name; plugin, Elixir, Rust, Go … |
| Previous → new | vX.Y.Z → vX.Y.Z |
| Commit / tag | exact SHA; tag or "not requested" |
| Checks | passed, failed, pending, or blocked with the reason |
| Artifact | release URL or the version file changed |
