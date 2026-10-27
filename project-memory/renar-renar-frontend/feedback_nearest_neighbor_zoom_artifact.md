---
name: feedback-nearest-neighbor-zoom-artifact
description: "Never use PIL Image.NEAREST to zoom a screenshot crop when judging rendering quality/anti-aliasing — it fakes staircase edges on any image, even a perfectly smooth one"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9c716faa-3805-45eb-9e11-372ee39b6089
  modified: 2026-08-17T10:49:04.562Z
---

When zooming into a screenshot crop to visually judge rendering quality
(anti-aliasing, pixelation, blur artifacts), never resize with
`Image.NEAREST` — it introduces its own blocky/staircase edges on *any*
source image, including a perfectly smooth vector-rendered circle. A crop
zoomed this way will look "pixelated" regardless of whether the actual
app has a rendering bug.

Use `Image.LANCZOS` (or just view the crop at native resolution without
resizing) instead — it preserves the true smoothness/roughness of the
source so a genuine anti-aliasing defect is still visible, but a
false-positive from the zoom method itself isn't introduced.

**Why:** wasted a debugging pass chasing a "pixelated progress ring" bug
in renar-frontend's hero card — the app's actual rendering (verified via
a live desktop screenshot, re-checked with LANCZOS) was perfectly
smooth. The apparent pixelation only existed in my own NEAREST-zoomed
debug crop.

**How to apply:** any time visual-quality verification involves zooming a
screenshot crop for closer inspection (in any project, not just Renar).
