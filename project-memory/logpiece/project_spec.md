---
name: logpiece-project-spec
description: "UX, behaviour, and technical requirements for logpiece — source of truth for design decisions"
metadata: 
  node_type: memory
  type: project
  originSessionId: c85bb7cb-940d-4a0f-a12b-4a56faef98ad
---

# logpiece — Project Spec

## Purpose
Desktop GUI app (PySide6) for browsing and editing the reska-op-card-api SQLite database (`optcg.db`). Read-mostly: primary use is browsing cards; secondary use is raw DB editing via table panel.

## Technical Stack
- Python 3.14+, PySide6, SQLModel (ORM layer over SQLite)
- `src/` layout under `src/logpiece/`
- uv for package management, ruff for linting/formatting

## Module Structure
```
src/logpiece/
  app.py            — MainWindow + main() entry point only; overlay hides in DB view; injects mirrored toolbar buttons into TablePanel
  db/               — package; __init__.py re-exports everything
    _core.py        — dataclasses (CardRow, CardDetailRow, NaipRow), connect/disconnect, upserts, junction ops, lookup creation
    _generic.py     — generic table ops: tables, columns, foreign_keys, fetch_all, fetch_lookup, fetch_set_code_lookup, fetch_rarity_lookup, fetch_rarity_symbol_lookup, fetch_rarity_full_lookup, fetch_print_variant_lookup, fetch_foil_variant_ids, insert_row, update_row, delete_row, has_card_schema
    _queries.py     — typed card queries: fetch_cards, fetch_card_detail, fetch_card_naips, fetch_naips_flat + _grouped_* helpers
    models.py       — SQLModel table definitions mirroring optcg_api schema exactly; timestamps use server_default only (no Python-side injection)
  settings/         — package; __init__.py re-exports everything
    _defaults.py    — SHORTCUT_DEFS, SHORTCUT_DEFAULTS, SHORTCUT_GROUPS, GENERAL_DEFAULTS, DEFAULTS; shortcut IDs include toggle_errata (E), toggle_star (S), dropdown_* group; GENERAL_DEFAULTS includes last_naips_mode (bool, persists naip-view state)
    _core.py        — load()/save() for %APPDATA%/logpiece/settings.toml; in-memory _cache; _normalise_shortcuts (multi-binding upgrade), _serialise_shortcuts (grouped TOML output)
  theme/            — package; __init__.py re-exports everything
    _palettes.py    — palette dicts (GRUVBOX_DARK/LIGHT, DARK, LIGHT), COLOR_MAP, color_hex_pixmap, hex_wedge_at, _HEX_WEDGE_ORDER
    _core.py        — DIMS, FONT_FAMILY, SVG icon helpers (svg_icon, svg_icon_outlined, svg_icon_toggle, svg_pixmap), ThemeManager, TOML theme loader, apply_palette, style_combo, p(), dim()
  stylesheet/       — package; __init__.py re-exports build_stylesheet
    _core.py        — build_stylesheet() + structural _ss_* sections (base, menu, statusbar, splitter, sidebar, searchbar, filterbar, listwidget, detail)
    _widgets.py     — widget-specific _ss_* sections (table, scrollbar, pushbutton, inputs, combobox, chrome_buttons, dialog_buttons, popups, image_widgets, misc)
  assets/icon.py    — embedded app icon
  assets/icons/     — SVG icon files (alert-triangle, bolt, check, chevron-left/right, coin, color-hexagon, database, edit, equals, errata, eye/eye-off, file-text, filter, folder-open, ghost, ghost-off, grid, hash, heart, info, key-transfer, layers, moon, move-left, move-right, plus, push-pin, rarity, refresh, reset-defaults, scroll, shield, sigma, star, sun, tag, transfer, trash, type, venn, x); loaded by theme.svg_icon()
  assets/themes/    — bundled TOML themes (catppuccin latte/mocha, dracula dark/light, gruvbox dark/light ×3 contrast, indigo dark/light, nord dark/light, solarized dark/light)
  widgets/
    __init__.py
    _utils.py         — shared widget utilities: _clear_layout, _sep, _to_display, _int_or_none (layout/display helpers); make_popup_plus_btn, make_action_btn (factory helpers for standard button patterns)
    about.py          — AboutPopup (frameless About panel)
    card_browser.py   — CardBrowserPanel (fixed-280px sidebar + detail splitter); accepts `initial_naips_mode: bool`; `current_naips_mode() -> bool`; filter row: `#filterPillNaips` toggle + `_IconOnlyButton` funnel opens `FilterPanel`; `_filter_spec: FilterSpec` applied client-side; artist lookup sourced from `db.fetch_artist_lookup()`; left/right arrow keys cycle naips; eventFilter handles toggle_errata shortcut via detail.toggle_errata_naip()
    filter_panel.py   — `FilterSpec` dataclass (colors_any/colors exact, types, rarities, set_types, `set_codes: set[str]` multi-select, artist str, cost/power/counter/life ranges, errata, serial, foil, print_variant); `FilterSpec.from_dict` migrates legacy `set_code` str to `set_codes`; `_ColorFilterCombo` (72 px hex-wheel trigger + popup swatch grid, Any/Exact mode badge toggled by bottom-right circle badge, right-click clears); errata/serial/foil/naips flag toggles (`#filterFlagBtn`) in a 2×2 grid in the color section (errata 0,0 · serial 0,1 · foil 1,0 · naips 1,1); `_PillChip` (dismissible `#filterPillChip` QPushButton, emits `removed(str)`); `_SingleSelectCombo` (generic single-select searchable popup label — used for variant and artist); `_MultiSelectCombo` (generic multi-select checkbox popup with dismissible pill row — used for set type and set code, supports `set_scope()`); `FilterPanel` QDialog (opens via `show_at(anchor)`, emits `filter_changed(FilterSpec)` and `hidden`); `_set_type_combo` + `_set_code_combo` replace old `_SetTypeFilter`/`_SetFilterCombo`; numeric-range section icons: cost=coin, power=bolt, counter=shield, life=heart
    card_detail/      — package; __init__.py re-exports CardDetailPanel
      _helpers.py     — re-exports _clear_layout/_sep/_to_display/_int_or_none from widgets._utils; defines _hide_owned_popups
      panel.py        — CardDetailPanel (hero image top-center, 2-col metadata, inline editing); stats grid: numeric fields (cost/power/counter/life) + attribute/tribe/card-type/rarity combos in one shared QGridLayout; rarity uses a QStackedWidget (_rarity_single_w naip mode, _rarity_w multi card mode); stats/combos show naip data by default, card-level data when "scroll" toggle is on; _reconnect_combo_saves() rewires signals on mode switch; public naip actions: toggle_errata_naip, toggle_star_naip, create_naip, modify_naip, displace_naip_left/right, naip_serial_action, naip_remove_serial
    card_dialogs.py   — _NewNameDialog, _NewSetDialog (create-on-spot dialogs for card fields); form labels are SVG icon labels, OK/Cancel are icon-only buttons
    card_image/       — package; __init__.py re-exports CardImageWidget
      _utils.py       — free functions: _blake3_file, _canonical_images_ref, _image_path_exists, _load_pixmap, drop/clipboard helpers
      _dialogs.py     — _DropZone (single or multi=True batch mode), _ImageSourceDialog, _BatchImportDialog (collects multiple image paths for bulk naip creation; drop zone + browse + clear list), _ImageExpandDialog
      _frame.py       — _ImageFrame (image display with hover nav overlay)
      _serial.py      — NaipSerialDialog (browse/add/delete serial numbers for a naip; inline print-run editor; ghost toggle shows missing serials; toast feedback)
      widget.py       — CardImageWidget (naip cycling, errata, foil toggle, image add/edit/batch-add, move-left/right sort_order; serial_btn/serial_count_btn injected into CardDetailPanel header; uses fetch_foil_variant_ids to determine foil variant IDs)
    card_list_item.py — CardListDelegate + CardListModel (compact 56px rows with cost badge, color-hex hexagon icon); thumbnails pre-scaled at cache time; _hex_cache is instance-level and cleared on theme change via clear_icon_cache(); index_of_card_id() for naip-mode selection restore
    combos.py         — InlineCombo (searchable floating FK picker)
    config_dialog.py  — ConfigDialog (File → Preferences…): default DB path, startup mode
    dialog_actions.py — dialog_action_button(), show_error(), show_warning(), confirm() — shared icon-only OK/Cancel dialog helpers used across widgets
    inline_edit.py    — base classes: _InlineBase (label↔editor QStackedWidget toggle), _MultiPickerBase (shared popup checklist machinery); concrete widgets: _InlineText (QLineEdit), _InlineMultiline (QPlainTextEdit), _InlineMultiCombo (multi-select FK checklist with optional create_fn), _RarityMultiCombo (multi-select rarity; renders as symbol pills), _RaritySingleCombo (single-select rarity; single symbol pill; click-again deselects), _SwatchButton (colored circle toggle), _ColorMultiCombo (swatch-grid color picker)
    shortcuts.py      — ShortcutsDialog (Help → Keyboard Shortcuts… / F1): multi-binding editor (_KeyChip pills, _KeyBindingRow, _FlowLayout); conflict dialog (_conflict_choice: transfer/allow/cancel); reset-to-defaults; auto-saves on every change
    table_editor.py   — TablePanel + RowDialog (raw DB editor); accepts extra_buttons injected by MainWindow for DB-view toolbar
    theme_editor.py   — ThemeEditorDialog (TOML theme picker, editor, save/apply)
