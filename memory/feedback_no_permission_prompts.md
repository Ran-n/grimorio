---
name: Never ask for permission
description: Do not ask for confirmation or permission before taking actions, unless the user has said so or is in "ask before edits" mode
type: feedback
---

Never ask for permission or confirmation before taking any action — just do it.

**Exception — commits and pushes:** do not commit or push unless the user explicitly requests it. When they do ask, execute immediately without re-asking. See [[push-semantics]].

**Why:** user prefers autonomous execution without interruption, but commits and pushes are permanent and externally visible — they require explicit intent.

**How to apply:** skip all "should I proceed?", "do you want me to?", "can I go ahead?" prompts. Additional exceptions:
- The user has explicitly said to ask first in the current conversation.
- The IDE/harness is in "ask before edits" mode.
