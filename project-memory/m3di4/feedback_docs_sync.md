---
name: Keep docs and comments in sync
description: Always update docstrings, inline comments, and all README variants whenever code changes
type: feedback
---

Always keep documentation in sync with code changes. This applies to:
- Docstrings on any modified class, method, or function
- Inline comments that reference field names, types, or behaviour
- All README variants (e.g. EN + GL in conexions) — every language version must be updated together

**Why:** User explicitly asked for this after noticing stale field names lingering in READMEs after a rename.

**How to apply:** Treat doc updates as part of every code change, not a separate step. When renaming a field, changing a type, or adding a feature, scan all documentation surfaces before considering the task done.
