---
name: file-headers-metadata
description: "Use `metadata` CLI (C:\\Scripts\\metadata.bat) to manage Created/Revised timestamps; never write Revised by hand"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 53532e8b-f785-4b95-b670-f3695028a191
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

**Never fabricate timestamps.** Only use values that `metadata -v` actually reported. If a Created date looks suspicious, it may have been set by `-c` at creation time — do not "restore" a made-up earlier date.
