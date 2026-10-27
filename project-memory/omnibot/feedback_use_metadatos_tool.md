---
name: feedback-use-metadatos-tool
description: "When updating doc files (CHANGELOG.md, etc.), run the metadatos tool to update the Revised timestamp in the file header"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d71b3d7b-e67a-4648-9838-951bea86470e
---

After editing any file in `d:\Users\{USER}\sw\doc\`, run the metadatos tool to update the `Revised` timestamp in the file header:

```
cd "d:\Users\{USER}\sw\metadatos" && python main.py -m "../doc/<filename>"
```

**Why:** The file headers contain `[//]: # (+ Revised: ...)` metadata that must be kept current; the metadatos tool handles this with a precise microsecond timestamp.

**How to apply:** Any time a doc file is written or edited, run `-m` on it immediately after.
