---
name: no-silent-failure
description: Never silently fail — always surface errors explicitly, don't swallow or hide them
metadata:
  type: feedback
---

Never silently fail. Always surface errors explicitly — throw, log, or report them. Do not swallow exceptions, ignore rejected promises, or let error paths do nothing.

**Why:** Silent failures make bugs invisible and extremely hard to diagnose. An error that disappears is worse than one that crashes.

**How to apply:** In any code written or reviewed — catch blocks must log or rethrow, unhandled promise rejections must be surfaced, Discord interaction errors must reply with an error message, and DB failures must propagate or be logged loudly. Never use empty catch `{}` or `.catch(() => {})` without at least logging.