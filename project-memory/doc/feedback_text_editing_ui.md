---
name: Use AskUserQuestion during text editing directives
description: When editing text and user gives directives, use AskUserQuestion instead of outputting text blocks
type: feedback
originSessionId: 26247f5d-3deb-44d2-8e44-3246ba58be83
---
When we are editing text (documents, markdown, prose) and the user is giving me directives (e.g. "make this shorter", "change the tone", "reword this"), use `AskUserQuestion` to present options or confirm choices rather than outputting a text block for the user to read and evaluate.

**Why:** User finds it easier to interact with the structured UI component than to read and parse response text when iterating on edits.

**How to apply:** Anytime I'm mid-edit on text content and need to present a result or ask which direction to take, surface it via `AskUserQuestion` with options instead of a prose response.
