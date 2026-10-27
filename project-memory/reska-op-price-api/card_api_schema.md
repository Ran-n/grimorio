---
name: card-api-schema
description: "reska-op-card-api data model, expand pattern, auth, and how price-api calls it"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4ef1695b-1fbb-4e51-8b26-676bb85d3dd2
---

The card-api (d:\Users\{USER}\sw\reska-op-card-api) uses SQLite + SQLModel. Base URL: `https://localhost:8000`. Auth: `X-API-Key` header (BLAKE3-hashed).

## Key entities

- **Card**: canonical card (set_fk, cardtype_fk, rarity_fk, number, name, effect, trigger, cost, power, life, counter). `number` = card number within set (e.g. OP01-001 → 1).
- **Naip**: physical print variant — FK to Card + set + artist + print_variant + language + per-print text/stat overrides. Prices attach at Naip level.
- **PrintVariant**: has `symbol` (STD, AA, TR, SP, GR…)

## Expand pattern (Stripe-style)

`GET /naips/{id}?expand=card,print_variant` returns inline expanded objects instead of FK ints:

```json
{
  "id": 1,
  "card": { "id": 1, "number": 1, "name": "Roronoa Zoro", "set_code": "OP01", ... },
  "print_variant": { "id": 2, "name": "Alternate Art", "symbol": "AA" },
  "name": "Roronoa Zoro",   // naip-level name override (may be null)
  ...
}
```

Available expand keys: `card`, `set`, `artist`, `print_variant`, `language`, `cardtype`, `block`

## ExpandedCard fields (when expand=card)
`id, number, name, effect, trigger, power, life, counter, cost, set_code, set_name, cardtype_name, cardtype_symbol, rarity_name, rarity_symbol, colors, tribes, attrs, keywords, reswords`

## How price-api uses it

Single call: `GET /naips/{naip_id}?expand=card,print_variant`
- `set_code` ← `naip["card"]["set_code"]`
- `card_number` ← `naip["card"]["number"]`
- `name` ← `naip["name"] or naip["card"]["name"]`
- `print_variant_symbol` ← `naip["print_variant"]["symbol"]` (if dict)

httpx client in `core/card_api.py` uses `verify=False` (self-signed cert) and reads key from `settings.card_api_key`.

[[project-context]]
[[price-api-architecture]]
