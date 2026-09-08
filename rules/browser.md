---
activation: relevance
description: Verify rendered UI behavior and appearance using the browser tools available in the current host.
---
# Browser verification

Choose tools by the assertion: an HTTP request for an API response, browser DOM/accessibility inspection for interactions, screenshots for visual layout. Use the available host browser or project test runner; do not assume a particular MCP server, subagent, model, or cost.

Check relevant loading, empty, error, and interactive states. Keep screenshots tied to a visual assertion. Do not use a browser as a substitute for inspecting source or running focused tests. Use isolated test data and retain the task's authorization boundaries for actions such as purchases, messages, or production mutations. Delegate only when the host supports it and applicable instructions authorize it.
