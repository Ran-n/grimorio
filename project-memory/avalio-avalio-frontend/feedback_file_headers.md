---
name: File Headers (metadatos)
description: Run metadatos script on every file edit to maintain metadata headers
type: feedback
originSessionId: e132952d-97d2-4a9b-a700-0c502415f387
---
Use `python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>`.
Source: https://github.com/ran-n/metadatos — update the copy when version changes.

- On every file edit: run `-m` to update the `Revised:` timestamp
- If file has no metadata header: run `-c` to create one
- If asked to view metadata: run `-v`
- Supported types: `.py`, `.pyw`, `.sh`, `.bash`, `.rs`, `.md` — skip and inform user for other types

**Why:** user enforces metadata headers on all source files across all projects.
**How to apply:** after every file edit in this project, run the metadatos script.
