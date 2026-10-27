---
name: renar-postgres-migration
description: renar-backend is fully on PostgreSQL (runtime, tests, alembic); SQLite removed; schema normalized 2026-07-10 with guard test
metadata:
  node_type: memory
  type: project
  originSessionId: 01eb64df-3231-47a8-9dcd-7147d7da3561
---

renar-backend runs fully on PostgreSQL as of 2026-07-10: `.env`
`DATABASE_URL=postgresql+psycopg://ran:...@127.0.0.1:5432/renar` (see
[[local-postgres-access]]), tests run against the local server too
(`tests/conftest.py` uses the `reska` scratch account with a per-run schema),
schema is owned by Alembic, and the SQLite code paths were removed. The
parallel TV Time import (8 workers) was verified on real Postgres, 5.3x
speedup.

On 2026-07-10 the schema was normalized (genres → `genres`+`title_genres`
tables, comments → `title_id` FK, users' login/request counters dropped in
favor of `login_events`/`request_days`) via alembic revision `a1f4e9c30b77`,
applied to the live DB (pre-migration pg_dump kept in that session's
scratchpad). `tests/test_normalization.py` is the permanent guard: mechanical
rules + regression pins; deliberate exceptions live in its allowlists and in
docs/design-decisions.md ("Normalized schema" entry). Known data caveat: one
of user `ran`'s logins predated `login_events` and is not in the derived
count; old `request_count` (163/139) and `request_days` sums (51/60) counted
different things — the panel now reports the middleware-based numbers.

**How to apply:** schema changes must keep `test_normalization.py` green;
never re-add stored aggregates or identity-duplicating columns — extend the
event tables or the allowlist (with justification + design-decisions entry)
instead.

Gotcha (hit 2026-07-10): psycopg3 auto-prepares statements after ~5 runs per
connection; DDL that recreates tables (tests' drop_all/create_all, alembic
migrations against a live app) leaves pooled connections with stale plans →
"cached plan must not change result type". Tests fix: `engine.dispose()` in
conftest's `_fresh_db` after recreate. Prod implication: restart/recycle the
app after running alembic migrations.
