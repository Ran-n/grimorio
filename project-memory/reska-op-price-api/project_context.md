---
name: project-context
description: "Reska system overview — One Piece TCG collection platform, microservice architecture, ports, and running state"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4ef1695b-1fbb-4e51-8b26-676bb85d3dd2
---

Reska is a trading card collection management app focused on One Piece TCG (OPTCG). It is a microservice system:

- **reska-auth** (d:\Users\{USER}\sw\reska\reska-auth): FastAPI + PostgreSQL, JWT auth, port **8008**, HTTPS
- **reska-backend** (d:\Users\{USER}\sw\reska\reska-backend): FastAPI + PostgreSQL, collection management, port 8001
- **reska-frontend** (d:\Users\{USER}\sw\reska\reska-frontend): Flet cross-platform UI
- **reska-op-card-api** (d:\Users\{USER}\sw\reska-op-card-api): FastAPI + SQLite, card metadata + print variants (Naips), port **8000**, **HTTPS** (mkcert self-signed cert, `certs/localhost+1.pem`)
- **reska-op-price-api** (d:\Users\{USER}\sw\reska-op-price-api): THIS PROJECT — FastAPI + PostgreSQL (reska_op_price DB), Cardmarket scraper, port **8002**, HTTP

**Running the price-api:**
```bash
cd d:/Users/{USER}/sw/reska-op-price-api
uv run python -m reska_op_price_api
```
`__main__.py` passes `loop_factory` to force `SelectorEventLoop` on Windows (required by psycopg3 async).

**JWT auth (price-api):** HS256, secret from `SECRET_KEY` in `.env`, payload must have `type: "access"` and `sub: <uuid>`.

**Card-api auth:** `X-API-Key` header (BLAKE3-hashed, looked up in `api_key` table). Key for price-api created with label `price-api` (read-only). Raw key stored in price-api `.env` as `CARD_API_KEY`.

**Why:** reska-op-price-api supplies card prices to the frontend/backend so users can see valuations for their collection.

[[card-api-schema]]
[[price-api-architecture]]
