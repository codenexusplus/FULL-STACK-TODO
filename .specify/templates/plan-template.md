# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.13+ (Backend), TypeScript (Frontend)
**Primary Dependencies**: FastAPI, SQLModel, Neon DB (Backend); Next.js (App Router), Tailwind CSS, Shadcn UI (Frontend)
**Storage**: PostgreSQL via Neon DB with SQLModel ORM
**Testing**: pytest for backend, Jest/React Testing Library for frontend
**Target Platform**: Web application (Full-stack)
**Project Type**: Web application (Backend/Frontend decoupled)
**Performance Goals**: Responsive UI with <200ms p95 API response times
**Constraints**: Strict separation of concerns between backend and frontend, type safety enforced
**Scale/Scope**: User authentication with row-level data ownership, task management system

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Zero Manual Code: All logic, UI, and database migrations must be generated via SDD
- Separation of Concerns: Backend (FastAPI) and Frontend (Next.js) remain strictly decoupled
- Strict Type Safety: Mandatory type hints in Python and strict typing in TypeScript
- Spec-Driven Development Pipeline: Specifications must be completed before implementation
- Data Ownership & Privacy: Every data item linked to user_id with proper filtering
- Authentication Security: Better Auth for secure user sessions and row-level ownership

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── todos.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   └── main.py
└── tests/
    ├── __init__.py
    ├── test_auth.py
    └── test_todos.py

frontend/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.ts
│   │   │   └── todos.ts
│   │   ├── components/
│   │   │   ├── auth/
│   │   │   │   ├── LoginForm.tsx
│   │   │   │   └── RegisterForm.tsx
│   │   │   └── todos/
│   │   │       ├── TodoItem.tsx
│   │   │       └── TodoList.tsx
│   │   ├── pages/
│   │   │   ├── login/
│   │   │   │   └── page.tsx
│   │   │   ├── register/
│   │   │   │   └── page.tsx
│   │   │   └── todos/
│   │   │       └── page.tsx
│   │   └── layout.tsx
│   ├── lib/
│   │   ├── auth.ts
│   │   └── types.ts
│   └── styles/
│       └── globals.css
└── tests/
    ├── __init__.py
    ├── test_auth_pages.py
    └── test_todo_pages.py

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
| Full-stack architecture | Required for complete solution | Single component insufficient for end-to-end functionality |
| Strict type safety enforcement | Prevents runtime errors and improves maintainability | Dynamic typing leads to more bugs and harder maintenance |
