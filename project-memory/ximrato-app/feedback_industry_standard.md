---
name: Follow industry standard by default
description: Always implement industry-standard behavior unless told otherwise; warn when a request deviates
type: feedback
---

Always implement the industry-standard approach by default without asking.

If the user explicitly requests something that deviates from industry standard: implement what they asked, but first state what the standard is and that their request differs, so they can decide whether to proceed.

**Why:** User explicitly requested this behavior.

**How to apply:** When making design/UX/architecture decisions, default to what established products (Google, GitHub, etc.) do. Flag deviations proactively — don't silently go non-standard, and don't ask permission to go standard.
