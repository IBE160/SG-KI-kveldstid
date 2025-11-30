# ibe160 - Epic Breakdown

**Author:** Mort1
**Date:** 2025-11-25
**Project Level:** (Inferred: Full product + architecture planning for greenfield projects (10-50+ stories typically) Customer-facing application)
**Target Scale:** (Not specified)

---

## Overview

This document provides the complete epic and story breakdown for ibe160, decomposing the requirements from the [PRD](./PRD.md) into implementable stories.

**Living Document Notice:** This is the initial version. It will be updated after UX Design and Architecture workflows add interaction and technical details to stories.

**Epic 1: User Authentication & Profile Management**
Goal: Enable users to securely manage their identity and personal data within the application.

**Epic 2: AI Mentor & Planning Engine**
Goal: Provide users with personalized career guidance and planning capabilities.

---

## Functional Requirements Inventory

- FR1: User registration (email/password)
- FR2: User login/logout
- FR3: Storage of user's CV
- FR4: Editing and updating of CV
- FR5: Conversational interface for career goal setting
- FR6: Generation of personalized career development plans
- FR7: Progress tracking and plan adjustments
- FR8: A database to store user accounts, profiles, and career plans

---

## FR Coverage Map

- FR1: User registration (email/password) → Epic 1
- FR2: User login/logout → Epic 1
- FR3: Storage of user's CV → Epic 1
- FR4: Editing and updating of CV → Epic 1
- FR5: Conversational interface for career goal setting → Epic 2
- FR6: Generation of personalized career development plans → Epic 2
  - FR7: Progress tracking and plan adjustments → Epic 2
  - FR8: A database to store user accounts, profiles, and career plans → Epic 1, Epic 2

---

## Epic 1: User Authentication & Profile Management

Goal: Enable users to securely manage their identity and personal data within the application.

### Story 1.1: User Registration with Email and Password

As a new user,
I want to create an account with my email and a secure password,
So that I can access the AI Career Development Assistant.

**Acceptance Criteria:**

**Given** I am on the registration page,
**When** I enter a valid email and a password (8+ chars, 1 uppercase, 1 number, 1 special char) and confirm it,
**Then** my account is created and I am logged in.

**And** Given I am on the registration page, When I enter an invalid email format or a weak password, Then I receive an appropriate error message.

**Prerequisites:** None.

**Technical Notes:** Implement email validation (RFC 5322). Password hashing (e.g., bcrypt). Store user credentials securely in the database.

### Story 1.2: User Login and Session Management

As a registered user,
I want to log in with my credentials and have my session maintained,
So that I can continue using the assistant without re-authenticating.

**Acceptance Criteria:**

**Given** I have an account,
**When** I enter my correct email and password on the login page,
**Then** I am logged in and my session persists.

**And** Given I am logged in, When I navigate through the application, Then my session remains active until I explicitly log out or the session expires.
**And** Given I enter incorrect credentials, Then I receive an error message "Invalid email or password."

**Prerequisites:** Story 1.1 (User Registration).

**Technical Notes:** Implement JWT-based authentication. Use refresh tokens for session persistence. Secure token storage (e.g., HTTP-only cookies).

### Story 1.3: User Profile for CV Storage and Editing

As a logged-in user,
I want to store my CV securely in my profile and be able to view and edit it,
So that I don't have to re-upload it for every application.

**Acceptance Criteria:**

**Given** I am logged in,
**When** I navigate to my profile,
**Then** I can see an option to upload/paste my CV.

**And** Given my CV is stored, When I view my profile, Then I can see my CV content and an option to edit it.
**And** Given I edit my CV and save changes, Then the updated CV is stored in my profile.

**Prerequisites:** Story 1.2 (User Login).

**Technical Notes:** Implement secure storage for user CV data in the database. Provide a rich text editor or markdown editor for CV content. Versioning of CVs (stretch goal for future).

---

## Epic 2: AI Mentor & Planning Engine

Goal: Provide users with personalized career guidance and planning capabilities.

### Story 2.1: Conversational Interface for Career Goal Setting

As a user,
I want to interact with the AI Mentor through a conversational interface to define my career goals,
So that the mentor can understand my aspirations.

**Acceptance Criteria:**

**Given** I activate "AI Mentor Mode",
**When** I state my career goals in natural language,
**Then** the AI Mentor asks clarifying questions to refine my goals.

**And** Given the AI Mentor asks questions, When I provide responses, Then the AI Mentor updates its understanding of my goals.

**Prerequisites:** Story 1.2 (User Login).

**Technical Notes:** Integrate with an LLM for conversational AI. Implement a state management system for the conversation flow. Store conversation history for context.

### Story 2.2: Personalized Career Development Plan Generation

As a user,
I want the AI Mentor to generate a personalized step-by-step career development plan based on my CV and stated goals,
So that I have a clear roadmap for my professional growth.

**Acceptance Criteria:**

**Given** I have defined my career goals and provided my CV,
**When** I request a career development plan,
**Then** the AI Mentor generates a plan with recommended skills, courses, and job types.

**And** Given the plan is generated, When I review it, Then it clearly reflects my CV content and stated goals.

**Prerequisites:** Story 1.3 (User Profile for CV Storage), Story 2.1 (Conversational Interface).

**Technical Notes:** Develop a logic layer to combine CV analysis, goal understanding, and LLM output. Store generated plans in the database.

### Story 2.3: Progress Tracking and Plan Adjustment

As a user,
I want to track my progress against the AI Mentor's plan and have the plan adjust to my achievements,
So that I stay motivated and on track.

**Acceptance Criteria:**

**Given** I have a career development plan,
**When** I mark a step as complete,
**Then** my progress is updated in the application.

**And** Given I make significant progress or changes to my goals, When I interact with the AI Mentor, Then the plan is adjusted accordingly.

**Prerequisites:** Story 2.2 (Personalized Career Development Plan Generation).

**Technical Notes:** Implement a UI for progress tracking. Develop logic for plan adjustment based on user input and progress.

---

## FR Coverage Matrix

- FR1: User registration (email/password) → Epic 1, Story 1.1
- FR2: User login/logout → Epic 1, Story 1.2
- FR3: Storage of user's CV → Epic 1, Story 1.3
- FR4: Editing and updating of CV → Epic 1, Story 1.3
- FR5: Conversational interface for career goal setting → Epic 2, Story 2.1
- FR6: Generation of personalized career development plans → Epic 2, Story 2.2
- FR7: Progress tracking and plan adjustments → Epic 2, Story 2.3
- FR8: A database to store user accounts, profiles, and career plans → Epic 1 (for user/profile), Epic 2 (for career plans)

---

## Summary

**✅ Epic Breakdown Complete**

**Created:** epics.md with epic and story breakdown

**FR Coverage:** All functional requirements from PRD mapped to stories

**Context Incorporated:**

- ✅ PRD requirements
  **Next:** Run UX Design (if UI) or Architecture workflow
  **Note:** Epics will be enhanced with additional context later

---

_For implementation: Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown._

_This document will be updated after UX Design and Architecture workflows to incorporate interaction details and technical decisions._
