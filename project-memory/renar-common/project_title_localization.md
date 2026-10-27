---
name: title-localization
description: How renar localizes library titles per user language (implemented 2026-07-14) — architecture to reuse for related work
metadata: 
  node_type: memory
  type: project
  originSessionId: b3efad98-d345-4f7f-b4f5-af453a600e22
---

Library titles used to be frozen in whatever language first added them (`Title.title` is one shared string per tmdb_id, set once at creation). Fixed by reusing infrastructure that already existed rather than building a new translation pipeline:

- `Title.original_title` (nullable) — TMDB's own `original_title`/`original_name`, populated whenever an English details payload is synced (`tmdb_store.sync_title_details`).
- `tmdb_store.localized_titles(db, title_ids, lang)` — reads a user's display language from the *already-existing* per-language `TmdbCache` rows (`kind="details"`, keyed by `(title_id, kind, season, language)`) — no live TMDB call, no new translations table.
- `GET /media?lang=xx` (`routers/media.py:list_media`) stamps each `LibraryEntryOut.display_title` from that cache, falling back to `Title.title`. Missing translations trigger a capped, non-blocking `BackgroundTasks` warm-up (`tmdb_store.warm_title_translations`) that fetches+caches them for the *next* request — current request never blocks on TMDB.
- Search matches `Title.title`, `Title.original_title`, or any cached-language `TmdbCache.payload` text — cross-language search self-reinforces as more users warm more languages' caches.
- `User.show_original_titles` (bool) lets a user pin `original_title` display regardless of app language; frontend caches it on `page._renar_show_original_titles` (via `i18n.get_show_original_titles`/`set_show_original_titles`), set at the existing `api.me()` call sites (login/register/session-restore/resume) — no extra network round-trip in Library's hot path.

**Why:** User reported Spanish-language app still showing English titles ("The Godfather" not "El Padrino") and Library search only matching English text. [[feedback_blazing_fast_performance]] ruled out any design needing a live TMDB call inside `list_media`.

**How to apply:** Any future work touching library title display, search, or TMDB caching should build on this (`tmdb_store.py`, `routers/media.py`) rather than re-deriving it. Existing library entries won't have `original_title` or non-English `TmdbCache` rows until something (a details-page visit, the notifier, or this feature's own warm-up) fetches them — no backfill migration was run, backfill happens progressively through normal use, consistent with how other typed `Title` columns were added historically in this codebase.
