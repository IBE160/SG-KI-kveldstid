# Story 1.2: Manually Edit Profile

Status: drafted

## Story

As a job seeker,
I want to manually edit my parsed CV information,
so that I can correct any parsing errors or add missing details.

## Acceptance Criteria

*   **Given** My CV has been parsed
*   **When** I navigate to the profile editing interface
*   **Then** I can see and modify extracted fields (e.g., job titles, dates, descriptions, skills).
*   **And** The changes are saved to my profile.

## Tasks / Subtasks

**1. Frontend Development: Profile Editing Interface**
    *   **Task:** Implement the "Profile Editing Interface" React component. (AC2)
        *   **Subtask:** Create `ProfileEditorForm.jsx` (or `.tsx`) in `frontend/src/pages/` or `frontend/src/components/`, adhering to `PascalCase` naming convention. (AC2)
        *   **Subtask:** Integrate `shadcn/ui` form components for input fields (e.g., `Input`, `Textarea`, `Select`) to display extracted CV fields. (AC3)
        *   **Subtask:** Implement state management for form data (e.g., using React hooks like `useState`, `useReducer`, or a context API). (AC3, AC4)
        *   **Subtask:** Implement "Save" and "Cancel" buttons, following button hierarchy patterns. (AC4)
        *   **Subtask:** Implement client-side validation for input fields, displaying inline error messages `On Blur` and `On Submit`. (AC3, AC4)
        *   **Subtask:** Ensure full responsiveness for desktop, tablet, and mobile views. (AC2)
        *   **Subtask:** Implement keyboard navigation and focus management. (AC2)
        *   **Subtask:** Integrate API calls to fetch existing CV data and submit updated data. (AC3, AC4)

**2. Backend Development: API Endpoints & Logic**
    *   **Task:** Develop or extend FastAPI endpoints for CV profile management. (AC3, AC4)
        *   **Subtask:** Define new Pydantic schemas in `backend/app/schemas/` for `CVProfileRead` and `CVProfileUpdate` (or similar) to handle data exchange for profile editing. (AC3, AC4)
        *   **Subtask:** Create or update API endpoints in `backend/app/api/endpoints/documents.py` (or a dedicated `profile.py`) for:
            *   `GET /cv_documents/{cv_id}/profile`: Retrieve parsed CV details for editing. (AC3)
            *   `PUT /cv_documents/{cv_id}/profile`: Update the parsed CV details. (AC4)
        *   **Subtask:** Implement input validation for incoming data using Pydantic models. (AC4)
        *   **Subtask:** Implement `CRUD` operations in `backend/app/crud/` to interact with the PostgreSQL database. This will involve fetching and updating the `parsed_sections_json` field of the `CV Document` model. (AC3, AC4)
        *   **Subtask:** Ensure all endpoints adhere to `snake_case` naming conventions. (AC3, AC4)
        *   **Subtask:** Implement robust error handling using FastAPI's `HTTPException` and standardized error responses. (AC3, AC4)
        *   **Subtask:** Implement structured logging for API requests and database operations. (AC3, AC4)
        *   **Subtask:** Apply `OAuth2/OpenID Connect` for securing endpoints, ensuring only the owner of the `cv_id` can modify their profile. (AC3, AC4)

**3. Database Updates (if necessary)** (AC3, AC4)
    *   **Task:** Review and confirm `CV Document` model in `backend/app/models/` supports `parsed_sections_json` for editing. (AC3, AC4)
        *   **Subtask:** If schema changes are required for `CV Document` (e.g., adding new fields to `parsed_sections_json` structure), create Alembic migration. (AC3, AC4)

