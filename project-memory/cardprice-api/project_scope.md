---
name: project-scope
description: "Core purpose, scope, and target marketplaces/games for cardprice_api"
metadata: 
  node_type: memory
  type: project
  originSessionId: 859177b2-579e-44aa-8cff-302a56bed17f
---

cardprice_api is an API to query trading card prices from multiple marketplaces.

**Initial scope (MVP):**
- Marketplace: Cardmarket only
- Card game: One Piece Card Game (Bandai)

**Planned future sources:**
- CardTrader (has official API, strong EU presence)
- TCGPlayer (largest US marketplace, official API)
- Scryfall (MTG-only aggregator, free API)
- eBay (general marketplace API)
- PriceCharting (API available)

**Why:** Starting narrow (one source + one game) to validate architecture before expanding to other games and marketplaces.

**How to apply:** Prioritize Cardmarket + One Piece integration first. Design data models to be game-agnostic so adding new games later is straightforward.
