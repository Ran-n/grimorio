---
name: feedback_verify_before_claiming_done
description: "always actually run/observe a fix working before telling the user it's fixed, not just reason about it or ship it on static analysis"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c6fcf0ba-09e3-4fb1-8a40-dbb5afc3aebd
---

Never claim a bug is fixed based on code reading/reasoning alone — actually run the app and observe the specific behavior before saying it works. If there's no way to easily run and observe it, say so explicitly instead of asserting success.

**Why:** on the Renar Upcoming-list scroll bug, three consecutive "fixes" were shipped as APKs with confident explanations (scroll_key → offset/delta math, a settle-delay theory) that turned out wrong every time — each was reasoned out from source/docs, never actually driven in the app. Only after spinning up the real backend+frontend and driving it with Playwright + screenshots did the actual bug surface (a pixel-height estimate, not a timing race), and only then did the fix actually verify correct. Confident static reasoning about async/UI timing bugs is unreliable; runtime observation is not optional for this class of bug.

**How to apply:** for any bug fix or feature that has an observable runtime behavior (especially UI/scroll/async/timing issues), spin up the actual app (or as close to it as feasible — e.g. backend+web build+headless browser with screenshots for this Flet project) and drive the exact reported scenario before reporting it fixed. Static code review / "this should work because X" is not sufficient evidence for this kind of bug. If verification genuinely isn't feasible in the environment, say explicitly "I could not verify this live" rather than implying it was confirmed.
