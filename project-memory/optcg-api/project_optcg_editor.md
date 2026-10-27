---
name: optcg-editor-status
description: "Status of optcg_editor — working Electron desktop app (FastAPI + React/Vite); Electron fixed, installer built"
metadata: 
  node_type: memory
  type: project
  originSessionId: 5e92c045-aa70-4728-9499-97e52207543d
---

# optcg_editor Desktop App — Current Status

**Goal:** CRUD UI for `optcg_api/optcg.db` matching the card detail screenshot (dark theme).

## What Works NOW

### Electron Desktop App (FIXED)

**Root cause of previous Electron crash:** `ELECTRON_RUN_AS_NODE=1` was set in the shell environment. This caused Electron to run in Node-compatibility mode, where `electron_browser_*` C++ bindings are unavailable, causing silent access violations.

**Fixes applied:**
1. `package.json` dev/build scripts use `cross-env ELECTRON_RUN_AS_NODE=` to explicitly clear the env var.
2. `node_modules/electron/index.js` — restored to a smart shim: returns real `{ app, BrowserWindow, ... }` when `process.type` is set (inside Electron browser process), otherwise returns the binary path (for build tools).
3. `electron/main.js` — removed the incorrect `process.type = 'browser'` workaround (no longer needed).
4. Electron upgraded from 27.3.11 → 36.9.5; `better-sqlite3` rebuilt for new version.

**Installer built:** `dist/OPTCG Editor Setup 1.0.0.exe` (89 MB, Electron 36 + React + win32-x64)

### Development workflow

1. **Start FastAPI**: `cd d:\Users\{USER}\sw\optcg_api && uv run uvicorn optcg_api.main:app --port 8000`
2. **Launch Electron dev**: `cd d:\Users\{USER}\sw\optcg_editor && npm run dev`
   - Or run `launch.bat` to do both at once
3. **Build installer**: `npm run build` → `dist/OPTCG Editor Setup 1.0.0.exe`

### Web App (still works)

- `npm run start` → Vite dev server at http://localhost:5173
- `start.bat` → starts FastAPI + Vite + opens browser

## Architecture

- **Backend**: FastAPI at `d:\Users\{USER}\sw\optcg_api` — port 8000
  - Full CRUD for cards with M2M junctions (colors/tribes/attrs/rarities/blocks/formats/keywords/reswords/naips)
  - Lookup endpoints for all reference tables
  - CORS enabled for all origins
- **Frontend**: React + Vite at `d:\Users\{USER}\sw\optcg_editor`
  - `src/api.js` — fetch client talking to localhost:8000
  - `src/App.jsx` — main app with filters/pagination state
  - `src/components/Sidebar.jsx` — card list with search/filter
  - `src/components/CardDetail.jsx` — view/edit switcher
  - `src/components/CardView.jsx` — read-only detail panel
  - `src/components/CardForm.jsx` — CRUD form with multi-select for M2M
- **Electron shell**: `electron/main.js` (main process), `electron/preload.js`
  - Production: loads `out/renderer/index.html`
  - Development: loads http://localhost:5173
  - Packaged with electron-builder as NSIS installer
