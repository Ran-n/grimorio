---
name: regression-safety-no-unintended-side-effects
description: Changes must not silently break unrelated parts of the program; flag ripple risks before implementing
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2357ec0d-7eb6-4caf-86db-e0049e064f79
---

When making a change, ensure it does not silently break unrelated parts of the program. Intentional behaviour changes requested by the user are always correct — this rule is only about unintended ripple effects.

**Why:** Changes in shared abstractions, utilities, or interfaces can silently break unrelated call sites.

**How to apply:**
- Before editing any shared module, grep all files that import or reference it.
- If touching a shared interface, signal, or schema: verify all call sites are still correct after the change.
- If an unintended side effect risk exists, name it before proceeding.
- Never remove, rename, or change a function/class signature without updating every caller.
