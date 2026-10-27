---
name: bounty-board-project-spec
description: "Source-of-truth spec for bounty_board (OPTCG event watcher desktop app): UX, behaviour and technical requirements agreed 2026-10-04"
metadata:
  node_type: memory
  type: project
  originSessionId: b2e62357-be6d-437d-b37a-f465ffe7843f
  modified: 2026-10-04T14:55:55.013Z
---

# Bounty Board — project spec (agreed 2026-10-04)

## Product
- Desktop-only Windows app (single user, no backend) replacing the `old/optcg_watch.py` script. User chose this over the backend+frontend split after discussion. Code must stay hexagonal so a FastAPI backend / multi-user version can be split out later.
- Name: **bounty_board** / "Bounty Board".
- Watches en.onepiece-cardgame.com/events (HTML scraping, no API): new event pages (all regions, keyword filter), Regionals in followed regions (default Europe).
- First version scope (all confirmed): core (scrape, diff, reminders, toast/email/Telegram, event browser, settings screen, .ics export) + change tracking (date/venue/link/note changes, removals, restores) + registration-opening alerts + map view with distance-from-home filter.
- First check sends one summary, not one alert per event.

## UX / behaviour
- Runs in the tray (pystray); closing the window hides to tray; Quit in tray exits cleanly; optional start at logon (HKCU Run key, `--minimized`); second launch shows the existing window.
- Tabs: Regionals, All events, Map, Alerts (log + delivery results + test), Settings.
- Settings edited inline, saved on Enter/blur/toggle; no dialogs.
- Themes: multiple, selectable in Settings → Appearance, applied live; **default Gruvbox (follows system light/dark)**. User explicitly asked for this (2026-10-04).
- Secrets (SMTP password, Telegram token) in Windows Credential Manager only.
- Notification channels: Windows toast, email (SMTP), Telegram — all three required.

## Technical
- uv, Python 3.14, Flet 0.85.3 (+ flet-map), SQLAlchemy + Alembic on SQLite, httpx, keyring, pystray, pytest/hypothesis/respx, ruff.
- Layout: domain / application (use cases + ports) / adapters / ui / bootstrap; dependency direction enforced by tests/test_architecture.py. User explicitly asked for principled organization (SOLID, hexagonal) after disliking the first layout.
- Schema must be BCNF; derived values (start/end dates, registration opening, last-changed, reminder-sent) are never stored.
- Data in %LOCALAPPDATA%\bounty_board (override BOUNTY_BOARD_HOME).
