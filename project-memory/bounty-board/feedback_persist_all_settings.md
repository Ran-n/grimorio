---
name: feedback-persist-all-settings
description: "every user-changeable setting, filter, choice and UI state must be remembered between runs"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 770aca1d-41a3-40d9-8890-821f3ef8b880
  modified: 2026-10-07T06:31:17.302Z
---

Every config value, filter, toggle, picked option (language, theme, tab, sort, chips, window placement…) the user can change must be persisted and restored on the next run. Defaults (e.g. "follow system locale") only apply until the user picks something.

**Why:** the user said this explicitly and had to repeat it ("i told you before") when adding language support to bounty_board.

**How to apply:** whenever adding a new option or filter, add its field to the persisted settings (bounty_board: `domain/preferences.py` `Settings`/`ViewState`, saved via `settings.json`) and restore it at start-up, in the same change. Treat an unpersisted option as a defect. Related: [[feedback-universal-behaviours]].
