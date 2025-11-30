# Architecture

## Executive Summary

The project, **ibe160 (AI Career Development Assistant)**, is a focused MVP web application designed to analyze a user's CV against a job description, providing feedback, suggestions, and a tailored cover letter. The project consists of 6 core functional requirements, broken down into 2 epics and 6 user stories.

Key architectural drivers identified from the project documentation include:
*   **Performance:** A fast analysis loop (< 5 minutes) and a highly responsive frontend (LCP < 2.5s) are critical.
*   **Security:** The MVP is stateless, meaning no user data is persisted on the server, which simplifies the security model.
*   **Accessibility:** The application must meet WCAG 2.1 Level AA standards.
*   **User Experience:** The architecture must support a simple, two-panel, real-time feedback loop, implying a client-heavy SPA architecture.

## Starter Template Decision

We have chosen **Create Next App** as the foundational starter template for this project. This decision provides a robust and modern starting point, aligning with best practices for web application development.

**Key Benefits of Create Next App:**
*   **Official React Framework:** Next.js offers an opinionated yet flexible framework built on React, ideal for highly interactive web applications.
*   **TypeScript Support:** Ensures type safety and improves code quality and maintainability.
*   **Tailwind CSS Integration:** Seamlessly integrates with our chosen design system, `shadcn/ui`, for efficient and customizable styling.
*   **Optimized Performance:** Next.js provides built-in optimizations for faster page loads and improved user experience.

This starter template makes many foundational architectural decisions for us, allowing us to focus on the unique aspects of the AI Career Development Assistant.

## Project Initialization

The project will be initialized using the **Create Next App** starter template.

### Initialization Command

The first implementation story will be to execute the following command:

```bash
npx create-next-app@latest ibe160-app --typescript --tailwind --eslint --app
```

### Starter-Provided Architectural Decisions

By using this starter template, the following architectural decisions are established from the outset:

*   **Framework:** Next.js (version latest)
*   **Language:** TypeScript
*   **Styling:** Tailwind CSS (for seamless integration with `shadcn/ui`)
*   **Linting:** ESLint
*   **Routing:** Next.js App Router
*   **Build Tooling:** Next.js's optimized build system (based on Webpack/Turbopack)

## Decision Summary

| Category | Decision | Version | Affects Epics | Rationale |
| -------- | -------- | ------- | ------------- | --------- |
| Deployment | Vercel | Latest | All | Best integration with Next.js, easy deployment, automatic scaling, generous free tier. |
| AI Integration | Next.js API Routes for external AI API | N/A | Epic 1 | Securely call external AI service, keep API keys safe, centralize AI calls, simplify frontend. |
| API Pattern | REST | N/A | All | Simple, widely understood, and sufficient for MVP's communication needs. |
| Error Handling | Clear user-facing messages & internal logging | N/A | All | Provides good user experience and aids developer debugging without exposing sensitive info. |
| Testing | Unit, Integration, E2E tests | N/A | All | Comprehensive coverage for robust and reliable application development. |
| Logging | Console logging | N/A | All | Sufficient for MVP, simple to implement and manage. |
| Date/Time | Standard JavaScript Date | N/A | All | Simple and effective for MVP, can be extended with libraries if complexity grows. |
| API Response | Simple JSON (data/error) | N/A | All | Standard and easy to parse, good for RESTful APIs. |

## Project Structure

