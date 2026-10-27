---
name: Avaliario Project Description
description: Core concept, users, features, and constraints for the Avaliario teacher-focused evaluation app
type: project
---

Avaliario is a secure, admin-controlled, teacher-focused student evaluation system. It is a closed institutional tool — not public, not self-service.

**Why:** Designed for explicit control, full auditability, and minimal/predictable UX for teachers managing students and grades.

**How to apply:** All design and implementation decisions should prioritize explicitness, auditability, and admin control over convenience or automation.

## Users
- **Admins**: create/approve teacher accounts, manage permissions, view all audit logs and student data, reassign/archive students
- **Teachers**: manage their classes and students, create evaluations and grades, see only authorized data — cannot create accounts or bypass admin controls
- **Students**: do not log in — managed by teachers, data visible only to authorized teachers/admins

## Account Model
- No self-registration, no social login
- Only admins create teacher accounts; teachers must be approved before login
- No MFA yet (can be added later)

## Core Features
- Student management: create, assign to classes, add evaluations/grades/notes, track progress, export/print reports (if admin-allowed)
- Evaluations: define criteria, enter grades or qualitative notes, view history, generate summaries
- Prevent accidental overwrites; keep full history of changes

## Audit Logging (core requirement)
Immutable, searchable, filterable logs for every action: logins, student create/edit, grade changes, evaluation creation, permission changes, account approvals/locks, password resets, admin actions. Filterable by user, student, date, action.

## UI/UX
- Black background / night mode, high contrast
- All elements visible — no hidden menus
- Floating preview windows for evaluations and student profiles
- Explicit input validation, no animations that hide state
- Teacher always sees: current class, current student, current evaluation, what will happen before clicking

## Security
- Admin-controlled accounts, strict password policy, strict rate limits
- Automated secret rotation, KMS/HSM-protected secrets
- Session invalidation on password change
- No user enumeration, no public endpoints, no unauthorized student data exposure

## Testing Requirements
- Unit tests: logic, validation, permissions
- Integration tests: student flows, teacher flows, admin flows
- GUI tests: full teacher workflows
- Must confirm: permissions enforced, audit logs generated, student data protected, UI predictable

## What it is NOT
Not a public LMS, student portal, messaging system, social platform, self-service signup, grade-sharing tool for parents, or multi-tenant SaaS (unless added later).

## Stack
- **Frontend**: Flet (Python, Flutter-rendered) — calls backend over HTTP
- **Backend**: FastAPI + Uvicorn
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **DB**: SQLite locally, likely Postgres on VPS
- **Auth**: JWT (short-lived access tokens) + DB-persisted refresh tokens, `python-jose`, `passlib[bcrypt]`, httpOnly cookies
- **Deployment**: local for now, VPS in production
