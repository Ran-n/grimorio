---
name: feedback-no-emdash-ui-text
description: never use em-dashes in user-facing UI copy/strings; they read as AI-generated
metadata: 
  node_type: memory
  type: feedback
  originSessionId: da54eda9-7f82-4002-9e66-9e70ef74a77c
  modified: 2026-07-27T11:07:23.940Z
---

Never use em-dashes (—) in user-facing text: UI strings, button labels, dialog copy, error messages, any text wrapped in a translation call like `_(...)`. Use a comma, period, or "so"/"and" instead.

**Why:** user flagged it explicitly while reviewing renar-frontend's import view copy — em-dashes make text look AI-generated.

**How to apply:** applies to strings actually rendered to end users. Does NOT apply to code comments, docstrings, log messages, or commit messages — those are developer-facing and the user's other style memories ([[feedback_response_style]]) don't restrict em-dash use there. When writing or editing any `_("...")` string (or equivalent i18n-wrapped literal) in renar-frontend or renar-backend, check for and avoid em-dashes before finishing the edit.
