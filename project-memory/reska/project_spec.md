---
name: reska-project-spec
description: "UX, behaviour, and technical requirements for the Reska card collection app (frontend + backend)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8c802fff-569c-4dac-b64d-f4a6c068f2ba
---

# Reska — Project Spec

> *From Latin **res** (a thing owned) + Japanese **カ** (the world of cards). A place for the things you collect.*

## Overview

A desktop/web/mobile card collection app, initially focused on **One Piece TCG**, with multi-game support planned.
Split into three active repos plus a defined future service:

- **reska-frontend** — Flet (Python), targets desktop / web / mobile
- **reska-auth** — FastAPI (Python), PostgreSQL (`reska` DB); auth only (login, register, JWT, logout)
- **reska-backend** — FastAPI (Python), PostgreSQL (`reska_app` DB); collection, social, tournaments, all app features

### Future services (not in v1)
- **reska-prices** — dedicated price API; scrapes/aggregates market prices (Cardmarket, TCGPlayer, eBay, etc.) per naip; stores historical snapshots for value-over-time graphs; reska-backend calls this to enrich collection responses
- **reska-aggregator** — federates multiple game-specific card APIs (optcg_api, future mtg_api, pokemon_api, etc.) behind a single endpoint; reska-backend would call this instead of individual game APIs once multi-game support is needed

### Card data API philosophy
Game-specific card data APIs follow the pattern `reska-[game]-card-api` (e.g. `reska-op-card-api`, future `reska-mtg-card-api`, `reska-pkm-card-api`). Each is a standalone public API for its game. `reska-aggregator` is the future abstraction layer that federates them.

### Service architecture

- `reska-auth` owns login/register/refresh/logout and the user table. Default port 8000.
- `reska-backend` verifies JWTs **stateless** (shared `SECRET_KEY`, no DB lookup); returns caller UUID from `sub` claim. Default port 8001.
- `reska-backend` calls **optcg_api** (port 8000 by default) for card data; enriches responses with user collection metadata.
- `reska-auth` exposes `GET /users/{username}/exists` for lightweight user existence checks by reska-backend (e.g. friend-code validation).
- Frontend uses `AUTH_BASE_URL` for reska-auth calls and `API_BASE_URL` for reska-backend calls.

### Card data source

`optcg_api` — Ran#'s own FastAPI service at `d:/Users/{USER}/sw/optcg_api`. Endpoints used:
- `GET /cards/` — paginated card list (filters: name, set_id, cardtype_id); returns `CardListItem` with image_path
- `GET /cards/{id}` — full card detail (`CardDetail`): name, effect, trigger, power, life, counter, cost, colors, tribes, attrs, keywords, reswords, formats, naips[]
- `GET /sets/` — set list; each set has `language_fk` and optional `parent_fk` (language variants point to a parent)
- `GET /lookups/` — colours, types, rarities, languages, regions, print variants, etc.
- `GET /naips/` — physical prints (naip = card + set + artist + print_variant + is_foil + language_fk)

**Key data model concepts:**
- `Set` is language-specific: OP01-EN and OP01-JP are different rows, linked by `parent_fk`
- `Region` groups languages (e.g. "Global" maps to EN; future regions for JP, FR, etc.)
- `Card` is the logical card (language-neutral game object, tied to a language via its set)
- `Naip` is a specific physical print: card + set + print_variant + is_foil + artist + language override; this is what a collector actually owns
  - `print_variant`: STD, ALT, SECRET, etc. (hierarchical via `parent_fk`)
  - `is_foil`: bool
  - `serial_max`: for serialised/numbered cards
- `NaipSerial`: a specific known serial number of a serialised naip

**API gap for v1:** `GET /cards/` currently only filters by name, set_id, cardtype_id. The Browse tab needs colour and rarity filters — these will need to be added to optcg_api.

### Collection ownership model (reska-backend)

A user owns copies of a specific **Naip** (not just a card), because the same card can exist in multiple print variants and foil states. Ownership is tracked **per individual copy** — each copy is its own row:
- `naip_id` (references optcg_api naip)
- `condition` (NM / LP / MP / HP / DMG — defaults to NM on add)

Total copies owned = count of rows for that naip. Language is derived from the naip's set `language_fk` — no separate language field needed.

## Status

