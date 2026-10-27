---
name: Toolbar fixed width
description: The toolbar window must never change size at runtime — lock width after initial layout
type: feedback
originSessionId: eb3e695a-48f9-4834-8878-715a799b41ac
---
The toolbar window must not resize when mode buttons change their text (e.g. "Draw" → "Drawing…", "Pan" → "Panning…", "Delete" → "Deleting…").

**Why:** Qt re-flows layout when button text changes, which widens the window unexpectedly during drawing mode.

**How to apply:** After `self.resize(self.sizeHint())` in `Toolbar.__init__`, call `self.setFixedWidth(self.width())` to lock the width. Any future buttons that change text at runtime must not be allowed to grow the window.
