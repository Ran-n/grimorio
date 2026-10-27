---
name: feedback_module_disable_behavior
description: "When a module is disabled on a guild, its Discord channels/categories are left intact — never deleted"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2d6b099-0fdf-49bb-a65f-f1da739d147c
---

When a module is disabled on a guild, leave its created channels and categories intact. Do not delete or archive them on disable.

**Why:** User's explicit preference — disabling a module should not destroy data or channel history.

**How to apply:** Module teardown logic should only unregister commands/listeners, never delete Discord resources.
