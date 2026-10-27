---
name: feedback-full-sweep
description: "Trigger phrase \"full sweep\" — instructs Claude to run a full autonomous audit-and-fix loop until nothing remains"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c5f65824-36c7-4f90-85c3-e30fe2acf847
---

When the user says **"full sweep"**, enter a fully autonomous, repeating audit-and-fix loop. Do NOT return control until the loop finds nothing left to address.

**What to cover each pass:**

_Correctness_
- Logic bugs, edge cases, unhandled errors, broken flows
- Empty or swallowed catch blocks; unhandled promise rejections
- No-silent-failure: `.catch(() => null)` is only acceptable for existence-check fetches; every catch on a Discord API action, DB write, or side-effect call must log or rethrow (see [[no-silent-failure]])
- Errors that should propagate but don't
- Race conditions and concurrency issues (async events, shared state)
- Resource leaks: event listeners, intervals, file handles, DB connections not cleaned up

_Type safety_
- TypeScript/Python/Rust type errors, missing types, unsafe casts
- Nullable values used without null guards at system boundaries

_Security_
- Hardcoded secrets or credentials anywhere in the codebase or committed files
- Sensitive data appearing in logs (including at startup/debug)
- Injection risks (SQL, shell, XSS, template), unvalidated input at ALL boundaries (user input, API responses, webhook payloads)
- Overly broad error messages that leak implementation details
- Non-constant-time comparisons for secrets (timing attack vectors)
- Rate limiting gaps, CSRF gaps, overly permissive CORS
- OWASP Top 10 in full

_Performance_
- N+1 queries, missing DB indexes, sequential awaits that could be parallel
- Unbounded list fetches with no pagination
- Expensive operations on hot paths

_Database_
- Missing migrations, schema/code drift, constraint gaps
- Missing foreign key constraints, NOT NULL where nullable is wrong
- Missing unique constraints, data validated only at app level when DB should enforce it
- Destructive migrations with no rollback path

_Dependencies_
- Outdated packages; known CVEs (`npm audit`, `cargo audit`, `pip audit`, etc.)
- Unused dependencies
- Duplicate functionality from multiple packages
- Packages with better-maintained alternatives

_Configuration & environment_
- Env vars referenced in code but missing from `.env.example` or config schema, and vice versa
- Magic numbers/strings that should be named constants
- Platform-specific hardcoding (path separators, line endings, encoding assumptions)

_Architecture & structure_
- Module/feature rules and naming conventions (consult project memory)
- Circular dependencies
- Files in wrong directories
- Command/feature parity: registered but not implemented, or implemented but not registered
- Inconsistent response shapes or API contracts
- Breaking API or config changes that silently break existing clients/deployments without a deprecation path

_Code quality_
- Dead code, unreachable paths, commented-out code
- DRY violations and duplicated logic
- Functions that are too long or have excessive cyclomatic complexity
- TODO/FIXME/HACK comments that should be resolved or tracked
- Misleading or ambiguous function/variable names
- Boolean parameters that should be option objects
- Unexplained abbreviations

_Tests_
- Missing coverage for new or changed code
- Weak or trivial assertions
- Untested edge cases and error paths
- Flaky or order-dependent tests
- Test data containing real-looking PII or credentials
- Unit tests that should have integration test counterparts

_Logging & observability_
- Important operations with no audit trail
- Missing error tracking or metrics on critical paths
- Health check / readiness endpoints absent where expected

_Documentation_
- Docs out of sync with implementation (README, API docs, inline comments that are wrong)
- CHANGELOG gaps
- Misleading or stale inline comments
- Apply file header / metadatos rules per global memory where relevant

_Internationalization_
- Hardcoded locale-specific formatting (dates, numbers, currencies)
- i18n key completeness across all locale files (per global memory)

_Frontend / UI (when applicable)_
- Missing ARIA labels, poor color contrast, broken keyboard navigation
- Disabled UI elements not visually distinct (per global memory)
- Missing fallback, loading, or empty states

_Resilience_
- No timeout set on external HTTP/DB calls
- No retry logic where transient failures are expected
- Infinite loops possible in recursive or polling code
- Graceful shutdown not handled (SIGTERM/SIGINT)

_Data privacy_
- PII collected but not actually needed
- PII stored or logged anywhere it shouldn't be
- Missing data retention or anonymization where required
- GDPR / privacy compliance gaps

_Error UX_
- User-facing errors that are too generic ("something went wrong") or too technical (stack traces leaked)
- Missing fallback, loading, or empty states in UI

_Memory management_
- Unbounded in-memory caches with no eviction policy
- Large objects held in memory longer than needed

_Git & build hygiene_
- `.gitignore` gaps — secrets, build artifacts, or large binaries accidentally tracked
- Build artifacts committed that should be generated
- Lint/format not enforced in CI (only locally)

_Runtime & version pinning_
- Runtime version (Node, Python, etc.) not documented or enforced
- Lockfiles absent or not committed

**Loop behavior:**
1. Audit the full project across all categories above
2. Fix everything found
3. Re-audit from scratch
4. Repeat until a full pass finds zero issues
5. Only then report done and return control

**Why:** User wants a single phrase to kick off deep, unattended remediation without having to re-prompt each round.

**How to apply:** On "full sweep", begin immediately without asking for scope clarification. Work autonomously. Apply all project-specific rules from memory alongside these general categories. Only stop when a complete pass yields nothing new.