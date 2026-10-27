---
name: file-headers-metadatos
description: Use metadatos_v0.2.1.py to manage Created/Revised timestamps; never write Revised by hand
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8d6ce87f-ebe4-4c7f-9a7c-dc4de51180fd
---

CLI (PowerShell): `metadata <flag> <file>`
Flags: `-v` view · `-m` update Revised · `-c` create header · `-d` delete header · `-h` help

**Invocation:** `metadata -m <file>` works in both the Bash tool (via `metadata.bat`) and the PowerShell tool (via `metadata.ps1`). Do not use `uv run`, `python -m`, `python <path>`, or any other wrapper. **Never invoke metadata via Python in any form.**

Supported file types: `.py .pyw .sh .bash .rs .md` — for any other type, inform the user and skip.

Rules:
- Before editing any file, run `metadata -v <file>`. If output is empty → run `metadata -c <file>` first.
- After every edit → run `metadata -m <file>` to update Revised.
- Never write the `Revised:` timestamp by hand — always run the command.
- Never try to locate the script with `where.exe`, `Get-Command`, or any shell lookup — it is always available as `metadata` directly in PowerShell.
- **NEVER write the header manually in any form** — not in the Write tool, not in Edit, not inline. Always use `metadata -c` to create and `metadata -m` to update. No exceptions.

**Header format for .py files** (produced by `-c`):
```
#!/usr/bin/env python3
"""
Authors: Ran# <ran.hash@proton.me>
Created: YYYY/MM/DD HH:MM:SS.ffffff
Revised: YYYY/MM/DD HH:MM:SS.ffffff
"""
```
The module docstring (if any) goes on the line immediately after the closing `"""`, then imports follow. Do NOT use comment-style (`# Authors:` etc.) headers — that format is wrong and the script cannot update it.

**`from __future__ import annotations`**: remove it rather than working around it. Modern Python 3.10+ does not need it for most use cases, and keeping it would require a comment-style header which the script does not support.

**Why:** manual timestamps drift from reality; script is the single source of truth for file provenance. Comment-style headers were an error introduced by Claude — the correct format is always the docstring style above. Hand-writing the header block (even in Write/Edit tool calls) is also an error — the tool must always be the one to produce it.
