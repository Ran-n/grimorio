---
name: source-tree-organization-principles
description: Principles governing how files/directories inside src/ are grouped — distinct from SOLID (which governs classes/functions, not files)
metadata:
  type: feedback
---

Apply these when creating new modules, deciding where a file belongs, or reviewing a source tree that has grown organically (many peer files in one directory, one file doing the job of several).

**Why:** SOLID (specifically SRP) explains *that* an oversized file/class needs splitting, but says nothing about *where* the resulting pieces should live on disk. These principles fill that gap. Surfaced when reviewing renar-backend's `src/renar_backend/` (22 flat peer files) and `routers/admin.py` (126KB vs. a ~20KB next-largest router) — a Common Closure Principle violation with no documented rationale in `docs/design-decisions.md`.

**How to apply:** Whenever adding a new module, ask "what changes together?" before "what layer is this?" — then use these principles to name and place the file. Apply proactively when reviewing/reorganizing an existing tree, not just when writing new code.

## Package cohesion principles (Robert C. Martin, *Agile Software Development*)

- **REP — Reuse/Release Equivalence Principle**: things released and versioned together belong in the same package. Relevant when a subsystem is (or could become) its own installable/deployable unit.
- **CCP — Common Closure Principle**: classes/modules that change for the same reason, at the same time, belong in the same directory. This is the direct file-system analogue of SRP — the most actionable lens for "why does this file keep growing" or "why are these two files always edited together." A god-file (e.g. one `admin.py` handling users, media, moderation, stats, and config) is a CCP violation as much as an SRP one.
- **CRP — Common Reuse Principle**: don't force consumers to depend on things they don't use. Classes used together belong together; classes *not* used together should not be forced into the same package. Guards against directories that are cohesive in name only.

## Package coupling principles (same source)

- **ADP — Acyclic Dependencies Principle**: no cycles in the package/module dependency graph. Check with an import graph, not by inspection.
- **SDP — Stable Dependencies Principle**: depend in the direction of stability — volatile packages depend on stable ones, never the reverse.
- **SAP — Stable Abstractions Principle**: stable packages should be abstract (interfaces/protocols), so they can be depended on without becoming a change bottleneck.

## Higher-level organizational patterns

- **Package by layer vs. package by feature**: layer (`routers/`, `services/`, `models/`) is the default most codebases start with; feature/domain (`billing/`, `auth/`, `media/`, each owning its own routes + models + services) scales better as the domain grows, because CCP-related changes stay in one folder instead of touching one file per layer. A codebase can mix both: layer at the top (`routers/` as the HTTP boundary), feature within a layer (`routers/admin/users.py`, `routers/admin/media.py`) once a single layer-file exceeds the god-object threshold.
- **Screaming Architecture** (Uncle Bob): top-level folder names should announce the *domain* (`billing/`, `catalog/`, `notifications/`), not the framework or layer (`routers/`, `utils/`, `helpers/`). Looking at the top-level tree should tell you what the app *is*, not what web framework it uses.
- **Hexagonal / Ports & Adapters**: separate domain/business logic from framework and I/O adapters (DB access, HTTP clients to third parties, the web framework itself). Domain code should not import framework code; adapters implement interfaces the domain defines.
- **Law of Demeter / dependency direction**: pick and enforce one direction — e.g. `routers → services → models`, never the reverse. A file that imports "up" a layer is a structural smell even if each individual file looks fine.
- **Colocation**: files that are almost always edited together (a router and its Pydantic schemas, a model and its Alembic migration helpers) benefit from living near each other rather than being split purely by technical type, if CCP and CRP agree.
- **God-object / god-file threshold**: reuse the existing "no file over ~200 lines without a strong reason" rule from [[feedback_clean_code.md]] as the trigger to apply CCP and split by what-changes-together, not just extract-and-rename.

## Practical checklist when reorganizing an existing flat/organic tree

1. Grep the import graph before moving anything — know every caller (ties into [[feedback_regression_safety.md]]).
2. Group files by CCP first ("what changes together"), then sanity-check with CRP ("is everything in this group actually used together").
3. Split any file over the god-object threshold along CCP lines, not arbitrary line-count halves.
4. Keep the dependency direction one-way (SDP/ADP) — a domain package should never import back from a layer that depends on it.
5. Name top-level folders after domain nouns (Screaming Architecture), reserve layer names (`routers`, `services`) for the level below domain, if both are needed.
6. Update every import site in the same change; run lint/tests immediately after, don't leave the tree in a half-moved state.
7. Document the resulting structure and its rationale in the project's design-decisions doc so the next review doesn't rediscover the same question.
