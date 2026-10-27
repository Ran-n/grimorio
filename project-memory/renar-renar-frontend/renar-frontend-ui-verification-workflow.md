---
name: renar-frontend-ui-verification-workflow
description: "How to spin up renar-frontend headlessly and drive it with Playwright to visually verify a Flet UI change, including a throwaway-account signup shortcut"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9c716faa-3805-45eb-9e11-372ee39b6089
  modified: 2026-08-17T10:49:21.115Z
---

To visually verify a `renar-frontend` UI change without the desktop
window (e.g. for automated screenshotting):

1. `RENAR_FRONTEND_PORT=<port> uv run web` serves the app over HTTP —
   Flet's web renderer, drivable with a headless browser.
2. Playwright's Python package isn't in this repo's own venv; use the
   system install at
   `C:/Users/{USER}/AppData/Local/Programs/Python/Python311` (both the
   `python.exe` and its `Lib/site-packages` on `sys.path`).
3. The page is a Flutter canvas, not real DOM — `get_by_role`/text
   locators mostly fail (elements resolve to
   `flt-semantics-placeholder`, positioned off in a hidden a11y layer).
   Click by pixel coordinate (`page.mouse.click(x, y)`) against a
   screenshot taken moments earlier instead.
4. No test account existed — the app's own signup flow works for this:
   click the "add person" icon below the login button, fill
   username/email/password, submit. The confirmation-code screen can be
   ignored: the account can already log in immediately, unconfirmed
   accounts just get 7 days before login is blocked and 14 before
   deletion.
5. Always Windows-path your screenshot outputs (`D:/tmp/...`), not
   POSIX (`/d/tmp/...`) — the system Python is a native Windows
   executable and silently no-ops on a POSIX-style path (script exits
   0, file never appears).
6. `home_view.py` exposes `/home-progress-style` — a Profile settings
   page that renders `render_hero_card`/`render_continuing_row` with
   mock data, independent of any real watch history. Faster than
   fabricating "in progress" state on a fresh account when the goal is
   just checking hero/row card layout.
7. Kill the server after: find the PID via
   `Get-NetTCPConnection -State Listen | Where LocalPort -eq <port>`,
   then `Stop-Process -Force`.

**Why:** built this up over a live session verifying hero-card
poster/ring sizing changes — re-deriving any one of these steps from
scratch cost real turns (wrong path silently dropping the screenshot,
role-locator timeouts against the Flutter canvas, not knowing signup
didn't need email confirmation).

**How to apply:** any future "run the app and check this UI change"
request in this repo, especially for Home/hero-card/progress-badge work.
See also [[feedback-nearest-neighbor-zoom-artifact]] for the zoom-quality
pitfall hit during the same investigation.
