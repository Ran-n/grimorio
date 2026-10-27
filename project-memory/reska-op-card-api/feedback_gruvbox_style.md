---
name: feedback-gruvbox-style
description: "Admin UI must use Gruvbox color palette, not the default indigo/dark theme"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b9784cb2-0f8a-4523-a2f6-4863ef129660
---

Use Gruvbox colors for all admin HTML pages in this project.

Gruvbox palette in use:
- --bg: #1d2021
- --surface: #282828
- --surface-hi: #32302f
- --border: #3c3836
- --border-sub: #32302f
- --text: #ebdbb2
- --text-2: #a89984
- --text-3: #7c6f64
- --accent: #d79921 (yellow)
- --violet: #d65d0e (orange)

Accent highlights (e.g. tile hover, focus rings) use rgba(215,153,33, …) and #fabd2f for bright yellow.

**Why:** User explicitly asked to use Gruvbox style.

**How to apply:** Any time a new admin page or component is added, copy the `:root` block above instead of the default indigo/zinc dark theme.
