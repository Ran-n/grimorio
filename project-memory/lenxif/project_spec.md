---
name: lenxif project spec
description: UX, behaviour, and technical requirements for the lenxif project
type: project
originSessionId: 28e31c9c-1455-48d0-a615-1f805c2e3117
---
# lenxif — Project Spec

**Current version:** 0.1.1  
**Language:** Rust (edition 2024)  
**GUI:** iced 0.13 + iced_fonts 0.1 (Bootstrap icons)  
**EXIF libs:** kamadak-exif 0.5 (read), little_exif 0.6.23 (write)  
**Image decode:** image 0.25  
**File dialog:** rfd 0.15  
**Remotes:** GitHub `git@github.com:Ran-n/lenxif.git`, GitLab `git@gitlab.com:Ran-n/lenxif.git` (multi-push-URL origin → `git push origin main`)

## Source layout

```
src/
  main.rs    — entry point, iced::application bootstrap
  app.rs     — application state, update logic, messages
  view.rs    — UI layout / view functions
  exif.rs    — EXIF read/write, tag filtering, field metadata
  types.rs   — shared types (TagEntry, AppState enums, etc.)
```

## UX requirements

- **File loading:** file picker button + drag-and-drop; both paths identical.
- **EXIF table:** alphabetically sorted, scrollable two-column (name | value); standard editable string tags always present even if absent from file.
- **Inline editing:** click value to edit; unsaved fields marked with a blue dot (●).
- **Save:** `Ctrl+S` or save button writes all dirty fields back to file; save button highlighted when changes pending.
- **Lock / read-only mode:** toggle prevents edits; all value fields switch to plain text when locked.
- **Unsaved-changes guard:** closing file or window with pending edits shows Save / Discard / Cancel dialog; `Escape` cancels dialog or closes file (with guard if needed).
- **Live filter:** case-insensitive search matches tag name and value simultaneously.
- **Thumbnail preview:** 240×240 px shown beside the tag list.
- **Theme:** light/dark toggle available at any time.
- **Supported formats:** JPEG, TIFF, WebP, HEIC, PNG (PNG rarely has EXIF — show empty editable fields).
- **Error display:** file read errors shown in red at bottom of window.
- **Clean shutdown:** all quit paths (window close, Escape with no file open) must be clean — no panics, no data loss without guard.

## Technical requirements

- Editable tags: string fields only (Artist, Copyright, Make, Model, dates, GPS refs, etc.); numeric/binary tags shown read-only.
- Release profile: `opt-level = 3`, `strip = true`, `lto = true`, `codegen-units = 1`.
- No installer; single statically-linked binary; no runtime deps.
- License: PayBack License (PBL) — never MIT/Apache.
- All file headers must follow `metadatos_v0.2.1.py` convention; `.rs` files supported.
