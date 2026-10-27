---
name: reference-central-verification-server
description: "The Discord server that serves as OmniBot's central verification hub is called \"OmniBot\""
metadata: 
  node_type: memory
  type: reference
  originSessionId: e51c161a-a74b-46da-a13c-233ad912fc43
---

The central verification server (referred to in [[docs/01-overview.md]] / [[docs/02-verification.md]] as "the central verification server") is an actual Discord server named **OmniBot**, and the bot is already a member of it.

This is where `/verify` tickets are opened, reviewed, and approved/denied by verification staff — approvals there propagate the verified role to every other server the bot is in. Its guild ID is stored as `central_guild_id` in the `bot_config` table (see `docs/05-database.md`).
