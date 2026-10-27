---
name: feedback-artifact-update-from-webfetch
description: "How to edit and republish an existing Artifact when you don't have its original source file, only a WebFetch-downloaded copy"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c6b2a8f3-9058-4993-9576-070dc2b61eab
  modified: 2026-08-20T07:39:34.747Z
---

To update a previously-published Artifact (e.g. the "Renar Backlog" page)
in a session that doesn't have its original source file on disk:

1. `WebFetch` the artifact URL with a prompt asking for the full raw
   source — the tool saves the complete fetched HTML to a local
   `tool-results/artifact-*.html` path (shown in its own output) even
   though the prompt-driven summary it returns inline is truncated/lossy.
   Read that saved file, not the summary.
2. That saved file is NOT republishable as-is: line 1 is the platform's
   injected `frame-runtime` script plus an opening
   `<!doctype><html><head>...<body>` wrapper, none of which was part of
   the original authored source (the `Artifact` tool adds this wrapper
   automatically at publish time and rejects/duplicates it if resubmitted).
   Strip that first line; the real content starts at the `<title>` tag
   on line 2 and runs to the final `</script>` with no closing
   `</body></html>` (the platform strips those too).
3. Edit the stripped copy, then `Artifact` publish with `url:` set to the
   original artifact's URL to update in place, not create a new one.

**Why:** cost a wasted round-trip discovering the frame-runtime preamble
would have been republished as page content, corrupting the artifact, if
sent through unedited — found while syncing the Renar Backlog artifact's
`DATA`/`PROGRESS` arrays to a `docs/backlog.md` edit per
[[feedback_backlog_artifact_sync]].

**How to apply:** any future "sync this artifact to the current doc"
task in a session that didn't originally publish that artifact.
