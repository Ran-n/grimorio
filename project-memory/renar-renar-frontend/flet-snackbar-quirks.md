---
name: flet-snackbar-quirks
description: "Flet 0.85.3 SnackBar theming/reactivity quirks (renar-frontend) — doesn't inherit ColorScheme tokens, doesn't repaint from in-place property updates"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0c89cf24-223a-4174-aec7-9c360870bc62
  modified: 2026-08-17T11:34:33.490Z
---

Two independent Flet 0.85.3 `SnackBar` bugs, both discovered the hard way (many test cycles) while theming the confirm-email banner in renar-frontend. See `docs/design-decisions.md`'s "`SnackBar` colors are computed in Python..." entry for the full writeup; this is the condensed lesson for next time.

**Bug 1 — `ft.Colors.PRIMARY_CONTAINER` (and friends) don't resolve from this app's custom `ColorScheme` for `SnackBar` specifically.** They silently fall back to Flutter's stock Material baseline (a blue nothing-to-do-with-the-theme) regardless of which theme is active or how fresh the process is. Verified: other controls (`Container(bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST)` etc.) render fine with tokens — it's `SnackBar` specifically. Fix: compute literal hex in Python (`branding/themes.py: surface_colors()`, pulled from the theme's own `ft.ColorScheme.primary_container`/`on_primary_container`, with a lighten/darken fallback for themes that only set `color_scheme_seed`) and pass those as `bgcolor=`/`color=` instead of a token.

**Bug 2 — mutating an already-shown `SnackBar`'s properties and calling `.update()` silently no-ops once it's been on screen a while.** `page.update(banner, banner.content, banner.action)` reports success (no exception), `banner.open` stays `True` the whole time, but the client stops applying further property changes to that already-mounted widget after some seconds. Confirmed by waiting past the 8s `duration` before testing — an immediate/fast test (bad, hides the bug) looked like it worked. Fix: don't mutate in place — `page.pop_dialog()` then build and `show_dialog()` a brand new `SnackBar`. A freshly mounted control always renders correctly.

**Red herring ruled out:** `SnackBar.open` does NOT flip to `False` on a server-side timer when `duration` elapses. Dismissal is client-driven (`Page._wrap_dialog_on_dismiss` only removes it from `page._dialogs.controls` once Flutter reports the dismiss animation actually finished) — don't waste time suspecting `banner.open` staleness as the cause of a "theme change doesn't update the banner" bug.

**Why:** if a future Flet upgrade is being evaluated, re-test whether `ColorScheme` inheritance and in-place `SnackBar.update()` reactivity got fixed before assuming the token-based or mutate-in-place approaches still don't work — both are simpler than the current workaround.

**How to apply:** any other transient overlay control (banners, toasts) added to this app should default to the dismiss-and-recreate pattern for live theme updates, and use `surface_colors()`-style literal colors rather than `ft.Colors.*` tokens, until this is retested on a newer Flet version.

## Process-hygiene lesson (applies beyond SnackBar)

Debugging this wasted enormous effort because of **orphaned `uv run app` processes** silently accumulating across a long session: killing `flet.exe` only kills the Flutter GUI shell, not the underlying Python server (`python.exe ... main.py`) — a "restart" that only closes/reopens the window can leave the old server process running old code, serving a new window that connects right back to it. Multiple overlapping instances (one even fully orphaned, listening on no port at all) caused hours of "the fix isn't working" false signals that were actually just stale processes.

**How to apply:** before trusting *any* "I restarted and it's still broken" report (or your own test) for this app, verify actual process state first: `wmic process where "name='python.exe'" get ProcessId,CommandLine 2>/dev/null | grep -i renar` and `tasklist /FI "IMAGENAME eq flet.exe"` — kill every match, confirm zero remain, *then* launch exactly once and re-verify exactly one `flet.exe` exists before testing. Note: `uv run python script.py` normally shows **two** `python.exe` entries per single launch (a benign parent/child pair) — that's not a duplicate instance; judge instance count by the `flet.exe` GUI count instead, which should be exactly one per real window.

A `uv run app` launch that immediately fails with `OSError: ... only one usage of each socket address ... 8080` is not a real failure — it means an earlier instance is already up and listening (`localhost:8080`), so the "restart" was redundant, not broken. Confirm with `Get-NetTCPConnection -LocalPort 8080 | Select LocalAddress,State,OwningProcess` then `Get-Process -Id <pid>` — if it resolves to this repo's `.venv\Scripts\python.exe`, the app is already running fine with whatever code was live when that process started (check its `StartTime` against your last edit to know if it's stale or current) and no further launch is needed.
