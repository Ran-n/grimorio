---
name: feedback_module_channel_recreation
description: "If a module's Discord channels/categories are manually deleted, the bot recreates them automatically"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d2d6b099-0fdf-49bb-a65f-f1da739d147c
---

If a module's managed Discord channels or categories are manually deleted, the bot should detect this and recreate them automatically — on startup, or when the deletion is detected via Discord events.

**Why:** User's explicit preference — modules should be self-healing; admins shouldn't need to re-toggle a module just to restore its channels.

**How to apply:** On bot startup and on `channelDelete`/`categoryDelete` events, check if any enabled module's managed resources are missing and recreate them with the correct permissions.
