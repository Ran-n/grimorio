---
name: Universal app behaviours
description: Behaviours expected in all projects unless explicitly overridden
type: feedback
originSessionId: a9faf96a-074c-4209-a524-30e5f7027481
---
## Shutdown
All threads, background workers, and child processes must be cleanly stopped before the process exits — on any quit path (button, shortcut, OS close, tray).

## Contradictions
If a request contradicts an established behaviour (universal or project-specific), flag it and ask which intent to keep before implementing.
