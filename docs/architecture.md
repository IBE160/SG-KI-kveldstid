# Architecture

## Executive Summary

I'm reviewing your project documentation for AI CV & Job Application Assistant.
I found 18 functional requirements organized into Document Management, Core AI Analysis & Generation, UI & Feedback, Output & Export, Platform & Browser Compatibility, Accessibility.
I also found your UX specification which defines the user experience requirements.

Key aspects I notice:
- The core functionality revolves around AI-driven analysis and generation for tailoring CVs and cover letters to job ads.
- Critical Non-Functional Requirements include high performance (fast UI, AI processing < 5 min), robust security (encryption, GDPR, API security), and scalability (99.9% uptime, elastic scaling).
- The UX specification indicates a high level of interactive complexity with custom components for AI suggestions, visualizers, and real-time feedback, all designed with WCAG 2.1 Level AA accessibility and a mobile-first responsive strategy.
- Novel patterns like Claim-to-Evidence Validation and Educational Feedback Loop require careful architectural consideration for AI integration and data flow.
- The project aims for a stateless MVP, React+Tailwind frontend, FastAPI backend, and OpenAI for AI capabilities, deployed on AWS with Docker.

This will help me guide you through the architectural decisions needed to ensure AI agents implement this consistently.

## Project Initialization

### Frontend (React with Tailwind CSS via Vite)

**Initialization Commands:**
```bash
# Create React project with Vite
npm create vite@latest frontend -- --template react

# Navigate into frontend directory
cd frontend

# Install dependencies
npm install

# Install Tailwind CSS and its peer dependencies
npm install -D tailwindcss postcss autoprefixer

# Initialize tailwind.config.js and postcss.config.js
npx tailwindcss init -p
```
**Configuration for Tailwind CSS:**
Update `frontend/tailwind.config.js`:
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
Add Tailwind directives to `frontend/src/index.css` (or `main.css`):
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**Frontend Starter-Provided Decisions:**
-   **Framework:** React
-   **Build Tool:** Vite
-   **Styling:** Tailwind CSS, PostCSS, Autoprefixer
-   **Language:** JavaScript (default, TypeScript optional)
-   **Project Structure:** Standard Vite/React application structure

### Backend (FastAPI)

