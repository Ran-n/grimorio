---
name: feedback-push-after-each-change
description: "push after every change in breren, not batched at the end"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 966c3227-c064-44ec-8a4f-fd4a5c3fbfa2
  modified: 2026-08-04T11:49:51.070Z
---

For this project, push after each individual change rather than waiting to batch several changes into one push.

**Why:** user explicitly asked for this cadence in the breren repo.

**How to apply:** after completing and (if requested) committing a change here, immediately run the full [[feedback_push_all_remotes]] workflow (update docs → commit → push to `github`, `gitlab`, `codeberg` over SSH) rather than deferring to a later batch. Still only commit/push when the user has asked for the change to be committed — this overrides the "one push at the end" default, not the [[feedback_push]] rule that pushing itself requires a request. Since the user asked to push in this same message, treat that as standing authorization to push after each subsequent change in this session/project going forward.
