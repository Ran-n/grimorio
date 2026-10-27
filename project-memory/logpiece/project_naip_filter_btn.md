---
name: project-naip-filter-btn
description: "naip toggle button exists in the filter panel; toggles \"naip view\" card filter"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3048207b-544f-47d2-89db-a1850bf78125
---

`FilterPanel._naips_btn` is a checkable `filterFlagBtn` QPushButton in the color-section flags grid at position (1, 1). It emits `naips_toggled(bool)` when toggled and uses the `naips` SVG icon. `set_naips_checked()` sets its state without re-emitting the signal.
