---
name: clean-code-solid-design-patterns
description: "Concrete clean code, SOLID, and design pattern rules to apply to all projects by default"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 53532e8b-f785-4b95-b670-f3695028a191
---

Always apply these principles to all projects without being asked.

**Why:** user requires this as a universal standard.

## Structure

- `src/` layout for Python packages.
- One class or module per concern. Never let a file grow into a god object.
- Split by layer: models, persistence, rendering, UI components, entry point — never mix.
- No file over ~200 lines without a strong reason. If it grows, split it.
- No function over ~20 lines. Extract named helpers instead of commenting blocks.

## SOLID

**S — Single Responsibility:** Each class/module does one thing and has one reason to change.
**O — Open/Closed:** Extend by adding new classes, not modifying existing ones.
**L — Liskov Substitution:** Subtypes must be substitutable without breaking callers.
**I — Interface Segregation:** Many small focused interfaces over one large one.
**D — Dependency Inversion:** High-level modules depend on abstractions. Inject dependencies; never hardcode concrete implementations in business logic.

## Clean Code

- Names are self-documenting. No abbreviations unless universally understood.
- Boolean names are assertions: `is_valid`, `has_permission`, `can_retry`.
- Functions do one thing. No side effects hidden inside a query.
- Avoid flag parameters. Split into two named functions.
- No magic numbers or strings. Name constants.
- Early returns over nested conditionals (guard clauses).
- Comments explain *why*, never *what*.
- Dead code is deleted, not commented out.
- No `print` debugging in committed code.

## Design Patterns

Apply when the structure genuinely calls for them — never force a pattern.

Key patterns: Factory, Builder, Singleton (only true global state), Facade, Adapter, Decorator, Observer/Event, Strategy, Command, State.

## Architectural Principles

- **DRY, YAGNI, KISS, Law of Demeter** — always applicable.
- **Composition over inheritance.**
- **Fail fast** — validate at boundaries, surface errors immediately.
- **Separation of concerns** — UI, business logic, and data access are never in the same layer.
- **DDD, CQRS, Hexagonal** — apply only when scale justifies.
