---
name: Avaliario System Description
description: Full behavioral description of the Avaliario teacher-focused evaluation app — users, principles, data model, UI/UX, security, and what it is NOT.
type: project
---

Avaliario is a **secure, admin-controlled, teacher-focused evaluation system**. It is NOT a public platform or self-service signup system.

## Users
- **Admins**: create/approve teacher accounts, manage permissions, view full audit logs, oversee all student data
- **Teachers**: log in with admin-created accounts, manage their own classes/students/evaluations, cannot create accounts or bypass admin controls
- **Students**: do NOT log in; managed by teachers; data visible only to authorized teachers and admins

## Core Principles
- No hidden behavior, no implicit actions, no auto-magic
- Everything visible, traceable, and logged
- Every student data action is audited; every permission is explicit

## Account Creation
- Teachers CANNOT sign up; only admins create accounts
- Teachers must be approved before login
- No self-registration, no social login

## Student Data
- Teachers: create students, assign to classes, add evaluations/grades/notes, track progress
- Admins: see all students, reassign, lock/archive records, view full history
- All changes logged

## Evaluation & Grading
- Teachers create evaluations, define criteria, enter grades/qualitative notes
- System prevents accidental overwrites, keeps change history
- Admins can audit who changed what and when

## Audit Logging (Core Requirement)
Logged: logins, student create/edit, grade changes, evaluation creation, permission changes, account approvals/locks, password resets, admin actions.
Logs must be: immutable, searchable, filterable by user/student/date/action.

## UI/UX Requirements
- Minimal, black background / night mode, high contrast
- All elements visible (no hidden menus)
- Floating preview windows for evaluations and student profiles
- Explicit input validation, predictable behavior (no animations that hide state)
- Teacher always sees: current class, current student, current evaluation, what will happen before clicking

## Security
- Admin-controlled accounts, strict password policy, strict rate limits
- Session invalidation on password change
- No user enumeration, no public endpoints, no student data exposure without permission

## Testing
- Unit tests (logic, validation, permissions)
- Integration tests (student/teacher/admin flows)
- GUI tests (full teacher workflows)
- Must confirm: permissions enforced, audit logs generated, student data protected, UI predictable

## What It Is NOT
- Not a public LMS, not a student portal, not a messaging system
- Not a social platform, not self-service signup, not a grade-sharing tool for parents
- Not multi-tenant SaaS (unless added later)

**Why:** This is an institutional tool for controlled environments — full auditability and admin control are non-negotiable requirements.
**How to apply:** Every feature decision should favor explicitness, visibility, and auditability over convenience. When in doubt, log it, show it, require explicit confirmation.
