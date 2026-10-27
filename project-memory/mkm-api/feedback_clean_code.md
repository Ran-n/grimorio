---
name: clean-code-solid-design-patterns
description: Concrete clean code, SOLID, and design pattern rules to apply to all projects by default
metadata:
  type: feedback
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

Apply patterns when the structure genuinely calls for them — never force a pattern onto a problem that doesn't need it. Scripts and small tools should use only what reduces complexity, not what demonstrates knowledge.

**Creational — how objects are created**
- **Factory Method / Abstract Factory:** when the exact type to instantiate varies or must be deferred. Never `if type == "x": return X()` scattered across callers.
- **Builder:** when constructing a complex object requires many optional steps. Prefer over telescoping constructors.
- **Singleton:** only for true global state (config, logger). Never use to avoid passing dependencies — that's just hidden coupling.
- **Prototype:** when cloning is cheaper than constructing from scratch.

**Structural — how objects are composed**
- **Facade:** expose a simple interface over a complex subsystem. Callers should not need to orchestrate internals.
- **Adapter:** wrap an incompatible interface so it fits an expected one. Use when integrating third-party code without modifying it.
- **Decorator:** add behavior by wrapping, not subclassing. Prefer for cross-cutting concerns (logging, caching, validation).
- **Composite:** when individual objects and collections of them must be treated uniformly (trees, UI hierarchies).
- **Proxy:** control access to an object (lazy init, access control, remote calls).
- **Bridge:** separate abstraction from implementation so both can vary independently.
- **Flyweight:** share common state across many fine-grained objects to reduce memory. Only when profiling confirms the need.

**Behavioral — how objects communicate**
- **Observer / Event:** when one change must notify many dependents without tight coupling. Default for UI signals, domain events.
- **Strategy:** swap algorithms at runtime without conditionals. When you see `if mode == "x"` branching into different logic, extract strategies.
- **Command:** encapsulate an action as an object. Enables undo/redo, queuing, logging of operations.
- **Template Method:** define a skeleton algorithm in a base class; let subclasses fill in steps. Use when steps vary but order doesn't.
- **Chain of Responsibility:** pass a request along a chain until one handler processes it. Middleware, validation pipelines.
- **State:** when an object's behavior changes based on internal state, replace conditionals with state objects.
- **Iterator:** provide a standard way to traverse a collection without exposing its internals.
- **Mediator:** centralize communication between objects that would otherwise reference each other directly. Good for complex UI or component systems.
- **Memento:** capture and restore state without exposing internals. Use for undo/snapshot features.
- **Visitor:** add operations to a class hierarchy without modifying it. Use when you have a stable structure but frequent new operations.
- **Interpreter:** only for actual grammar/DSL parsing. Don't apply elsewhere.

---

## Architectural Principles

Apply only when project scale and structure justify the overhead. Never impose architecture for its own sake.

**Always applicable (any scale):**
- **DRY** — every piece of knowledge has a single authoritative representation. Duplication is not just copy-paste; it's any two things that must change together.
- **YAGNI** — don't build what isn't needed yet. Design for now; extend later. YAGNI applies to features and abstractions, not to standard language-level organisation: grouping related modules that already exist into a package/namespace is not premature — it is the correct tool when the grouping reflects a real, present concern.
- **KISS** — the simplest solution that works is correct. Complexity must be justified.
- **Law of Demeter** — a unit should only talk to its immediate collaborators. No `a.b.c.method()` chains.
- **Composition over inheritance** — prefer assembling behavior from parts over deep inheritance hierarchies. Inherit only for true is-a relationships.
- **Fail fast** — validate at boundaries, surface errors immediately, never swallow exceptions silently.
- **Separation of concerns** — UI, business logic, and data access are never in the same layer.

**Apply for any app with a UI layer (GUI, web, TUI):**
- **MVC (Model-View-Controller):** separate data (Model), presentation (View), and user-input handling (Controller). The Model has no knowledge of the View; the View has no knowledge of the Model — both talk only through the Controller (or via signals/events). Never put query logic inside a widget; never put layout code inside a data function. If a widget method does more than update the UI from data it was handed, extract a controller method.
- **MVP (Model-View-Presenter):** variant of MVC where the Presenter holds all UI logic and the View is passive — it only renders what the Presenter tells it and forwards raw events back. The View has no conditionals. Prefer over MVC when the View must be fully testable without rendering (e.g., unit-testing UI logic without a display).
- **MVVM (Model-View-ViewModel):** the ViewModel exposes observable state; the View binds to it and never calls business logic directly. No direct View↔Model coupling. Prefer when the framework supports data-binding natively (Qt properties/signals, WPF, SwiftUI, Vue). The ViewModel is unit-testable with no UI instantiation.

**Apply for any app that touches a data store:**
- **Repository:** abstracts the data source behind a collection-like interface (`find`, `save`, `delete`). Business logic has no knowledge of SQL, files, or APIs — it just talks to the repository. One repository per aggregate root.
- **Unit of Work:** tracks all changes made during a business transaction and commits or rolls them back atomically. Pairs with Repository. Prevents partial writes. Most ORMs implement this internally — expose it explicitly when you need explicit transaction boundaries.
- **Active Record vs Data Mapper:** two ORM philosophies. Active Record: the object knows how to save/load itself (`user.save()`). Simple but couples domain to persistence. Data Mapper: a separate mapper moves data between objects and the DB; the domain object knows nothing about storage. Prefer Data Mapper for complex domains; Active Record is fine for simple CRUD.

