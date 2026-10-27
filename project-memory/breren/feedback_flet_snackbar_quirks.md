---
name: feedback_flet_snackbar_quirks
description: Flet 0.85.x SnackBar theming/reactivity quirks — ignores custom ColorScheme tokens, ignores in-place property updates after a while; plus a general uv-run-app process-hygiene lesson
metadata:
  type: feedback
---

Discovered in renar-frontend (a Flet desktop/web/mobile app) while theming a themed `SnackBar` banner — cost many wasted test cycles before being pinned down. Applies to any Flet project (confirmed on 0.85.3; re-verify on other versions before assuming these still hold).

**Bug 1 — `ft.Colors.PRIMARY_CONTAINER` (and other `ColorScheme` role tokens) don't resolve from a custom `ft.ColorScheme` for `SnackBar` specifically.** They silently render as Flutter's stock Material baseline color instead, regardless of which theme is active or how fresh the process is. Other controls (e.g. `Container(bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST)`) picked up the same custom scheme correctly — this is a `SnackBar`-specific gap, not a general "tokens don't work" issue.
**Fix:** compute the actual color as a literal hex string in Python (read the active theme's `ft.ColorScheme.primary_container`/`on_primary_container` etc. directly, or replicate the seed-derived tonal computation) and pass that literal value as `bgcolor=`/`color=` instead of a token.

**Bug 2 — mutating an already-shown `SnackBar`'s properties and calling `.update()` silently no-ops once it's been on screen for a while.** `page.update(control, ...)` reports success (no exception), the control's `.open` stays `True`, but the client stops applying further property changes to that already-mounted widget after some seconds. A fast/immediate test after showing it will look like it works — the bug only appears once real time has passed (waiting past whatever `duration` was set no longer matters once its dismissal is client-driven, but the update-goes-nowhere behavior itself is time-dependent regardless).
**Fix:** don't mutate in place — pop/dismiss the existing dialog and show a brand-new `SnackBar` control built with current values. A freshly mounted widget always renders correctly; there is no reliable in-place repaint path for an already-shown one.

**Red herring to skip re-discovering:** `SnackBar.open` does not flip to `False` on a server-side timer when `duration` elapses — dismissal is client-driven (the server only removes the dialog from its stack once the client reports the dismiss animation actually finished). Don't waste time suspecting `.open` staleness as the cause of "an update to this control isn't showing up" — it isn't that.

## General process-hygiene lesson (any Flet desktop app, not just SnackBar)

Killing `flet.exe` only kills the Flutter GUI shell — it does **not** kill the underlying Python server process (`python.exe ... main.py`, launched via `uv run app`/`flet run`/similar). A "restart" that only closes/reopens the app window can leave the old server process running old code, with the new window simply reconnecting to it. Multiple overlapping server instances can accumulate silently across a long debugging session (one may even end up fully orphaned, listening on no port at all), producing persistent, confusing "the fix isn't working" false signals that are actually just stale processes serving pre-fix code.

**How to apply:** before trusting any "I restarted and it's still broken" report — or your own verification test — for a Flet desktop app, check actual process state first: list `python.exe` processes and filter for the project's script/entry point, and check the `flet.exe` GUI count. Kill every matching `python.exe`, confirm zero remain, *then* launch exactly once and re-verify before testing. Note: `uv run python script.py` normally spawns **two** `python.exe` entries per single launch (a benign parent/child pair, not a duplicate instance) — judge actual live-window count by the `flet.exe` process count instead, which should be exactly one per real open window.
