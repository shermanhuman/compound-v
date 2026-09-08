---
description: Persist a requested project rule and synchronize configured native instruction output.
---

# Add a project rule

Resolve the target repository. Ask for the rule only when none was provided. Read `.promptherder/hard-rules.md` and relevant existing rules before appending. If the new rule contradicts another rule, use the user’s explicit replacement intent; otherwise ask which policy should prevail before changing that conflict. Do not create duplicate or knowingly contradictory bullets.

Save the agreed rule in `.promptherder/hard-rules.md`. When the Promptherder CLI and target configuration are available, preview and sync the change. Do not silently adopt conflicting generated files or choose new targets. If sync cannot complete, say that the source is saved but native output is pending. Hosts may need to reload instructions; never promise automatic enforcement in an already-running session.
