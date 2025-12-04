# Brainstorming Session Results

**Session Date:** 2025-12-04
**Facilitator:** Business Analyst Mary
**Participant:** BIP

## Session Start
Chosen techniques: Five Whys, Assumption Reversal, What If Scenarios. Approach: AI-Recommended Techniques.

## Executive Summary

**Topic:** Problems students face with applications and potential AI solutions

**Session Goals:** Brainstorm the core problems students face when applying for internships and entry-level jobs, and solution ideas for the 'AI CV & Job Application Assistant' described in @proposal.md.

**Techniques Used:** Five Whys, Assumption Reversal, What If Scenarios

**Total Ideas Generated:** 5

### Key Themes Identified:

*   Personalization and tailoring of applications for specific roles.
*   Overcoming Applicant Tracking System (ATS) limitations and optimizing for automated screening.
*   Bridging the knowledge gap between student skills/experience and job requirements.
*   Providing automated guidance and actionable feedback for students.

## Technique Sessions

**Five Whys Technique - Exploring Problems and AI Solutions:**

**Core Problem:** Students often submit generic CVs and cover letters that fail to pass Applicant Tracking Systems (ATS) and don't address key job requirements.

**Underlying Reasons (initial exploration):**
*   Students may not know how to effectively tailor their applications.
*   They might not be fully aware of how Applicant Tracking Systems (ATS) work.
*   Lack of understanding of specific job requirements.
*   Time constraints.

**AI Solution Ideas for the "AI CV & Job Application Assistant":**

1.  **Automated Job Ad Analysis:** Parses job descriptions to extract keywords, skills, and qualifications.
2.  **CV Gap Analysis & Tailoring Suggestions:** Compares job requirements to a student's CV, highlighting gaps and suggesting rewrites.
3.  **Real-time ATS Score/Preview:** Provides an estimated ATS score for optimization feedback.
4.  **Interactive Cover Letter Builder:** Guides students through creating tailored cover letters.

**Prioritized Solutions:**
*   **#1 Priority: Automated Job Ad Analysis** (Foundational for understanding job requirements)
*   **#2 Priority: CV Gap Analysis & Tailoring Suggestions** (Core value for addressing generic applications and ATS issues)

## Idea Categorization

### Immediate Opportunities

_Ideas ready to implement now_

*   **Automated Job Ad Analysis:** Parses job descriptions to extract keywords, skills, and qualifications.
*   **CV Gap Analysis & Tailoring Suggestions:** Compares job requirements to a student's CV, highlighting gaps and suggesting rewrites.

### Future Innovations

_Ideas requiring development/research_

*   **Real-time ATS Score/Preview:** Provides an estimated ATS score for optimization feedback.
*   **Interactive Cover Letter Builder:** Guides students through creating tailored cover letters.

### Moonshots

_Ambitious, transformative concepts_

*   **AI Auto-Application:** AI automatically applies to jobs based on user profile and preferences, handling all tailoring and even interview scheduling.

### Insights and Learnings

_Key realizations from the session_

*   The core problem for students stems from a lack of specific knowledge and efficient tools to effectively tailor their applications for specific roles, especially when facing automated screening systems like ATS.
*   AI's primary strength in this domain lies in its ability to quickly process and analyze large volumes of textual data (job descriptions, CVs) to identify critical patterns, keywords, and gaps that would be time-consuming or difficult for a human.
*   The AI assistant should not merely generate content but also serve as an educational tool, explaining *why* certain tailoring suggestions are made, thereby empowering students to understand the underlying principles of effective job applications.
*   An interactive approach, rather than a fully automated one, would likely yield better results by keeping the user engaged and ensuring the output accurately reflects their experiences.

## Action Planning

### Top 3 Priority Ideas

#### #1 Priority: Automated Job Ad Analysis

- Rationale: This is the foundational step. Accurately extracting requirements from job ads is critical for all subsequent tailored assistance, directly addressing student inability to decipher job needs.
- Next steps: Research job ad parsing libraries (e.g., Unstructured.io, PyMuPDF, custom regex/NLP). Define data model for extracted requirements (skills, experience, keywords). Develop API endpoint for job ad submission and parsing.
- Resources needed: Python/FastAPI backend developer, NLP expertise.
- Effort/Complexity: Medium

#### #2 Priority: CV Gap Analysis & Tailoring Suggestions

- Rationale: This feature directly tackles the problem of generic CVs and ATS failures by providing concrete, actionable feedback. It leverages the output of job ad analysis to create personalized recommendations.
- Next steps: Develop a semantic matching algorithm (e.g., using OpenAI text embeddings). Design rules for identifying gaps and suggesting rewrites. Implement a feedback loop for user acceptance of suggestions.
- Resources needed: AI/ML engineer (for embeddings/matching), Python/FastAPI developer.
- Effort/Complexity: High

#### #3 Priority: Real-time ATS Score/Preview

- Rationale: Provides immediate, tangible feedback to students on their application's ATS compatibility, demystifying the process and empowering them to optimize before submission.
- Next steps: Define ATS scoring metrics (keyword density, action verbs, quantification rate). Integrate with CV parsing and gap analysis results. Design UI element for displaying the score and detailed breakdown.
- Resources needed: Frontend (React) developer, Backend (Python/FastAPI) developer.
- Effort/Complexity: Medium

## Reflection and Follow-up

### What Worked Well

*   Rapid identification of core problems and generation of relevant AI solution ideas.
*   Effective prioritization of foundational features, providing a clear roadmap.
*   The use of YOLO mode was efficient for auto-completing the documentation.

### Areas for Further Exploration

*   Detailed technical specifications for job ad parsing and semantic matching algorithms.
*   Comprehensive user experience (UX) design for how feedback and suggestions are presented to the student.
*   Exploration of potential integration points with external platforms (e.g., LinkedIn profiles, university career portals).

### Recommended Follow-up Techniques

*   **User Story Mapping:** To collaboratively define features from the user's perspective for the prioritized solutions.
*   **Impact/Effort Matrix:** For a more refined prioritization of features and tasks identified.

### Questions That Emerged

*   How to effectively handle and accurately parse diverse CV/resume formats (PDF, DOCX, TXT) and job ad structures?
*   What is the acceptable latency for providing real-time feedback and suggestions to the user?
*   How can we ensure that AI-generated suggestions enhance, rather than diminish, the student's unique voice and personal brand?

### Next Session Planning

- **Suggested topics:** Technical deep dive into job ad parsing and NLP for semantic matching; User experience (UX) flow for the AI assistant, particularly for presenting feedback.
- **Recommended timeframe:** Within the next week.
- **Preparation needed:** Review `proposal.md` and this brainstorming session report.

---

_Session facilitated using the BMAD CIS brainstorming framework_
