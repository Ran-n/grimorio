---
name: Always run metadatos -m after file edits
description: Must run the metadatos script to update Revised timestamp after every file edit — do not set the timestamp manually
type: feedback
originSessionId: 747959c6-0d09-450b-82fe-93f0a1de9ae3
---
After editing any supported file (`.py`, `.pyw`, `.sh`, `.bash`, `.rs`, `.md`), always run:

```
python C:/Users/{USER}/.claude/memory/metadatos_v0.2.1.py -m <file>
```

Never write the `Revised:` timestamp by hand — the script must set it.

**Why:** User caught me manually writing a placeholder timestamp instead of running the script.

**How to apply:** Immediately after every Edit or Write tool call on a supported file type, run the `-m` command as the next step. Do not skip it or defer it.
