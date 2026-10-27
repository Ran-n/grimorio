---
name: logging-requirement
description: "Every app must have a structured logging system — not prints, not silent failures, named loggers with levels and consistent format"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7d6bc53b-bfe2-46c8-a329-47e548edc658
---

Logging is a required part of writing good code, not an optional add-on. Every module that does anything meaningful must log it.

**Why:** user explicitly requires logging as a baseline quality standard, on par with SOLID and clean code. Silent apps are undebuggable apps.

**How to apply:** whenever writing or reviewing code, treat missing logging as a defect — add it without being asked. Use the patterns below.

---

## Setup

- Each app gets a `core/logging.py` that configures a named logger tree (`appname.*`) with a consistent format.
- Format: `%(asctime)s [%(levelname)-8s] %(name)s: %(message)s` with `datefmt="%Y-%m-%d %H:%M:%S"`.
- Log level configurable via `LOG_LEVEL` in settings/env, defaulting to `"INFO"`.
- Call `setup_logging()` at the earliest entry point (lifespan startup for servers, `__main__` for GUI/CLI apps).
- Set `propagate = False` on the root app logger to stay isolated from third-party logger noise.

## Per-module loggers

Every module that logs uses `logger = logging.getLogger("appname.module")`. Never use the root logger directly.

## What to log

| Level | When |
|-------|------|
| `DEBUG` | Internal flow, token refresh, route changes — verbose detail useful only when diagnosing |
| `INFO` | All successful business operations: user registered, authenticated, logged out, resource created |
| `WARNING` | Expected failures: invalid credentials, validation rejected, resource not found, conflict |
| `ERROR` | Unexpected server errors, unhandled exceptions, third-party failures |

## What never to log

- Passwords, raw tokens, secrets, or any credential — log `username=` but never `password=`.
- Full request/response bodies that may contain PII.
- Stack traces at INFO or WARNING — reserve tracebacks for ERROR with `logger.exception(...)`.

## Specific patterns

- Network/IO errors caught in service layers → log at WARNING with the error message, then re-raise as a domain error.
- All branch paths in auth flows (attempt, success, failure) must each have a log line.
- Background tasks log start and completion at INFO, errors at ERROR.
- No `print()` anywhere — `print` is not logging and is never acceptable as a substitute.
