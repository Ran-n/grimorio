---
name: file-headers-metadata
description: "Use `metadata` CLI (C:\\Scripts\\metadata.bat) to manage Created/Revised timestamps; never write Revised by hand"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0901e300-e5eb-4465-b783-97a56d464508
  modified: 2026-08-25T13:01:58.780Z
---

CLI (PowerShell): `metadata <flag> <file>`
Flags: `-v` view · `-m` update Revised · `-c` create header · `-d` delete header · `-h` help

**Invocation:** run as a PowerShell script: `metadata -m <file>`. Do not use `uv run`, `python -m`, or any other wrapper. From the Bash tool (git-bash), plain `metadata` is not on PATH — call `metadata.bat -m <file>` instead. **One file per invocation** — passing several space-separated paths to a single `metadata -m` call updates some files but silently skips others (observed: only the first of 6 paths in one call actually got a fresh Revised timestamp, with no error). Loop/call it once per file, and verify with `metadata -v` afterward on anything that mattered — don't trust a multi-file call blindly.

Supported file types: `.py .pyw .sh .bash .rs .md` — for any other type, inform the user and skip.

Rules:
- Before editing any file, run `metadata -v <file>`. If output is empty → run `metadata -c <file>` first.
- After every edit → run `metadata -m <file>` to update Revised.
- Never write `Created:`/`Revised:` timestamps by hand — always run the command. This includes brand-new files: write the file's code/prose with NO header at all, run `metadata -c <file>` to stamp real Created/Revised, then (for .py) merge any description prose into the generated docstring between `Revised:` and the closing `"""` — don't invent placeholder timestamps and clean them up after.

**Why:** manual timestamps drift from reality; the command is the single source of truth for file provenance.