**4. Testing** (AC1, AC2, AC3, AC4)
    *   **Task:** Develop comprehensive tests for the new functionality. (Ref: `architecture.md` - Quality Assurance)
        *   **Subtask:** **Frontend Unit Tests:** Write unit tests for the `ProfileEditorForm` component using a framework like Jest/React Testing Library, covering state changes, input handling, and rendering. (AC2, AC3, AC4)
        *   **Subtask:** **Frontend Integration Tests:** Test the integration of the form with the API client. (AC2, AC3, AC4)
        *   **Subtask:** **Backend Unit Tests:** Write unit tests for new/modified CRUD operations and utility functions. (AC3, AC4)
        *   **Subtask:** **Backend Integration Tests:** Write integration tests for the API endpoints using `pytest`, ensuring correct data retrieval and updates, and proper error handling. (AC1, AC2, AC3, AC4)
        *   **Subtask:** **Accessibility Tests:** Perform manual keyboard navigation and screen reader tests on the profile editing interface. (AC2, AC3)
        *   **Subtask:** **Performance Tests:** Basic load testing on the new backend endpoints to ensure `User Interaction Latency` goals are met. (AC2, AC3, AC4)

**5. Documentation** (AC3, AC4)
    *   **Task:** Update API documentation for new endpoints. (AC3, AC4)
        *   **Subtask:** Verify FastAPI's automatic OpenAPI documentation reflects the new endpoints and schemas. (AC3, AC4)

## Dev Notes

### Requirements Context Summary

This story focuses on providing users with the ability to manually edit their CV information after it has been parsed by the system. This is crucial for data accuracy and user satisfaction, allowing for corrections of parsing errors and the addition of missing details.

**Epic:** Epic 1: Core Profile Management
**Epic Goal:** Enable users to input and manage their CV data for job application purposes.

**Story Statement:**
As a job seeker,
I want to manually edit my parsed CV information,
So that I can correct any parsing errors or add missing details.

**Acceptance Criteria:**
*   **Given** My CV has been parsed
*   **When** I navigate to the profile editing interface
*   **Then** I can see and modify extracted fields (e.g., job titles, dates, descriptions, skills).
*   **And** The changes are saved to my profile.

**Prerequisites:** Story 1.1: Upload CV (Text-only)

**Relevant Functional Requirements (from PRD.md):**
*   **FR3:** The system can analyze a user's uploaded CV to extract relevant skills, experiences, and qualifications. (This story builds upon the output of FR3).
*   **FR13:** Users can review and, if necessary, edit the AI-generated cover letter draft and CV suggestions within the application. (This story aligns with the editing aspect, specifically for raw CV data).

**Relevant Non-Functional Requirements (from PRD.md):**
*   **User Interaction Latency:** All user interactions (e.g., button clicks, form submissions) should have a response time of less than 500ms. (Applies to the profile editing interface).
*   **Data Protection:** All user data, especially CV content and personal information, must be encrypted both in transit and at rest. (Applies to the edited profile data).

**Architectural Considerations (from architecture.md):**
*   **Frontend (React):** The profile editing interface will likely be a React component, leveraging `shadcn/ui` for UI elements as per UX specification.
*   **Backend (FastAPI):** The backend will need endpoints to `GET` the parsed CV data and `PUT`/`PATCH` updated CV data. This will interact with `backend/app/api/documents.py` and `backend/app/crud/`.
*   **Database (PostgreSQL):** The edited CV information will be stored in the `CV Document` table, potentially updating `parsed_sections_json`.
*   **Naming Conventions:** API endpoints for editing will likely follow `snake_case` (e.g., `/cv_documents/{cv_id}`). React components will use `PascalCase` (e.g., `CvProfileEditor`).
*   **Error Handling:** Standardized API Error Responses and Frontend Error Boundaries should be implemented for the editing interface.

**UX Design Considerations (from ux-design-specification.md):**
*   **Key Interactions:** This story directly aligns with the "Editing & Refinement" stage of the user journey.
*   **Custom Components:** An "Interactive CV/Job Ad Parser Editor" custom component is identified as potentially needed for manual review and correction, which could be relevant here.
*   **Form Patterns:** Standardized form patterns (top-aligned labels, inline error messages, on-blur validation) should be applied to the profile editing interface.
*   **Feedback Patterns:** Clear feedback (e.g., success toasts for saved changes) is essential.

