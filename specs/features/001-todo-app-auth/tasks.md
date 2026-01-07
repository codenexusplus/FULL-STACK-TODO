

---
description: "Task list template for feature implementation"
---

# Tasks: Todo App with Authentication

**Input**: Design documents from `/specs/001-todo-app-auth/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Setup `/backend` folder using `uv init`
- [X] T003 Setup `/frontend` folder using `npx create-next-app@latest`
- [ ] T004 [P] Configure linting and formatting tools for both backend and frontend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T005 Setup database schema and migrations framework (Neon DB/PostgreSQL with SQLModel)
- [X] T006 [P] Implement authentication/authorization framework (Better Auth)
- [X] T007 [P] Setup API routing and middleware structure (FastAPI)
- [X] T008 Create base models/entities that all stories depend on (with user_id for ownership)
- [X] T009 Configure error handling and logging infrastructure
- [X] T010 Setup environment configuration management
- [X] T011 [P] Configure type checking (Python type hints, TypeScript strict mode)
- [X] T012 Setup SDD pipeline for code generation (Zero Manual Code principle)
- [X] T013 Create `.env` file in project root with `DATABASE_URL=postgresql://user:password@ep-cool-name.aws.neon.tech/neondb`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Account Creation (Priority: P1) 🎯 MVP

**Goal**: Enable users to create accounts so their tasks are private and persistent

**Independent Test**: Can be fully tested by registering a new user account and verifying that the account is created successfully in the system.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T014 [P] [US1] Contract test for `/api/auth/register` in tests/contract/test_auth.py
- [ ] T015 [P] [US1] Contract test for `/api/auth/login` in tests/contract/test_auth.py

### Implementation for User Story 1

- [X] T016 [P] [US1] Create User model with user_id foreign key in backend/src/models/user.py
- [X] T017 [P] [US1] Create User service in backend/src/services/user_service.py
- [X] T018 [US1] Implement registration endpoint in backend/src/api/auth.py
- [X] T019 [US1] Implement login endpoint in backend/src/api/auth.py
- [ ] T020 [US1] Add validation and error handling for auth endpoints
- [ ] T021 [US1] Add logging for user story 1 operations
- [X] T022 [US1] Create RegisterForm component in frontend/src/components/auth/RegisterForm.tsx
- [X] T023 [US1] Create LoginForm component in frontend/src/components/auth/LoginForm.tsx
- [X] T024 [US1] Create register page in frontend/src/app/register/page.tsx
- [X] T025 [US1] Create login page in frontend/src/app/login/page.tsx
- [X] T026 [US1] Connect frontend auth forms to backend auth endpoints

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Task Dashboard Access (Priority: P2)

**Goal**: Allow authenticated users to see a professional dashboard of their tasks in a browser

**Independent Test**: Can be fully tested by logging in as an authenticated user and viewing the task dashboard with proper layout and responsiveness.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T027 [P] [US2] Contract test for `/api/todos` GET endpoint in tests/contract/test_todos.py
- [ ] T028 [P] [US2] Integration test for user dashboard access in tests/integration/test_dashboard.py

### Implementation for User Story 2

- [X] T029 [P] [US2] Create Todo model with user_id foreign key in backend/src/models/todo.py
- [X] T030 [US2] Implement Todo service in backend/src/services/todo_service.py
- [X] T031 [US2] Implement GET `/api/todos` endpoint in backend/src/api/todos.py
- [X] T032 [US2] Add authentication middleware to ensure users only access their own data
- [X] T033 [US2] Create TodoList component in frontend/src/components/todos/TodoList.tsx
- [X] T034 [US2] Create TodoItem component in frontend/src/components/todos/TodoItem.tsx
- [X] T035 [US2] Create dashboard page in frontend/src/app/todos/page.tsx
- [X] T036 [US2] Implement data fetching for dashboard in frontend/src/app/api/todos.ts
- [X] T037 [US2] Ensure API filters results by user_id for privacy (Data Ownership & Privacy principle)
- [X] T038 [US2] Implement responsive layout using Tailwind CSS and Shadcn UI

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Task Management (Priority: P3)

**Goal**: Allow users to create, update, delete, and mark tasks as complete to manage their to-do list effectively

**Independent Test**: Can be fully tested by performing CRUD operations on tasks and verifying they persist correctly and are only visible to the owning user.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T039 [P] [US3] Contract test for `/api/todos` POST endpoint in tests/contract/test_todos.py
- [ ] T040 [P] [US3] Contract test for `/api/todos/{id}` PATCH endpoint in tests/contract/test_todos.py
- [ ] T041 [P] [US3] Contract test for `/api/todos/{id}` DELETE endpoint in tests/contract/test_todos.py

### Implementation for User Story 3

- [X] T042 [P] [US3] Implement POST `/api/todos` endpoint in backend/src/api/todos.py
- [X] T043 [US3] Implement PATCH `/api/todos/{id}` endpoint in backend/src/api/todos.py
- [X] T044 [US3] Implement DELETE `/api/todos/{id}` endpoint in backend/src/api/todos.py
- [X] T045 [US3] Add proper validation for all todo operations
- [X] T046 [US3] Create form components for task creation/update in frontend/src/components/todos/
- [X] T047 [US3] Implement task creation functionality in frontend/src/app/todos/page.tsx
- [X] T048 [US3] Implement task update functionality in frontend/src/app/todos/page.tsx
- [X] T049 [US3] Implement task deletion functionality in frontend/src/app/todos/page.tsx
- [X] T050 [US3] Implement task completion toggle in frontend/src/components/todos/TodoItem.tsx
- [X] T051 [US3] Ensure API filters results by user_id for privacy (Data Ownership & Privacy principle)
- [X] T052 [US3] Add toast notifications for user feedback (e.g., "Task Added")

**Checkpoint**: All user stories should now be independently functional

---

[Add more user stories as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T053 [P] Documentation updates in docs/
- [X] T054 Code cleanup and refactoring
- [ ] T055 Performance optimization across all stories
- [ ] T056 [P] Additional unit tests (if requested) in tests/unit/
- [X] T057 Security hardening with focus on authentication (Better Auth)
- [X] T058 Run quickstart.md validation
- [X] T059 Verify compliance with Zero Manual Code principle (all code generated via SDD)
- [X] T060 Verify strict separation between Backend and Frontend maintained
- [X] T061 Verify all functions have Google-style docstrings
- [X] T062 Verify type safety in both Python and TypeScript codebases
- [X] T063 Implement proper session management and handle expired sessions
- [X] T064 Add proper error handling for edge cases (accessing other users' tasks)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for /api/auth/register in tests/contract/test_auth.py"
Task: "Contract test for /api/auth/login in tests/contract/test_auth.py"

# Launch all models for User Story 1 together:
Task: "Create User model with user_id foreign key in backend/src/models/user.py"
Task: "Create RegisterForm component in frontend/src/components/auth/RegisterForm.tsx"
Task: "Create LoginForm component in frontend/src/components/auth/LoginForm.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence