---
name: Project avalio
description: Avalio project structure, repos, and GitHub locations
type: project
originSessionId: e132952d-97d2-4a9b-a700-0c502415f387
---
Two repos under GitHub account Ran-n, both public:
- Frontend: https://github.com/Ran-n/avalio-frontend — Flet (Python) desktop app, located at `d:/Users/{USER}/sw/avalio/avalio-frontend`
- Backend: https://github.com/Ran-n/avalio-backend — FastAPI (Python) REST API, located at `d:/Users/{USER}/sw/avalio/avalio-backend`

Both initialized 2026-04-21 from local folders (no prior git history).
Backend uses SQLite (`avalio.db`), Alembic for migrations, uv for package management.
Frontend uses Flet UI framework, uv for package management.

**Why:** monorepo split into two separate public GitHub repos per user request.
**How to apply:** when referencing repos or pushing changes, use the above URLs and paths.
