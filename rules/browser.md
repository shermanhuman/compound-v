---
trigger: manual
---

# Browser Agent

Use the Antigravity browser subagent for true **end-to-end UI testing** — verifying rendered output, forms, and interactions in a real browser. It runs on a separate model (Gemini 2.5 Pro UI Checkpoint), meaning each action incurs a distinct model invocation. Use it sparingly.

## Approach hierarchy (cheapest → most capable)

1. **Native fetch / `curl`** — static HTML, REST APIs, docs, JSON endpoints. No JS execution. Near-zero cost.
2. **Headless browser (MCP)** — JS-rendered pages, SPAs, form interactions. Uses accessibility tree snapshots (text, not pixels). Low token cost.
3. **Browser subagent** — visual verification. Does the UI _look_ right? Screenshots + vision model. High cost.

## When to use what

| Need | Use |
|------|-----|
| Read docs, static HTML, API responses | **Fetch** |
| Check if an element exists in rendered DOM | **Headless MCP** |
| Fill forms, click buttons, navigate SPAs | **Headless MCP** |
| Verify visual layout, colors, spacing | **Browser subagent** |
| Confirm modals, toasts, animations render | **Browser subagent** |
| Debug why a page looks wrong | **Browser subagent** |
| Scrape data from non-JS pages | **Fetch** |

## Key principles

- **Fetch first.** Check if the data is available via a direct URL or API before launching a browser.
- **Accessibility tree over screenshots.** Headless MCP uses semantic snapshots (roles, labels, states) — fast, deterministic, cheap. Only use screenshots for visual validation.
- **Screenshots are expensive.** Each one requires vision model inference. Use them to _verify_ results, not to _navigate_.
