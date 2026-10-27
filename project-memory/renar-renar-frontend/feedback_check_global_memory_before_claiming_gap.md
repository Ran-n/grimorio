---
name: feedback_check_global_memory_before_claiming_gap
description: "Before telling the user a capability/credential is unavailable, grep global memory (C:\\Users\\{USER}\\.claude\\memory\\), not just the current project's mirrored memory folder"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 35d6b3cb-f97a-4f4e-bf4d-6305457ad5d5
  modified: 2026-07-28T19:47:53.545Z
---

Before claiming "I don't have X" (a tool, credential, or integration), search global memory at `C:\Users\{USER}\.claude\memory\` in addition to the current project's local memory folder — don't rely on the project's `MEMORY.md` index alone.

**Why:** Told the user Telegram delivery wasn't possible ("no Telegram tool/integration available") when [[reference_telegram_bot_token]] and [[feedback_apk_telegram_delivery]] had existed in global memory the whole time — just not yet mirrored into this project's index. The user had to correct me ("you always had it in memory") before I found it.

**How to apply:** When about to say a capability is missing, grep global memory for the relevant keyword first. If found there but not mirrored locally, copy it in per [[feedback_project_memory_mirror]] and proceed — don't ask the user to confirm the gap is real.
