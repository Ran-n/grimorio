---
name: feedback-bot-messages
description: "How Claudia bot messages should be written — language, name, pings"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3b07ec36-664b-43c4-9c7c-c3d5b7dcbc52
---

Bot messages sent via the Discord API must follow these rules:

1. **Always write in Galician** — all bot messages go out in Galician, not Spanish or English.
2. **The bot is called Claudia**, not Claudio or Claude. Always sign off or refer to the bot as Claudia.
3. **Only ping roles/users that can see the channel** — e.g. pinging Membro/Lider in #mods makes no sense because they can't see it. Ping the Mod role in #mods, ping individual users in channels they can read.
4. **When pinging individuals, use only those with known IDs** — Hugo and Julio were the relevant ones for voice PTT issues. Don't ping others unnecessarily.

**Why:** User corrected these one by one during the USE_VAD fix session.
**How to apply:** Any time drafting or sending a Discord message through the bot, run through this checklist before sending.
