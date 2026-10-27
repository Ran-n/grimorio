---
name: always-use-ask-user-question
description: "Use AskUserQuestion tool for all questions and choices, including mid-edit options; never ask in plain prose"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

Always use the `AskUserQuestion` tool when asking the user anything — clarifications, choices, confirmations, or options mid-edit. Never pose questions as plain prose.

**Why:** User explicitly instructed this as a universal rule; structured UI is easier to interact with than parsing response text, especially when iterating on edits.

**How to apply:**
- Any time I would write a sentence ending in "?" or present choices, use `AskUserQuestion` instead.
- When editing text (documents, markdown, prose) and the user gives directives ("make shorter", "change tone", "reword"), surface options or results via `AskUserQuestion` rather than a text block.
