---
name: renar-bcnf
description: "renar-backend's Postgres schema must stay BCNF, not just 3NF; every new column/table needs this checked before it's considered done"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 058adc74-9b9d-4a5e-8261-32ebec30c9e8
---

The renar-backend database must be kept in BCNF (Boyce-Codd Normal
Form): for every non-trivial functional dependency, the determinant must
be a superkey. This is stricter than the "3NF, mechanically approximated"
bar that was in place before 2026-07-13 — see [[renar-postgres-migration]]
for the general normalization background and `docs/design-decisions.md`
in renar-backend for the full rationale (search "Normalized schema,
enforced by a guard test" and "Only root comments store
title_id/season/episode").

**Why:** the user explicitly asked for the DB to be BCNF, not just the
project's prior ad-hoc heuristics. An audit found one real violation
(`comments.title_id`/`season`/`episode` copied onto reply rows — a
transitive dependency through `parent_id`) which was fixed by nulling
those columns on replies and deriving them via a recursive CTE
(`comment_threads.resolve_root_scope`) instead of storing a copy.

**How to apply, every time a column or table is added to renar-backend:**
1. Check `tests/test_normalization.py` still passes — it mechanically
   catches 1NF violations (plural string columns), missing FKs on `*_id`
   columns, unregistered stored aggregates, and columns copied from a
   table reachable through one of the table's own FKs (the 2NF/3NF/BCNF
   proxy). Run it, don't just assume.
2. That mechanical check cannot see self-referential copies (a table
   copying an attribute from an ancestor of itself via a chain, like the
   comments case) or true BCNF violations among a single table's own
   non-key columns (no FK involved). For those, manually verify: does
   every non-key column depend on the *whole* of every candidate key
   (PK and every multi-column UNIQUE constraint), and nothing else? If a
   non-key column's value is derivable from another non-key column or
   from a subset of a composite key, that's a violation — normalize it
   (usually: don't store the copy, derive it via a join or a recursive
   walk) rather than widening an allowlist to make the test pass.
3. If a genuine exception is needed (a same-named column that's actually
   a different fact, a bounded counter, an external-system cache that
   depends on the whole of this table's own key), register it explicitly
   in `ALLOWED_COPIED_COLUMNS` / `ALLOWED_AGGREGATES` /
   `ALLOWED_FKLESS_ID_COLUMNS` in `test_normalization.py` with a
   justification string, and document the decision in
   `docs/design-decisions.md` — never silently skip the check.
4. Caching a fact from an *external* system (TMDB, Open Library) on the
   owning row is not a BCNF concern as long as it depends on the whole of
   that row's own key — don't flag or "fix" those.
