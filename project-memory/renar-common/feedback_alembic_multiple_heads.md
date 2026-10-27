---
name: alembic-multiple-heads
description: "Always run `alembic heads` before writing a migration, and `alembic upgrade head` after — in any project using Alembic"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b3efad98-d345-4f7f-b4f5-af453a600e22
---

Before creating a new Alembic revision, run `uv run alembic heads` first and set `down_revision` to whatever it reports — don't assume the newest-looking file in `alembic/versions/` is the current tip. After writing the migration, always run `uv run alembic upgrade head` to actually apply it — don't leave a migration file sitting unapplied.

**Why:** Hit the multi-head issue directly: authored a migration with `down_revision` pointing at what looked like the latest file, but another session had already added a different migration branching from the same parent moments earlier, producing two heads and an `alembic upgrade head` failure ("Multiple head revisions are present"). Separately, the user asked to always apply migrations rather than just generate the file — an unapplied migration leaves the dev DB schema out of sync with the models, breaking anything that touches the new column/table until someone remembers to run upgrade.

**How to apply:** Run `alembic heads` (or `alembic history`) right before writing a new revision file, and rebase `down_revision` onto whatever the real tip is. If a fork already happened, fix the stray migration's `down_revision` rather than writing a merge migration, when the fork is trivial to rebase. Once the migration file is written, immediately run `alembic upgrade head` against the dev DB as part of the same task — not just when the user separately asks to run migrations. This applies to renar-backend and any other project with an `alembic/` directory.
