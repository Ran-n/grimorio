---
name: feedback-no-ddl-in-logpiece
description: logpiece never does DDL — all schema changes go through reska-op-card-api Alembic; data changes (DML) are fine
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a7d1b73a-ea74-4b01-905c-d32ea6d8c6e7
---

Never write DDL in logpiece (`ALTER TABLE`, `CREATE TABLE`, `DROP TABLE`, `CREATE INDEX`, etc.). Schema structure is owned by `reska-op-card-api` and managed via Alembic migrations there.

**Why:** logpiece is a consumer of the reska-op-card-api database. It reads structure (via PRAGMA introspection for the table editor) and reads/writes data rows, but it must never mutate the schema. Schema drift between logpiece DDL and reska-op-card-api Alembic would silently break migrations.

**How to apply:** If a new column or table is needed, write the Alembic migration in `reska-op-card-api` and update `doc/logpiece_schema_changes.md` there to document it. Then update `logpiece/models.py` and `logpiece/db.py` to use the new column — but no DDL in logpiece itself, not even as a "migration helper" on connect.

DML (INSERT, UPDATE, DELETE on existing rows) is the whole point of the editor and is always fine.

See also: [[logpiece-project-spec]]
