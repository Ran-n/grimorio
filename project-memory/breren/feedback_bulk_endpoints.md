---
name: bulk-endpoints
description: Prefer a bulk/list endpoint over a frontend loop of N single-item API calls when N can be large
metadata:
  type: feedback
---

Before writing a frontend loop that calls a per-item API endpoint N times, check whether a bulk/list-shaped endpoint already exists. If not, and N can realistically be large, add one instead of accepting N round trips.

A bulk endpoint should do the batched work in one request/transaction: one query for existing state, one commit for all the writes, and — critically — any expensive post-write recomputation (progress sync, aggregate summaries, trigger-driven recalculation) run **once for the whole batch**, not once per item. Looping single-item calls multiplies that recomputation cost by N on top of the N HTTP round trips.

**Why:** Confirmed while building a "mark earlier unwatched episodes too" feature in [[project_renar_layout]] (renar) — the existing single-episode `PUT /media/{id}/episodes/{season}/{episode}` endpoint each triggers `_sync_progress` + `_ratings_summary` (each a full re-query over the item's watch rows). The existing season-scoped `POST /media/{id}/episodes/bulk` endpoint already did the batching correctly (one bulk insert, one `_sync_progress`, one `_ratings_summary` regardless of list length) — reused it for the new feature instead of looping the single-item call. User confirmed this is the general rule to always respect, not just a one-off for that feature.

**How to apply:** Any time a new feature needs to touch multiple items of the same kind at once (mark-all, bulk-delete, bulk-update-status, etc.), reach for or add a bulk endpoint first. When auditing existing code (e.g. during a full sweep or code review), flag any frontend `for` loop that calls a single-item API method inside it as a candidate for this fix — check `api_client.py` (or equivalent) for an existing bulk method before looping.
