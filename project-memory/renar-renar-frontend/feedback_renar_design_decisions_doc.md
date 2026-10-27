---
name: renar-design-decisions-doc
description: Maintain docs/design-decisions.md in both renar repos — non-obvious architecture/tuning choices with rationale
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b8e87e15-7b5b-4376-8fe4-0c8605191ec8
---

Both renar-frontend and renar-backend have `docs/design-decisions.md`: a single running doc (not per-decision ADR files), grouped by area, each entry structured as a short heading, what the decision is, then a **Why:** paragraph — sometimes with an explicit non-obvious edge case called out.

**Why:** the user asked to "document design decisions and that type of stuff" in addition to the usual README/CHANGELOG updates; chose single-doc format over ADRs, and both repos over backend-only, when asked. See also [[feedback_renar_docs_both_repos]].

**How to apply:** when making a non-obvious architectural or tuning choice in either repo (data model shape, caching strategy, security tuning, why X over Y), add an entry to that repo's `docs/design-decisions.md` in the same session — don't wait to be asked. Link it from the repo's README/docs index like the other docs files.
