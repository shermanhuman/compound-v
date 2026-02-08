---
description: Add a hard rule to the project's always-on prompt. Lightweight, no ceremony. Use any time.
---

// turbo-all

# Rule

Append the user's rule to `.promptherder/hard-rules.md`.

## Steps

1. Read `.promptherder/hard-rules.md` if it exists.

2. If it doesn't exist, create it with a header:

```markdown
---
trigger: always_on
---

# Hard Rules

Project-level rules that are always active. Added by `/rule` or manually.
```

3. Append the rule as a bullet point:

```markdown
- <rule>
```

4. Confirm to the user: **"Added hard rule."** with the line that was added.

That's it. No planning, no research, no approval. Just append and confirm.
