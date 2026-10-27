---
name: file-headers-metadata
description: Use `metadata` CLI (C:\Scripts\metadata.bat) to manage Created/Revised timestamps; never write Revised by hand
type: feedback
---

CLI (PowerShell): `metadata <flag> <file>`
Flags: `-v` view · `-m` update Revised · `-c` create header · `-d` delete header · `-h` help

**Invocation:** run as a PowerShell script: `metadata -m <file>`. Do not use `uv run`, `python -m`, or any other wrapper.

Supported file types: `.py .pyw .sh .bash .rs .md` — for any other type, inform the user and skip.

Rules:
- Before editing any file, run `metadata -v <file>`. If output is empty → run `metadata -c <file>` first.
- After every edit → run `metadata -m <file>` to update Revised.
- Never write the `Revised:` timestamp by hand — always run the command.

**Why:** manual timestamps drift from reality; the command is the single source of truth for file provenance.
