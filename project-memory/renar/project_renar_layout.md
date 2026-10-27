---
name: project-renar-layout
description: "Renar is two separate git repos (renar-backend/ FastAPI, renar-frontend/ Flet) inside one non-repo parent folder; envs managed with uv"
metadata: 
  node_type: memory
  type: project
  originSessionId: 430e967c-7c13-4d0d-b2e4-023dd0a6c413
---

Renar (D:\Users\{USER}\sw\renar) is a TV Time-style media tracker (films, TV shows, YouTube videos). The parent folder is NOT a git repo; `renar-backend/` and `renar-frontend/` (renamed from backend/frontend on 2026-07-03) are each their own independent git repository — commit to each separately.

- Environments use **uv** (uv venv + uv pip install -r requirements.txt; run via `uv run ...`). uv venvs have no pip, so the frontend needs `flet[all]` (plain `flet` makes `flet run` try to pip-install flet-cli at runtime and fail).
- `renar-backend/`: FastAPI + SQLAlchemy + SQLite + Alembic (schema owned by migrations, batch mode for SQLite). Run: `uv run uvicorn app.main:app --port 8000`.
- `renar-frontend/`: Flet pinned `flet[all]==0.28.*` (0.85+ alpha API breaks the code). Run: `uv run flet run --web --port 8550 main.py`. Backend URL via `RENAR_API_URL`.
- Servers must be started as detached processes (Start-Process -WindowStyle Hidden), NOT harness background tasks — those get killed between turns.
- The user keeps the project open in VS Code, whose git extension holds handles on `.git` dirs and blocks folder renames — ask them to close the folder first.
- A commit hook on this machine rejects `Co-Authored-By:` trailers — commit without them. See [[feedback-commits]].
