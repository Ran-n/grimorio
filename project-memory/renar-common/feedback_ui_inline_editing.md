---
name: feedback_ui_inline_editing
description: User strongly prefers inline editing over modal/dialog-based editing for all UI data entry
metadata:
  type: feedback
---

Prefer inline editing for all editable data in UI designs — click a cell/field in place, edit it directly, confirm with Enter or blur.

**Why:** User wants to get UI designs right on the first try; dialog-based or separate edit-form workflows are not acceptable unless there is no viable inline alternative (e.g., complex multi-field create flows where inline is ambiguous).

**How to apply:**
- Tables: use delegate-based in-cell editors (e.g., QStyledItemDelegate in PySide6), not "edit in panel below" or modal dialogs.
- Cards/detail views: fields should toggle to editable input on click/double-click, saving on blur or Enter.
- Lists: single-click or double-click activates an in-place line editor.
- Only fall back to a dialog when the edit target has no natural inline representation (e.g., a rich-text field that needs a full editor, or a create-new flow requiring many required fields simultaneously).
- Always save/discard with keyboard shortcuts (Enter = confirm, Escape = cancel) in addition to any pointer interaction.

See also: [[feedback_ui_disabled_buttons]]