---
name: optcg-db-design
description: "Intentional design decisions for the optcg-api database schema — what looks like an error but isn't, and what actually needs fixing"
metadata: 
  node_type: memory
  type: project
  originSessionId: bcfb8b44-1d96-4821-98d1-14b14ba80cae
---

## Naip table — design rationale

`Naip` represents a **specific physical print** of a card (e.g. OP-01 base art, OP-01 alt art, OP-07 treasure rare reprint). One abstract `Card` can have many `Naip` rows across different sets and rarities.

### Naip.set_fk — intentional redundancy
`Naip.set_fk` duplicates `card.set_fk` by design. A card can be reprinted in a later set as an alternate art, so each `Naip` independently records which set *that print* belongs to — the card's original set and the print's set can differ.
**Do not remove it.**

### Naip.name_fk — intentional nullable column
A `Naip` can have its own `name_fk` (distinct from `Card.name_fk`) to record misprints or alternate-art name variations on that specific print. Currently always NULL for ingested data; will be populated when a misprint/alt-name is known.
**Do not remove it.**

### Card.rarity_fk — canonical base rarity
`Card.rarity_fk → rarity.id` records what tier the card was designed as (C, UC, R, SR, SEC, L, D, P). This is the abstract card's rarity, independent of any specific print. Nullable (some cards may be unclassified). Do not confuse with print-level variants.

### Naip.print_variant_fk — print-level variant
`Naip.print_variant_fk → print_variant.id` records the specific variant of this physical print (STD for standard, AA/TR/SP/etc. for special). NOT NULL — every naip has an explicit variant (use STD for ordinary prints). `naip.rarity_fk` was removed; rarity is now exclusively on `card.rarity_fk`.

### print_variant hierarchy — parent_fk self-reference
`print_variant.parent_fk` encodes an "is a subtype of" hierarchy. A naip stores the most specific variant (e.g. GR for Ghost Rare); traversing up gives inherited types (GR → SP → AA). Roots (STD, AA) have `parent_fk = NULL`. Query all SP prints: `WHERE print_variant_fk IN (SELECT id FROM print_variant WHERE symbol = 'SP' OR parent_fk = (SELECT id FROM print_variant WHERE symbol = 'SP'))`. Do not re-introduce a flat rarity system for print variants.

### Naip.is_default — partial unique index
`Index("ix_naip_one_default_per_card", "card_fk", unique=True, sqlite_where=sa.text("is_default = 1"))` enforces at most one default print per card. Already implemented in models.py.

### Naip.is_errata — errata flag
`is_errata: bool = Field(default=False)` marks that this specific print carries errata text (i.e. the effect/trigger on this Naip differs from the original print due to an official ruling correction).

### Naip.serial_max — serialization cap
`serial_max: int | None` records the total print run for serialized cards (e.g. 500 for a 1-of-500 serial). NULL means not a serialized print.

### NaipSerial table — known revealed copies
`NaipSerial` (naip_fk, serial_number, image_fk) tracks individually revealed copies of a serialized print. Unique constraint on (naip_fk, serial_number); serial_number must be ≥ 1 (CHECK constraint). A CHECK constraint also enforces `serial_number <= naip.serial_max` via a trigger (SQLite cannot reference other tables in CHECK). Has its own `updated_ts` trigger.

### Naip junction tables — print-level M2M
`NaipColor`, `NaipTribe`, `NaipAttribute`, `NaipKeyword`, `NaipResword` mirror the Card junction tables but at the print level.
**NaipFormat was dropped** — format legality is always card-level; a specific print cannot have different format legality from its abstract card.
**NaipBlock was dropped** — block is now a direct FK on both Card and Naip.

### Naip text is immutable — print-as-originally-printed
`Naip.effect_fk` and `Naip.trigger_fk` record the text **as it was printed on that physical card**. They are set at creation and never updated. If a later reprint has different text (e.g. corrected errata printed in the new set), that reprint is a new `Naip` row with its own FK pointing to the new text.
- Errata (official rules corrections) live exclusively on `Card` via `CardEffectHistory` / `CardTriggerHistory`.
- `Naip.is_errata = True` flags that this print's text was later errata'd, for display purposes only.
**Do not update naip.effect_fk / naip.trigger_fk after creation.**

### Bans are card-level only
Bans (`CardBan`, `BannedPair`) apply to the abstract `Card`. If a card is banned, **all its naips** are banned. There is no naip-level ban concept.

### CardBan / BannedPair — NULL-safe uniqueness
`format_fk = NULL` means "banned in all formats". SQLite UNIQUE does not treat NULL = NULL, so a partial index guards the NULL case:
- `CardBan`: unique partial index on `card_fk WHERE format_fk IS NULL` prevents duplicate "global ban" rows.
- `BannedPair`: unique partial index on `(card_a_fk, card_b_fk) WHERE format_fk IS NULL` prevents duplicate global pair bans.

### Naip.cardtype_fk + power/life/counter/cost — print-level overrides
`Naip` carries its own `cardtype_fk`, `power`, `life`, `counter`, `cost` that can override `Card`'s values for a specific print. NULL means "same as the abstract card".

## Rarity table — base card rarities only
`rarity` now contains only: C, UC, R, SR, SEC, P, L, D. `is_type` and `is_base` columns were removed (migration 0003). NFD was removed (foil distinction is `naip.is_foil`). Print-level variants (AA, TR, SP, MR, FA, etc.) live in `print_variant`. Do not re-add print-variant symbols to `rarity`.

## Dedup text tables — Name, Image, Effect, Trigger
`Card.name_fk` → `Name.id`, `Card.effect_fk` → `Effect.id`, `Card.trigger_fk` → `Trigger.id`, `Card.image_fk` (via `Naip.image_fk`) → `Image.id`. These normalize repeated strings so the same text has exactly one row. All have a UNIQUE constraint on the text column. **Do not inline these back into Card/Naip.**

## CardEffectHistory / CardTriggerHistory — planned, not premature
These tables are intentionally present for future **errata/ruling tracking**: when a card's effect or trigger text is officially changed, the old text is preserved with a `valid_from/valid_to` date range. Currently unused by routers and ingest — that is expected. Do not remove them.

**Open gap:** No overlap-prevention constraint or `CHECK (valid_to IS NULL OR valid_to > valid_from)` yet. Add these when the feature is implemented.

## Set.code — UNIQUE constraint
`Set.code` is declared with `sa.Column(sa.String, nullable=False, unique=True)` in models.py. The natural key used for upserts in ingest.py is correctly constrained.

## Timestamp columns — fully DB-side
All timestamps are handled entirely by SQLite:
- **`server_default`** on both `created_ts` and `updated_ts`: raw `INSERT` statements that omit these columns get `strftime('%Y-%m-%d %H:%M:%f', 'now')` automatically.
- **`AFTER UPDATE` triggers** (`trg_<table>_update`) on all tables: refreshes `updated_ts` on every row update. The `WHEN NEW.updated_ts IS OLD.updated_ts` guard prevents recursive re-firing.

`_ts_col()` in models.py is the single factory — `sa.Column(sa.String, nullable=True, server_default=...)` with no Python `default` or `onupdate`.