**Apply for event-driven or distributed systems:**
- **Pub/Sub (Publish-Subscribe):** publishers emit events to a broker; subscribers register interest by topic. Neither knows the other exists. Prefer over Observer when producers and consumers must be decoupled at deployment time (different processes, services, or systems). Use Observer for in-process UI signals; Pub/Sub for cross-service communication.
- **Event Sourcing:** store state as an immutable log of domain events rather than current values. Replay events to reconstruct state. Enables full audit history, temporal queries, and event replay. High overhead — only apply when audit trail or temporal queries are a first-class requirement. Natural pair with CQRS.
- **Saga:** coordinate a long-running, multi-step business transaction across services without a distributed lock. Each step publishes an event; compensating transactions roll back on failure. Use when a distributed transaction spans multiple services and two-phase commit is too expensive.

**Apply when the domain is complex (business logic–heavy apps):**
- **DDD (Domain-Driven Design):** model the domain explicitly with entities (identity matters), value objects (equality by value), aggregates (consistency boundary), repositories (collection abstraction), and domain services (logic that doesn't belong to one entity). Use bounded contexts to isolate different subdomains.
- **Specification:** encapsulate a business rule as an object with an `is_satisfied_by(candidate)` method. Specifications can be combined with `and` / `or` / `not`. Use when the same filtering/validation rule is applied in multiple places or must be composed dynamically at runtime.
- **Service Layer:** a thin application-service layer that orchestrates domain objects, repositories, and external services to fulfil a use case. Contains no business logic itself — only sequencing. Keeps controllers/handlers thin by moving use-case flow here.

**Apply when read and write paths diverge significantly:**
- **CQRS:** separate command handlers (write, mutate state) from query handlers (read, return data). Don't apply just because there's a database.

**Apply when multiple delivery mechanisms or deep testability are needed:**
- **Hexagonal / Ports & Adapters:** business logic depends on abstract ports; adapters implement them (HTTP, CLI, DB, queue). The core has zero knowledge of the outside world.

**If the user suggests a pattern that doesn't fit the problem:** apply what they asked, name the standard pattern that would fit instead, and explain the tradeoff in one sentence.

---

## Code Smells (signals that refactoring is needed)

**Bloaters** — code that has grown too large to work with:
- Long Method, Large Class, Primitive Obsession, Long Parameter List, Data Clumps

**Object-Orientation Abusers** — incomplete or incorrect use of OO principles:
- Switch Statements (use polymorphism/Strategy instead), Temporary Field, Refused Bequest, Alternative Classes with Different Interfaces

**Change Preventers** — one change forces many others:
- Divergent Change (one class changed for many reasons → SRP violation), Shotgun Surgery (one change scattered across many classes), Parallel Inheritance Hierarchies

**Dispensables** — things that add no value and should be removed:
- Comments (that describe *what*, not *why*), Duplicate Code, Lazy Class, Data Class, Dead Code, Speculative Generality

**Couplers** — excessive coupling between classes:
- Feature Envy (method more interested in another class's data), Inappropriate Intimacy, Message Chains (`a.b.c.d()`), Middle Man (class that only delegates)

---

## Refactoring Techniques

Apply these when code smells are identified. Never refactor and add features in the same commit.

**Composing Methods:**
- Extract Method, Inline Method, Extract Variable, Inline Temp, Replace Temp with Query, Split Temporary Variable, Remove Assignments to Parameters, Replace Method with Method Object, Substitute Algorithm

**Moving Features Between Objects:**
- Move Method, Move Field, Extract Class, Inline Class, Hide Delegate, Remove Middle Man, Introduce Foreign Method, Introduce Local Extension

**Organizing Data:**
- Self Encapsulate Field, Replace Data Value with Object, Change Value to Reference, Change Reference to Value, Replace Array with Object, Replace Magic Number with Symbolic Constant, Encapsulate Field, Encapsulate Collection, Replace Type Code with Class/Subclass/State/Strategy, Replace Subclass with Fields

**Simplifying Conditional Expressions:**
- Decompose Conditional, Consolidate Conditional Expression, Consolidate Duplicate Conditional Fragments, Remove Control Flag, Replace Nested Conditional with Guard Clauses, Replace Conditional with Polymorphism, Introduce Null Object, Introduce Assertion

**Simplifying Method Calls:**
- Rename Method, Add/Remove Parameter, Separate Query from Modifier, Parameterize Method, Replace Parameter with Explicit Methods, Preserve Whole Object, Replace Parameter with Method Call, Introduce Parameter Object, Remove Setting Method, Hide Method, Replace Constructor with Factory Method, Replace Error Code with Exception, Replace Exception with Test

**Dealing with Generalization:**
- Pull Up Field/Method/Constructor Body, Push Down Method/Field, Extract Subclass/Superclass/Interface, Collapse Hierarchy, Form Template Method, Replace Inheritance with Delegation

---

## How to apply

- Proactively structure new code this way without waiting to be asked.
- When adding a feature, refactor toward these principles rather than growing existing files.
- When a file is getting long, split it as part of the same task — don't defer it.
- Call out violations found in existing code before touching them, so the user can decide scope.
- When the user suggests a design approach: if it's correct, apply it; if it's the wrong pattern for the problem, name what they asked for, implement it if they insist, but flag what the right pattern is and why.