**Initialization Commands:**
```bash
# Create backend directory
mkdir backend
cd backend

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (example for Windows/Linux/macOS)
# On Windows: .\venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

# Install FastAPI and Uvicorn
pip install fastapi "uvicorn[standard]"
```
**Example `backend/main.py`:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI backend!"}
```
**Backend Starter-Provided Decisions:**
-   **Framework:** FastAPI
-   **ASGI Server:** Uvicorn
-   **Language:** Python
-   **Basic Project Structure:** Manual, with a `main.py` for API endpoints

**Note for first implementation story:**
Project initialization (setting up both frontend and backend as described above) should be the first implementation story.


## Decision Summary

| Category | Decision | Version | Affects Epics | Rationale |
| -------- | -------- | ------- | ------------- | --------- |
| Data Persistence | PostgreSQL with pgvector extension | 16.3 (as of May 2024) | All | Handles both regular application data and AI vector embeddings efficiently in one place, simplifying architecture. Robust and well-supported. |
| Client-Server Communication | REST with FastAPI | N/A | All | FastAPI built around REST principles, provides automatic interactive documentation, well-suited for MVP, clear separation of concerns, well-understood. |
| Security and User Management | OAuth2/OpenID Connect | N/A | All | Simplifies implementation, offloads complex security, supports social logins, critical for GDPR and user privacy, allows focus on core AI features. |
| Infrastructure and Hosting | AWS (ECS/Fargate, S3/CloudFront, RDS) | N/A | All | Aligns with PRD, robust, scalable, containerization for flexibility, managed services reduce operational overhead, highly available, performs well. |
| Artificial Intelligence Services | OpenAI API (GPT-4-turbo, Embeddings API) with PostgreSQL pgvector | Latest stable APIs | All | Aligns with PRD, leverages powerful external AI, pgvector for efficient embedding storage/querying within the primary database, simplifies architecture for semantic matching and Claim-to-Evidence Validation. |
| Data Ingestion (Document Parsing) | Open-source Python Libraries for MVP, migrate to AWS Textract | N/A | All | Cost-effective for MVP, faster iteration. AWS Textract offers higher accuracy and better integration with AWS for future scaling and robustness. |
| Live Data Updates | WebSockets (using FastAPI's native support) | N/A | All | Provides immediate, continuous communication for dynamic ATS score and real-time AI suggestions, aligns with UX design, FastAPI has excellent built-in support. |
| File Storage | AWS S3 (Simple Storage Service) | N/A | All | Scalable, durable, secure object storage, integrates seamlessly with other AWS services, optimal for storing uploaded CVs and generated documents, separates file storage from database. |
| Error Handling | Standardized API Error Responses (FastAPI HTTPException), Centralized Error Logging (AWS CloudWatch Logs), Frontend Error Boundaries (React). | N/A | All | Robust multi-pronged approach for consistent error presentation, efficient debugging, and graceful UI degradation, leading to better user experience and developer productivity. |
| Observability and Monitoring (Logging) | Structured Logging (JSON) with Python logging module, standard levels, integrated with AWS CloudWatch Logs. | N/A | All | Enables efficient machine parsing, querying, debugging, monitoring, and analysis in cloud environments, ensuring consistent event recording across the application. |
| Data Standardization (Date/Time Handling) | Store as UTC in PostgreSQL, use ISO 8601 for API, convert to local time on frontend for display. | N/A | All | Gold standard for global applications, prevents time zone issues, ensures unambiguous communication, and provides user-friendly display. |
| Data Exchange (API Response Format) | Standardized Wrapper Object ({data: <payload>, meta: <pagination/other info>, errors: <error details>}) | N/A | All | Ensures consistent API responses, simplifies frontend processing, reliable error handling, and prevents inconsistent API interfaces across agents. |
| Quality Assurance (Testing Strategy) | Layered approach: Unit Tests (frontend & backend), Integration Tests (API, DB), Component Tests (UI), targeted E2E Tests, and Manual Testing. | N/A | All | Ensures robust and reliable application, catches bugs early, reduces regressions, and ensures high quality for a critical user tool. |

## Project Structure

```
.
├── .git/
├── .bmad/
├── docs/
│   ├── architecture.md
│   ├── prd.md
│   ├── product-brief.md
│   ├── ux-design-specification.md
│   └── ...
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── App.jsx/tsx
│   │   ├── main.jsx/tsx
│   │   └── index.css (with Tailwind directives)
│   ├── index.html
│   ├── package.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── vite.config.js
├── backend/
│   ├── venv/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/ (e.g., ai.py, auth.py, documents.py)
│   │   │   └── __init__.py
│   │   ├── core/ (e.g., config.py, security.py, logging.py)
│   │   ├── crud/ (database operations)
│   │   ├── models/ (Pydantic models for API, SQLAlchemy models for DB)
│   │   ├── schemas/ (Pydantic schemas for request/response)
│   │   ├── main.py (FastAPI app entry point, includes WebSockets)
│   │   └── __init__.py
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── pyproject.toml / setup.py
└── README.md
```

## Epic to Architecture Mapping

### Functional Requirement Category to Architectural Component Mapping

| FR Category | Primary Architectural Component(s) | Notes |
|---|---|---|
| Document Management | `backend/app/api/documents.py`, `backend/app/crud/`, `backend/app/models/`, `backend/app/core/` | Handles CV upload, parsing, and storage. |
| Core AI Analysis & Generation | `backend/app/api/ai.py`, `backend/app/core/` | Integrates OpenAI API, `pgvector` logic for embeddings. |
| UI & Feedback | `frontend/src/` components, `backend/app/main.py` | Components for display, WebSockets for real-time updates. |
| Output & Export | `backend/app/api/documents.py` | Endpoints for exporting generated content. |
| Platform & Browser Compatibility | Frontend (React), Backend (FastAPI) | Ensures broad compatibility and responsive design. |
| Accessibility | Frontend (React components, styling) | WCAG 2.1 Level AA compliance implemented in UI. |

## Technology Stack Details

### Core Technologies

-   **Frontend:** React (via Vite)
    -   **Styling:** Tailwind CSS, PostCSS, Autoprefixer
    -   **Language:** JavaScript (with option for TypeScript)
-   **Backend:** FastAPI
    -   **Language:** Python
    -   **ASGI Server:** Uvicorn
-   **Database:** PostgreSQL (Version 16.3) with `pgvector` extension
-   **AI Services:** OpenAI API (GPT-4-turbo for text generation, Embeddings API)
-   **Deployment Platform:** AWS (ECS/Fargate, S3, CloudFront, RDS)

### Integration Points

-   **Frontend ↔ Backend:** REST API calls (JSON payload, standardized wrapper), WebSockets for real-time updates.
-   **Backend ↔ Database (PostgreSQL):** ORM (e.g., SQLAlchemy) for data persistence, `pgvector` extension for embeddings.
-   **Backend ↔ OpenAI API:** HTTP requests to OpenAI endpoints (embeddings, chat completions).
-   **Backend ↔ AWS S3:** AWS SDK for Python (`boto3`) for file storage operations.
-   **Backend ↔ AWS CloudWatch:** Python's `logging` module configured for CloudWatch.

## Novel Pattern Designs

No new novel architectural patterns were designed in this workflow. Established patterns and existing AI service capabilities are leveraged to achieve the project's unique features.

## Implementation Patterns

These patterns ensure consistent implementation across all AI agents:

### Error Handling
- **Strategy:** Standardized API Error Responses (FastAPI HTTPException), Centralized Error Logging (AWS CloudWatch Logs), Frontend Error Boundaries (React).
- **Rationale:** Robust multi-pronged approach for consistent error presentation, efficient debugging, and graceful UI degradation.

### Logging
- **Strategy:** Structured Logging (JSON) with Python `logging` module, standard levels, integrated with AWS CloudWatch Logs.
- **Rationale:** Enables efficient machine parsing, querying, debugging, monitoring, and analysis in cloud environments, ensuring consistent event recording.

### Date/Time Handling
- **Strategy:** Store as UTC in PostgreSQL, use ISO 8601 for API, convert to local time on frontend for display.
- **Rationale:** Gold standard for global applications, prevents time zone issues, ensures unambiguous communication, and provides user-friendly display.

### API Response Format
- **Strategy:** Standardized Wrapper Object (`{"data": <payload>, "meta": <pagination/other info>, "errors": <error details>}`).
- **Rationale:** Ensures consistent API responses, simplifies frontend processing, reliable error handling, and prevents inconsistent API interfaces across agents.

### Testing Strategy
- **Strategy:** Layered approach: Unit Tests (frontend & backend), Integration Tests (API, DB), Component Tests (UI), targeted E2E Tests, and Manual Testing.
- **Rationale:** Ensures robust and reliable application, catches bugs early, reduces regressions, and ensures high quality.

## Consistency Rules

### Naming Conventions
-   **API Endpoints (paths & query params):** `snake_case` (e.g., `/users/{user_id}/cv_documents`, `query_param_name`)
-   **Database Tables:** Plural `snake_case` (e.g., `users`, `cv_documents`)
-   **Database Columns:** Singular `snake_case` (e.g., `user_id`, `file_name`)
-   **Python Variables/Functions:** `snake_case`
-   **React Components:** `PascalCase` (e.g., `CvDocumentCard`)
-   **React Props, JS/TS Variables/Functions:** `camelCase`

### Code Organization
-   **Monorepo Structure:** `frontend/` and `backend/` as top-level directories.
-   **Frontend (`frontend/`):**
    -   `src/components/`: Reusable UI components.
    -   `src/pages/`: Page-level components/views.
    -   `src/api/`: Frontend API client logic.
    -   `src/hooks/`: Custom React hooks.
    -   `src/utils/`: General utility functions.
    -   `src/styles/`: Global styles and Tailwind config.
-   **Backend (`backend/app/`):**
    -   `api/endpoints/`: Group API endpoints by resource (e.g., `users.py`, `ai.py`, `documents.py`).
    -   `core/`: Application-wide configuration, security, logging, external service integrations (OpenAI, S3).
    -   `crud/`: Database interaction logic (Create, Read, Update, Delete).
    -   `models/`: Database ORM models (e.g., SQLAlchemy models).
    -   `schemas/`: Pydantic models for API request/response validation and serialization.
    -   `tests/`: Unit and integration tests (at `backend/tests/`).
    -   `alembic/`: Database migrations.

### Error Handling

- **Strategy:** Standardized API Error Responses (FastAPI HTTPException), Centralized Error Logging (AWS CloudWatch Logs), Frontend Error Boundaries (React).
- **Rationale:** Robust multi-pronged approach for consistent error presentation, efficient debugging, and graceful UI degradation.

### Logging Strategy

- **Strategy:** Structured Logging (JSON) with Python `logging` module, standard levels, integrated with AWS CloudWatch Logs.
- **Rationale:** Enables efficient machine parsing, querying, debugging, monitoring, and analysis in cloud environments, ensuring consistent event recording.

## Data Architecture

-   **Database:** PostgreSQL (Version 16.3)
-   **ORM:** SQLAlchemy (with Asyncio support)

### Key Entities and Relationships

-   **User:**
    -   `id` (PK), `email` (unique), `password_hash`, `created_at`, `updated_at`
-   **CV Document:**
    -   `id` (PK), `user_id` (FK to User), `s3_file_path`, `upload_date`, `raw_text_content`, `parsed_sections_json`, `embedding` (pgvector column)
    -   Relationship: One-to-many from User
-   **Job Advertisement:**
    -   `id` (PK), `user_id` (FK to User), `title`, `company`, `description`, `raw_text_content`, `embedding` (pgvector column), `created_at`
    -   Relationship: One-to-many from User
-   **Application Session:**
    -   `id` (PK), `user_id` (FK to User), `cv_id` (FK to CV Document), `job_ad_id` (FK to Job Advertisement), `generated_cover_letter`, `ats_score`, `ai_suggestions_json`, `created_at`
    -   Relationship: Many-to-one from User, CV Document, Job Advertisement

### Embedding Storage

-   **`pgvector` Extension:** Used in `CV Document` and `Job Advertisement` tables to store OpenAI embeddings directly alongside text content, enabling efficient semantic search and matching within the database.

## API Contracts

-   **Automatic Documentation:** FastAPI automatically generates OpenAPI (Swagger UI/ReDoc) documentation based on code, serving as the primary API contract.
-   **Request/Response Validation:** Pydantic models will be used extensively for validating incoming request data and serializing outgoing response data, ensuring strict type enforcement and clear data structures.
-   **Standardized Error Responses:** API errors will follow the previously defined Standardized Wrapper Object.

### Key API Endpoints (Examples)

-   **CV Management:**
    -   `GET /cv_documents`: List all user's uploaded CVs.
    -   `POST /cv_documents`: Upload a new CV (expects file upload), returns `CvDocumentSchema`.
    -   `GET /cv_documents/{cv_id}`: Retrieve details of a specific CV.
-   **Job Advertisement Management:**
    -   `POST /job_advertisements`: Submit a new job ad text, returns `JobAdvertisementSchema`.
-   **Application Session:**
    -   `POST /application_sessions`: Create a new application tailoring session (takes `cv_id`, `job_ad_id`), returns `ApplicationSessionSchema` with initial analysis.
    -   `PUT /application_sessions/{session_id}/suggestions`: Apply/update AI suggestions for the session.
    -   `GET /application_sessions/{session_id}/export`: Export tailored application content.
-   **Real-time Updates:**
    -   `WebSocket /ws/{session_id}`: Provides real-time ATS score updates and AI suggestion notifications.

## Security Architecture

-   **Authentication/Authorization:** As decided, OAuth2/OpenID Connect will be implemented.
    -   Backend uses JWT-based tokens for API access validation.
    -   Frontend securely handles tokens (e.g., HTTP-only cookies, Web Workers, or in-memory with appropriate CSRF/XSS protection).
    -   Role-Based Access Control (RBAC) to manage user permissions.
-   **Data Encryption:**
    -   **In Transit:** All communication will use TLS/HTTPS.
    -   **At Rest:** AWS RDS encryption for PostgreSQL database, AWS S3 encryption for stored files.
-   **Input Validation:** Strict validation on all incoming API requests using FastAPI's Pydantic models to prevent injection attacks and malformed data.
-   **GDPR Compliance:** Design will incorporate principles for data subject rights (access, rectification, erasure), data minimization, and transparent privacy policies.
-   **API Security:** Implement rate limiting, proper CORS (Cross-Origin Resource Sharing) configuration, and secure header settings.
-   **Vulnerability Management:** Regular dependency scanning and security audits will be part of the development lifecycle.

## Performance Considerations

-   **Frontend Optimization:**
    -   **Lazy Loading:** Load UI components and data only when needed.
    -   **Code Splitting:** Break down JavaScript bundles into smaller chunks for faster initial load.
    -   **Image Optimization:** Use efficient image formats and responsive images.
    -   **Caching:** Browser caching for static assets.
-   **Backend Optimization:**
    -   **Asynchronous I/O:** Leverage FastAPI's native async/await for non-blocking operations to handle many requests concurrently.
    -   **Database Indexing:** Optimize database queries with appropriate indexes on frequently accessed columns.
    -   **Query Optimization:** Write efficient SQLAlchemy queries to minimize database load.
    -   **Caching (Backend):** Implement Redis for caching frequently accessed data or API responses to reduce database hits.
-   **AI Processing:**
    -   **Asynchronous Background Tasks:** Use a task queue (e.g., Celery with Redis or a simple FastAPI `BackgroundTasks` pattern) for long-running AI operations (document parsing, embeddings generation, complex LLM calls) to avoid blocking API responses.
    -   **Rate Limiting:** Implement rate limiting for calls to external AI APIs (OpenAI) to manage costs and stay within service limits.
    -   **Progress Indicators:** Provide clear visual feedback on the frontend during AI processing to manage user expectations (as per UX).
-   **Deployment:**
    -   **Auto-scaling:** Configure ECS/Fargate containers to auto-scale based on load, ensuring consistent performance during traffic spikes.
    -   **CDN (CloudFront):** Delivers static frontend assets from edge locations globally for low latency.

## Deployment Architecture

-   **Containerization:** Both frontend (React) and backend (FastAPI) applications will be containerized using Docker.
-   **Frontend Deployment (React):**
    -   Production build of React application.
    -   Hosted as static assets on AWS S3.
    -   Content distributed globally via AWS CloudFront (CDN) for low-latency delivery.
-   **Backend Deployment (FastAPI):**
    -   Packaged into a Docker image.
    -   Deployed to AWS Elastic Container Service (ECS) using Fargate launch type (serverless containers, eliminating server management).
    -   Traffic distributed by an AWS Application Load Balancer (ALB).
-   **Database:** AWS RDS for managed PostgreSQL.
-   **CI/CD (Continuous Integration/Continuous Deployment):** Implement automated pipelines (e.g., using GitHub Actions or AWS CodePipeline/CodeBuild) for testing, building, and deploying changes, ensuring rapid and reliable releases.

## Development Environment

### Prerequisites

-   **Git:** For version control.
-   **Node.js & npm/yarn:** For frontend development (React, Vite, Tailwind CSS).
-   **Python (3.9+):** For backend development (FastAPI).
-   **Docker & Docker Compose:** For running local database, Redis, and potentially local backend/frontend containers for consistent environments.
-   **Code Editor:** VS Code with recommended extensions (e.g., Python, Pylance, Prettier, ESLint, Docker, Tailwind CSS Intellisense).
-   **PostgreSQL Client:** `psql` command-line tool or a GUI client (e.g., DBeaver, PgAdmin).

### Setup Commands

```bash
1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd SG-KI-kveldstid # Or your project root directory
    ```
2.  **Frontend Setup:**
    ```bash
    cd frontend
    npm install
    # Ensure Tailwind CSS is configured as per Project Initialization section
    ```
3.  **Backend Setup:**
    ```bash
    cd backend
    python -m venv venv
    # Activate virtual environment:
    # On Windows: .\venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    pip install -r requirements.txt # Assuming requirements.txt is generated from pip freeze
    ```
4.  **Local Services (Database, etc. - via Docker Compose):**
    ```bash
    # From project root, assuming docker-compose.yml defines services like PostgreSQL, Redis
    docker compose up -d
    ```
5.  **Run Applications:**
    ```bash
    # In 'frontend' directory:
    npm run dev

    # In 'backend' directory (after activating venv):
    uvicorn app.main:app --reload
    ```
```

## Architecture Decision Records (ADRs)

-   **Format:** Lightweight Markdown files, stored in a dedicated `docs/adr/` directory.
-   **Content:** Each ADR will document a significant architectural decision, including:
    -   **Context:** The problem or challenge being addressed.
    -   **Decision:** The chosen solution.
    -   **Status:** (e.g., Proposed, Accepted, Superseded).
    -   **Consequences:** Positive and negative impacts of the decision.
    -   **Rationale:** The reasoning behind the decision, including alternatives considered.
-   **Reason:** ADRs provide a historical log of architectural choices, preventing "architectural amnesia" and aiding future maintainability and onboarding.

---

_Generated by BMAD Decision Architecture Workflow v1.0_
_Date: 2025-12-04_
_For: BIP_