---
name: file-headers-metadatos
description: Use metadatos_v0.2.1.py to manage Created/Revised timestamps; never write Revised by hand
type: feedback
---

Script: `python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py <flag> <file>`

Flags: `-c` add header · `-m` update Revised · `-v` view header

Rules:
- Before editing any file, check for `// ---` (JS/TS) or `# ---` (Python/etc) at the top.
- No header → run `-c` then verify `Created:` matches filesystem `ctime`; correct if off.
- Every edit → run `-m` after saving.
- Never write the `Revised:` timestamp by hand — always run the script.
- Supported extensions: `.py .pyw .sh .bash .rs .md` — skip other types, inform user.
- Update local copy when version changes.

**Why:** manual timestamps drift from reality; script is the single source of truth for file provenance.
