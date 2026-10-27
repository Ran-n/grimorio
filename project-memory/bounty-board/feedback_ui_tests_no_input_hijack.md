---
name: feedback-ui-tests-no-input-hijack
description: "UI/desktop tests must never take over the user's real mouse or keyboard; post messages to the app window instead"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 144b2045-9c93-4068-b622-1c2edc3c1e10
  modified: 2026-10-10T11:28:09.498Z
---

Desktop/UI tests must not move the real cursor or send global key presses (no SetCursorPos, mouse_event, keybd_event, SendInput, SetForegroundWindow tricks). The user works while tests run and found it annoying.

**Why:** the user said tests hijacking their mouse "is annoying" (2026-10-10, bounty_board desktop tests).

**How to apply:** drive the app by posting window messages (WM_MOUSEMOVE/WM_LBUTTONDOWN/UP, WM_MOUSEWHEEL, WM_CHAR, WM_KEYDOWN) straight to the app's child window (Flutter: class `FLUTTERVIEW`), and take screenshots with PrintWindow so it works while the window is covered. Verified working with Flet 0.85 on Windows.
