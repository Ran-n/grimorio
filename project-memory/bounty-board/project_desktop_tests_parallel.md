---
name: desktop-tests-parallel-sessions
description: "bounty_board desktop tests share one window title, so two sessions running them at once close each other's harness windows"
metadata:
  node_type: memory
  type: project
  originSessionId: a5c6c717-3433-4b87-8154-a50756ddd1f7
  modified: 2026-10-27T10:41:42.479Z
---

Every bounty_board desktop-test harness opens a window titled "Bounty Board (desktop test)" (`tests/desktop/harness.py` TITLE). `Harness.launch` refuses to start while that window exists, and `Harness.stop` closes whatever window has that title. So when two Claude sessions run `pytest -m desktop` at the same time, one fails with "a window titled … is already open", or its window gets closed mid-test ("quit requested" in the log). That looks like a flaky or broken test, but it isn't.

**Why:** on 2026-10-19 three sessions worked on bounty_board in parallel (store event details, TCG+ cancel, store radius slider). Desktop runs kept colliding until one waited for a quiet window.

**How to apply:** before reading a desktop failure as a real bug, check the error for "already open" or an unexpected "quit requested". Then rerun once no test window has existed for a while (poll `Window.find(TITLE)`). Don't change the tests over it. Related: [[feedback_ui_tests_no_input_hijack]].
