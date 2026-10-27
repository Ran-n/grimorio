---
name: project-person-profile-linking
description: "Future feature request — clicking an actor/director's photo in cast & crew should link to their renar profile if they have an account"
metadata: 
  node_type: memory
  type: project
  originSessionId: fc71d234-1672-4047-9cf9-0d4a4ed00353
---

Desired future behavior: on the title page's cast & crew row ([people_row.py](d:\Users\{USER}\sw\renar\renar-frontend\src\renar_frontend\views\people_row.py), rendered via `build_people_row` in [title_view.py](d:\Users\{USER}\sw\renar\renar-frontend\src\renar_frontend\views\title_view.py)), if an actor or director has a real renar user account, clicking their photo/card should navigate to their profile instead of doing nothing.

**Why:** User wants cast/crew photos to double as profile links when the person is also a registered renar user — ties into [[project_director_photo_feature]] (director/actor photos with `profile_url` from TMDB, added 2026-07-14).

**How to apply:** Not implemented yet — there is no existing mechanism linking a TMDB person (`cast`/`crew` entries, identified by TMDB person id) to a renar user account. Before building the click-through, this needs: (1) a way to associate a renar `User` with a TMDB person id, (2) the `/tmdb/credits` backend endpoint ([tmdb.py](d:\Users\{USER}\sw\renar\renar-backend\src\renar_backend\routers\tmdb.py)) to expose that linkage (e.g. `user_id` or `has_account` per cast/crew entry) so the frontend knows whether to make the card clickable. Revisit when user account profiles / social features are being built.
