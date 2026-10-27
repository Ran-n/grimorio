---
name: cleanup-own-resources
description: Anything Claude spins up (emulators, servers, browsers, background processes, temp files/dirs, port forwards, containers) gets closed or deleted when Claude is done with it
metadata:
  type: feedback
---

When you finish using a resource you started yourself, close it or delete it before handing control back. This covers emulators (`adb emu kill`), dev servers, headless browsers, background shells and processes, `adb reverse`/`adb forward` rules, device settings you changed (e.g. `wm size`), Docker containers, temp files and scratch dirs. Long-lived things you *created* on purpose (a new AVD, a repo, a config the user asked for) stay; only the running instances and throwaway leftovers go.

**Why:** the user asked (2026-10-13), while Claude was booting an Android emulator for timtapper's device tests, that a resource Claude spins up never be left running after use.

**How to apply:** note each thing you start as you start it. Once the task that needed it is over, stop or delete it, then check it's really gone (e.g. `adb devices` empty, the port is free, the process has exited). This applies even when the task failed or was abandoned midway. Never close something you didn't start (e.g. an emulator or server the user already had running). Test fixtures that start resources must tear them down too, in `finally`/fixture teardown ([[tests-requirement]]).
