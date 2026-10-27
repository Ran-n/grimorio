---
name: Clean Code, SOLID, and Software Design Principles
description: Concrete clean code, SOLID, and design pattern rules to apply to all projects by default
type: feedback
originSessionId: a9faf96a-074c-4209-a524-30e5f7027481
---
Always apply these principles to all projects without being asked.

**Why:** user requires this as a universal standard. Vague reminders like "apply SOLID" are useless — these rules are specific enough to enforce.

---

## Structure

- `src/` layout for Python packages.
- One class or module per concern. Never let a file grow into a god object.
- Split by layer: models, persistence, rendering, UI components, entry point — never mix.
- No file over ~200 lines without a strong reason. If it grows, split it.
- No function over ~20 lines. Extract named helpers instead of commenting blocks.

---

## SOLID

**S — Single Responsibility**
Each class/module does one thing and has one reason to change. If you can describe it with "and", split it.

**O — Open/Closed**
Extend behavior by adding new classes or functions, not by modifying existing ones. Use composition, protocols, or strategy patterns instead of growing a class with conditionals.

**L — Liskov Substitution**
Subtypes must be substitutable for their base types without breaking callers. Never override a method in a way that weakens its contract (e.g., raising exceptions the base doesn't, ignoring required parameters).

**I — Interface Segregation**
Don't force a class to implement methods it doesn't need. Prefer many small, focused interfaces/protocols over one large one. If a caller only uses 2 of 8 methods, the interface is too fat.

**D — Dependency Inversion**
High-level modules must not depend on low-level modules — both depend on abstractions. Inject dependencies; don't instantiate them inside. Prefer constructor injection. Never hardcode concrete implementations in business logic.

---

## Clean Code

- Names are self-documenting: `user_invoice_total` not `t`, `x`, `tmp`, or `data`.
- No abbreviations unless universally understood (`url`, `id`, `db` are fine; `usr`, `mgr`, `proc` are not).
- Boolean names are assertions: `is_valid`, `has_permission`, `can_retry`.
- Functions do one thing: no side effects hidden inside a query, no queries hidden inside a command.
- Avoid flag parameters (`process(mode=True)`). Split into two named functions.
- No magic numbers or strings. Name constants.
- Early returns over nested conditionals (guard clauses).
- Comments explain *why*, never *what*. If you need to comment what the code does, rewrite it.
- Dead code is deleted, not commented out.
- No `print` debugging left in committed code.

---

## Design Patterns

Apply patterns when the structure genuinely calls for them — never force a pattern onto a problem that doesn't need it.

**Creational**
- **Factory Method / Abstract Factory:** when the exact type to instantiate varies or must be deferred.
- **Builder:** when constructing a complex object requires many optional steps.
- **Singleton:** only for true global state (config, logger). Never use to avoid passing dependencies.
- **Prototype:** when cloning is cheaper than constructing from scratch.

**Structural**
- **Facade:** expose a simple interface over a complex subsystem.
- **Adapter:** wrap an incompatible interface so it fits an expected one.
- **Decorator:** add behavior by wrapping, not subclassing. Prefer for cross-cutting concerns.
- **Composite:** when individual objects and collections must be treated uniformly.
- **Proxy:** control access to an object (lazy init, access control, remote calls).
- **Bridge:** separate abstraction from implementation so both can vary independently.
- **Flyweight:** share common state across many fine-grained objects. Only when profiling confirms the need.

**Behavioral**
- **Observer / Event:** when one change must notify many dependents without tight coupling.
- **Strategy:** swap algorithms at runtime without conditionals.
- **Command:** encapsulate an action as an object. Enables undo/redo, queuing, logging.
- **Template Method:** define a skeleton algorithm; let subclasses fill in steps.
- **Chain of Responsibility:** pass a request along a chain until one handler processes it.
- **State:** replace conditionals with state objects when behavior depends on internal state.
- **Iterator:** standard traversal without exposing internals.
- **Mediator:** centralize communication between objects that would otherwise reference each other.
- **Memento:** capture and restore state without exposing internals.
- **Visitor:** add operations to a class hierarchy without modifying it.
- **Interpreter:** only for actual grammar/DSL parsing.

---

## Architectural Principles

**Always applicable:**
- **DRY** — every piece of knowledge has a single authoritative representation.
- **YAGNI** — don't build what isn't needed yet.
- **KISS** — the simplest solution that works is correct.
- **Law of Demeter** — a unit should only talk to its immediate collaborators.
- **Composition over inheritance** — prefer assembling behavior from parts.
- **Fail fast** — validate at boundaries, surface errors immediately.
- **Separation of concerns** — UI, business logic, and data access are never in the same layer.

**When domain is complex:** DDD (entities, value objects, aggregates, repositories, domain services, bounded contexts).

**When read/write paths diverge significantly:** CQRS.

**When multiple delivery mechanisms or deep testability are needed:** Hexagonal / Ports & Adapters.

**If the user suggests a wrong pattern:** apply what they asked, name the standard pattern that would fit, explain the tradeoff in one sentence.

---

## How to apply

- Proactively structure new code this way without waiting to be asked.
- When adding a feature, refactor toward these principles rather than growing existing files.
- When a file is getting long, split it as part of the same task.
- Call out violations found in existing code before touching them.
