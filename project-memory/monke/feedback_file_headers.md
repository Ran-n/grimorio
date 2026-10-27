---
name: File headers — metadatos
description: Rules for running metadatos_v0.2.1.py to manage file metadata headers
type: feedback
---

Use `python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>`.
Source: https://github.com/ran-n/metadatos — update the copy when the version changes.

- Before editing a file, check whether it already has a metadata header (look for `// ---` or `# ---` at the top)
- If no header exists, run `-c` to create one first, then `-m` to update the revised timestamp
- On every file edit, run with `-m` to update the `Revised:` timestamp
- After `-c`, verify the `Created:` timestamp matches the filesystem creation time; correct it manually if needed
- If asked to view metadata, run with `-v`
- Supported types: `.py`, `.pyw`, `.sh`, `.bash`, `.rs`, `.md` — for any other type, skip and inform the user

**Why:** project convention for tracking file history via headers.
**How to apply:** every time a supported file type is created or edited.
