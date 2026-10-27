---
name: project_renar_logo_mark
description: "Renar logo mark decided: spiral-in-ring, thin open end to thick vessel dot; supersedes other explored directions"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1c935f04-c125-41eb-a8a0-889a7f9ca751
---

# Renar logo mark — decided direction

**Decided:** 2026-07-18. Working artifact: https://claude.ai/code/artifact/1c902275-8060-4bd7-b6a6-8a86c681b7a3 (redeploy that same URL for further iteration — don't mint a new one).

## The mark

A single unbroken line, drawn as one tapering stroke, sitting inside a soft double ring (like a coin/seal die):
- Positioned to start in the gap between the two concentric rings, tapering to a fine point there (the open, unfinished "journey" end — [[project_renar_branding]] `ren`).
- Spirals inward (~1.5 turns, slightly off-vertical start for a struck, non-mechanical feel) and thickens toward the centre.
- Ends in a solid dot at the centre, sized to exactly match the line's tapered width at that point — no seam — so it reads as the line pooling into the dot rather than a separate shape stuck on (the "vessel" end — `-ar`).

## Palette

Not terracotta/cream (flagged as an AI-design cliché) — instead granite/patina, matching the Bronze Age Atlantic-Galicia petroglyph reference:
- Ink/slate `#26282A` (light) / `#E9E5DA` (dark) — the spiral line itself.
- Patina `#3F6C5F` (light) / `#6FA391` (dark) — the ring, soft/faint opacity, tied proportionally to the mark's radius (not a fixed px floor) so it doesn't go relatively bulkier at small sizes.
- Bronze `#A67A4F` (light) / `#C99B6C` (dark) — the vessel dot only, rare accent.
- Stone ground `#EDEBE4` (light) / `#17191A` (dark).

## Rejected/parked alternatives

- **R-monogram bend** (squeezed coil + kicked-out tail like a letterform leg): tried, reverted — user wants a true circular spiral inside a circle, not a bent letterform.
- **Amphora/vessel silhouette (Option B)**: kept as a documented "considered, not recommended" comparison on the same page. Needed two rounds of fixing — first pass read as a teardrop blob, second pass (with handles added) read anatomically inappropriate (wide double belly bulge + centre groove + pointed base). Final version: belly width kept close to shoulder width (subtle bulge, not twin lobes), small flat foot instead of a point, no centre groove. User called the fixed version "cute" — it's a fine reference piece but the spiral is the chosen direction.

## Working notes for further iteration

- Ring weight must be computed from `rOuter`, not from the tip stroke width (`wTip`) — an earlier version floored on `wTip` and the ring went disproportionately thick at small (16–32px) sizes.
- Don't let the two ring radii collapse into a merged single ring as a small-size fallback — user explicitly rejected that; keep both rings distinct at every size, just thinner.
- The dot at the vessel end must exactly equal the polygon's tapered width at that point (multiplier 1.0) — overshooting it (tried 1.55, 1.22, 1.16) reads as a mismatched blob stuck onto the line.

## Applied to renar-frontend (2026-07-18)

Replaced the old logo in `renar-frontend/src/renar_frontend/assets/`: `icon.png`, `icon_small.png`, `favicon.png`, `icon-192.png`, `icon-512.png`, `icon-maskable-192.png`, `icon-maskable-512.png`, `apple-touch-icon.png`, `icon.ico`. This project has no Flet-standard icon/splash pyproject config — icons are hand-copied at runtime by `branding/brand_flet_web.py` and embedded as base64 by `branding/__init__.py`; see that module if any of these paths ever move.

- `icon.png`/`icon_small.png` — transparent background (composited directly into the in-app AppBar/welcome-screen UI via `branding.logo()`), dark-bg mark palette (cream/patina/bronze) since the app chrome is dark.
- All other files (favicon, icon-192/512, maskable 192/512, apple-touch, .ico) — same dark-bg mark palette but on an opaque `#17191A` ink background tile, since OS/browser icon surfaces need an opaque tile (mandatory for maskable). Maskable variants render the mark at 75% scale to stay inside the safe zone.
- Generator script + a neutral light-theme master SVG (ink-on-transparent, same geometry) saved to `renar/common/branding/`: `gen_logo.py` (re-run to regenerate any size/palette from the exact approved geometry) and `renar-mark.svg`.
- `badge_premium.svg`, `badge_verified.svg`, and the `flags/` icons were left untouched — not part of the app logo.