As of 2026-06-29:
- **reska-auth**: fully implemented (login, register, JWT refresh tokens, logout, `/me`).
- **reska-backend**: fully implemented for v1 scope — collection CRUD (`/collection/`), optcg proxy (`/sets/`, `/settypes/`, `/cards/`, `/cards/{id}`), dashboard (`/dashboard/`, `/prices/{naip_id}`), mock price store (`mock_prices` table seeded on demand). `reska_app` DB on port 8001.
- **reska-frontend**: fully implemented for v1 scope — shell with nav bar (Home / Collection / Browse tabs), home dashboard tab (collection value + top holdings), collection tab (set list with type sub-tabs, card grid with inline add/remove), browse tab (search + set filter, card detail bottom sheet with add-to-collection). Auth views (login, register) remain from before.

### Auth decisions
- Access token: JWT HS256, 15 min TTL; `sub` = user UUID
- Refresh token: 64-char hex (BLAKE3-hashed in DB), 30-day TTL, rotated on use
- Password hashing: Argon2id
- Registration: open (anyone can register)

### Identity model

| Field | Login credential | Uniqueness | Allowed characters |
|---|---|---|---|
| `username` | Yes (primary login identifier) | Global, case-insensitive | ASCII: `a-z`, `0-9`, `_`, `-`; 3–32 chars; must start with a letter or digit |
| `display_name` | No | Global, Unicode-normalised (NFC, case-folded) | Any Unicode except control chars and leading/trailing whitespace; 1–64 chars |

**Rules:**
- Usernames are stored lowercased; comparison is always lowercased.
- Display name uniqueness is checked after Unicode NFC normalisation + case-folding (so "Ñoño" and "ñoño" collide).
- Both fields have a unique index in the DB.
- JWT `sub` claim carries the user **UUID** (not username).
- `username` is **immutable** after registration; `display_name` is freely changeable (still subject to uniqueness — no two accounts may hold the same display name at the same time).

## Technical Requirements

| Concern | Decision |
|---|---|
| Python version | 3.14+ (all repos) |
| Package manager | uv |
| Frontend framework | Flet |
| Backend framework | FastAPI |
| Database | PostgreSQL (separate DBs per service) |
| License | PayBack License (PBL) |

## UX — Screen Structure (v1)

### Tab 1 — Home (Dashboard)
- Total collection value (sum of all owned cards' market prices)
- Price history graph — collection value over time
- Top value items list — highest-value cards the user owns

### Tab 2 — Collection
- Header: region selector (e.g. "Global") + grid/list toggle + filter icon + search icon
- Sub-tabs: **Booster | Starter | Promo | Other** (horizontal tab bar; hardcoded for v1, driven by `set_type` in a future iteration)
- Under each sub-tab: game group header showing circular completion ring + game name + overall % complete
- Set list rows beneath, each containing:
  - Circular badge with set code (OP01, OP02, ST01…)
  - Set name
  - Owned / total count right-aligned (e.g. 125/155)
  - Horizontal progress bar (red fill on dark track) below the set name row
- Tap a set → card grid for that set
  - Each item: image, name, card number (or product name), owned count
  - Inline add / remove button (no dialog)
  - Sealed products (packs, boxes) use the same tile format as cards; image is the front of the product
- Cards can also be added via **Search** (by name or card code) anywhere the add flow is reachable
- Visual theme: dark (charcoal/near-black background), red accent colour for progress bars and highlights

### Tab 3 — Browse (optcg.app style)
- Full card catalogue with filters: set, colour, type, rarity, name/keyword
- Card grid with images
- Tap a card → card detail view (full art, stats, rulings if available from optcg_api)
- Add-to-collection button on detail view

### Add flow (shared)
Two entry points reach the same result:
1. **Search** — type name or card code → results list → tap Add
2. **Set browser** (Collection tab) — navigate set → card grid → tap Add

Tapping Add silently creates one new copy of that naip (condition defaults to NM). No dialog or picker.

### Copies detail view
Each card tile shows the total number of copies owned. Tapping "see copies" opens a list of individual copy entries for that naip — one row per copy, each showing its condition. Copies can be edited (change condition) or deleted inline from this view.

### Price data (v1 stub)
No real price source yet. Build a mock: static or randomly-seeded price values per naip, stored in reska-backend. The Home dashboard and card detail view are built against this mock so the UI is complete. Swap for a real source later without frontend changes.

### Out of scope for v1
- Deck building
- Trade features
- Tournaments
- Multi-game support beyond One Piece TCG

## Scope (known)

- Browse One Piece TCG cards (via optcg_api)
- User collection management (copies owned per card)
- Collection value tracking with price history graph
- Social features: friend requests via QR / friend code; lazy resolution (no hard existence check required)
- Future: deck building, trades, tournaments, multi-game support

## Open Questions

- Offline-first vs online-first
- Deployment target (self-hosted, cloud, packaged desktop app?)
- Price data source (v1 uses a mock; real source TBD)
