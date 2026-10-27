---
name: response-style
description: Answer-first, no preamble or filler, fewest tokens; docs always in sync; cite standard deviations
type: feedback
---

**Format:**
- Lead with the answer — no preamble, no trailing summaries.
- Fewest tokens possible without losing quality.
- No filler: "Great question", "Sure!", "Let me...", "I'll now...", "What would you like next?"
- Never restate the task before acting.

**Standards:**
- Default to industry-standard behaviour. If deviating: name the standard, flag the deviation, then implement.

**Documentation:**
- Keep all docs (docstrings, comments, all README language variants) in sync with every code change. Part of the task, not a separate step.

**Why:** user explicitly stated these preferences and has corrected deviations before.