```

## Domain Model

### Lookup tables
`set_type`, `card_type`, `artist`, `rarity`, `tribe`, `attribute`, `color`, `block`, `format`, `keyword`, `resword` — all have `id`, `created_ts`, `updated_ts`, `name`. `card_type` and `rarity` also have `symbol`. Most have an optional `desc`.

`block` — `id`, `name`, `desc`, `image_fk → image` (nullable).

`print_variant` — `id`, `symbol`, `name`, `desc`, `parent_fk` (self-referential FK to `print_variant.id`). Hierarchical: AA is the root foil type; descendants are queried via recursive CTE in `fetch_foil_variant_ids`.

`language` — `id`, `code` (unique), `name`, `desc`, `image_fk → image`. Represents a card language edition.

`region` — `id`, `code` (unique), `name`, `desc`.

`region_language` — junction: `region_fk → region`, `language_fk → language`; unique `(region_fk, language_fk)`.

### Text-dedup lookup tables (unique-value pools)
`name` (`name` col), `image` (`path` col), `effect` (`effect` col), `trigger` (`trigger` col) — values are unique; rows are shared across cards/naips.

### Core tables
- `set` (`Set`) — `type_fk → set_type`, `language_fk → language`, `code`, `name`, `parent_fk → set` (nullable, self-referential), `desc`, `release_ts`; unique constraint on `(code, language_fk)`
- `Card` — `set_fk`, `cardtype_fk`, `name_fk → name`, `rarity_fk → rarity` (nullable), `effect_fk → effect`, `trigger_fk → trigger`, `block_fk → block` (nullable), `number`, `power`, `life`, `counter`, `cost`
- `Naip` — one physical printing of a card. Fields: `card_fk`, `set_fk`, `artist_fk`, `print_variant_fk → print_variant`, `name_fk`, `image_fk → image`, `effect_fk`, `trigger_fk`, `cardtype_fk`, `language_fk → language` (nullable), `block_fk → block` (nullable), `power`, `life`, `counter`, `cost`, `is_default`, `is_errata`, `is_foil`, `sort_order`, `serial_max`. A card can have many naips. `is_default` marks the de-facto naip shown first. `is_foil` is a boolean flag; whether a print_variant is foil is determined from `fetch_foil_variant_ids` (AA + descendants). **Default rule:** new naips are created with stats and text FKs copied from the base naip (or from the card if no base). A null naip FK means the card genuinely has no effect/trigger text — not inheritance. Overrides are written directly to the naip's FK columns.
- `NaipSerial` (`naip_serial`) — a known revealed copy of a serialized naip. Fields: `naip_fk`, `serial_number` (≥1, unique per naip), `image_fk` (nullable). Unique constraint on `(naip_fk, serial_number)`, index on `naip_fk`.

### History tables
- `card_effect_history` — `card_fk`, `effect_fk`, `valid_from`, `valid_to` (null = current)
- `card_trigger_history` — `card_fk`, `trigger_fk`, `valid_from`, `valid_to`

### Junction tables (card many-to-many)
`card_tribe`, `card_attribute`, `card_color`, `card_format`, `card_keyword`, `card_resword` — all have `card_fk` + the respective `*_fk`, a `UniqueConstraint` on the pair, and indexes on both FK cols. Note: `card_rarity` junction was dropped; rarity is now stored directly on `card.rarity_fk`. `card_trigger` junction was also dropped; trigger is stored on `card.trigger_fk`.

### Junction tables (naip many-to-many)
`naip_color`, `naip_tribe`, `naip_attribute`, `naip_keyword`, `naip_resword` — same structure as card junctions but keyed on `naip_fk`. These hold per-printing overrides. On first connect, `card_color` rows are migrated into `naip_color` for any naip that has no `naip_color` rows yet (`_migrate_card_colors_to_naip` in `db.py`).

### Ban tables
- `card_ban` (`CardBan`) — `card_fk`, `format_fk` (nullable; NULL = banned in all formats). Unique `(card_fk, format_fk)`; partial unique index `ix_card_ban_global_unique` on `card_fk` where `format_fk IS NULL`.
- `banned_pair` (`BannedPair`) — `card_a_fk`, `card_b_fk` (ordered: `card_a_fk < card_b_fk`), `format_fk` (nullable). Unique `(card_a_fk, card_b_fk, format_fk)`; partial unique for global bans.

## DB Access Rules
- Use SQLModel `Session` + `select()` for all typed card queries
- Generic table-editor ops (PRAGMA introspection, arbitrary table CRUD) use `session.exec(text(...))` — acceptable because the table name is dynamic
- No raw `sqlite3` imports; connection is via `create_engine` + `Session`
- Models are defined in `models.py` and mirror optcg_api exactly — do not diverge
- **Schema changes (DDL) are NEVER done in logpiece.** No `ALTER TABLE`, `CREATE TABLE`, `DROP TABLE`, `CREATE INDEX`, or any other DDL. All schema changes belong to `optcg_api` via Alembic migrations.
- **Data changes (DML) are fine** — INSERT, UPDATE, DELETE on existing tables is the whole point of the editor.
- `CardRow.__slots__` includes `is_errata` (bool), `is_foil` (bool), `print_variant` (str), and `serial_max` (int | None), populated in both `fetch_cards` and `fetch_naips_flat`; used by `FilterSpec.matches()` for client-side filtering.
- `NaipRow` carries `color_ids`, `tribe_ids`, `attribute_ids` (lists of int) plus `cost`, `power`, `counter`, `life`, `cardtype_fk`, `set_type_name`, `is_foil` (bool), `print_variant_fk` (int|None), and `rarity` (symbol string from `Card.rarity_fk`) — all sourced from naip-level tables/columns (or joined through `Set → SetType` / `Card → Rarity`), not the card directly. NaipRow does NOT carry a `rarity_fk`; rarity is looked up via the card join.
- `_grouped_colors/rarities/tribes/attributes` short-circuit and return `{}` when called with an empty `card_ids` list.
- Key db functions: `fetch_cards`, `fetch_card_detail`, `fetch_card_naips`, `fetch_naips_flat`, `fetch_artist_lookup` (returns `list[str]` of all artist names sorted) (one CardRow per naip for the Naips filter), `set_naip_default`, `clear_naip_default`, `save_naip_order`, `upsert_naip_effect`, `upsert_naip_trigger`, `upsert_card_effect`, `upsert_card_trigger`, `update_junction_ids`, `update_junction`, `fetch_junction_ids`, `upsert_image`, `upsert_text_lookup`, `create_lookup_entry`, `create_set` (now takes `language_fk: int` param), `fetch_set_type_name`, `fetch_rarity_full_lookup` (id→(symbol,name)), `fetch_rarity_symbol_lookup` (id→symbol), `fetch_print_variant_lookup` (id→`[symbol] name`), `fetch_foil_variant_ids` (returns set[int] of AA+descendant print_variant IDs via recursive CTE), `fetch_naip_serials`, `upsert_naip_serial`, `delete_naip_serial`.

## Design Rules
- No file over ~200 lines; no function over ~20 lines
- One concern per file (theme, models, db, each widget)
- Widget classes do not import from each other directly — they go through `db.py` for data
- `CardBrowserPanel` owns the session reference; `MainWindow` passes it in

## UX
- Two modes toggled via View menu: Card Browser (default) and Database Editor
- Card Browser: left sidebar (search + list), right panel (card detail)
- Database Editor: left table list, right table grid with add/edit/delete toolbar
- Dark theme throughout; gold accent (#e8c97a) for cost badges and focus states
