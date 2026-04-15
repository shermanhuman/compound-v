---
trigger: manual
---

# Browser Testing

Use the `browser_subagent` tool to test web UI in the browser. This rule is loaded manually when browser-based verification is needed.

## When to use

- Verifying UI changes after implementation (layout, styling, interactions)
- Testing login flows, form submissions, or multi-step wizards
- Checking responsive behavior at different viewport sizes
- Validating that a local dev server renders correctly

## How to use

1. **Start the dev server** first (`npm run dev`, `mix phx.server`, etc.)
2. **Navigate** to the target URL with the browser subagent
3. **Interact** — click, type, scroll as needed to test the flow
4. **Capture** screenshots or read DOM state to verify expected outcomes
5. **Report** pass/fail with specific observations

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
