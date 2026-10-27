---
name: feedback-arbore-design
description: "Design decisions and rejected approaches for the arbore family tree viewer (index.html) — layout, palette, and UX preferences"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ce587a27-9ffc-4ab0-af18-96805e37200d
  modified: 2026-08-24T11:49:20.368Z
---

Working on [[project_arbore]], several rounds of visual feedback landed on these settled choices — don't re-propose the rejected alternatives without a new reason:

- **Layout: top-down, not left-to-right.** First version used generation *columns* (root on the left, ancestors expanding rightward). User explicitly preferred a top-down layout (root at top, each generation a row below, vertical elbow connectors) — implemented via a computed pedigree layout (leaves get sequential positions, internal nodes sit at the average of their children), not CSS border-trick nested lists (those don't align cleanly once branches have uneven depth).
- **Palette: not gruvbox.** Style was copied from the user's other project breren.com (Gruvbox palette, light/dark via `prefers-color-scheme` + `data-theme` override, sans-serif system font stack) but the user disliked gruvbox's actual colors in both light and dark mode. Replaced with a custom ink/gold palette (warm off-white/charcoal light, deep slate dark, muted gold accent, muted navy/rose for male/female indicators) while keeping the same light/dark mechanism.
- **Language picker: copy breren.com's exact widget**, not a simplified segmented button pair. Trigger button (flag + name + chevron) opening a dropdown listbox with flag+name options, click-outside/Escape to close — mirrors `breren/public/common.js`'s `setupLangPicker`. Only English + Galician (Galego first/default, matching breren's convention), not the full breren language list.
- **Navigation: click-and-drag pan, not scrollbars.** Tree sits in a fixed-height viewport (`overflow:hidden`) with a `translate()`-transformed pan layer driven by Pointer Events (mouse+touch+pen unified), plus a recenter button — not native `overflow:auto` scrollbars.
- **Card design matters — first pass (flat list-item cards with a colored left border bar) read as generic/cheap.** What fixed it: circular colored initial-letter avatars (blue-ish male, rose female, gold for root), a bordered/shadowed frame panel around the whole tree so it doesn't float in empty page space, and alternating subtle background bands per generation row for visual rhythm. When asked to improve visuals again, actually render a headless-Chrome screenshot and inspect it before changing CSS blind — guessing at fixes without looking wasted a round.
- Missing parents render as dashed-border "unknown" placeholder cards (own leaf slot in the layout) rather than being omitted, to keep the generation alignment intact.
