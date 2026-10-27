---
name: feedback_ui_cta_hierarchy
description: "Primary call-to-action must visually dominate; secondary/reference links (source repos, etc.) go smaller in their own row below, using each platform's real logo"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f68bdf91-6c0a-4287-899b-f144b83cced9
  modified: 2026-08-04T10:38:30.818Z
---

When a page has one primary action (e.g. "Download") plus several secondary reference links (e.g. source repo mirrors on GitHub/GitLab/Codeberg), don't give them equal visual weight in a single row.

**Why:** On vitralis's landing page, the download button and the GitHub source link started as equal-sized buttons in the same row. Once GitLab and Codeberg source links were added alongside, the user pointed out the download button "doesn't look that important now" — visual weight had drifted to match the count of buttons rather than actual importance.

**How to apply:**
- Give the primary CTA its own row, sized up (larger font/padding, e.g. a `.btn-lg` modifier) so it reads as the main action.
- Put secondary/reference links (source mirrors, docs, etc.) in a separate row below, sized down (e.g. `.btn-sm`).
- For any brand/platform link (GitHub, GitLab, Codeberg, etc.), always use that platform's real official logo — never a generic placeholder icon (e.g. a generic fork/branch icon). Pull the accurate SVG path data (e.g. from the simple-icons project, `cdn.jsdelivr.net/npm/simple-icons@latest/icons/<name>.svg`) rather than hand-approximating it — the risk of a wrong/garbled brand shape is not worth guessing.
- This generalizes beyond vitralis: any project page with one primary action and multiple secondary links should follow this size/row hierarchy.
