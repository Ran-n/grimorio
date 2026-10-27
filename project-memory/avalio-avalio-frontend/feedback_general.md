---
name: General Feedback
description: Token economy, docs sync, industry standards behavior
type: feedback
originSessionId: e132952d-97d2-4a9b-a700-0c502415f387
---
- Use the fewest tokens possible without compromising result quality. Lead with the answer, skip preamble, hypotheses, trailing summaries, and filler.
- Always keep docs in sync with code: update docstrings, inline comments, and all README variants (every language version) as part of every code change. Treat it as part of the task, not a separate step. **Why:** stale field names lingered in READMEs after a rename.
- Always implement industry-standard behavior by default. If a request deviates from standard: do it, but first name the standard and flag the deviation so the user can decide.
