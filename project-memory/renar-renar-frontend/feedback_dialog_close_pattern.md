---
name: feedback-dialog-close-pattern
description: "Flet AlertDialogs must dismiss via an X IconButton in the title row, top-right — never a bottom \"Close\" text button or a bottom-right X"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 062969c8-55eb-4d90-8316-8c364d50bf22
  modified: 2026-08-02T12:45:04.047Z
---

Every `ft.AlertDialog` that has a plain dismiss (not a Cancel/Confirm decision) must close via an `ft.IconButton(ft.Icons.CLOSE, ...)` placed top-right in the dialog's `title` row — not as a `ft.TextButton(_("Close"), ...)` in `actions`, and not as an X positioned bottom-right.

**Why:** User flagged inconsistency across renar-frontend dialogs — some used a bottom "Close" text button, others an X in different corners. Confirmed working pattern already existed in `profile_view.py`'s Theme-picker dialog (`open_theme_dialog`); the rule is to make every other dialog match it.

**How to apply:** For any new or edited `ft.AlertDialog` in `renar-frontend`, use this shape:
```python
title=ft.Row(
    [
        ft.Text(_("Dialog title"), expand=True),
        ft.IconButton(
            ft.Icons.CLOSE,
            tooltip=_("Close"),
            on_click=lambda e: page.pop_dialog(),
            icon_size=18,
            style=ft.ButtonStyle(padding=0),
        ),
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
),
```
and omit a "Close" entry from `actions` entirely.

**Exception:** Binary decision dialogs (Cancel/Confirm, e.g. delete confirmations) keep their `Cancel`/`Delete` (or similar) bottom `actions` — Cancel already serves as the dismiss action there, so no top-right X is added on top of it.
