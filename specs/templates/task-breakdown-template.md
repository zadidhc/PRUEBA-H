# [Task Checklist] Implementation Plan: Feature Name

| Attribute | Details |
| :--- | :--- |
| **Spec Reference** | [Tech Spec Link](../02-architecture/...) |
| **PRD Reference** | [PRD Link](../01-requirements/...) |
| **Target Milestone**| Sprint X / Release Y |
| **Status** | Planning \| In Progress \| Verification \| Done |

---

## 1. Specification & Contract Sign-Off
- [ ] PRD reviewed and approved by stakeholders
- [ ] Tech Spec reviewed and approved by engineering team
- [ ] API Contract committed to `specs/03-api/`
- [ ] Acceptance criteria / Gherkin features written in `specs/04-acceptance/`

---

## 2. Test-First & Mock Preparation (Spec-Driven Phase)
- [ ] Scaffold contract/mock server tests against the API spec in `tests/contract/`
- [ ] Define unit test stubs for business domain rules in `tests/unit/`
- [ ] Write integration test harness against acceptance criteria in `tests/integration/`
- [ ] Confirm all new tests fail cleanly as expected (Red phase)

---

## 3. Implementation Tasks (Green Phase)
- [ ] **Data / Persistence Layer**:
  - [ ] Implement database migrations or repositories
  - [ ] Write entity mappers
- [ ] **Core Business Domain**:
  - [ ] Implement domain models and validation rules
  - [ ] Implement use cases / service layer
- [ ] **Interface & API Layer**:
  - [ ] Implement controllers / handlers matching `specs/03-api/`
  - [ ] Add schema validation middleware
  - [ ] Implement RFC 7807 error formatting

---

## 4. Verification & Hardening (Refactor / QA Phase)
- [ ] Run contract tests - verify 100% compliance with API specification
- [ ] Run unit & integration test suite - verify all tests pass (Green phase)
- [ ] Performance benchmark against NFR thresholds
- [ ] Security / static analysis scan passes
- [ ] Peer code review against the approved Tech Spec
- [ ] Update documentation and spec status to `Completed`
