---
name: feedback-stripe-expand-pattern
description: FK fields in REST API responses use the Stripe-style expandable pattern — integer by default, full object when ?expand=field is requested
metadata:
  type: feedback
---

All FK relations in REST API response models use the Stripe-style expandable field pattern.

- Without `?expand=field`: the field holds the raw integer FK — e.g. `"card": 1`
- With `?expand=field`: the field holds the full expanded object — e.g. `"card": {"id": 1, "name": "Roronoa Zoro", ...}`

No separate `*_fk` fields are exposed in responses. Denormalized convenience scalars derived from related entities (e.g. `set_code`, `artist_name`) are also removed — callers use expand to get that data.

**Why:** Clean API design; each FK field is self-describing; clients opt in to extra round-trips rather than always receiving bloated responses. Matches Stripe's industry-standard pattern.

**How to apply:**
- Response model field type: `field: int | ExpandedModel` (nullable: `field: int | ExpandedModel | None`)
- No `*_fk` suffix in the response model
- Add a `_expand_*_bulk(fks, session)` helper for the related entity
- Wire it into the endpoint's expand logic: build an expand map when the key is in `expand_set`, pass FK int otherwise
- `image_fk` + `image_path` are a conventional exception — images are path-only resources, no benefit to full expansion