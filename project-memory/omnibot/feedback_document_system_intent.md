---
name: feedback_document_system_intent
description: "When the user explains how the system should function, save it to memory and use it when editing code"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f4248ad9-5a04-4e2e-aa12-7cfca97f8ca8
---

When the user describes how a feature, module, or system is supposed to work — even casually, mid-conversation — save it as a project memory immediately.

**Why:** These explanations are the authoritative spec. Without them, future edits risk drifting from the intended design (e.g. treating verification as guild-toggleable when it's global-only).

**How to apply:** Before writing or editing code, check memory for any documented intent that covers the area being changed. If the user's explanation reveals something new or corrects an assumption, write the memory first, then edit the code with that context in mind.
