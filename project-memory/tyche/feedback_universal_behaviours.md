---
name: universal-app-behaviours
description: Behaviours expected in all projects unless explicitly overridden
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

## Shutdown
All threads, background workers, and child processes must be cleanly stopped before the process exits — on any quit path (button, shortcut, OS close, tray).

## Contradictions
If a request contradicts an established behaviour (universal or project-specific), flag it and ask which intent to keep before implementing.
