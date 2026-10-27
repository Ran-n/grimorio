---
name: database-bcnf
description: "relational database schemas must be BCNF, checked and enforced explicitly, not just informally \"normalized\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 058adc74-9b9d-4a5e-8261-32ebec30c9e8
---

Every relational database schema (any project, any language/ORM) must
satisfy BCNF (Boyce-Codd Normal Form): for every non-trivial functional
dependency, the determinant must be a superkey. "Normalized" isn't enough
on its own — verify the actual textbook property, not just an absence of
obvious string-list/comma-joined columns.

**Why:** the user explicitly rejected an informal, heuristic-only
definition of "normalized" and asked for the real BCNF property, checked
and enforced. See [[renar-bcnf]] for the concrete worked example: an
audit caught `comments.title_id`/`season`/`episode`
being copied onto every reply row (a transitive dependency through
`parent_id`), fixed by storing it only on the thread root and deriving it
for replies via a recursive query instead of a stored copy.

**How to apply, for any schema work (new table, new column, or a review):**
1. For every candidate key (primary key and every multi-column UNIQUE
   constraint) in the table, confirm every non-key column depends on the
   *whole* key, not a subset (2NF) and not on another non-key column
   instead of the key (3NF/BCNF).
2. Watch specifically for: a column whose name/value duplicates one
   reachable through one of the table's own foreign keys (a transitive
   dependency); and self-referential copies (a tree/thread structure
   copying an ancestor's attribute onto every descendant row instead of
   deriving it via a walk/recursive query when needed).
3. If the codebase has a mechanical normalization guard test (e.g.
   renar-backend's `tests/test_normalization.py`), run it and extend it
   for the new shape rather than working around it. If the codebase has
   none, consider whether one is warranted, and at minimum note the
   BCNF check was done in the PR/commit description or design docs.
4. A genuine exception (same-named column that's actually a different
   fact, a bounded/derived counter, a cache of an *external* system's
   data keyed on the whole of the row's own key) is fine, but must be
   written down with a justification — never silently allowed to pass
   an existing check, and never left undocumented.
5. Caching a fact from an external system (a third-party API response)
   on the owning row is not a BCNF concern by itself, as long as it
   depends on the whole of that row's own key and nothing else —
   staleness of an external cache and redundant storage of the
   database's *own* data are different properties.
