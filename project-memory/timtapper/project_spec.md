---
name: project-spec-timtapper
description: timtapper product/tech spec — local-only Flet One Piece TCG match tracker with shareable stat images (davyback.gg-like)
metadata:
  node_type: memory
  type: project
  originSessionId: e0fe7d8e-9d0a-40e7-95d6-47e4bc85bc07
  modified: 2026-10-12T22:38:48.117Z
---

# timtapper — project spec

Confirmed with the user 2026-10-11. Reference product: https://davyback.gg (web OPTCG match tracker).

## Product
- Match tracker for the **One Piece Trading Card Game** (OPTCG).
- **Local-only**: no backend, no accounts, no server. All data lives on the device.
- Social layer = **shareable images** generated on-device (no sync between users).

## Core features
- Events: testing sessions, locals, majors (type, date, name, own leader/deck).
- Event types (changed 2026-10-12): Bandai's official tiers, casual to world level: Pirates Party, locals (store tournament), release event, sealed, Heroines Battle (heroine leaders only), team battle (2on2/3on3), Store Championship, Treasure Cup, Flagship Battle, Extra Grand Battle, regional, national, World Championship; plus testing and other. No "online" (the OPTCG has no online tier): stored online events and old backups become "other". Official event names stay in English in every language.
- Event standing (changed 2026-10-12): optional placement and player count per event, shown as "#3 of 32"; placement can't exceed the player count; testing sessions have none.
- Events list (changed 2026-10-12): search by name, plus inline filters by own leader and event type (the same filters as stats); filters persist while navigating.
- Matches/rounds per event: opponent leader, result (W/L), die roll won, went first/second, notes; top-cut rounds flagged.
- Rounds (changed 2026-10-13, "copy davyback.gg and improve"): each round is Swiss, top cut or bye (no opponent, automatic win, shown with a jester portrait). Swiss row = die, turn, result (one-tap cycles), notes visible on the row. Top cut defaults to best of 3, any round switchable Bo1/Bo3; a Bo3 keeps its round number (plus a "TC" tag) and lists each game under it (who chose turn, turn, result). Who chose the turn: game 1 by die (Swiss) or higher seed (top cut); later games derived (previous game's loser chose) but overridable. Stats: record counts matches (Bo3 once), plus a game record; turn and who-chose splits per game; byes are wins in the event standing but excluded from win rates and matchups.
- Event extras (2026-10-13): the set it was played in (default newest, filterable), dropped flag, placement shown as a bracket ("Top 4 · #3 of 32", "1st place", "Dropped").
- **No draws** (changed 2026-10-12): the OPTCG has none; a drawn game is a loss for both players. Stored draws and draws in old backups become losses.
- Leader catalogue (100+ leaders, 17+ sets), updatable as new sets release. Full names are stored; tight rows (round rows) show the short names players use ("Doflamingo", "Kid").
- Text is never cut off with "…" anywhere: long text wraps (between words) or the layout makes room.
- Stats: overall record, win rate per opposing leader, first vs. second split, recent form.

## Share images (all three)
Each leader shows as its portrait framed in its colours (changed 2026-10-12: card-art crops are now drawn on share cards; before, only names and colour stripes).
1. **Event result card** — own leader, final record, standing in its own big gold band ("#3 of 32 players") when known, round list with opponent leaders, turn order, die roll (the app's die faces) + W/L.
All cards carry the app's logo mark beside the TIMTAPPER wordmark.
2. **Matchup stats** — win rate per opposing leader, first/second split.
3. **Overall summary** — total record, best/worst matchups, recent form.

## Platforms
- **Android (APK) + desktop** (desktop mainly for development). No iOS for now.

## Tech
- Python + uv, Flet frontend only (deviation from [[reference_preferred_stack]]: no FastAPI backend, single repo).
- Local SQLite via SQLAlchemy (+ Alembic for schema migrations), BCNF schema.
- Images rendered on-device (Pillow), then shared via the OS share sheet or saved to the gallery.
- pytest, ruff, structured logging, per global rules.
