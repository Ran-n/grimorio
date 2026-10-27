---
name: feedback_updated_ts_trigger
description: Every new DB table must have an updated_ts trigger created alongside it in the same migration
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f0480f4c-c9c6-4fa9-8507-644cba024e62
---

Every time a new table is created in a migration, a corresponding `updated_ts` trigger must be created in the same migration.

Use this pattern (matching all existing triggers in the project):

```sql
CREATE TRIGGER trg_<table>_update
AFTER UPDATE ON <table>
FOR EACH ROW
WHEN NEW.updated_ts IS OLD.updated_ts
BEGIN
    UPDATE <table>
    SET updated_ts = strftime('%Y-%m-%d %H:%M:%f', 'now')
    WHERE id = NEW.id;
END
```

**Why:** All tables in this project track `updated_ts`. The `WHEN NEW.updated_ts IS OLD.updated_ts` guard lets the app override the timestamp explicitly (e.g. data imports) while auto-stamping normal updates.

**How to apply:** When writing or autogenerating a migration that calls `op.create_table(...)`, always follow it with `op.execute(sa.text(...))` for the trigger, and add `op.execute(sa.text("DROP TRIGGER IF EXISTS trg_<table>_update"))` in `downgrade`.
