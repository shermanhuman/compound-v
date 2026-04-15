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

## What to verify

- Page loads without errors (check console)
- Key elements are visible and correctly positioned
- Interactive elements respond (buttons, links, forms)
- Data displays correctly (tables, lists, dynamic content)
- Error states render properly (404, empty states, validation messages)

## What NOT to do

- Don't use browser testing for API-only changes — use curl/httpie instead
- Don't capture screenshots just to capture them — have a specific assertion
- Don't test in the browser what can be tested with unit/integration tests
>>>>>>> 7b5f1a6 (fix: audit fixes — browser.md stub, stack ordering, hard-rules dedup)
