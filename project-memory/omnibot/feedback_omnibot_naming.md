---
name: feedback_omnibot_naming
description: OmniBot Discord resource naming spec — every bot-managed resource requires the Ω symbol; exact format depends on whether the resource allows uppercase/brackets
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 073da14b-cfa5-4a10-b716-9f3ef5cb2dc5
---

Every Discord resource created or managed by OmniBot must carry the Ω (ohm) symbol. The format depends on whether the resource type allows uppercase letters and special characters:

**Rule: supports uppercase + brackets → `NAME [Ω]`**
- Categories: `LOGS [Ω]`, `JAIL [Ω]`, `MODERATION [Ω]`, `VERIFY [Ω]`, `TICKET HISTORY [Ω]`
- Roles: `Admin [Ω]`, `Mod [Ω]`, `Staff [Ω]`, `Jail [Ω]`, `Verified [Ω]`

**Rule: lowercase-only (Discord channel names) → `name-ω`**
- Text channels: `mod-log-ω`, `security-alerts-ω`, `ticket-logs-ω`, `verify-logs-ω`, `mod-actions-ω`, `publicity-approvals-ω`
- Voice channels: same pattern, e.g. `lobby-ω`
- Transcript/archive channels: `{ticket-type}-ω` e.g. `support-ω`, `appeal-ω`, `verify-ω`

**Rule: no exceptions** — if OmniBot creates or owns it, it gets the Ω. This includes any future resource type.

**Constants:** Canonical names are defined as exported constants in `src/bot/lib/channelManager.ts` (channels + categories) and as the `name` field in `ROLE_TIERS` in `src/bot/lib/roleManager.ts` (roles). Never hardcode these strings — always reference the constant.

**Why:** Ω visually identifies all bot-owned resources at a glance and lets the bot reliably find, deduplicate, and manage its own resources without touching manually-created ones.

**How to apply:** Before writing any `guild.channels.create()` or `guild.roles.create()` call, check whether a constant already exists. If not, add one to the appropriate file and use it everywhere.
