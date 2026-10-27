---
name: Database must be fully normalized
description: Always design and maintain the database in fully normalized form (3NF); no inline enums or denormalized columns
type: feedback
---

Always keep the database fully normalized (3NF or better).

**Why:** User explicitly required normalization after seeing auth events stored with an inline string enum column — "that's bad design."

**How to apply:**
- Never use SQLAlchemy `Enum(...)` columns or plain string/integer columns for controlled vocabularies. Use a dedicated lookup table with a FK instead.
- Every lookup table gets seeded at startup (idempotent).
- Models expose the string name via a `@property` backed by an eager-loaded relationship, so the API contract stays clean.
- When adding any new field that has a fixed set of values, create a lookup table from the start — do not add inline enums with the intent to normalize later.
- **`metric_type: str` is the canonical example of this violation** — body metrics used `metric_type: Mapped[str]` initially; correct design is a `metric_types` lookup table + FK `metric_type_id`.
