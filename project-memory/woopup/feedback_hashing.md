---
name: hashing-default-blake3
description: Always use BLAKE3 for any hashing need unless the user specifies otherwise
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 53532e8b-f785-4b95-b670-f3695028a191
---

Always use BLAKE3 as the default hash algorithm. "Hash" means BLAKE3 unless the user specifies a different algorithm. Use the platform-appropriate tool.

**Why:** user explicitly set this as a universal default.

**How to apply:** whenever hashing is needed (checksums, IDs, integrity), reach for BLAKE3 first. Only switch to another algorithm if the user names it or the context requires a specific standard (e.g., SHA-256 for JWT).
