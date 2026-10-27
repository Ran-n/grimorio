---
name: feedback_db_source_of_truth
description: "DB is the single source of truth — for configurable data, state tracking, and anything that needs to be queried; never rely on in-memory cache or derived state"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: dc0fb465-21b1-4701-b01e-83c2bc1ae8d0
---

All persistent state must live in the DB, properly normalized. This has two applications:

1. **Configurable/list data** — option lists, reasons, labels, toggles must be stored in `command_choices` and surfaced via autocomplete, never hardcoded in `.addChoices()`.

2. **Runtime state** — membership, active flags, join/leave history, etc. must be tracked in the DB with the right columns (e.g. `active`, `left_at`). Never use `client.guilds.cache` or other in-memory structures as a source of truth — cache is wiped on restart and can't be queried.

**Why:** Hardcoded lists break when options change without a deploy. In-memory cache is unreliable across restarts and produces wrong query results (e.g. mutual server count showing 0 for quiet members).

**How to apply:** Before using `.addChoices()` with literal values, seed into `command_choices` and use `buildData()`. Before reading from Discord.js cache to derive state, check whether the DB has (or should have) a column for it. When adding any feature that tracks state over time, ensure the table has columns to represent current state and that join/leave/update events keep them accurate.
