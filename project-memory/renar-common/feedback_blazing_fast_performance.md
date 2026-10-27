---
name: feedback-blazing-fast-performance
description: Top-priority constraint for renar frontend/backend work — the app must be and feel blazing fast
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7bf57748-bc65-4997-bffd-f20232216e38
---

Constraint #1, above all others: the renar app (frontend + backend) must be and feel blazing fast — in every window/view and every action.

**Why:** User explicitly flagged the app as feeling slow across all windows and actions and wants speed treated as the top priority going forward, not a nice-to-have.

**How to apply:** For any change touching renar-frontend, renar-backend, or common:
- Default to the fastest reasonable implementation — avoid blocking calls on UI/event threads, avoid redundant network/DB round-trips, reuse HTTP clients/sessions, cache/avoid refetching unchanged data, avoid rebuilding full widget/page trees when a partial update suffices.
- When proposing or reviewing designs, weigh perceived latency (time-to-interactive, responsiveness of navigation and actions) as a first-class criterion, not just correctness.
- When a fix trades off simplicity vs. speed on a user-facing interaction path, prefer speed unless the user says otherwise.
- Flag (don't silently accept) any new code that introduces synchronous blocking I/O in an event handler, N+1 API calls, or per-request client/session creation.

**Reaffirmed 2026-07-17:** user restated this unprompted ("always prioritize efficiency and lowest load times and responsiveness... nothing worse than having to wait while using the app") while reviewing an unrelated bug-fix pass — treat as confirmation this is a standing rule to apply proactively on every renar change, not just when explicitly asked to optimize.
