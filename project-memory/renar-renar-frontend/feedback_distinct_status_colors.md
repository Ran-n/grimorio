---
name: feedback-distinct-status-colors
description: every distinct status/state value shown to the user needs its own distinct color; never let two states share one color (including "dim/neutral" as a shared fallback) or the states become visually indistinguishable
metadata:
  node_type: memory
  type: feedback
  originSessionId: unknown
  modified: 2026-08-17T11:34:02.043Z
---

When a UI element cycles through 2+ named states (status badges, fact lines, chips), each state needs a color of its own — don't let two states share a color, and don't let "no color" (plain dim/neutral) double as one of the states once there are 3+ possible values.

**Why:** found in renar-frontend's `share_image.py` episode/season share cards. First pass colored an episode's aired/unaired fact green for "unaired" only, aired left the plain dim gray — corrected to green=aired/blue=unaired instead. Then the season card's three-state aired/airing/unaired fact initially reused the same green for both "airing" and "aired" (asked: "what about airing in season?") — the two states were indistinguishable by color even though the text differed. Fixed by giving "aired" a third distinct color (aqua) instead of falling back to green or dim. Final ask ("I want colors for all") confirmed every state should get a real color, not a "highlight vs. neutral" binary. Same underlying principle as [[feedback-distinct-icons]] (never reuse one icon for two different controls) applied to color instead of iconography.

**How to apply:** when adding a status fact/badge with N possible values, map out all N up front and assign N distinct colors (or confirm the design intentionally treats some as "no color" — but state that explicitly, don't let it happen by default because only the "important" state got a color). Reserve red specifically for states that are genuinely bad news (e.g. a show being cancelled) — don't use it for "hasn't happened yet"/neutral states just because a bool ended up mapping to it.
