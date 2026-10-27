---
name: metadata header order
description: always check for existing header before running metadatos; create with -c first if missing, then -m
type: feedback
originSessionId: d3889307-6d9a-4b29-a327-032dba291a8d
---
Before running `-m` on any file, check whether a metadata header already exists. If the file has no header, run `-c` first to create it, then `-m` to set the revised timestamp.

**Why:** ran `-m` on a headerless file, which silently did nothing; user had to correct the order.

**How to apply:** on every file edit — read the first few lines, if no `// ---` / `# ---` header is present, run `-c` then `-m`; otherwise just `-m`.
