---
name: feedback_atomic_permissions
description: "Permissions must be atomic — each permission is purpose-specific, never reused across unrelated features"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 282d3ba6-9c39-4b16-8788-07e2b3834f24
---

Permissions must be atomic: each permission string should correspond to exactly one capability. Never reuse an existing permission to gate an unrelated feature just because the target role happens to have it.

**Why:** Reusing permissions (e.g. gating `/botinfo topcmds` behind `VIEW_AUDIT_LOG`) couples unrelated features together — revoking or repurposing one breaks the other silently.

**How to apply:** Any time a new restricted feature is added, define a new permission string in `BUILT_IN_ROLES` in `src/db/index.ts`, add it to the appropriate role tier(s), and add a migration `INSERT OR IGNORE` so existing DBs pick it up. Never reuse an existing permission as a proxy for role membership.
