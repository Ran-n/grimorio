---
name: logpiece-project
description: "Core facts about the logpiece project — stack, entry point, tooling, current state"
metadata: 
  node_type: memory
  type: project
  originSessionId: c85bb7cb-940d-4a0f-a12b-4a56faef98ad
---

logpiece — PySide6 desktop app for browsing and editing the optcg_api SQLite database.

**Stack:** Python 3.14+, PySide6, SQLModel, uv, ruff

**Entry point:** `logpiece.app:main` (defined in pyproject.toml scripts)

**Module layout:**
- `src/logpiece/app.py` — MainWindow + main()
- `src/logpiece/db.py` — SQLModel session + typed queries + generic table CRUD
- `src/logpiece/models.py` — SQLModel table definitions mirroring optcg_api
- `src/logpiece/theme.py` — palette constants + global stylesheet
- `src/logpiece/widgets/` — CardBrowserPanel, CardDetailPanel, CardListItem, TablePanel

**Related projects:**
- `optcg_api`: FastAPI backend + SQLite DB at `d:\Users\{USER}\sw\optcg_api` — [[optcg-api-project]]
- Models in logpiece mirror `d:\Users\{USER}\sw\optcg_api\src\optcg_api\models.py` exactly

**How to apply:** See [[logpiece-project-spec]] for full design rules and UX spec.
