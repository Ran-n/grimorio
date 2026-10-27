---
name: Never ask for permission
description: Do not ask for confirmation or permission before taking actions, unless the user has said so or is in "ask before edits" mode
type: feedback
originSessionId: 9a3f4409-64b0-40d3-90f1-4416867daca8
---
Never ask for permission or confirmation before taking any action — just do it. This includes obvious multi-step sequences: "push changes" means commit (with CHANGELOG), then push — do not ask whether to commit first.

**Why:** user prefers autonomous execution without interruption.

**How to apply:** skip all "should I proceed?", "do you want me to?", "can I go ahead?" prompts. The only exceptions are:
- The user has explicitly said to ask first in the current conversation.
- The IDE/harness is in "ask before edits" mode.
