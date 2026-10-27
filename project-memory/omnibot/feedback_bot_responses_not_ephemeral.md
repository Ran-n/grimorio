---
name: feedback_bot_responses_not_ephemeral
description: All bot command replies use replyEphemeral (ephemeral + auto-delete after duration) unless the handler explicitly states otherwise
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9c86c10a-1d53-4feb-9ccc-337e66d3b9ea
---

All bot command replies use `replyEphemeral` (ephemeral + scheduled auto-delete) by default. Only deviate when the handler explicitly calls for a different pattern (e.g. `deferReply` + `editReply` for long-running ops that post a persistent result).

**Why:** User confirmed this is the standard pattern for all slash command responses in this codebase.

**How to apply:** Always use `replyEphemeral(interaction, ...)` for command responses unless there's a specific documented reason to do otherwise (e.g. approve/deny posting a permanent embed in a ticket channel).
