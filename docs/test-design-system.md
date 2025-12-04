# System-Level Test Design

**Date:** 2025-12-04
**Author:** BIP
**Status:** Approved

## Executive Summary

**Scope:** Full system-level test design for the AI CV & Job Application Assistant.

**Risk Summary:**

- Total risks identified: 4 Architecturally Significant Requirements (ASRs)
- High-priority risks (score ≥6): 3 (Performance, Security, Scalability)
- Critical categories: Performance, Security

**Coverage Summary:**

- P0 scenarios: 35 tests (70 hours)
- P1 scenarios: 95 tests (95 hours)
- P2/P3 scenarios: 370 tests (185 hours)
- **Total effort**: 500 tests (~350 hours / ~44 days)

## Testability Assessment

- Controllability: PASS - APIs and managed services (S3, OpenAI) allow for data seeding and mocking of external dependencies, enabling controlled testing environments. User state can be manipulated via API calls.
- Observability: PASS - Structured logging with AWS CloudWatch Logs, standardized API error responses, and React error boundaries provide comprehensive visibility into system behavior and issues.
- Reliability: PASS - The architecture's focus on elastic scaling, high availability, and robust error handling patterns supports a strong reliability testing approach, including graceful degradation and recovery.

## Architecturally Significant Requirements (ASRs)

These are key quality attributes derived from PRD NFRs and architectural decisions, scored by Probability x Impact.

*   **Performance (Score 9)**
    *   **Description:** User Interaction Latency (<500ms), AI Processing Time (<5 min), Frontend Load Time. High probability (3) of impacting user experience if not met, critical impact (3) on product usability and retention.
    *   **Category:** PERF
*   **Security (Score 9)**
    *   **Description:** Data Protection (encryption in transit/at rest), GDPR Compliance, API Security (OAuth2/OpenID Connect), Vulnerability Management. High probability (3) of exposure, critical impact (3) due to personal data handling and legal/reputational consequences.
    *   **Category:** SEC
*   **Scalability (Score 6)**
    *   **Description:** High Availability (99.9% uptime), Elastic Scaling for backend/AI. Possible probability (2) of issues with growth, high impact (3) on service availability and user satisfaction.
    *   **Category:** TECH/OPS
*   **Accessibility (Score 4)**
    *   **Description:** WCAG 2.1 Level AA compliance. Possible probability (2) of oversight, medium impact (2) on inclusivity and potential for rework.
    *   **Category:** BUS/TECH

## Test Levels Strategy

A layered testing approach balancing speed, confidence, and coverage.

-   **Unit Tests:** ~60%
    *   **Rationale:** Fastest feedback. Focus on isolated business logic, algorithms (e.g., CV parsing helpers, scoring calculations), utility functions, and complex data transformations.
    *   **Tools:** Jest/Vitest (Frontend - JS/TS), Pytest (Backend - Python).
-   **Integration Tests:** ~30%
    *   **Rationale:** Validate interactions between components and external services. Cover API endpoint contracts, database operations (ORM), and backend-to-OpenAI API interactions.
    *   **Tools:** Playwright `request` API (for backend API tests), Pytest with mock services/DB.
-   **End-to-End (E2E) Tests:** ~10%
    *   **Rationale:** Highest confidence for critical user journeys. Validate UI interactions, cross-system workflows (e.g., full CV upload to cover letter export), and core business flows in a production-like environment.
    *   **Tools:** Playwright (for web UI automation).

## NFR Testing Approach

Specific strategies and tools for validating Non-Functional Requirements.

-   **Security**:
    *   **Approach:** Playwright E2E tests to validate authentication/authorization flows (e.g., unauthorized access attempts, RBAC enforcement), secure handling of sensitive data (no logging/exposure), and input sanitization (SQL injection/XSS attempts). Supplement with automated static application security testing (SAST) in CI and manual penetration testing for critical areas.
    *   **Tools:** Playwright, npm audit (frontend dependencies), SAST tools, OWASP ZAP (for DAST).
-   **Performance**:
    *   **Approach:** Conduct load, stress, spike, and endurance tests using k6 to validate backend API performance, database throughput, and AI service latency under various load conditions. Monitor frontend perceived performance using Lighthouse/Core Web Vitals integrated with Playwright.
    *   **Tools:** k6, Playwright (for Lighthouse integration), AWS CloudWatch (for resource monitoring).
-   **Reliability**:
    *   **Approach:** Implement Playwright E2E tests to verify graceful degradation (e.g., when backend APIs return 500s or network disconnects), retry mechanisms for transient failures, and health check endpoint functionality. Basic chaos engineering principles can be applied (e.g., simulate service outages).
    *   **Tools:** Playwright, API testing frameworks, mock servers, AWS CloudWatch (for health metrics).
-   **Maintainability**:
    *   **Approach:** Integrate code quality tools into CI pipelines to enforce test coverage thresholds (e.g., >80% for critical paths), detect code duplication (jscpd), and scan for software vulnerabilities (npm audit). Use Playwright E2E tests to validate observability (e.g., verify structured logs are generated, error reporting services are invoked).
    *   **Tools:** GitHub Actions (or similar CI), jscpd, npm audit, Playwright (for observability validation).

## Test Environment Requirements

-   **Development:** Local environment with Docker Compose for local PostgreSQL (with `pgvector`) and potentially mock APIs for OpenAI/S3. Frontend and Backend running locally.
-   **CI/CD:** Ephemeral environments for each pull request, closely mirroring production setup, including access to a test PostgreSQL instance and mocked/sandbox OpenAI/AWS S3 services.
-   **Staging:** Production-like environment for E2E tests and NFR validation, with real (or highly realistic) external services for comprehensive testing.

## Testability Concerns (if any)

None identified. The proposed architecture (React/FastAPI, containerized, cloud-native) coupled with a strong emphasis on observability and API-first design promotes excellent testability.

## Recommendations for Sprint 0

-   Set up foundational test frameworks: Jest/Vitest for frontend unit, Pytest for backend unit, Playwright for E2E and API integration tests.
-   Configure CI/CD pipelines to run unit, integration, and E2E smoke tests on every commit.
-   Establish test data management strategy (factories, fixtures, API seeding).
-   Implement initial structured logging and error reporting to CloudWatch.
-   Define clear test-level ownership for each epic's stories.

---

## Quality Gate Criteria

### Pass/Fail Thresholds

-   **P0 pass rate**: 100% (no exceptions)
-   **P1 pass rate**: ≥95% (waivers required for failures)
-   **P2/P3 pass rate**: ≥90% (informational)
-   **High-risk mitigations**: 100% complete or approved waivers

### Coverage Targets

-   **Critical paths**: ≥80%
-   **Security scenarios**: 100%
-   **Business logic**: ≥70%
-   **Edge cases**: ≥50%

### Non-Negotiable Requirements

-   All P0 tests pass
-   No high-risk (score ≥6) items unmitigated
-   Security tests (SEC category) pass 100%
-   Performance targets met (PERF category)

---

## Next Steps

1.  Review risk assessment with team
2.  Prioritize mitigation for high-risk items (score ≥6)
3.  Run `atdd` workflow to generate failing tests for P0 scenarios
4.  Allocate resources per effort estimates
5.  Set up test data factories and fixtures
