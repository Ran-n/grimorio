---
name: feedback-distinct-icons
description: every distinct UI action/setting must have its own icon; never reuse one icon for two different controls
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f23505c2-ebfc-476f-9c16-0495ca517950
  modified: 2026-08-05T14:41:00.151Z
---

Two different settings/actions in the same UI must never share the same icon, even if they're thematically related (e.g. "Language" selector and "Show original titles" toggle both touch language but are different controls).

**Why:** found in renar-frontend's profile_view.py — the "Language" ListTile and the "Show original titles" switch_tile both used `ft.Icons.TRANSLATE`, making them visually indistinguishable at a glance. Fixed by giving "Show original titles" `ft.Icons.SUBTITLES_OUTLINED` instead.

**How to apply:** when adding or reviewing any tile/button/menu-item list, check that no two items share an icon constant. If a new setting is conceptually close to an existing one, pick a related-but-distinct icon rather than reusing the same one.
