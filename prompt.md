Case -- Ai Cv & Job Application Assistant (student‑focused, Aligned To
Brief) -- En

**\## Case Title**

AI CV & Job Application Assistant (Student‑Focused)

**\## Background**

Students often apply to internships and entry‑level roles with generic
applications that fail ATS filters and do not explicitly address
must‑have requirements. A practical assistant should help them tailor
content, surface missing qualifications, and demonstrate how AI is used
in modern recruiting workflows.

**\## Purpose**

Build a web application that takes a student's CV and a specific job ad
and produces:

\- a tailored cover letter in the requested tone/language,

\- CV improvement suggestions,

\- a clear gap analysis (missing and partially matched qualifications),
and

\- simple ATS optimization guidance.

**\## Target Users**

Primary: Students and recent graduates (internships and entry‑level
jobs) Secondary: Other job seekers and career advisors (nice‑to‑have
support)

**\## Core Functionality**

**\### Must Have (MVP)**

**\#### Input & Parsing**

\- Upload CV (PDF/DOCX/TXT) → extract sections, bullets, dates, skills
into JSON

\- Paste job ad → extract role, must‑have/nice‑to‑have,
responsibilities, keywords

\- Manual keywords (optional input): user‑provided terms to emphasize

\- Previous applications (optional input): short text samples to reuse
preferred arguments/style

\- Tone/style & language selector (EN/NO)

**\#### Analysis**

\- Semantic matching (embeddings) of requirements ↔ CV content

\- Gap analysis (match / partial / missing); evidence pointers back to
CV lines

\- Simple ATS checks (keyword coverage, formatting hints, action verbs,
quantification)

**\#### Generation**

\- Tailored cover letter (low‑temperature, no‑fabrication)

\- CV bullet rewrites (STAR, action verbs, numbers)

**\#### Output**

\- Letter draft + CV suggestions + gap table + ATS tips

\- Export to DOCX/PDF/MD

**\### Nice to Have (Optional Extensions)**

\- Recruiter Panel (multi‑agent) for explainable sub‑scores (Hiring
Manager, Recruiter, Specialist, Culture)

\- Interview Question Generator driven by panel concerns and must‑have
gaps

\- Bias Auditor that flags gendered/age‑coded/ableist/cultural phrasing
and proposes neutral alternatives

\- Tone mimicking from 2--3 sample texts; ATS simulator with traffic
lights; multi‑ad comparison

**\## Data Requirements**

\- User (optional in MVP): name, email, language/tone, consents

\- CV: raw text, sections, bullets, extracted skills/entities, evidence
IDs

\- Job Ad: role, company/location, must‑have/nice‑to‑have,
responsibilities, keywords

\- Manual Keywords (optional): list of user‑entered terms to prioritize

\- Previous Applications (optional): short snippets for style/argument
reuse

\- Match Reports: similarity scores, gap list, ATS score, evidence
mapping

\- Generated Artifacts: letter drafts, rewritten bullets, export
metadata

**\## Decision Points**

\- Degree of rewriting vs. suggestions only

\- Output formats (DOCX/MD/PDF) and template styles

\- Language/style level (formal, enthusiastic, concise; EN/NO)

**\## Technical Constraints**

\- Security/Authentication: If any data is stored, it must be encrypted;
access behind login

\- Privacy: MVP runs locally with no persistence; if storage is enabled,
add auto‑deletion and explicit consent

\- Deterministic generation for letters/rewrites; claim‑to‑evidence
validation to prevent fabrication

\- Accessible, responsive UI; BMAD workflow (plan → develop → QA →
flatten)

**\## Success Criteria**

\- Coverage ≥ 80% of must‑have requirements addressed in the letter

\- Precision ≥ 95% of claims traceable to CV evidence

\- ATS +15 pp vs. non‑tailored baseline

\- Time‑to‑result ≤ 5 minutes for the full flow (upload → analyze →
generate → export)

**\## User Stories**

\- As a student, I upload my CV and paste a job ad to receive a tailored
cover letter that addresses must‑have requirements.

\- As a student, I want a gap table that shows what I meet, partially
meet, or miss, so I can adjust my CV accordingly.

\- As a student, I want suggestions that rewrite my CV bullets using
action verbs and numbers, so my CV becomes more ATS‑friendly.

\- (Optional) As a student, I want panel‑based feedback, interview
questions, and a bias check to prepare better and avoid exclusionary
language.
