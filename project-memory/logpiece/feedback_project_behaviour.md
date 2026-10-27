---
name: project-spec-file-track-and-respect-per-project
description: Maintain a project_spec.md per project; treat as source of truth; flag contradictions; update only on explicit user request
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8d6ce87f-ebe4-4c7f-9a7c-dc4de50180fd
---

For every project, maintain a `project_spec.md` in its memory folder covering UX, behaviour, and technical requirements.

- Read it at the start of every session on that project.
- After every change, verify the result still matches the spec; flag anything that might have broken.
- If a new request contradicts the spec, point it out and ask which intent to keep before implementing.
- Update the spec only when the user explicitly confirms a change in intent.
