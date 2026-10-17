# Spec-Driven Development (SDD) Project Foundation

Welcome to the project repository structured around **Spec-Driven Development (Spec-First)**. In this project, system requirements, architecture decision records (ADRs), API interface contracts, and acceptance criteria are specified and versioned before writing implementation code.

---

## 📁 Repository Directory Structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── spec_proposal.md         # Template to propose new specs or changes
│   └── PULL_REQUEST_TEMPLATE.md     # PR checklist requiring spec traceability
├── docs/
│   └── architecture/                # General project architectural diagrams & docs
├── specs/                           # The Single Source of Truth
│   ├── templates/                   # Reusable templates for the team
│   │   ├── prd-template.md          # Product Requirements Document
│   │   ├── tech-spec-template.md    # Technical System Design Specification
│   │   ├── adr-template.md          # Architecture Decision Record
│   │   ├── api-contract-template.yaml # OpenAPI 3.1 contract boilerplate
│   │   └── task-breakdown-template.md # Implementation task checklist & matrix
│   ├── 01-requirements/             # Approved PRDs, user stories, acceptance criteria
│   ├── 02-architecture/             # Architecture specifications
│   │   └── adrs/                    # Architecture Decision Records (e.g. ADR-0001)
│   ├── 03-api/                      # API contracts (OpenAPI / AsyncAPI / Schemas)
│   │   ├── openapi.yaml             # Baseline API specification
│   │   └── schemas/                 # Reusable data models & JSON schemas
│   ├── 04-acceptance/               # Acceptance criteria & BDD feature files
│   │   └── features/                # Gherkin .feature definitions
│   └── 05-tasks/                    # Task breakdowns linked to approved specs
├── src/                             # Source code implementing the specifications
├── tests/                           # Multi-tier test suite enforcing specifications
│   ├── contract/                    # Contract & schema conformance tests
│   ├── unit/                        # Unit tests validating domain rules
│   ├── integration/                 # Integration tests between components
│   └── e2e/                         # End-to-end user journey tests
├── .gitignore                       # Standard cross-platform git ignore
├── README.md                        # Project overview and navigation
└── SPEC_WORKFLOW.md                 # Complete guide to the Spec-First development cycle
```

---

## 🚀 How to Start a New Feature (Spec-First)

Follow this 5-step cycle:

1. **Requirements (PRD)**:
   - Copy [`specs/templates/prd-template.md`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/specs/templates/prd-template.md) into `specs/01-requirements/<feature-name>.md`.
2. **Architecture & Contract**:
   - Copy [`specs/templates/tech-spec-template.md`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/specs/templates/tech-spec-template.md) into `specs/02-architecture/<feature-name>.md`.
   - Update [`specs/03-api/openapi.yaml`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/specs/03-api/openapi.yaml) with the new endpoints or payloads.
   - Record any architectural decisions in [`specs/02-architecture/adrs/`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/specs/02-architecture/adrs/).
3. **Acceptance & Contract Tests**:
   - Write scenarios in [`specs/04-acceptance/features/`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/specs/04-acceptance/features/).
   - Add contract tests in [`tests/contract/`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/tests/contract/) ensuring requests/responses validate against the OpenAPI contract.
4. **Implementation**:
   - Copy [`specs/templates/task-breakdown-template.md`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/specs/templates/task-breakdown-template.md) into `specs/05-tasks/<feature-name>-tasks.md`.
   - Implement your application code in [`src/`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/src/).
5. **Verification**:
   - Run your test suite. Once all contract, unit, and integration tests pass, submit your PR referencing the spec.

For detailed guidelines and principles, see [`SPEC_WORKFLOW.md`](file:///c:/Users/ZADID/Documents/Codex/PRUEBA-HUBEL/SPEC_WORKFLOW.md).
