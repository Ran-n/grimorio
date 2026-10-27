---
name: feedback-backlog-blocking-tags
description: "Every renar backlog item must be tagged [Blocking for 1.0], [Future], or [Pending manual review]; ask the user when the call isn't clear-cut, don't guess"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 15497838-85fa-4285-b16c-a79306f48d6b
  modified: 2026-08-24T11:09:51.843Z
---

Every entry in both renar repos' `docs/backlog.md` carries a tag right after the opening `- **`: `[Blocking for 1.0]`, `[Future]`, or `[Pending manual review]`. "1.0" means the next major version bump (first stable/public release), not the next minor/patch — confirmed explicitly: "next version, like 1.0.0 2.0.0 not 1.1.0 or 1.0.1".

`[Pending manual review]` (added 2026-08-24) marks an item whose code side is fully implemented and tested, where what remains is a one-time real-world action only the user can take — buying an account, generating and safeguarding a credential, etc. — not further engineering work. First use: renar-frontend's Android release-signing entry, once `_patch_android_signing_config()` shipped and only keystore generation + Play Console signup were left.

**Why:** the user wants to be able to tell at a glance what's actually gating the 1.0 release versus what's deferred feature/polish work, without re-deriving it each time. See [[feedback_backlog_no_done_entries]] for the related rule that resolved entries get deleted rather than annotated — the two rules compose: every *remaining* item should be one of these two tags, nothing else.

**How to apply:**
- New backlog entries get a tag at creation time, not left untagged for later.
- Rough guide used so far: store-launch prerequisites (privacy policy, ToS, data-safety audit, HTTPS-by-default, crash monitoring, payment/IAP decision, required build/signing/store-assets work, a real support mailbox) and core correctness bugs users would hit immediately (data integrity, core-flow bugs like the "Watch Next" caught-up bug or future-episode marking, missing images/truncated text on primary screens, general perceived performance) lean **blocking**. New/optional features not yet committed to (social login, recommendation feed, push notifications, new trackable media types, admin role granularity, minor edge-case bugs that self-correct) lean **future**.
- **When a call isn't clear-cut, ask — don't guess.** Borderline calls already surfaced and confirmed: "make the app snappier" → blocking; Cloudflare Turnstile's remaining loose ends (in-memory session store, desktop skip, cleartext-manifest hack) → blocking (ties to the already-blocking HTTPS item). Use AskUserQuestion for future ambiguous ones rather than picking silently.
- iOS/web build-path items are conditionally tagged (`[Blocking for 1.0 if iOS/web ships alongside Android]`) since Android-first is the documented launch plan — only fully blocking once that assumption changes.
