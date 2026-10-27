---
name: project-stripe-expand-pattern
description: "FK fields in API responses use the Stripe-style expandable pattern — integer by default, full object when ?expand=field is requested"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d0a65e0-8692-49bf-a90f-e0f5f6dd1d0e
---

All FK relations in response models use the Stripe-style expandable field pattern:

- Without `?expand=field`: the field contains the raw integer FK (e.g. `"card": 1`)
- With `?expand=field`: the field contains the full expanded object (e.g. `"card": {"id": 1, "name": "Roronoa Zoro", ...}`)

No separate `*_fk` fields are exposed in responses. Denormalized convenience scalars (like `set_code`, `artist_name`) are also removed — callers use expand to get that data.

**Exception:** `image_fk` + `image_path` are kept as-is since the path is the only useful field.

**Implemented across:**
- `/naips`: `card`, `set`, `artist`, `print_variant`, `language`, `cardtype`, `block`
- `/cards`: `set`, `cardtype`, `rarity`, `block`
- `/sets`: `language`, `parent`, `type`

**Why:** Clean API design — each FK field is self-describing; clients opt in to extra data rather than always receiving it. Matches Stripe's industry-standard expand pattern.

**How to apply:** Any new FK relation added to a response model must follow the same pattern: `field: int | ExpandedModel` (nullable: `field: int | ExpandedModel | None`). Add a corresponding `_expand_*_bulk` helper in `_common.py` and wire it into the endpoint's expand logic.

**Applies to list/array relations (many-to-many junctions) too, not just scalar FKs:** `field: list[int] | list[ExpandedModel] = []`. Without `?expand=field`: list of raw FK ids (never `[]` as a "not expanded" placeholder — ids must always be fetched). With `?expand=field`: list of full objects. A true empty relation (e.g. card with zero colors) is `[]` regardless of expand state — that's a real empty list, not a stand-in for unexpanded.

**Past mistake (fixed 2026-06-30):** commit 5d44f1b introduced junction tag lists (colors/tribes/attrs/formats/keywords/reswords on cards and naips) that returned `[]` when not expanded instead of the FK ids — violates the rule above. Don't repeat: when adding/touching any list-relation field, default must be ids, not empty.
