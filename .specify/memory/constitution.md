<!--
Sync Impact Report:
- Version change: 0.1.0 → 1.0.0
- Modified principles: All principles completely redefined for Full-Stack Evolution project
- Added sections: Core Mandate, Technical Stack & Standards, Workflow Protocol, Database & Auth Rules, Definition of Done
- Removed sections: Original template placeholders
- Templates requiring updates: .specify/templates/plan-template.md ✅ updated, .specify/templates/spec-template.md ✅ updated, .specify/templates/tasks-template.md ✅ updated
- Follow-up TODOs: None
-->
# Full-Stack Evolution Constitution

## Core Principles

### Zero Manual Code
No code is to be written by the human Architect. All logic, UI, and database migrations must be generated via Spec-Driven Development (SDD). This ensures consistency, reduces human error, and enforces systematic development practices.

### Separation of Concerns
The Backend (FastAPI) and Frontend (Next.js) must remain strictly decoupled. Communication happens only via JSON APIs. This ensures scalability, maintainability, and allows independent development and deployment of each component.

### Strict Type Safety
Mandatory type hints in Python and strict typing in TypeScript. All functions require Google-style docstrings. This ensures code clarity, reduces runtime errors, and improves maintainability across the full-stack application.

### Spec-Driven Development Pipeline
Before any code generation, the following must be updated in specs/: Specify (specify.md): Define the API endpoints, UI pages, and User Auth flow. Plan (plan.md): Define the Database Schema (ERD) and the folder structure. Tasks (tasks.md): Create a checklist of atomic implementation steps. This ensures systematic, well-documented development.

### Data Ownership & Privacy
Every "Todo" item must be linked to a user_id. The API must filter results so users can only access their own data. This ensures user privacy and proper data governance across the application.

### Authentication Security
Better Auth for secure user sessions and row-level task ownership. This ensures robust authentication and authorization mechanisms protecting user data and application resources.

## Technical Stack & Standards

### Backend Requirements
Backend: Python 3.13+, uv, FastAPI, SQLModel (for ORM), and Neon DB (PostgreSQL). This technology stack provides high performance, modern Python features, and robust database management capabilities.

### Frontend Requirements
Frontend: Next.js (App Router), TypeScript, Tailwind CSS, and Shadcn UI. This provides a modern, responsive user interface with strong typing and efficient component architecture.

## Workflow Protocol (SDD Pipeline)

### Specification Requirements
Before any code generation, the following must be updated in specs/:
- Specify (specify.md): Define the API endpoints, UI pages, and User Auth flow.
- Plan (plan.md): Define the Database Schema (ERD) and the folder structure.
- Tasks (tasks.md): Create a checklist of atomic implementation steps.

This ensures all development is properly planned and documented before implementation.

### Database Migration Planning
Database schema changes must be planned before execution. This prevents data loss and ensures smooth transitions between application versions.

## Definition of Done

### Backend Requirements
The Backend passes all API tests. This ensures all endpoints function correctly and meet the specified requirements.

### Frontend Requirements
The Frontend is responsive and correctly handles Auth states (Login/Logout). This ensures a good user experience and proper security handling.

### Documentation Requirements
All specification files are moved to specs/history/ after a successful build. This maintains a clean project structure and preserves historical documentation.

## Governance

All development must comply with the principles outlined in this constitution. Amendments to this constitution require explicit approval and must be documented with proper versioning. The constitution supersedes all other development practices and serves as the authoritative guide for the Full-Stack Evolution project.

**Version**: 1.0.0 | **Ratified**: 2025-01-07 | **Last Amended**: 2025-01-07