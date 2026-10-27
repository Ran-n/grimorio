---
name: project_module_quirks
description: "Module system design quirks — what's global-only vs guild-toggleable, and how config/oconfig relate"
metadata: 
  node_type: memory
  type: project
  originSessionId: f4248ad9-5a04-4e2e-aa12-7cfca97f8ca8
---

Verification (`modulesVerification`) is a **global-only module** — it is not exposed in `/config module enable/disable`, not in the guild wizard toggle menu, and not in `GUILD_DEFAULTS`. It only appears in `oconfig` (global availability + detail view).

**Why:** Verification is an identity system managed at the bot level, not per-server. Guilds don't control whether it exists.

**How to apply:** When adding new modules, decide upfront if they're global-only or guild-toggleable:
- Global-only → add to `MODULE_LABELS` in `oconfig.ts` only; add a `MODULE_DETAILS` entry; do NOT add to `MODULE_KEYS` in `config.ts` or `GUILD_DEFAULTS`.
- Guild-toggleable → add to both `config.ts` (`MODULE_KEYS`, `MODULE_LABELS`, `MODULE_CHOICE_TO_KEY`, `buildViewEmbed` handler) and `oconfig.ts` (`MODULE_LABELS`, `GUILD_DEFAULTS`, `MODULE_DETAILS`).

Labels must match between `config.ts` and `oconfig.ts`. Current canonical labels: Tickets, Jail, Roles, Sticky, Tagging, Moderation, Profiles, Automod, Audit Log, Leveling.
