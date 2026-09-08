---
description: Record observed project toolchain versions and distinguish them from proposed upgrades.
---

# Record the stack

Read `.promptherder/stack.md`, or legacy `.agents/rules/stack.md` / `.agent/rules/stack.md` if no source record exists. Inspect project manifests, lockfiles, runtime manager config, and Dockerfiles for actual versions. Distinguish declared ranges from resolved versions.

Write observed versions to `.promptherder/stack.md` when updating the stack record was requested. Preserve relevant hand-written notes. This source file is context, not a host output file. Never write into generated `.agents/rules/`.

When asked to compare upgrades, consult official current documentation and show actual, recorded, and proposed versions separately. Do not record a proposed version as installed or upgrade dependencies merely because the user requested an inventory. If an actual upgrade is authorized, carry it out and verify it before updating the observed record.
