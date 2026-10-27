---
name: feedback-response-style
description: "answer-first, no preamble/filler/trailing prompts; docs always in sync; cite standard deviations; hard 100-word cap on every response"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 711d93f0-acdb-47ef-b5c3-ddf4079836d2
  modified: 2026-08-19T19:20:18.315Z
---

Answer first, no preamble/filler/trailing prompts; docs always kept in sync; cite standard deviations explicitly.

**Hard cap: every response must be 100 words or fewer.** No exceptions unless the user explicitly asks for more detail in that turn.

Why: user confirmed 2026-08-19 — wants terse output by default, including for substantial engineering turns.

How to apply: before sending any reply, count/estimate word length and trim ruthlessly — cut examples, restate findings as bullet fragments, drop restated context. If a task produces a long deliverable (code diff, doc edit), let the artifact/diff carry the detail and keep the chat response to a short summary of what changed and what's next.
