---
name: optcg-api-project
description: "Core facts about the optcg-api project — stack, entry point, tooling, current state"
metadata: 
  node_type: memory
  type: project
  originSessionId: 86a311e0-a51b-4166-9e25-fed495c71001
---

FastAPI REST API for One Piece TCG card information. Package name: `optcg-api`, version `0.1.0`. License: PayBack License (PBL) v2.0.

- Entry point: `src/optcg_api/main.py` — creates FastAPI app with lifespan calling `init_db()`, CORS middleware (allow_origins=["*"]), includes all 3 routers
- No CLI script alias (removed `opapi` script)
- Runtime deps: FastAPI ≥0.135.2, uvicorn ≥0.42.0, sqlmodel ≥0.0.38, alembic ≥1.18.4, beautifulsoup4 ≥4.14.3, httpx ≥0.28.1, python-multipart ≥0.0.28; Python ≥3.14
- Dev deps: pytest ≥9.0.2, ruff ≥0.15.7
- Build system: setuptools, packages found under `src/`
- Ruff: line-length 120, target py314, rules E/F/I/B/UP/SIM, double quotes, space indent

**Git remotes:** `origin` → GitHub (`git@github.com:Ran-n/optcg_api.git`), `gitlab` → GitLab (`git@gitlab.com:Ran-n/optcg_api.git`), `codeberg` → Codeberg (`git@codeberg.org:Ran-n/optcg_api.git`). Push to all three on every push. (Note: global memory says "github"+"gitlab" but this repo uses `origin` for GitHub and adds `codeberg`.)

**Current state (2026-06-03):** 5 Alembic migrations; language images seeded; data/images/ reorganised into cards/ and langs/.

**Database layer** (`src/optcg_api/database.py`):
- SQLite at `./data/optcg.db`, engine + `init_db()` (calls `alembic upgrade head`) + `get_session()` dependency

**Models** (`src/optcg_api/models.py`):
- Lookup tables: `SetType`, `CardType`, `Artist`, `Rarity` (C/UC/R/SR/SEC/L/D/P only — no `is_type`/`is_base`), `PrintVariant` (STD/AA/TR/SP/GR/MR/EMR/RMR/FA/AUD/PTR/MTR/AU/AG; `parent_fk` self-ref hierarchy), `Tribe`, `Attribute`, `Color`, `Block`, `Format`, `Keyword`, `Resword`, `Language`, `Region`, `RegionLanguage`
- Dedup/text tables: `Name`, `Image`, `Effect`, `Trigger`
- Core tables:
  - `Set` — `(code, language_fk)` unique, `type_fk`, `name`, `series`, `ord`, `release_ts`
  - `Card` — `set_fk`, `cardtype_fk`, `name_fk`, `rarity_fk` (nullable canonical base rarity), `effect_fk`, `trigger_fk`, `block_fk`, `number`, `power`, `life`, `counter`, `cost`; unique `(set_fk, number)`
  - `Naip` — physical print; `card_fk`, `set_fk`, `artist_fk`, `print_variant_fk` (NOT NULL), `name_fk`, `image_fk`, `effect_fk`, `trigger_fk`, `is_default`, `is_errata`, `is_foil`, `sort_order`, `serial_max`, `cardtype_fk`, `block_fk`, `language_fk`, `power`, `life`, `counter`, `cost`; partial unique `ix_naip_unique_print` on `(card_fk, set_fk, artist_fk, print_variant_fk, is_foil)` where `artist_fk IS NOT NULL`
  - `NaipSerial` — known revealed copies; `naip_fk`, `serial_number`, `image_fk`; `serial_number >= 1`
- Card junction tables: `CardTribe`, `CardAttribute`, `CardColor`, `CardFormat`, `CardKeyword`, `CardResword`
- Naip junction tables: `NaipColor`, `NaipTribe`, `NaipAttribute`, `NaipKeyword`, `NaipResword`
- Ban tables: `CardBan` (per-card ban, optional `format_fk`), `BannedPair` (`card_a_fk < card_b_fk` constraint, optional `format_fk`)
- Audit tables: `CardEffectHistory`, `CardTriggerHistory`
- All tables: `id`, `created_ts`, `updated_ts` (SQLite server_default + AFTER UPDATE triggers)

**Routers** (`src/optcg_api/routers/`):
- `cards.py` — full CRUD; `CardDetail` exposes `rarity_fk`/`rarity_name`/`rarity_symbol` (card-level); `NaipItem` exposes `print_variant_name`/`print_variant_symbol`/`is_foil`; `CardWrite` accepts `rarity_fk`; no longer exposes `rarities` list
- `naips.py` — full CRUD (`GET/POST/PUT/DELETE /naips/{id}`); `NaipDetail` exposes `print_variant_fk`/`print_variant_name`/`print_variant_symbol`; `NaipWrite` accepts `print_variant_fk`; per-naip junction sync + orphaned-image cleanup
- `sets.py` — read-only `GET /sets/`, `GET /sets/{id}`
- `lookups.py` — `GET /lookups/{type}` for all lookup types including `GET /lookups/print-variants` (returns `symbol`, `name`, `desc`, `parent_fk`)

**Alembic migrations** (`alembic/versions/`):
- `0001_initial` — full schema, all triggers, seed data (languages/regions)
- `0002_naip_is_foil` — `Naip.is_foil`; idempotent (skips if column exists in squashed DB); removes `FD` rarity
- `0003_print_variant` — `print_variant` table + seed (14 variants); `Card.rarity_fk`; rebuilds `naip` with `print_variant_fk` replacing `rarity_fk`; strips `is_type`/`is_base` from `rarity`; removes `NFD` rarity

**Scripts:** `scripts/ingest.py` — sets `card.rarity_fk` from scraped rarity symbol; recognises print_variant symbols and skips them (no naip rows created during ingest yet); unknown symbols raise `RuntimeError`

**Why:** Project moved past skeleton to real implementation with full card CRUD + lookup APIs.
**How to apply:** Always run `ruff format` + `ruff check` on every edited `.py` file; fix errors per ruff config.
