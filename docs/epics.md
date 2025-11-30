# ibe160 - Epic Breakdown

**Author:** Mort1
**Date:** 2025-11-30
**Project Level:** (Inferred: Full product + architecture planning for greenfield projects (10-50+ stories typically) Customer-facing application)
**Target Scale:** (Not specified)

---

## Overview

This document provides the complete epic and story breakdown for ibe160, decomposing the requirements from the [PRD](./PRD.md) into implementable stories.

**Living Document Notice:** This is the initial version. It will be updated after UX Design and Architecture workflows add interaction and technical details to stories.

## Epic Summary

The project is broken down into the following two epics, each designed to deliver a distinct piece of user value.

*   **Epic 1: Foundation & Core Analysis Engine:** This epic focuses on setting up the web application and implementing the core analysis functionality. By the end of this epic, a user will be able to paste their CV and a job description and receive immediate, actionable feedback.
*   **Epic 2: Content Generation & Export:** Building on the analysis from Epic 1, this epic focuses on generating the tailored cover letter and providing the functionality to export all generated content, delivering the final tangible assets to the user.

---

## Functional Requirements Inventory

Here is the inventory of Functional Requirements (FRs) extracted from the Product Requirements Document:

*   **FR1: Paste CV Content:** As a user, I can paste my CV content (plain text) into the application.
*   **FR2: Paste Job Description:** As a user, I can paste a job description into the application.
*   **FR3: Generate Tailored Cover Letter:** As a user, I can get a tailored cover letter based on my CV and a job description.
*   **FR4: View Gap Analysis:** As a recent graduate, I can see a clear analysis of how my CV matches a job description.
*   **FR5: Receive CV Improvement Suggestions:** As a job seeker, I can receive suggestions for improving my CV bullet points.
*   **FR6: Export Generated Content:** As a user, I can export the generated cover letter and CV suggestions.

---

## FR Coverage Map

This map shows how the Functional Requirements (FRs) from the PRD are covered by the proposed epics.

*   **Epic 1: Foundation & Core Analysis Engine**
    *   **FR1:** Paste CV Content
    *   **FR2:** Paste Job Description
    *   **FR4:** View Gap Analysis
    *   **FR5:** Receive CV Improvement Suggestions
*   **Epic 2: Content Generation & Export**
    *   **FR3:** Generate Tailored Cover Letter
    *   **FR6:** Export Generated Content

---

## Epic 1: Foundation & Core Analysis Engine

**Goal:** This epic focuses on setting up the web application and implementing the core analysis functionality. By the end of this epic, a user will be able to paste their CV and a job description and receive immediate, actionable feedback.

### Story 1.1: Foundational Web Application Setup
*   **User Story:** As a developer, I want a basic project structure for a web application set up with necessary build tools and dependencies, so that I can start building the UI and features.
*   **Acceptance Criteria:**
    *   Given the project is initialized, When I run the development server, Then a blank page is served successfully on a local port.
    *   And the project includes a linter, a formatter, and a testing framework.
*   **Technical Notes:** Use Vite for project setup with a React/TypeScript template. Install `tailwindcss` and `shadcn/ui` for the design system.

### Story 1.2: Implement Two-Panel UX Layout
*   **User Story:** As a user, I want to see a two-panel layout with an input area on the left and a feedback area on the right, so that I have a clear and intuitive interface.
*   **Acceptance Criteria:**
    *   Given I land on the main page, When the page loads, Then I see a large text area on the left half of the screen and an empty panel on the right.
    *   And the layout is responsive, stacking vertically on mobile screens.
*   **Technical Notes:** Implement the layout using Flexbox or CSS Grid. Use the `CVInputPanel` custom component for the left panel.

### Story 1.3: CV & Job Description Input
*   **User Story:** As a user, I want to paste my CV and a job description into the application, so that the analysis can begin.
*   **Acceptance Criteria:**
    *   Given the two-panel layout, When I paste text into the CV input area, Then the application accepts the text.
    *   And there is a separate input area for the job description.
*   **Technical Notes:** For the MVP, we will have two `Textarea` components, one for the CV and one for the job description, to simplify the interaction. An "Analyze" button will trigger the analysis.

### Story 1.4: Implement Core Analysis Logic (Gap Analysis & Suggestions)
*   **User Story:** As a user, I want to click an "Analyze" button and see a gap analysis and CV improvement suggestions, so that I can understand how to improve my CV.
*   **Acceptance Criteria:**
    *   Given I have pasted my CV and a job description, When I click the "Analyze" button, Then the feedback panel populates with cards for "Gap Analysis" and "CV Improvement Suggestions".
    *   And the "Gap Analysis" card shows a list of skills matched, partially matched, and missing.
    *   And the "CV Improvement Suggestions" card shows at least one actionable suggestion.
*   **Technical Notes:** This involves creating a service that sends the CV and job description to an AI model (can be simulated initially). The results are then formatted and displayed in `AnalysisCard` components.

---

## Epic 2: Content Generation & Export

**Goal:** Building on the analysis from Epic 1, this epic focuses on generating the tailored cover letter and providing the functionality to export all generated content, delivering the final tangible assets to the user.

### Story 2.1: Generate Tailored Cover Letter
*   **User Story:** As a user, I want to receive a tailored cover letter based on the analysis of my CV and the job description, so that I have a strong starting point for my application.
*   **Acceptance Criteria:**
    *   Given the analysis from Epic 1 is complete, When I click a "Generate Cover Letter" button, Then a new card appears in the feedback panel containing a generated cover letter.
    *   And the cover letter incorporates skills from my CV that match the job description.
*   **Prerequisites:** Story 1.4
*   **Technical Notes:** This will extend the AI service to include a prompt for generating a cover letter based on the CV, job description, and the identified skill gap analysis.

### Story 2.2: Export All Generated Content
*   **User Story:** As a user, I want to export all the generated content (gap analysis, suggestions, cover letter) into a single file, so that I can easily use it in my application process.
*   **Acceptance Criteria:**
    *   Given the analysis and content generation is complete, When I click an "Export" button, Then a Markdown file is downloaded to my computer.
    *   And the file contains the Gap Analysis, CV Improvement Suggestions, and the generated Cover Letter, formatted with clear headings.
*   **Prerequisites:** Story 1.4, Story 2.1
*   **Technical Notes:** Implement a function that concatenates the content from the various feedback cards into a single string with Markdown formatting and triggers a file download in the browser.

---

## FR Coverage Matrix

This matrix validates that every Functional Requirement (FR) from the PRD is covered by one or more stories.

*   **FR1: Paste CV Content** → Epic 1, Story 1.3
*   **FR2: Paste Job Description** → Epic 1, Story 1.3
*   **FR3: Generate Tailored Cover Letter** → Epic 2, Story 2.1
*   **FR4: View Gap Analysis** → Epic 1, Story 1.4
*   **FR5: Receive CV Improvement Suggestions** → Epic 1, Story 1.4
*   **FR6: Export Generated Content** → Epic 2, Story 2.2

---

## Summary

The epic and story breakdown for the ibe160 MVP is now complete. The requirements from the PRD have been decomposed into two value-driven epics, which are further broken down into six implementable user stories. All functional requirements have been mapped, and the structure provides a clear path for incremental development.

---

_For implementation: Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown._

_This document will be updated after UX Design and Architecture workflows to incorporate interaction details and technical decisions._
