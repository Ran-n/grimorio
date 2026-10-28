---
name: file-headers-metadata
description: Use `metadata` CLI (`~/.claude/bin/metadata`, on PATH) to manage Created/Revised timestamps; never write Revised by hand
type: feedback
---

CLI (PowerShell): `metadata <flag> <file>`
Flags: `-v` view · `-m` update Revised · `-c` create header · `-d` delete header · `-h` help

**Invocation:** run as a PowerShell script: `metadata -m <file>`. Do not use `uv run`, `python -m`, or any other wrapper. Agent shells may not have it on PATH: then call `& C:\Users\{USER}\.claude\bin\metadata.ps1 -m <file>` directly; never conclude it's missing without checking that path.

Supported file types: `.py .pyw .sh .bash .rs .md` — for any other type, inform the user and skip.

Rules:
- Before editing any file, run `metadata -v <file>`. If output is empty → run `metadata -c <file>` first.
- After every edit → run `metadata -m <file>` to update Revised.
- Never write the `Revised:` timestamp by hand — always run the command.
- `-c` on a `.py` that already has a module docstring adds a *second* docstring above it (ruff E402 follows): merge the description into the header docstring, as the other files do, then `-m`.

**Why:** manual timestamps drift from reality; the command is the single source of truth for file provenance.
