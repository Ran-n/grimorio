---
name: flet-gridview-runs-count-default
description: "Flet's ft.GridView.runs_count field defaults to 1, not None — truthiness checks on it silently misfire for max_extent-only grids"
metadata: 
  node_type: memory
  type: project
  originSessionId: 209a5ce8-34f4-4ad6-b650-98a6a3ab97e8
  modified: 2026-08-20T08:50:04.254Z
---

`ft.GridView.runs_count` is a dataclass field defaulting to `1`, not
`None`/`0` (see `flet/controls/core/grid_view.py`). A grid built with only
`max_extent` set (e.g. explore_view.py's results grid) still reports a
truthy `runs_count` of `1`. Any code doing `if grid.runs_count: ...` to
decide between "fixed column count" and "max_extent-based" sizing will
always take the `runs_count` branch and get a bogus 1-column answer.

**Why:** this shipped a real bug in `views/lazy_list.py`'s
`_gridview_columns()` — it checked `runs_count` before `max_extent`, so
Explore's end-of-list tile landed inline in the next grid cell instead of
centered on its own row. The existing unit tests never caught it because
they passed `runs_count=None` explicitly, which doesn't match how
explore_view.py actually constructs the grid (default left in place).

**How to apply:** when writing code or tests against `ft.GridView`, check
`max_extent` first and only trust `runs_count` when it's explicitly set
above the default (e.g. `> 1`, or track "was this constructor kwarg passed"
some other way). When testing such logic, construct the control the same
way the real call site does — don't override defaults away just to make
the "other" branch reachable, or the test stops covering the real usage.