**Learnings from Previous Story (1-1-upload-cv-text-only):**
Previous story not yet implemented, but this story has a direct dependency on "Story 1.1: Upload CV (Text-only)". The parsing mechanism and output of Story 1.1 will directly influence the data available for manual editing in Story 1.2.

### Project Structure Notes

This story, "1-2-manually-edit-profile", directly impacts and aligns with the existing project structure and architectural decisions, primarily within the backend and frontend components.

**Frontend Alignment:**
*   **Component Location:** The manual editing interface will reside within `frontend/src/components/` or `frontend/src/pages/`, adhering to the defined frontend structure in `architecture.md` and `ux-design-specification.md`. Components will likely use `PascalCase` (e.g., `ProfileEditorForm`, `CvFieldEditor`).
*   **Styling:** Tailwind CSS will be used for styling, in line with the project's frontend decisions.
*   **Interaction:** The UI will follow `shadcn/ui` principles and the UX patterns defined in `ux-design-specification.md` for form fields, buttons, and feedback.

**Backend Alignment:**
*   **API Endpoints:** New or updated API endpoints for fetching and saving user profile data will be added to `backend/app/api/endpoints/` (e.g., within `documents.py` or a new `profile.py`). Naming conventions will follow `snake_case`.
*   **CRUD Operations:** The logic for interacting with the database to read and update CV data will be implemented in `backend/app/crud/`, leveraging SQLAlchemy models.
*   **Models and Schemas:** Pydantic schemas in `backend/app/schemas/` will define the structure for API requests and responses related to profile editing, and SQLAlchemy models in `backend/app/models/` will represent the database entities.

**Database Alignment:**
*   **Entity Impact:** The `CV Document` entity in the PostgreSQL database will be directly affected, specifically the `parsed_sections_json` field which will store the editable CV information.
*   **Data Consistency:** Ensure that updates to `parsed_sections_json` maintain data integrity and are validated against appropriate schemas.

**General Lessons Learned / Best Practices Applied:**
*   **Consistency in Naming:** Adhere strictly to the defined `snake_case` for backend and `PascalCase`/`camelCase` for frontend components and variables.
*   **Layered Architecture:** Maintain clear separation of concerns between API, CRUD, and database models.
*   **Error Handling:** Implement robust error handling (FastAPI `HTTPException`, React Error Boundaries) for the editing process to provide clear feedback to users and facilitate debugging.
*   **Input Validation:** Utilize Pydantic models for strict validation of all incoming data from the frontend to prevent malformed data and potential security vulnerabilities.
*   **Accessibility:** Ensure the profile editing interface is WCAG 2.1 Level AA compliant, especially regarding keyboard navigation and ARIA attributes for form elements.

**No specific learnings from previous story due to it not being implemented yet.**
The parsing output from Story 1.1 will directly feed into the input for this story, making the successful and accurate completion of Story 1.1 critical for the user experience of Story 1.2. Any future issues in parsing accuracy will directly manifest as manual correction needs in this story.

### References

*   [Source: docs/architecture.md#Decision Summary]
*   [Source: docs/prd.md#Functional Requirements]
*   [Source: docs/prd.md#Non-Functional Requirements]
*   [Source: docs/ux-design-specification.md#7. UX Pattern Decisions]
*   [Source: docs/ux-design-specification.md#6. Component Library]
*   [Source: docs/epics.md#Epic 1: Core Profile Management]

### Change Log

| Date       | Version | Change Description | Author     |
| ---------- | ------- | ------------------ | ---------- |
| mandag 8. desember 2025 | 1.0     | Initial draft generated | Gemini CLI |

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

Gemini CLI Agent

### Debug Log References

### Completion Notes List

### File List