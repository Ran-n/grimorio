---
name: Disabled buttons must be visually distinct
description: Disabled UI buttons must always appear greyed out, not identical to enabled buttons
type: feedback
---

When a button is disabled (action unavailable), it must have a clearly greyed-out visual appearance — dimmed background and dimmed label/icon. Never leave disabled buttons looking identical to enabled ones.

**Why:** user feedback — clickable-but-noop buttons are confusing; disabled state must be visually obvious.

**How to apply:** whenever defining button styles, always include a disabled visual variant. For disabled state: significantly reduce opacity/brightness of both background and foreground so the button reads as inactive at a glance.
