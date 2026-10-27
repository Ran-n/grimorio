---
name: product_renar_vision
description: "Comprehensive product vision, architecture, and roadmap for the personal experience curator"
metadata: 
  node_type: memory
  type: project
  originSessionId: cf1b9f8b-d1bd-4402-b630-a756b3e78a79
---

# Personal Experience Curator

**Project:** Renar  
**Current Status:** Alpha (films/TV shows shipped, backend ready for all domains)  
**Target Launch:** TBD  

---

## Core Mission

A personal experience curator where you track, rate, share, and discover everything you consume and experience — films, TV shows, books, YouTube videos, concerts, art exhibitions, cities, countries, and more.

Unlike traditional media trackers that live in a silo, it's a **social platform** where your curated taste becomes a searchable profile that friends can follow, creating a network of taste discovery. It's Letterboxd's taste-curation DNA + TV Time's episode tracking + a broader scope that grows beyond media into experiences.

---

## Why This Matters

People spend hundreds of hours discovering, consuming, and experiencing culture and the world. Yet there's no unified place to:
- **Track it consistently** (one app for films, another for books, another for visits)
- **Remember it** (what was that great show I watched 2 years ago?)
- **Share it meaningfully** (I want friends to see *my* taste, not just what I watched today)
- **Discover through taste** (show me what my favorite people are into, not what algorithms think I'll click)

The app solves this by being the **single source of truth for your personal taste and experiences**.

---

## Core Features (MVP Shipped / In Flight)

### 1. **Library** ✓ (Films/TV shows live)
- Track watch status: planning, watching, completed, dropped, rewatched
- For TV shows: per-episode tracking with checkboxes, season progress, overall grade + episode ratings
- Mark favorites (starred favorites are prominent on your profile)
- Search, filter by type, filter by status
- Custom notes on entries
- Progress visualization: two-ring badges (season + series progress), capsule bars, percentages
- Custom posters/backdrops (premium: TMDB alternates or upload)
- Custom episode stills (premium: TMDB alternates)

### 2. **Explore** ✓
- TMDB trending/popular feeds (films, TV shows, filtered by region)
- TMDB search with rich metadata (year, runtime, episode count, genres, cast)
- Books: Open Library trending/search
- YouTube search (requires API key)
- One-tap add to library

### 3. **Ratings & Stats** ✓
- Grade films/shows 1-10 (overall)
- Rate individual episodes 1-10
- Combined score for shows: average of overall grade + episode average
- TV Time-style stats dashboard:
  - Total watch time (hours), films watched, episodes watched, shows completed
  - Watch time breakdown by show (top 10)
  - Genre breakdown (pie/bar, drill-down)
  - Rating distribution (histogram)
  - Leaderboards: rank by watch time, episodes watched, shows completed (premium: visible rank badge on profile)
  - Streaks: current binge streak, longest streak
  - Weekday breakdown: heatmap of activity by day-of-week

### 4. **Social** ✓
- Find & follow users by username
- View user profiles: name, avatar, background image, verified badge, bio, favorite count, watch time
- View user's library (filtered by type/status like your own)
- View user's stats (watch time, genres, leaderboard rank if premium)
- Activity feed: personalized stream of what followed users watched/rated recently
- Comments thread on every title (global per title, not per user) with likes and nested replies
- Users see comment count on title cards (indicator of community engagement)

### 5. **Notifications** ✓
- Bell with unread badge
- Alerts when tracked TV shows air new episodes
- Marked read/unread
- Optional push notifications (mobile)

### 6. **Upcoming Countdowns** ✓
- Next episodes for tracked shows (countdown to air date + time)
- Film premieres for tracked films
- History view: past episodes/releases you tracked

### 7. **Home Screen (Continue Watching)** ✓
- Featured hero card: most recent in-progress title (backdrop art + two-ring progress badge + episode number)
- Compact list of other in-progress items
- Settings: 
  - Toggle hero on/off
  - Choose progress style (rings, bar, percentage)
  - Premium: ring accent color picker, username color picker
  - Premium: custom poster/backdrop overrides

### 8. **Account & Auth** ✓
- Persistent login (JWT + refresh tokens) across restarts
- Profile editing: username, email, password, avatar, background image, language, theme
- Theme selection (Gruvbox free; other themes premium)
- Language selection: English, Galego, Português, Español, Esperanto
- Change password
- Delete account (cleans up all data)
- Verified badge request (admin-approved, badge on profile + in comment threads)

### 9. **Premium** ✓
- Avatar ring color picker (branded colors)
- Username color picker
- Verified badge request
- Custom posters/backdrops/episode stills (TMDB alternates or upload)
- Progress ring accent colors (Home screen)
- Leaderboard rank badge on profile
- Additional themes beyond Gruvbox
- Free accounts see all premium controls dimmed/locked with link to upgrade

### 10. **Onboarding** ✓
- One-time welcome tour after first login (server-side `has_seen_welcome` flag so it doesn't repeat on other devices)

### 11. **Import** ✓
- Bring history from TV Time GDPR export zip
- Runs in background with progress polling
- Handles TMDB lookups, deduping, partial failures

### 12. **Anti-Abuse** ✓
- Rate limiting (configurable per endpoint)
<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdA6n62ewvF2B3auuAjya4sYoS6hNoTik7lizx9smbBa0ow
6L+3lvQoScDL9bW0Yk1kQxp90c8P1EC1BhvHmZizCr8hHKCzIeplntjC1chbZ7B5
1HwBCQIQuYjVY+WAjTH7q63XfQVtE5uPFbngy1xXGNlX/baCqPLfqPn2rPAb6Uqp
3a3+vty96gjnUFarYfgkzHFjL6gG/Qog/eRQtZqrGrVcP0skyzF1owxr73PPbsFe
dlBg2d5vvOe7T4+Q0kzBiQtoOXPog2n4qCkxP4Pr
=UF9/
-----END PGP MESSAGE-----
<!-- /private -->
- Login backoff (exponential after N failures)
- Comment flood detection
- Admin panel: view bans, strike history, ban/unban users
- All limits tunable at runtime (no restart needed)

---

## Data Model

### Entities

- **`users`**: accounts with email, username, language, theme, premium status, aggregate stats (total_watch_minutes, computed via DB trigger)
- **`titles`**: catalog-sourced facts (title, year, poster, genres, runtime/episode count, TMDB id or normalized title_key)
  - Identity: TMDB ID when available, else normalized title_key (allows manual entries + YouTube videos + books to dedupe)
  - Types: `film`, `tv_show`, `book`, `youtube_video`, `concert`, `art_exhibition`, `city`, `country` (future ones exist in code but UI hidden for now)
- **`library_entries`**: user's state against a title (status, rating, notes, favorite, progress, custom poster/backdrop)
- **`title_genres`**: normalized M:N (title ↔ genre)
- **`episode_watches`**: per-episode watch state (episode number, rating, watched_at timestamp)
- **`comments`**: global thread per title (not per user), with nesting + like counts
- **`follows`**: user follow relationship
- **`notifications`**: new-episode alerts (read/unread, polymorphic: can be for a show or a film premiere)
- **`login_events`**: login history (no denormalized login_count on users; derived at read time)
- **`request_days`**: per-user daily request count (for analytics/anti-abuse)
- **`endpoint_stats`**: site-wide requests by endpoint (for admin analytics)
- **`bans` / `strikes`**: anti-abuse state

### Schema Quality

- **Strict normalization enforcement:** tests fail the suite if denormalization is introduced (BCNF via mechanical checks for the classic anomalies)
- **No copied columns across FKs:** e.g., comments don't store `tmdb_id` redundantly — they reference titles by FK and derive it if needed
- **Facts cached from external systems (TMDB metadata like `next_episode_air_date`) are NOT a normalization concern** — they depend only on the title's ID and are inherently stale

---

## Technical Architecture

### Backend
- **Framework:** FastAPI (Python, async)
- **Database:** PostgreSQL (schema managed by Alembic migrations)
- **Auth:** JWT + refresh tokens (HTTP-only cookies in web, localStorage on mobile/desktop)
- **API design:** RESTful with optional `?expand=field` to return related objects inline (Stripe-style expansion pattern)
- **Caching:** TMDB/Open Library responses cached in-memory for 30 minutes; book covers for 24 hours
- **Background tasks:** Episode checks, film release syncs, anti-abuse cleanup (configurable intervals)

### Frontend
- **Framework:** Flet (Python + Flutter)
- **Platforms:** Desktop (Windows/Mac/Linux), Web (FastAPI/uvicorn), Mobile (Android APK, iOS IPA)
- **Performance optimizations:**
  - Lazy list rendering (30 rows at a time)
  - Two-tier poster cache (in-memory + on-disk)
  - Stale-while-revalidate: paint cached data instantly, refresh in background
  - Separate connection pools for API calls vs. image downloads
  - Only re-render when fresh data differs (no flicker on unchanged data)
  - TMDB poster resizing: request small bucket (w92 ~4KB instead of w342 ~40KB) for thumbnails
  - Separate thread pool for image prefetching

### Admin Panel ✓
<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdALzNd2BlG1etm+go4WIksCGGikSuFYEy3wOfr4FHeXTEw
LEJccZZgOqHnApJCjtP7ur4AvynOpzXLk+hvOK/ybaCs3B4XcQgyP64mj8JQhbtc
1FcBCQIQPQdkjE5/jNn9ptD6yFSgyq5UDUYdUoi+EaWcKi0eP8tBt34QNy2dSHFS
vNk8OAo3zxc1yYrXCN0mLPFcDH4mW2MtxcuHXJ4StQOtaCay2Rtr1Oo=
=gbAo
-----END PGP MESSAGE-----
<!-- /private -->
- User manager: view usage, ban/unban, delete, edit account, grant/revoke premium days, verify/unverify
- Per-user charts: requests, connections, watches, comments, library additions (30 days, hover tooltips)
- Usage & analytics: requests-by-endpoint heatmap, drill-down to caller list
- Comment manager: view and delete comments
<!-- private -->
-----BEGIN PGP MESSAGE-----

hF4DQ/EuiSPJ5t0SAQdA/7ezjJHhq1J+Yel2pFYly1/Ocqtdpx5EIlKVnnGsPAAw
APHFHJU3yapKSR3ZY8yrvdf35/i5QMx2CWwE7JvZms7kjJVOBDiUtwYwgQdYfC73
1HEBCQIQ12DbzavdfYGYOFFSgR8yDDnRYpbD+ksR3hP8+U+uU7qrNFTdWGJT/Aan
uZMe/eSo7bhyH120nEQ4D3zTNLoHsZEYk6hqer27akRBeg3p7YfVce0UTAM9WZ91
u5iOCyRlL9znJCKwtx54wQZGfg==
=WTah
-----END PGP MESSAGE-----
<!-- /private -->
- Site Settings: toggle registration open/invite-only, tune all anti-abuse limits (no restart)
- Invite Codes: generate with max-uses and optional expiry

---

## Planned Expansions (Roadmap)

### Phase 2: Books (Backends ready, UI hidden)
- Open Library search/trending
- Page count tracking
- Author tracking (future: author profiles?)
- Genres from Open Library

### Phase 3: YouTube (Backends ready, UI hidden)
- YouTube Data API integration
- Channel subscriptions
- Video rating/watch tracking
- Trending channels feed

### Phase 4: Experiences (Data model ready, UI pending)
- **Concerts**: venue, date, artists, notes (photos?)
- **Art Exhibitions**: museum, dates, notes, rating
- **Cities**: visited date, notes, rating (replaces travel apps for taste curation)
- **Countries**: visited dates, regions explored
- Each gets its own card design, Explore feed, library filters

### Phase 5: Advanced Features (Planned, not scoped yet)
- **Badge/achievement system**: unlock badges for accomplishments (finish franchise, binge streak, watch N hours of genre)
- **Granular ranking metrics**: time by show, time per franchise, time per genre (beyond current watch_time only)
- **Person profiles**: cast/crew photo clicks link to their renar account (once actor/director accounts exist)
- **Recommendation engine**: ML-driven suggestions based on taste similarity with followed users
- **Collections/lists**: user-curated lists ("Best sci-fi of 2024", "Essential Scorsese")
- **Seasonal tracking**: "what I watched in 2026", annual wrap-up
- **Export/backup**: GDPR export, import to other systems

---

## Differentiators

1. **Multi-domain scope:** Not just films/shows; one unified place for all cultural consumption
2. **Social taste network:** Follow friends, see what they rate, discover through their taste (not algorithmic feeds)
3. **Granular tracking:** Episode-level progress, per-item ratings, notes; not just "watched/not watched"
4. **Stats-first design:** TV Time-level analytics, not an afterthought
5. **Blazing fast UX:** Every interaction feels snappy (lazy loading, cached results, separate image pools, no rebuilds on unchanged data)
6. **Privacy-conscious:** No algorithmic feeding, no tracking pixels, no surprise dark patterns — just your taste and your friends' taste
7. **Open import:** TV Time GDPR import on day 1; future imports from Letterboxd, Goodreads, etc.
8. **Premium with teeth:** Real value (rank badges, custom imagery, themes, color customization) not cosmetic upsells

---

## Current State

- **Live (Films/TV shows only):**
  - Library tracking, explore feeds, ratings, stats, social graph, comments, notifications, upcoming countdowns, account management, admin panel
  - Desktop app (Windows/Mac/Linux via Flet)
  - Web app (guarded by anti-abuse middleware)
  - Mobile app (Android APK via Flet, iOS via Flutter)
  - Full test coverage (pytest on both backend/frontend)

- **Ready but UI hidden:**
  - Books (Open Library integration)
  - YouTube (YouTube Data API integration)

- **In data model, no UI yet:**
  - Concerts, art exhibitions, cities, countries

- **Not yet scoped:**
  - Badge system, granular ranking metrics, person profiles, recommendations, lists, wrap-ups

---

## User Personas

1. **The Completionist** — tracks every film, every episode, wants stats that prove they watched everything. Uses: library, stats, leaderboards
2. **The Taste Curator** — cares about discovery through friends' taste, not algorithms. Uses: social, explore, comments, ratings
3. **The Fan** — deep dives into a franchise or genre, rates every episode, writes notes. Uses: episode tracking, notes, favorites
4. **The Social Butterfly** — shares what they're watching in real-time, cares about followers and comments. Uses: activity feed, comments, follows
5. **The Casual Watcher** — tracks what they watched so they don't repeat, doesn't care about rankings. Uses: library search, status filters

---

## Success Metrics

- DAU/MAU (daily/monthly active users)
- Library size per user (avg titles tracked)
- Social graph depth (followers per user, follow/follower ratio)
- Comment engagement (comments per title, replies per thread)
- Premium conversion rate
- Churn rate (monthly active to inactive)
- Time to meaningful action (add first title, follow first user, leave first comment)
- App performance: median request latency, p95 latency (target: sub-200ms for interactive calls)

