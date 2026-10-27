---
name: feedback-render-before-showing-icons
description: "Render hand-coded SVG/icon work to an actual image and inspect it before sending to the user — never eyeball raw coordinates"
metadata:
  type: feedback
  originSessionId: renar-frontend-reviewer-badge-icon
  modified: 2026-08-25T11:58:52.808Z
---

When building or editing hand-coded SVG (custom icons, badges, illustrations), always render the file to a PNG (Playwright + a small HTML wrapper works, already available in renar-frontend) and actually view it via Read before showing it to the user. Also render at the icon's real deployed size(s), not just a large preview — a design can look fine at 96px and collapse into an unreadable blob at the actual 14-20px render size.

**Why:** spent ~12 iterations hand-tuning SVG path coordinates for a reviewer badge icon based on visual description alone, without ever rendering the output. Multiple sends had obvious bugs (a highlight shape poking outside the rounded corner into the outline stroke, glyphs accidentally forming a cartoon face) that would have been caught by a two-second look at the actual render. Once rendering-before-sending started, bugs were caught and fixed in one pass instead of requiring another round of user feedback.

**How to apply:** before any `SendUserFile`/`Artifact` call showing a graphic that was hand-authored (not a screenshot of a running app), render it first and inspect the image yourself. For icons/badges specifically, render at every size the code actually uses (check call sites for the real `size=`/`badge_size=` values) — legibility at the deployed size is not optional context, it's the actual spec.
