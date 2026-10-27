---
name: flet 0.80+ API changes
description: Correct Flet API usage for version 0.80+
type: feedback
---

In Flet >= 0.80 (this project uses 0.82):
- `ft.app(target=main)` → `ft.run(main)`
- `page.go(route)` is deprecated but still works (calls `asyncio.create_task(push_route(...))` internally) — use it in sync handlers, not `page.push_route` which is async
- `page.session` is the `Session` object; the key-value store is `page.session.store` (has `.get()`, `.set()`, `.clear()`, `.contains_key()`). **`SessionStore.get(key)` takes only one argument — no default parameter.** Use `page.session.store.get("key") or "default"` for a fallback.
- `ft.alignment.center` was removed — use `ft.Alignment(0, 0)` instead

- `ft.DatePickerChangeEvent` does not exist — `DatePicker.on_change` receives a `ControlEventHandler["DatePicker"]`; access the selected date via `e.control.value` (a `datetime` or `date` object, already updated before the event fires). `e.date` does not exist.
- `page.open()` does not exist in 0.82.2 — to open a `DatePicker`, append it to `page.overlay` and set `date_picker.open = True`, then call `page.update()`; cache the picker instance to avoid accumulating overlay entries on repeated opens

- `ft.ExpansionTile` does not accept `initially_expanded` — remove it (tiles are collapsed by default).
- `ft.padding.symmetric()` is deprecated since 0.80 — use `ft.Padding.symmetric()` instead. Same applies to all `ft.padding.*` constructors.
- `ft.FilePicker` does not accept `on_result` in `__init__` — create it first, then assign: `fp = ft.FilePicker(); fp.on_result = handler`.
- `ft.ImageFit` does not exist as a top-level export — pass the string value directly, e.g. `fit="cover"` instead of `fit=ft.ImageFit.COVER`.
- `ft.Image` requires `src` as a positional argument — always pass `src=""` when creating an image that will be populated later.
- `ft.FilePickerResultEvent` does not exist — omit the type annotation on the `FilePicker.on_result` callback (the event object still has `.files`).
- `FilePicker.pick_files()` is async and **returns** the selected files directly — there is no `on_result` callback event in Flet 0.82. The old `on_result` attribute is silently ignored. Correct pattern:
  ```python
  async def _pick_avatar(e):
      files = await _file_picker.pick_files(allowed_extensions=[...], allow_multiple=False)
      if not files:
          return
      file_path = files[0].path
      # handle file_path
  ```
- `FilePicker` is a `Service` subclass (not a widget) — it self-registers with `context.page._services` on creation. Do NOT add it to `page.overlay`; doing so causes Flutter to try to render it visibly, producing the "Unknown control: FilePicker" red banner. Just create it and `await pick_files()`.
- `DatePicker` is a `DialogControl` (a visible widget) — it DOES require `page.overlay.append()` + `open = True` + `page.update()`.

- **Use `ft.CircleAvatar` for avatar images, not `ft.Image`.** It natively falls back to `content` (icon) when no image is set, with no manual `visible` toggling needed.
- **`src` mutations via `page.update()` work only after the view is on screen.** If `src` is mutated and `page.update()` is called before `ft.View` is returned (i.e. still inside the view-builder function), that update is lost. Preferred pattern: build the view with placeholder state, then load data asynchronously via `page.run_task(...)` — mutations made in that async task reach Flutter correctly because by then the view is already on screen.
- **`foreground_image_src=bytes` (raw msgpack binary) does NOT work on Flutter web** — on web, the msgpack-decoded binary arrives as a `Uint8List` view that `MemoryImage` cannot reliably decode on the Flutter web runtime, leaving the circle dark. It works on desktop (native Dart) only.
- **Correct cross-platform avatar approach (including Firefox)**: fetch image bytes server-side in Python (`get_client(token).get(urlparse(avatar_url).path)`), then use `ft.Stack([ft.CircleAvatar(content=icon_fallback), ft.Image(src=r.content, visible=True)])`. Pass raw `bytes` as `src` — msgpack sends binary, Flutter web decodes via `MemoryImage` with no `fetch()` call. Do NOT use `data:` URI strings: Firefox 65+ blocks `fetch()` with `data:` URIs (throws `TypeError: NetworkError`), causing avatars to silently fail on Firefox web. Do NOT use URL strings — `NetworkImage` on Flutter web is unreliable with CORS.
- **Local file preview (after pick)**: pass `data` bytes directly to `_show_avatar` / `ft.Image.src`. No base64 encoding needed.
- `FilePicker.pick_files()` does NOT populate `f.bytes` unless `with_data=True` is passed. Without it, `f.bytes` is `None` even when `f.path` is also `None`, leaving no way to read the file. Always pass `with_data=True` when bytes are needed (e.g. upload flows).

- **Avatar URL port mismatch**: The server constructs `avatar_url` using its `BASE_URL` config. If that config uses a different port than what the Flet client connects to (e.g., server BASE_URL=`:8000`, client API_URL=`:8888`), `httpx.get(avatar_url)` silently fails — every avatar fetch returns empty string. Fix on both sides: (a) keep server `BASE_URL` port in sync with the client's `XIMRATO_API_URL`; (b) on the client, always use `get_client()` + extract the path from `avatar_url` rather than calling `httpx.get(avatar_url)` directly, so the correct base URL is always used regardless of server config.