```
/
├── .next/                    # Next.js build output (automatically generated)
├── public/                   # Static assets (images, fonts, favicons)
├── src/                      # Application source code
│   ├── app/                  # Next.js App Router: Defines routes, layouts, and pages
│   │   ├── (auth)/           # Optional: Route group for authentication flows (future)
│   │   ├── api/              # Next.js API Routes - Our serverless backend for frontend
│   │   │   ├── ai/           # Module for AI service integration (e.g., /api/ai/analyze)
│   │   │   └── export/       # Module for export functionality (e.g., /api/export/markdown)
│   │   ├── dashboard/        # Main application dashboard/feedback display
│   │   ├── layout.tsx        # Root layout for the entire application
│   │   └── page.tsx          # Root page (e.g., CV input screen)
│   ├── components/           # Reusable UI components
│   │   ├── ui/               # shadcn/ui components (copied and potentially extended)
│   │   ├── custom/           # Our unique custom components (e.g., CVInputPanel, FeedbackDashboard, AnalysisCard)
│   │   └── common/           # Generic components shared across the app
│   ├── lib/                  # Utility functions, helpers, constants, service clients
│   │   ├── utils.ts          # General utility functions
│   │   ├── ai/               # AI service client logic, types, model interfaces
│   │   └── export/           # Export utility functions
│   ├── styles/               # Global styles and Tailwind CSS configuration
│   │   └── globals.css
│   └── types/                # TypeScript global type definitions, interfaces
├── .env.local                # Environment variables (local development)
├── .eslintrc.json            # ESLint configuration for code quality
├── .gitignore                # Git ignore rules
├── next.config.mjs           # Next.js framework configuration
├── package.json              # Project dependencies and scripts
├── pnpm-lock.yaml            # Package manager lock file
├── postcss.config.mjs        # PostCSS configuration (used by Tailwind)
├── README.md                 # Project overview and setup instructions
├── tailwind.config.ts        # Tailwind CSS specific configuration
├── tsconfig.json             # TypeScript compiler configuration
└── docs/                     # Project documentation (PRD, Epics, Architecture, UX Spec, Validation Reports)
    ├── architecture.md
    ├── epics.md
    ├── prd.md
    ├── ux-design-specification.md
    └── prd-validation-report-2025-11-30.md
```

## Epic to Architecture Mapping

*   **Epic 1: Foundation & Core Analysis Engine:** This epic will primarily involve setting up the core Next.js project, configuring styling and linting, and implementing the UI components within `src/components/`, `src/app/page.tsx`, and `src/app/api/ai/`. The AI service client logic will reside in `src/lib/ai/`.
*   **Epic 2: Content Generation & Export:** This epic will extend the API Routes with `src/app/api/export/` for handling content export, utilizing utility functions in `src/lib/export/`. The generated content will be displayed in `src/components/custom/FeedbackDashboard`.

## Technology Stack Details

### Core Technologies

*   **Frontend Framework:** Next.js (with React)
*   **Language:** TypeScript
*   **Styling:** Tailwind CSS + shadcn/ui
*   **Hosting:** Vercel
*   **AI Integration:** External AI API (via Next.js API Routes)

### Integration Points

*   **Frontend-to-Backend (Internal API):** The React components in the frontend will communicate with our Next.js API Routes (`/api/*`) using standard RESTful JSON over HTTP.
*   **Backend (API Routes)-to-External AI:** The Next.js API Routes within `src/app/api/ai/` will make direct calls to the chosen external AI API (e.g., OpenAI, Anthropic). This keeps API keys and complex AI logic encapsulated on the server-side.

## Implementation Patterns

These patterns ensure consistent implementation across all AI agents:

Cross-cutting concerns are decisions that affect multiple parts of the application and require consistent implementation to avoid conflicts and ensure maintainability.

*   **Error Handling:** A consistent strategy for user-facing and internal errors (clarity for users, logging for developers).
*   **Logging:** Basic console logging for MVP, extensible for production.
*   **API Response Format:** Simple JSON structure with `data` and `error` fields.
*   **Testing Strategy:** A comprehensive approach including Unit, Integration, and End-to-End tests.
*   **Date/Time Handling:** Standard JavaScript `Date` object for MVP.

## Consistency Rules

### Naming Conventions
*   **Files/Folders:** `kebab-case` (e.g., `my-component.tsx`, `my-feature/`).
*   **Components:** `PascalCase` (e.g., `MyComponent`).
*   **Functions/Variables:** `camelCase` (e.g., `myFunction`, `myVariable`).
*   **API Endpoints:** `kebab-case`, plural (e.g., `/api/users`, `/api/ai/analyze`).

### Code Organization
*   **Next.js App Router:** Follow official App Router conventions for routes (`src/app/`) and API Routes (`src/app/api/`).
*   **Components:** `src/components/ui` for `shadcn/ui`, `src/components/custom` for project-specific components, `src/components/common` for generic reusable components.
*   **Utilities:** `src/lib/` for client-side and server-side utilities.
*   **Types:** `src/types/` for global TypeScript type definitions.

### Error Handling
*   **User-Facing:** Clear, non-technical messages in "toast" notifications or inline.
*   **Internal:** Detailed server-side logging for debugging.

