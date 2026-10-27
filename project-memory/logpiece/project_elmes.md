---
name: project-elmes
description: "elmes — La Resistencia classical-question scoreboard tracker; FastAPI + SQLite backend, Flet frontend; lives at d:\\Users\\{USER}\\sw\\elmes"
metadata: 
  node_type: memory
  type: project
  originSessionId: 678d79c6-7c6c-40dc-b17f-122b342d5b61
---

## Purpose

**elmes** tracks the two "preguntas clásicas" (classical questions) that David Broncano asks every guest on *La Resistencia* (Movistar+):

1. ¿Cuánto dinero tienes en el banco? — how much money in your bank account?
2. ¿Cuántas relaciones sexuales has tenido en el último mes? — how many sexual encounters in the last month?

Both answers are stored as free-text strings (guests often dodge, give ranges, or refuse), keyed to a guest appearance (name + season + episode). The app builds a persistent "marcador" (scoreboard) across the full run of the show.

**Why:** fan project; data source is public show broadcasts.

## Location

`d:\Users\{USER}\sw\elmes`

## Stack

| Layer    | Library / Tool |
|----------|----------------|
| Frontend | Flet ≥ 0.22 (Python, Flutter-based, cross-platform) |
| Backend  | FastAPI ≥ 0.111 + Uvicorn |
| Database | SQLite via SQLModel ≥ 0.0.19 |
| Build    | Hatchling (pyproject.toml) |
| Lint     | Ruff |
| Python   | ≥ 3.11 |

## Module Layout

```
src/elmes/
├── __init__.py
├── backend/
│   ├── __init__.py
│   ├── main.py       — FastAPI app, startup hook, router registration
│   ├── db.py         — engine, init_db(), get_session() dependency
│   ├── models.py     — Guest (table), GuestCreate, GuestRead (SQLModel)
│   └── routes.py     — /guests CRUD router (list, get, create, update, delete)
└── frontend/
    ├── __init__.py
    └── main.py       — Flet app entry point (ft.app)
```

## Data Model

`Guest` table:
- `id` (PK, auto)
- `name` (str) — guest name
- `season` (int)
- `episode` (int)
- `money` (str, optional) — free-text bank answer
- `relations` (str, optional) — free-text monthly relations answer

## Running

```bash
# backend
uvicorn elmes.backend.main:app --reload

# frontend (separate terminal)
flet run src/elmes/frontend/main.py
```

## Planned Features (not yet implemented)

- Full Flet UI: guest list view, add/edit form, scoreboard aggregation view
- Filter/search by guest name, season, episode
- Stats: average answers, refusal rate, most/least forthcoming guests
- Possible: web-based Flet deployment

## Git

- Branch: `main`
- Initial commit: f2b8fd3
- No remote yet (user will add when ready)

**How to apply:** Read this at session start when working in `d:\Users\{USER}\sw\elmes`. The backend API is already wired (CRUD routes at `/guests`); frontend is a skeleton only.
