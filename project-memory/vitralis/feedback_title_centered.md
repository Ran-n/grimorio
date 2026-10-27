---
name: Toolbar title always centered
description: The Vitralis logo+title in the toolbar header must always be centered, regardless of surrounding buttons
type: feedback
originSessionId: 2860c22c-0f26-4b26-be55-21aac06dbbc2
---
The toolbar title row (icon + "itralis" text) must always be visually centered within the toolbar width.

**Why:** The quit button on the right was offsetting the title to the left; user wants it centered at all times.

**How to apply:** When laying out the title row, mirror any fixed-width widget on one side with an equal-sized invisible spacer on the other side (e.g. a `QWidget` with `setFixedSize` matching the quit button), so the handle always sits in the true center.
