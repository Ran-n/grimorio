---
name: preferred-stack
description: Default software stack for new apps — uv, FastAPI + SQLAlchemy/Alembic backend, Flet frontend, pytest, ruff
metadata:
  type: reference
---

Default stack for new app projects unless the user says otherwise (confirmed 2026-09-30, derived from renar and avalio):

- **Tooling:** Python, **uv** for envs (`uv run ...`), pyproject.toml per [[reference_pyproject_scaffold]], ruff per [[feedback_python_projects]].
- **Backend:** FastAPI + Uvicorn; SQLAlchemy ORM; Alembic owns the schema (batch mode for SQLite); SQLite locally, Postgres on a VPS.
- **Frontend:** Flet (desktop/web/Android), talks to the backend over HTTP; backend URL from an env var. Pin `flet[all]==0.28.*` (0.85+ alpha API broke renar) — re-check before pinning on new projects.
- **Tests:** pytest per [[feedback_tests]] — backend via httpx.AsyncClient + ASGITransport on a real DB, frontend via respx-mocked httpx.
- **Layout:** two independent git repos `<name>-backend/` and `<name>-frontend/` under a non-repo parent folder (like renar).

**How to apply:** When scaffolding or planning a new app, propose this stack by default; only deviate when the project clearly doesn't fit (e.g. a pure CLI/library).
