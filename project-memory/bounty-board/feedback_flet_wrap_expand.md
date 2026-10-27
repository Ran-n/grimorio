---
name: flet-wrap-expand-grey-box
description: Flet Row(wrap=True) with an expand child renders a silent grey box in the real window; widget-tree tests pass
metadata:
  type: feedback
---

In Flet, a `ft.Row(wrap=True)` that holds a child with `expand=True` (a Text, a Container spacer, a nested Row) fails inside Flutter: the real window shows a flat grey box where that subtree (often the whole list around it) should be. Python logs nothing, and widget-tree tests built against a fake Page pass.

**Why:** found 2026-10-19 in bounty_board's store event details panel. Two rows (a badge row next to the player count, and a footer with a stretching "read at" text) turned the panel grey. Only a screenshot of the running app showed it.

**How to apply:** never combine `wrap=True` with an `expand` child in the same Row. Use `tight=True` children in a wrapping row, or drop `wrap` and let one `expand` child absorb the space. When a Flet screen shows a grey box with no error logged, look for this first, and confirm every new layout in the real window ([[tests-requirement]] rendered UI tests), not only in widget-tree tests. See also [[flet-snackbar-quirks]].
