---
trigger: manual
---

# Browser Agent

Use the Antigravity browser subagent for true **end-to-end UI testing** — verifying rendered output, forms, and interactions in a real browser. It runs on a separate model (Gemini 2.5 Pro UI Checkpoint), meaning each action incurs a distinct model invocation. Use it sparingly.

## Approach hierarchy (cheapest → most capable)

1. **`read_url_content` / `curl`** — for static HTML, REST APIs, markdown files, docs. No JS execution. Very fast, near-zero tokens. Use this first.
2. **Playwright MCP** (`@playwright/mcp --headless`) — for JS-rendered pages that need DOM interaction without visual verification. Uses accessibility tree snapshots (text-based), not vision. No image model cost. A good middle ground for SPAs.
3. **Browser subagent** — reserve for E2E UI verification: does the feature _look_ right in a real browser? Checking forms submit, modals open, LiveView updates render correctly. This is its sweet spot.

## When to invoke

Invoke this rule (via `@browser`) when you need to control the browser. Prefer the cheapest approach that answers the question.
