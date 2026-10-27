---
name: feedback_no_scripts
description: "Don't write patch scripts — execute Discord/DB operations directly"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c2ed755d-cd25-4831-8d3a-da44476e85d5
---

Don't create patch scripts in `scripts/` to perform one-off operations. Execute the action directly (e.g. run tsx inline or use the existing script runner) instead of leaving a file behind.

**Why:** User finds it more direct and cleaner — no script file to clean up afterward.

**How to apply:** When asked to fix something in the live Discord guild or DB, run the code immediately via `npx tsx` inline or a temp invocation. Only create a script file if the user explicitly asks for one.
