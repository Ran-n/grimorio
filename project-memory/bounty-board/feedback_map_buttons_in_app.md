---
name: map-buttons-in-app
description: "bounty_board — every \"Map\" button opens the app's own Map tab focused on that event, never Google Maps"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 87259a4a-3379-44ec-916d-a4bb72c8a451
  modified: 2026-10-06T10:29:00.232Z
---

In bounty_board, a "Map" button on any event (tournaments, store events, anything added later) must open the in-app Map tab focused on that event. Opening Google Maps / an external browser is only a fallback when the place can't be shown on the app map (no coordinates).

**Why:** User said (2026-10-06) "map has to open the one on the app, remember this always" after the Stores tab's Map button opened Google Maps.

**How to apply:** When adding any new event kind or card, wire its Map action to the Shell's in-app map focus (like `Shell.show_on_map`), and make sure the Map tab can show that kind of event. Related: [[bounty-board-project-spec]].
