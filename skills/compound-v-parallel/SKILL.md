---
name: compound-v-parallel
description: Identify independent work that can safely run concurrently within the host’s available capabilities.
---

# Concurrent work

Identify data and mutation dependencies before grouping work. Reads of unrelated files or independent searches can run together. Writes touching the same file, repository index, lockfile, shared build output, service, or external record must be coordinated even when commands look different.

Keep build-before-test and other actual dependencies sequential. Bound concurrency to available tools and resources; no particular host API or worker count is assumed. Subagents are optional and require applicable authorization. If unavailable, perform the same checks locally; do not pretend separate agents ran.

Await every started operation and inspect its result. Do not declare success while work remains running. Stop dependent work on failure, preserve useful independent progress, and repair the cause before resuming.
