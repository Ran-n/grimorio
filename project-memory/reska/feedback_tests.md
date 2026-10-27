---
name: tests-requirement
description: Every app must have tests — new code without tests is incomplete code; add the maximum number of tests, across every applicable test type, for every change
metadata:
  type: feedback
---

Tests are a required part of writing good code. New modules, functions, and endpoints are not done until they have tests.

**Why:** user explicitly requires tests as a baseline quality standard, same level as SOLID and logging. Untested code is unverified code.

**How to apply:** whenever writing new code, add tests in the same pass. When reviewing existing code without tests, flag the gap.

## Maximize coverage per change, across every applicable test type

For every change (a bug fix, a new feature, a refactor), don't stop at one test or one test type — add the maximum number of tests that meaningfully apply, across every test type the project's suite recognizes (unit, integration, property, contract, snapshot, visual, E2E/UI, regression, ...). Confirmed 2026-08-21 (renar-frontend, comments_widget.py's own-comment delete button): a single small UI change got both a fast unit-level suite (widget tree built with a fake Page + `MagicMock(spec=ApiClient)`, covering structural correctness, the click wiring, success *and* failure/error paths — 7 tests) and a real-browser E2E test (Playwright driving the actual click, verified via the backend API) — not either/or.

**Why:** user asked, after seeing that pairing land well, to make "maximum tests of every type per change" a standing rule rather than a one-off — each test type catches a different failure class (unit: wiring/logic bugs cheaply and fast; E2E: the pixels a real user actually clicks are wired to the right place at all), and skipping a type just because another one exists leaves a gap.

**How to apply:** before calling a change done, check which of the project's recognized test types (see its pytest marker list / test directory layout) plausibly apply to it, and write a test in each one that does — not just the cheapest one to write. This supersedes the older "do not attempt to test Flet widget rendering" guidance below: build the real widget tree with a fake `Page` (`SimpleNamespace` with `run_thread` executing inline, `update` as a no-op, plus whatever else the code under test touches) and a `MagicMock(spec=<the real client class>)` — spec'ing against the real class means a renamed/removed method fails the test instead of silently returning a fresh Mock. Navigate the returned control tree by index to assert on the specific controls the change touches.

## Test-type checklist (go through it for every change)

Write a test in every row that applies, and add a marker or folder for any type the project doesn't have yet:

- **Unit**: pure logic, helpers, service functions with mocked I/O.
- **Integration**: real DB, real filesystem (tmp dir), real migrations. Never mocks for the DB.
- **Property-based** (`hypothesis`, marker `property`): anything with an input domain (parsers, formatters, crops/geometry, maths, round-trips like serialize→parse). Assert invariants, not examples.
- **Regression** (marker `regression`): every bug fix starts with a test that fails before the fix and passes after. Its docstring or a comment says what used to go wrong. Confirm it really fails on the old code (e.g. `git stash` the fix, run it, pop). A bug a property test finds gets its own pinned `regression` case too, so it stays covered even if hypothesis stops generating that example.
- **Contract/schema**: API response shapes, Pydantic models, file formats, CLI output. Pin them so a silent shape change fails. Anything that outlives an app version (backups, exports, saved files) gets a **checked-in golden file** (e.g. `tests/backup/golden/v1.json`), built from hand-made fixed objects so it's deterministic. Test that the export equals it (minus timestamps), that the golden file still parses, and that it restores into a fresh install. A round-trip test alone isn't enough: export and import can change together and still agree with each other.
- **Migrations**: `alembic upgrade head` on an empty DB, then `downgrade base`, then upgrade again. Also: re-running the migrations on a DB with history leaves the data untouched and the DB at head, and stepping through **every revision one at a time** (walk `ScriptDirectory`) with data inserted once the tables exist keeps that data at each step.
- **Widget tree** (Flet): fake `Page` + `MagicMock(spec=RealClient)` (see above).
- **Rendered real-app UI** (marker `desktop`): see the section below.
- **Snapshot/visual** (marker `snapshot`): whole-screen captures compared with checked-in baselines.
- **E2E browser** (web frontends): Playwright driving real clicks, results checked through the backend API.
- **Live** (marker `live`): the real external API, kept out of the default run.
- **i18n**: one test that fails when any locale is missing a key or has an extra one ([[i18n-completeness]]).
- **Logging and errors**: assert the right logger and level fire on error paths (`caplog`), and that nothing gets swallowed ([[no-silent-failure]]).
- **Shutdown/lifecycle**: every quit path cleans up (threads, DB connections, temp files). Parametrize over each handler (e.g. Flet's `on_close` and `on_disconnect`) and assert the resource was actually released.
- **Entry points**: `run()`, launchers and `main()` are tested too: monkeypatch the framework call (`ft.run`, `uvicorn.run`) and assert the setup order (logging first) and the arguments passed.
- **Version/metadata**: the version in the app matches `pyproject.toml`.

Branches that are easy to miss (look for them in every handler):
- an edit that changes nothing saves nothing (spy on the repository method, assert it wasn't called);
- a dismissed dialog/picker (value `None`) changes nothing;
- the repository refusing an action (raise its domain error) shows the error and leaves the data and the screen as they were;
- sync and async callbacks both work where the code accepts either;
- the "unknown value" fallback of any lookup/cycle helper.

Slow or invasive types (`live`, `desktop`) stay out of the default run through `addopts = "-m \"not live and not desktop\""`, but must all pass before a version bump ([[version-bump]]).

## Rendered real-app UI tests (marker `desktop`)

Widget-tree tests prove the tree is built right. They can't prove what's actually on screen or that a real click lands. For every UI change, also test the real running app. Reference implementation: timtapper `tests/rendered/` + `scripts/app_driver.py` + `scripts/app_window.py` (commit 19f54de, 2026-10-12):

- **Driver process** (`scripts/app_driver.py serve`): starts the real app on a throwaway demo DB in a scratch dir, so the user's data is never touched. It takes one JSON command per stdin line (`show` route/mode/theme/lang/width, open dialogs, `close`, `quit`) and answers with one `@@{...}` line on stdout. Logs go to stderr, into a file. A failed command answers `{"ok": false, "error": ...}` and the test raises.
- **Window helper** (`scripts/app_window.py`): finds the app window, captures its pixels, and sends **real mouse clicks**. Taps are never driver commands.
- **Session fixture**: one app process for the whole test session, a reply timeout, and a clean quit at teardown.
- **Pixel assertions** (`pixels.py`): find controls in the capture by their **exact theme colour tokens** (blobs with a tolerance, min area, size filters). Then assert on layout: counts, order, alignment, gaps, nothing clipped or pushed off-screen.
- **Parametrize** each assertion over dark/light mode and normal/narrow (minimum) window width.
- **Every screen** gets at least one rendered assertion and one baseline. A screen with widget tests only is a gap.
- **Longest locale at the minimum width**: add a baseline in the language with the longest labels (e.g. Spanish) at the narrowest window. English-only baselines miss labels that wrap or get clipped in other languages.
- **Driver state queries**: give the driver read-only commands (`state`, `round`, `picker_shown`) so a test can check that a real tap changed the app's data, not just the pixels. A test that changes app state restores it in `finally`, since the app is shared by the whole session.
- **Pixel tolerances**: group grid positions within a few pixels (a selected item's thicker border nudges its content) instead of requiring exact equality.
- **Snapshots** (`test_snapshots.py`): whole screens compared with `baselines/*.png` using a per-pixel tolerance and a max changed-pixel count. A failure saves `-actual.png` and `-diff.png`. Approve by rerunning with `<APP>_UPDATE_BASELINES=1`, opening every rewritten baseline, and committing them. Before approving, check that the diff box sits only where the change was meant to land, and look at each image for clipped, wrapped or "…"-cut text and controls pushed off-screen. **Never approve a baseline that shows a bug**: fix the bug first. A baseline only proves nothing changed, not that it was right (timtapper once committed a baseline with "Regiona" clipped).
- When a layout change moves things on purpose (taller rows push content below the fold), update the rendered assertions that count visible items, with a comment saying why.
- Reuse the same driver for the README screenshot script (DRY).
- Web frontends use Playwright for the same job.

**Why:** the user asked (2026-10-12) to make real-app UI tests a standing part of "fully tested". Widget-tree tests passed while what actually rendered (pills, die faces, portraits) could still be wrong.

**How to apply:** when a project has a UI, set this harness up if it's missing. Every UI change then gets a rendered assertion and, when the look changes on purpose, refreshed and reviewed baselines.

## Coverage gate

- `[tool.coverage.run] branch = true`, plus `fail_under` in `[tool.coverage.report]`, set to the current whole-number total (raise it as coverage grows, never lower it).
- Enforce it with `uv run pytest --cov` on full runs, and document that command in the README. Don't put `--cov` in `addopts`: then running a single test file would fail the gate.
- Read the `term-missing` report after every change. Cover each uncovered line or branch, or delete it if nothing calls it (grep first). Dead code isn't something to write tests for. Only the `if __name__ == "__main__":` guard and dev-only CLI fallbacks may stay uncovered.
- Now and then, run mutation testing (`mutmut`) on the core logic to find tests that execute code without really checking it. On Windows it may need WSL.

## Auditing a project against these rules

When asked whether a project follows these guidelines (or to "fix the gaps"):
1. Run the default suite with `--cov --cov-report=term-missing`, then the deselected markers (`live`, `desktop`).
2. Go through the checklist above type by type, citing the test file that covers each type or saying it's missing.
3. List the uncovered lines and branches, rendered screens without baselines, and persisted formats without a golden file.
4. When fixing the gaps, run the new tests on the real app too. Gap-filling tests (property tests, rendered tests in other languages) find real bugs, so fix those in the same pass, each with a `regression` test.

**Why:** the 2026-10-12 timtapper audit found every one of these gaps (no gate, a screen without rendered tests, migrations tested only empty, an unpinned backup format, untested entry points and quit paths, dead code). Filling them found 5 real bugs: 2 in name parsing (found by property tests), plus a wrapped label, a clipped dropdown and cut-off leader names (found by rendered tests in Spanish at the minimum width).

---

## Framework

- Python: use `pytest`. Never `unittest` directly.
- Async tests: `pytest-asyncio` with `asyncio_mode = "auto"` in `pyproject.toml`.
- Tests live in a top-level `tests/` directory, mirroring the `src/` structure.
- One test file per source module: `src/app/routers/auth.py` → `tests/routers/test_auth.py`.

## What to test

- **Happy path** — the normal successful flow for every public function/endpoint.
- **Failure cases** — every known error path: bad input, conflict, unauthorized, not found.
- **Boundary conditions** — empty strings, nulls, edge values where relevant.

Do not write tests for private helpers unless the public API cannot exercise them.

## Backend (FastAPI)

- Use `httpx.AsyncClient` with `transport=ASGITransport(app=app)` — no real server needed.
- Use a real test database (not mocks). Spin up with a fixture that applies migrations and tears down after. [[regression-safety]]
- One fixture creates a fresh DB session per test; another creates a test client.
- Test every route: success status code, response shape, and at least one error path.

## Frontend (Flet / GUI)

- Unit-test service functions by mocking `httpx` responses (e.g., `respx` or `unittest.mock`).
- Test `AuthError` is raised correctly for each error status code.
- Test `_extract_detail` parses Pydantic 422 bodies correctly.
- Widget trees ARE testable, not just the logic behind them — see "Maximize
  coverage per change" above for the fake-`Page` + `MagicMock(spec=...)`
  pattern. Prefer testing pure/extracted helpers directly when they exist,
  but don't skip the widget-tree test just because the logic also happens
  to live in a closure with no standalone entry point.

## Coverage expectations

- All new code: aim for full branch coverage on business logic.
- Legacy code without tests: add tests before modifying, not after.
- Never merge a feature that has zero tests.

## pyproject.toml additions

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]

[dependency-groups]
dev = ["pytest", "pytest-asyncio", "pytest-cov", "respx", "hypothesis"]  # add httpx if not already a dep; pillow for rendered UI tests
```
