---
name: price-api-architecture
description: "reska-op-price-api architecture — models, scrape flow, endpoints, valuations, and Windows startup fix"
metadata: 
  node_type: memory
  type: project
  originSessionId: bd31526a-760e-45a9-9552-095a50ff7e91
---

## Stack
FastAPI + SQLAlchemy asyncio + psycopg3 + PostgreSQL (`reska_op_price` DB). Port 8002. Run via `uv run python -m reska_op_price_api`. Python 3.14, ruff-clean (preview rules — uses PEP 758 parenthesis-free `except`), pytest suite in `tests/` (parsers, slugify, valuation stats, route smoke test). Git repo (local only, branch `main`) since 2026-07-02, v0.2.0. A commit-msg hook rejects `Co-Authored-By` lines.

## Models
- **Source**: scraping source (name, currency, base_url). Cardmarket seeded on startup.
- **NaipUrl**: maps (naip_id, source_id) → product_url. Required before scraping a naip.
- **Listing**: active market listing (naip_id, source_id, price, condition, seller, scraped_at, removed_at)
- **Sale**: one row per (naip_id, source_id, day) — **daily average price from Cardmarket's chart**, condition/seller null. Deduplicated on (naip_id, source_id, sold_at).
- **PriceGuide**: snapshot per scrape of Cardmarket's price guide (price_trend, avg_sell_1d/7d/30d), parsed from `dl.labeled`.
- **ApiKey**: BLAKE3-hashed keys for read endpoints.

## Scraper transport
**FlareSolverr** (HTTP API at `localhost:8191`) renders pages past Cloudflare; requests proxied through **Tor** (`socks5://127.0.0.1:9050`). Both are **auto-started as subprocesses on server startup** (`core/services.py`, `FLARESOLVERR_BIN`/`TOR_BIN` config) and stopped on shutdown. `fetch_html(url)` in `scrapers/base.py` is the single entry point, 3 retries.

## Cardmarket scraper (`scrapers/cardmarket.py`)
- **Listings**: paginates `?language=0&minCondition=0&start=N&rows=20` until short page; parses `div.article-row`.
- **Sales**: parsed from the price chart JSON in `script.chart-init-script` (`new Chart(..., {json})`) — daily average prices, NOT a sales table.
- **Price guide**: `dl.labeled` dt/dd pairs (Price Trend, 1/7/30-day averages).
- `scrape_sales` returns `(sales, price_guide | None)`.

## Key endpoints
<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdA8RlwOqgtGfZ9jkqCub0ZIU9CmZiTT+GWNsj4hDPYLDEw
uDb3gtzxO/9oqOz0yL5h5crr+RbQfQayD3Z7x+GzVEjRSkVDDiLzxQg1HmLXElTm
1MByAQkCEHVaoK9oHAC+tcq6us3kIqE1+y39ZvviYYZIG4AnbfBns8N0CcgI7B1W
DuT/3kP+tKRy3sWPrsM1U+Wgkimu4MJv0w4BhpN70VndqIHmqmLGmdiszON2WsOo
fhJbtRW+D8i+Tmha0NogooYJEvt8rYki/Oj+8kUJfp6C8AE9dNxFIemNYrsyRw6D
CpvS+Xm/iBIuNAgkmN+NR7q25mZeMzvD34Ukm4RCirfpiuc2m0TbZsaB9k5WQgmj
ssKGqAC0Msk7/7Wvl34KvPaHdkXkBIEPaukNESTK+ZMja4Nv0YddpftspDAQmIgH
IDlrwdytz7z3/vM/vVVTKpY8OJZiHd8zD9iRGzPv/jHRjF4QE+iOw9nQs5zz1tRy
Nm0iAGDyKNAJ6wKwQCwR2TALJQnO
=woq5
-----END PGP MESSAGE-----
<!-- /private -->
- API key (`X-API-Key`): `GET /listings/`, `GET /sales/`, `GET /valuations/`.
- **`GET /valuations/`** (`routers/valuation.py`): per-naip, per-source + aggregate stats — sale median/min/max/avg over `days` window (default 90), lowest active listing, latest PriceGuide snapshot; `valuation` = sale median, fallback lowest listing. `naip_id` repeatable; omit to value all naips with recent data.

## Cardmarket URL format
`https://www.cardmarket.com/en/OnePiece/Products/Singles/{set_slug}/{name-slug}-{SET_CODE}-{3-digit-number}` (+`-V{sort_order+1}` for alt prints). Slug: strip `.''`, replace non-alphanum runs with `-`, strip leading/trailing `-`.

## Windows event loop fix
psycopg3 async requires SelectorEventLoop. `__main__.py` passes `loop="reska_op_price_api.core.loop:selector_loop_factory"` to uvicorn (zero-arg factory returning SelectorEventLoop; works in `--reload` watcher too). No Playwright anywhere — scraping is pure HTTP via FlareSolverr.

## Dev notes
- `scripts/dump_page.py` dumps rendered Cardmarket HTML to d:/tmp for selector debugging.
- While the server is running, `uv run` can't re-sync (`api.exe` locked) — use `uv run --no-sync`.
- LICENSE = PayBack License v2.0 + CONTRIBUTORS file (same as card-api).

[[project-context]]
[[card-api-schema]]
