---
name: Project spec file — track and respect per project
description: Maintain a project_spec.md per project; treat as source of truth; flag contradictions; update only on explicit user request
type: feedback
originSessionId: b1919612-18b3-42e2-826b-d27f7852ca1c
---
For every project, maintain a `project_spec.md` in its memory folder covering UX, behaviour, and technical requirements.

- Read it at the start of every session on that project.
- After every change, verify the result still matches the spec; flag anything that might have broken.
- If a new request contradicts the spec, point it out and ask which intent to keep before implementing.
- Update the spec only when the user explicitly confirms a change in intent.
