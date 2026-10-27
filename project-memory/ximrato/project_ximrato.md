---
name: ximrato-project-overview
description: "What ximrato is, its architecture, scope, and key design decisions"
metadata: 
  node_type: memory
  type: project
  originSessionId: 40726a15-54a9-49cc-a7d2-43f6cea2a291
---

Ximrato is a cross-platform (desktop/mobile/web) gym and fitness logger built with Flet (Python). This repo (`ximrato`, to be renamed `ximrato-app`) is the frontend. The backend lives in a separate repo: `ximrato-server`.

**Why:** Personal fitness tracking app with multi-user support and sync across devices.

## Repos
- `ximrato-app` — Flet frontend (this repo)
- `ximrato-server` — REST API backend (FastAPI, separate repo at `d:/Users/{USER}/sw/ximrato-server`)
- VSCode workspace: `d:/Users/{USER}/sw/ximrato.code-workspace`

## Auth
- Self-registration
- JWT-based login against the backend
- Auth events logged to `auth_events` table (event type via `EventType` lookup)
- Auth history screen in the app (`/auth-history`)

<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdABM72A5A6zNQ/xXRaPh66kGhFYxQznfRMEW5/rRT+Xh8w
DYgsFH5kRKsh3yJMdyY4LiOakJ+R2j8CBEbM5mraKrOuCngid6bB0eLvJL/SDG+O
1MBuAQkCEBd5hKpo7gBUQVphpJYZWk8FNR6UI5jXijchdGrnaexNC5iEBJUjLSbD
mLMEH6AUQr3gO1R7HdvzZ91GdXmgPPTr7u5NNUsS497XVzPVdQqaC6nP9lzZSf5a
5XTZzywn6VK+4D8Wrr/OAxYa9Cnh7JlCKRmQ4+oFK5qB4MU8aHEV0CjDibITsCBl
9HlnDDnjHW50r5i4B5pPNsm3H3tgnxTuWGnJ4U+CHtDwRFTu/068u9iHPrLggyvy
rYxlmi4e2GkLqj7VxY+Nmk3wY1l0oOOCQRTPgcTjx2/CiBgCP9TQdhIPJH4WxzFT
ssL3xKgOXTOq/t4sr24lK7mUxdOe2CTz+IZ9sMwQ+THV2gWRzSSd4826oYy51mLg
SZbcxLlk+PB/M3scQNOmNLg=
=DlrV
-----END PGP MESSAGE-----
<!-- /private -->

## User Profile & Config
- Static: display name, sex, date of birth, height, avatar (uploaded file, served from `/static`)
- `UserConfig` (1:1 with User): weight unit, distance unit, height unit, language
- Units config screen: weight (kg/lb), distance (km/mi), height (cm/in)
- Body metrics screen (time-series log): weight, waist, chest, hips, neck, arms, thighs

## i18n
- Three languages: English (`en`), Spanish (`es`), Galician (`gl`)
- Language stored in `UserConfig.language_id` (FK to `languages`) and locally in `SharedPreferences`
- `__lang_explicit` flag in session store distinguishes user choice from auto-detected default

## Exercise Types (v1)
- **Strength** — DB-seeded fixed list. Bodyweight exercises use weight=0 + `bodyweight_counted` flag.
  - Each exercise has: `name`, `category_id` (FK → `exercise_categories`), `equipment_type`, `primary_muscles` (JSON array), `secondary_muscles` (JSON array), `description`, `name_es`, `name_gl`
- **Cardio** — running, cycling, rowing only for v1. DB-seeded.
  - Each cardio exercise has: `name`, `name_es`, `name_gl`

## Logging Flows
- **Session** — strength only. User starts session, logs sets freely across exercises, clicks end. `workout_sessions` table has `started_at` / `ended_at` and `notes`.
- **Quick log** — cardio only. No session wrapper needed.
- **Body metrics** — separate button/screen, not tied to sessions.

## Data Model — Strength

### `workout_sessions`
- `id`, `user_id` (FK), `started_at`, `ended_at` (nullable), `notes` (nullable), `created_at`, `updated_at`

### `workout_sets`
- `id`, `session_id` (FK → `workout_sessions`), `exercise_id` (FK → `exercises`), `reps`, `weight` (float), `bodyweight_counted` (bool), `rpe_level_id` (FK → `rpe_levels`, nullable), `to_failure` (bool), `logged_at`, `created_at`, `updated_at`
- No `session_exercises` join table — sets point directly to session + exercise
- No `rest_seconds` on sets (only on cardio)

### `rpe_levels` (lookup)
- Qualitative labels (no numbers shown to user): No reps left / Could do 1 more / Could do 2 more / Could do 3 more / Could do 4–5 more / Very light

## Data Model — Cardio

### `cardio_logs`
- `id`, `user_id` (FK), `exercise_id` (FK → `cardio_exercises`), `duration_seconds`, `distance` (nullable), `logged_at`, `rest_seconds` (nullable), `avg_heart_rate` (nullable), `elevation_gain` (nullable), `stroke_rate` (nullable/rowing), `created_at`, `updated_at`

## Data Model — Body Metrics

### `body_metrics`
- `id`, `user_id` (FK), `logged_at`, `metric_type_id` (FK → `metric_types`), `value` (float), `created_at`, `updated_at`

## Data Model — Auth

### `auth_events`
- `id`, `user_id` (FK), `event_type_id` (FK → `event_types`), `occurred_at` (indexed), `updated_at`

## Data Model — Security

### `banned_ips`
- `id`, `ip`, `reason`

## Lookup Tables
`event_types`, `rpe_levels`, `exercise_categories`, `sexes`, `weight_units`, `distance_units`, `height_units`, `languages`, `metric_types`

## Progress Screen
- `/progress` — canvas-drawn line charts (no external charting lib)
- Two tabs: Strength (exercise progress — max weight per session) and Body (body metric over time)
- Tab and selected exercise/metric persisted in session store across navigation

## App Routes
`/login`, `/register`, `/home`, `/profile`, `/account`, `/auth-history`, `/settings`, `/session`, `/session-history`, `/cardio`, `/cardio-history`, `/metrics`, `/progress`

## Schema Patching
Server uses `_apply_schema_patches()` at startup to add new columns if absent — safe to run on existing DBs without migrations.

## v2 Scope (deferred)
- HIIT / circuit training
- Sports logging
- Additional exercise categories (swimming, jump rope, etc.)
- Additional body measurements beyond the v1 set