### Logging Strategy
*   Basic `console.log` and `console.error` for MVP.

## Data Architecture

For the MVP, there is no application-specific data persistence. Data is processed in-memory during a user session. If user accounts or persistent CV storage are introduced in future phases, a relational database (e.g., PostgreSQL) will be considered.

## API Contracts

API contracts will be implicit for the MVP, following REST principles. Request bodies will be JSON containing CV text and job description. Responses will be JSON with a `data` field for successful analysis results/generated content or an `error` field for error details.

## Security Architecture

As the MVP is stateless and does not store user data or require authentication, the primary security focus is on protecting the external AI API key (stored securely as an environment variable on Vercel) and ensuring Next.js API Routes are not vulnerable to common web exploits (e.g., input sanitization).

## Performance Considerations

Performance is critical for a smooth user experience, especially given the AI analysis component. Strategies include:

*   **Next.js Optimizations:** Leveraging Next.js's built-in features like image optimization, code splitting, and static asset serving.
*   **Serverless Functions:** Next.js API Routes will run as serverless functions, optimized for fast cold starts for AI invocations.
*   **Frontend Rendering:** Efficient React component rendering and state management to ensure a responsive UI and meet LCP targets.

## Deployment Architecture

The application will be deployed to **Vercel**, leveraging its tight integration with Next.js.

*   **Platform:** Vercel
*   **Benefits:**
    *   Automatic deployments from Git (GitHub, GitLab, Bitbucket).
    *   Serverless functions for Next.js API Routes, providing automatic scaling.
    *   Global CDN for static assets, ensuring fast content delivery worldwide.
    *   Simplified configuration and maintenance.
*   **CI/CD:** Continuous Deployment (CD) will be configured to automatically deploy on pushes to the main branch.

## Development Environment

### Prerequisites

*   **Node.js:** Active LTS version (e.g., v18.x or v20.x).
*   **pnpm:** Recommended package manager (or npm/yarn).
*   **Git:** Version control system.

### Setup Commands

```bash
# 1. Clone the repository
git clone [YOUR_REPOSITORY_URL] ibe160-app

# 2. Navigate to the project directory
cd ibe160-app

# 3. Install dependencies
pnpm install # or npm install / yarn install

# 4. Start the development server
pnpm dev # or npm run dev / yarn dev
```

## Architecture Decision Records (ADRs)

The following key architectural decisions have been made, forming the foundation of the project's technical direction:

1.  **Deployment Target (Vercel):**
    *   **Decision:** Vercel for hosting the Next.js application.
    *   **Rationale:** Best integration with Next.js, ease of deployment, automatic scaling, and generous free tier. Affects all epics.
2.  **AI Service Integration (Next.js API Routes):**
    *   **Decision:** Next.js API Routes to securely call external AI APIs.
    *   **Rationale:** Secures API keys, centralizes AI calls, simplifies frontend. Affects Epic 1.
3.  **API Pattern (REST):**
    *   **Decision:** RESTful API pattern for internal frontend-to-backend communication.
    *   **Rationale:** Simple, widely understood, sufficient for MVP. Affects all epics.
4.  **Error Handling (Clear user-facing messages & internal logging):**
    *   **Decision:** Consistent strategy for user-facing errors (clear messages) and internal errors (logging).
    *   **Rationale:** Good UX, aids debugging, protects sensitive info. Affects all epics.
5.  **Testing Strategy (Unit, Integration, E2E tests):**
    *   **Decision:** Comprehensive testing strategy including Unit, Integration, and End-to-End tests.
    *   **Rationale:** Ensures robust and reliable application development. Affects all epics.
6.  **Logging (Console logging):**
    *   **Decision:** Basic console logging for MVP.
    *   **Rationale:** Sufficient for MVP, simple to implement. Affects all epics.
7.  **Date/Time Handling (Standard JavaScript Date):**
    *   **Decision:** Standard JavaScript `Date` object for date/time operations.
    *   **Rationale:** Simple and effective for MVP. Affects all epics.
8.  **API Response Format (Simple JSON):**
    *   **Decision:** Simple JSON structure with `data` and `error` fields for API responses.
    *   **Rationale:** Standard and easy to parse, good for RESTful APIs. Affects all epics.

---

_Generated by BMAD Decision Architecture Workflow v1.0_
_Date: 2025-11-30_
_For: Mort1_