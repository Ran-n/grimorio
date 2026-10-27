---
name: Avalio — Project Description
description: Canonical behavioral description of the Avalio teacher-focused evaluation app
type: project
---

Avalio is a secure, admin-controlled, teacher-focused evaluation system for managing students, evaluations, and academic data.

**Why:** Institutional control, auditability, and security — not a public LMS or self-service platform.

**How to apply:** Every design/implementation decision should favor explicitness, visibility, and control. No implicit actions, no hidden state, no self-registration, no magic.

---

## Who Uses It
- **Admins:** Create/approve teacher accounts, manage permissions, view full audit logs, oversee all student data
- **Teachers:** Log in with admin-created accounts, manage classes/students, create evaluations/grades/notes, see only authorized data
- **Students:** Do not log in — managed by teachers, data visible only to authorized teachers/admins

## Core Principles
- No hidden behavior, no implicit actions, no auto-magic
- Everything visible, traceable, and logged
- Explicit permissions, explicit UI elements (nothing hidden behind menus)
- All student data changes are audited

## Account Creation Model
- Teachers CANNOT sign up — admins only create accounts
- Teachers must be approved before they can log in
- No self-registration, no social login

## Student Data
- Teachers: create students, assign to classes, add evaluations/grades/notes, track progress
- Admins: see all students, reassign, lock/archive records, view full change history
- All changes logged

## Evaluation & Grading
- Teachers create evaluations, define criteria, enter grades/qualitative notes, view history
- System prevents accidental overwrites, keeps history, allows admin audit (who changed what, when)

## Audit Logging (core requirement)
Logged events: logins, student creation/edits, grade changes, evaluation creation, permission changes, account approvals/locks, password resets, admin actions.
Logs must be: immutable, searchable, filterable by user/student/date/action.

## UI/UX
- Minimal, black background / night mode, high contrast
- All elements visible (no hidden menus)
- Explicit input validation
- Floating preview windows for evaluations and student profiles
- Predictable behavior — no animations that hide state
- Teacher always sees: current class, current student, current evaluation, what will happen before clicking

## Security
- Admin-controlled accounts, strict password policy, strict rate limits
- Automated secret rotation, KMS/HSM-protected secrets
- Session invalidation on password change
- No user enumeration, no public endpoints, no unauthorized student data exposure

## Testing Requirements
- Unit tests (logic, validation, permissions)
- Integration tests (student flows, teacher flows, admin flows)
- GUI tests (full teacher workflows)
- Must confirm: permissions enforced, audit logs generated, student data protected, UI predictable

## What It Is NOT
- Not a public LMS, not a student portal, not a messaging system
- Not a social platform, not a self-service signup system
- Not a grade-sharing tool for parents
- Not multi-tenant SaaS (unless added later)
