---
name: project-db-timestamps
description: How created_ts/updated_ts are managed in the optcg_api/logpiece shared SQLite DB
metadata: 
  node_type: memory
  type: project
  originSessionId: 1c193acd-f9a3-4bd9-9f34-32c0997fc01d
---

The DB handles all timestamp stamping — the app never needs to set them manually.

Two mechanisms were added to the schema (managed in optcg_api Alembic):

1. **`server_default` on all `created_ts` and `updated_ts` columns** — `strftime('%Y-%m-%d %H:%M:%f', 'now')`. Any raw SQL INSERT that omits these columns gets them filled by SQLite automatically.

2. **`AFTER UPDATE` triggers on all 35 tables** — named `trg_<table>_update`. Refreshes `updated_ts` to the current time on every row update. Guard clause `WHEN NEW.updated_ts IS OLD.updated_ts` prevents the trigger re-firing recursively on its own UPDATE.

**How to apply:** logpiece's `db.py` must never inject `_now_ms()` or pass `created_ts`/`updated_ts` in INSERT/UPDATE statements — the DB fills them. The `models.py` in logpiece mirrors optcg_api's model definitions (using `_ts_col()` with `server_default`) and is kept in sync manually when optcg_api's schema changes.
