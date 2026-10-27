---
name: feedback_channel_default_topic
description: All bot-created channels must have a default topic/description set at creation time
metadata: 
  node_type: memory
  type: feedback
  originSessionId: dc2a1278-ef54-4eba-95f8-ce7965510ada
---

Every channel the bot creates must include a meaningful `topic` string. This is already the established pattern in `channelManager.ts` — every entry in the channel/category creation lists includes a `topic` field.

**Why:** The user expects all bot-managed channels to be self-describing by default so members know what each channel is for without needing staff to explain.

**How to apply:** When adding a new module or channel to `channelManager.ts`, always include a `topic` alongside the channel name. Never create a channel with an empty or missing topic.
