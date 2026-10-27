---
name: Keep docs and comments in sync
description: Always update docstrings, inline comments, and both READMEs (EN + GL) whenever code changes
type: feedback
---

Always keep documentation in sync with code changes. This applies to:
- Docstrings on any modified class, method, or function
- Inline comments that reference field names, types, or behaviour
- `README.md` (English) and `doc/README.gl.md` (Galician) — both must be updated together

**Why:** User explicitly asked for this after noticing that `proxy.https` lingered in the READMEs after the field was renamed to `proxy.protocol`.

**How to apply:** Treat doc updates as part of every code change, not a separate step. When renaming a field, changing a type, or adding a feature, scan all four surfaces (docstrings, inline comments, README.md, doc/README.gl.md) before considering the task done.
