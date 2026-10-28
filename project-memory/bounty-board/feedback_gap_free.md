---
name: gap-free-implementation
description: Every implementation must be gap-free before it's reported done — audit every path the change touches, fix what's found, don't leave a "gaps" list for the user
metadata:
  type: feedback
---

When implementing anything, make it gap-free before calling it done: audit every path the change touches and its neighbours — every error/refusal path, every language, every caller, every entry point (sign-in, retry, background refresh), what the user actually sees on screen, upkeep (data that can go stale, a check that catches it) and the tests the [[tests-requirement]] checklist asks for — then fix everything found in the same task. Don't hand back a list of known gaps for the user to ask about.

Applies in particular to user-facing errors: nothing technical, raw (codes, exception type names, HTTP internals, English-only text in another language) ever reaches the screen; see [[no-silent-failure]].

**Why:** 2026-10-27, bounty_board: a TCG+ refusal fix handled the one code reported, and asking "gaps?" turned up eleven more (raw sentences treated as codes, untranslated network errors, "TypeError:" in the UI, sign-in not covered, no staleness check…). The user then said: "as a rule when u implement something always make sure it's gap free".

**How to apply:** Before the final report, run the gap audit yourself (the question "what's still not handled?") and fix what it finds; the report then says what was covered, and names only what truly can't be done (with why).