- **`page.window.icon`** takes an `.ico` file path (Windows only). The path must be **absolute** — a relative path is resolved against the Flutter executable's directory (inside `.venv`), not the project root. Use `str(pathlib.Path(__file__).parents[N] / "assets" / "icon.ico")`. The web favicon equivalent is `assets/favicon.png` — placing it in the project's `assets/` folder overrides Flet's built-in `favicon.png` without any rebuild (Flet's static file server checks `assets_dir` first).

- **`ft.LineChart`, `ft.LineChartData`, `ft.LineChartDataPoint`, `ft.ChartAxis`, `ft.ChartAxisLabel` do NOT exist in Flet 0.82.** For line charts use `flet.canvas.Canvas` with `canvas.Line`, `canvas.Circle`, `canvas.Text` shapes and `ft.Paint`. `cv.Text(x, y, value="label", style=ft.TextStyle(...))` — `x` and `y` are the first two positional args, not `value`. Do NOT rely on `on_resize` for charts that are swapped in dynamically (e.g. on tab change) — `on_resize` does not reliably fire after a content swap. Instead, draw shapes at construction time using fixed `width`/`height` dimensions: `cv.Canvas(shapes=shapes, width=W, height=H)` wrapped in a scrollable `ft.Container`.

- **`ft.TextButton` uses `content` not `text`** — `ft.TextButton(content="label", ...)`. Passing `text=` raises `TypeError`.

- **`ft.Dropdown` uses `on_select`, NOT `on_change`** — in Flet 0.82, the selection event field is `on_select: Optional[ControlEventHandler["Dropdown"]]`. Assigning `dd.on_change = handler` silently sets a phantom attribute; Flet's `_trigger_event` dispatches `"select"` events that look for `on_select`, so `on_change` is never called. Always use `dd.on_select = handler`. `on_select` CAN be passed in `__init__` (it is a proper dataclass field). Other Dropdown events: `on_text_change`, `on_focus`, `on_blur`.

- **Nested control content swap unreliable for controls added to the tree after initial render** — if a control (e.g. a chart area Container) is part of a panel that is NOT in the initial `active_panel.content` (because another tab is default), mutating `.content` on that nested control + `page.update()` does NOT propagate to Flutter. Fix: always swap at the `active_panel.content` level (the same level used for tab switching). For dynamic content (charts, loading states), rebuild the full panel via a `_make_panel(content)` helper and set `active_panel.content = _make_panel(new_content)` from an async task via `page.run_task()`.

- **`ft.Tab` has no `content` kwarg in Flet 0.82, and `ft.Tabs` takes `(content: Control, length: int)` — not a list of tabs.** The correct pattern for labeled tabbed content is a manual implementation: build a `ft.Row` of `ft.TextButton` chips as the tab bar and swap a single `active_panel` container's `.content` between pre-built panel Columns. Do NOT use `ft.Tabs(tabs=[...])` or `ft.Tab(content=...)`. Do NOT toggle `visible=False/True` on multiple panels — on Flet web, controls inside a `visible=False` container never get their event handlers (e.g. `on_change`) registered with Flutter. When the panel becomes visible, the handlers remain dead. Fix: keep only the active panel in the tree by swapping `container.content`.

- **`ft.Wrap` does not exist in Flet 0.82** — use `ft.Column` of `ft.Row`s instead for wrapping form fields across multiple lines.
- **`ft.View` positional arg order is `controls` first, `route` second** — always pass both as keyword args to avoid collision (`ft.View(route="/", controls=[...])`).
- **`page.run_task` vs `await` in `main`**: `page.run_task(coro)` schedules on the next event loop tick — `main` exits first, leaving a blank page visible briefly. Use `await coro()` directly inside `async def main` when you need the page rendered before `main` returns. Use `page.run_task` only for work that should run *after* the initial render.
- **`SharedPreferences` is a `Service` (same as `FilePicker`) — do NOT add to `page.overlay`.** It self-registers to `page._services` via `Service.init()` and is included in the first `page.update()` automatically. Adding it to `overlay` puts the same control ID in two places, which prevents the Flutter invoke listener from registering. Pattern: create prefs → `page.update()` → `await asyncio.sleep(0)` (yield so the send loop flushes the patch to Flutter before the invoke_method message) → `await prefs.get(...)` → render real screen.

**Why:** Hit all four API issues when first running the app; DatePickerChangeEvent discovered when wiring date picker; page.open() crash discovered at runtime; ExpansionTile and padding issues discovered via runtime TypeError during GUI tests; pick_files coroutine and desktop timeout discovered at runtime; FilePicker/Service architecture discovered after "Unknown control" error; async-loading pattern discovered after sync fetch approach left inconsistent behavior; port mismatch discovered as root cause of "avatar never loads" on both desktop and web; Firefox-only failure traced to Firefox blocking `fetch()` with `data:` URIs — fixed by sending raw bytes via msgpack; visible=False panel bug traced via debug prints — body dropdown on_change never fired on web because Flutter never registers event handlers for controls inside hidden containers; Dropdown on_change in __init__ TypeError found via cardio screen crash; nested content swap not propagating traced to body chart never updating on progress screen — fixed by always rebuilding at active_panel.content level.

**How to apply:** Use these patterns in all new Flet screens/views.
