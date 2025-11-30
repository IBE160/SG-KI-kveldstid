# Project Brief: AI Career Development Assistant

**Date:** November 15, 2025

## 1. Overview

This document outlines a project to create a comprehensive AI Career Development Assistant. The project merges the practical, application-focused features of an AI CV & Job Application Assistant with the long-term, strategic guidance of an AI Mentor Mode.

The goal is to create a holistic tool that helps users not only with immediate application needs but also supports their continuous professional growth.

## 2. Background & Purpose
### Background

Students and professionals often struggle to connect their skills and experiences to concrete career opportunities.

Common issues include:

* Generic job applications failing to pass ATS filters
* Weak alignment between skills and job-market demand
* Lack of structured, data-driven career planning

The project addresses both tactical needs (job applications) and strategic needs (career development).

### Purpose

To create a web-based AI assistant that empowers users to:

* Craft highly tailored and effective job applications
* Understand the value of their skills in the current job market
* Receive personalized guidance for long-term career growth

## 3. Target Users

**Primary Users:**
Students and recent graduates applying for internships or entry-level positions.

**Secondary Users:**
Professionals seeking to upskill, transition careers, or strategically plan their professional development.

## 4. Core Functionality

The assistant includes two major modes:

* **Application Mode (MVP)**
* **AI Mentor Mode (Integrated Advanced Features)**

### 4.1. Application Mode (MVP)
#### CV & Job Ad Analysis

* User uploads CV (PDF/DOCX/TXT) and pastes a job advertisement.
* System extracts structured text, skills, and job requirements.

#### Gap Analysis & Optimization

Semantic matching detects:

* Matched skills
* Partial matches
* Missing skills
* Provides ATS optimization insights (keyword density, action verbs, formatting).

#### Content Generation

* Generates a tailored cover letter.
* Suggests optimized CV bullet points aligned with the job description.

#### Export

* Allows users to export generated content to Markdown.

### 4.2. AI Mentor Mode (Integrated Features)
#### Skill-to-Job Mapping

* Analyzes existing and acquired skills.
* Matches users to in-demand job roles, salary expectations, and career paths.
* Generates a skill synergy score showing how new skills complement existing ones.

#### Project-to-Portfolio Guidance

* Helps users frame academic, hobby, or work projects in CV/portfolio.
* Generates talking points for interviews.

#### Career Storytelling Assistance

* Helps users build a consistent and compelling professional narrative.

#### Micro-learning & Just-in-Time Advice

* Provides targeted suggestions, such as resources, articles, or reminders.

## 5. Technical Architecture

* **Frontend:** React + Tailwind CSS
* **Backend:** FastAPI (Python)
* **AI Components:** OpenAI API (or similar) for embeddings and text generation
* **Document Parsing:** Unstructured.io or PyMuPDF
* **Database:** Stateless for MVP (all processing in-session)

## 6. Success Criteria
### Application Mode

* Cover letters must address at least 80% of required job qualifications.
* At least 95% of generated statements must be verifiable from the user’s CV.
* Improves ATS score by ≥15 percentage points.

### Mentor Mode

* Provides accurate and actionable career path suggestions.
* Maps user projects to portfolio-ready descriptions.

### General

* End-to-end generation time under 5 minutes.

## 7. Out of Scope (MVP)

* Visual CV design/templates
* Direct integrations with job boards or LinkedIn
* Salary negotiation tools
* Cloud persistence (stateless MVP)
* Multi-language support (English only)

## 8. Mobile Strategy

To enhance accessibility, the web app will be provided on mobile without rewriting the codebase.

### Recommended Approach
**Progressive Web App (PWA) — Preferred**

* Low overhead, cross-platform
* Offline capabilities via service worker
* Installable from mobile browser

### Hybrid App (Fallback)

* Use Capacitor or Cordova to wrap the web app if app store presence is required.

### User Experience Enhancements

* Mobile-first responsive layout
* Native splash screen + loading indicators
* Push notifications for "Always-On Mentor" features
