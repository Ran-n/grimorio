---
name: ximrato project overview
description: What ximrato is, its architecture, v1/v2 scope, data model, and key design decisions
type: project
---

Ximrato is a cross-platform (desktop/mobile/web) gym and fitness logger built with Flet (Python). Frontend repo: `ximrato-app`. Backend repo: `ximrato-server`.

**Why:** Personal fitness tracking app with multi-user support and sync across devices.

## Repos
- `ximrato-app` — Flet frontend (`d:/Users/{USER}/sw/ximrato-app`)
- `ximrato-server` — FastAPI REST backend (`d:/Users/{USER}/sw/ximrato-server`)
- VSCode workspace: `d:/Users/{USER}/sw/ximrato.code-workspace`

## Auth
- Self-registration
- JWT-based login against the backend

## User Profile & Config
- Static: display name, sex, date of birth, height, profile picture
- Units config screen: weight (kg/lb), distance (km/mi), height (cm/in)

## Logging Flows (v1)
| Flow | What it logs | Session wrapper |
|------|-------------|-----------------|
| Session | Strength exercises | Yes — start / end |
| Quick log | Cardio | No |
| Body metrics | Body measurements | No |

## Exercise Types (v1)
- **Strength** — DB-seeded, fixed list. Bodyweight: weight=0 + bodyweight_counted flag.
- **Cardio** — running, cycling, rowing only.

## Strength Set Fields
- reps, weight (decimal; 0 for bodyweight), bodyweight_counted (boolean)
- RPE: qualitative labels only (no numbers shown to user):
  - No reps left / Could do 1 more / Could do 2 more / Could do 3 more / Could do 4–5 more / Very light
- to_failure (boolean)
- logged_at (timestamptz) — used to derive rest time between sets
- rest_seconds (integer, null for first set) — denormalized for read performance

## Cardio Log Fields
- duration_seconds, distance, logged_at, rest_seconds
- avg_heart_rate (optional), elevation_gain (optional), stroke_rate (optional, rowing)
- Single table for all cardio types with optional columns per type

## Body Metrics (time-series)
weight, waist, chest, hips, neck, arms, thighs. Height is static on user profile.

## Data Model Notes
- All tables: created_at, updated_at
- `session_exercises` join table with `order` column — same exercise can appear multiple times in a session
- rest_seconds stored explicitly (denormalized) for read performance, derived from adjacent logged_at timestamps

## v2 (deferred)
- HIIT / circuit training
- Sports logging
- Additional exercise categories (swimming, jump rope, etc.)
- Additional body measurements beyond the v1 set

**How to apply:** When implementing any feature, check v2 list before adding scope. Data model decisions (single cardio table, denormalized rest_seconds) are intentional v1 tradeoffs.
