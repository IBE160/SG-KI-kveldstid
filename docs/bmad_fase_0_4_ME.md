# 📘 BMAD Kompendium – Fase 0–4  
## AI CV & Job Application Assistant

Dette kompendiet beskriver hele BMAD-prosessen fra Fase 0 til Fase 4 for utviklingen av **AI CV & Job Application Assistant (Student-Focused)**.  
Alle steg har forklaringer og kommandoer som kan limes direkte inn i VS Code.

---

# 🟦 FASE 0 – INITIERING OG FORSTÅELSE

## 0.1 – Initialiser workflow
### Hvorfor?
Starter BMAD-prosessen og oppretter workflow-statusen.

### Kommando
```
/run-agent-task analyst *workflow-init
```

---

## 0.2 – Brainstorming

### 0.2.1 – Problem & løsning
```
/run-agent-task analyst *brainstorm "Brainstorm the core problems students face when applying for internships and entry-level jobs, and solution ideas for the AI CV & Job Application Assistant described in @proposal.md."
```

### 0.2.2 – Brukerflyt og edge cases
```
/run-agent-task analyst *brainstorm "Map the ideal and non-ideal user flows for the AI CV & Job Application Assistant, including edge cases such as poor CV formatting, incomplete job ads, parsing failures and language mismatch."
```

### 0.2.3 – Suksessdefinisjon
```
/run-agent-task analyst *brainstorm "Define what success looks like for a student using the AI CV & Job Application Assistant."
```

---

## 0.3 – Teknisk research
```
/run-agent-task analyst *research "Recommend Python, FastAPI, React, Tailwind and document parsing tools for the AI CV Assistant."
```

---

## 0.4 – Product Brief
```
/run-agent-task analyst *product-brief "Create a product brief based on brainstorming, technical research and proposal.md."
```

---

# 🟩 FASE 1 – PLANLEGGING (PRD + UX)

## 1.1 – PRD
```
/run-agent-task pm *prd "Create a PRD for the AI CV & Job Application Assistant based on product-brief.md and proposal.md."
```

## 1.2 – Valider PRD
```
/run-agent-task pm *validate-prd "Validate PRD.md against product-brief.md and proposal.md."
```

## 1.3 – UX-design
```
/run-agent-task ux-designer *create-ux-design "Create UX flows, layouts and color themes for the AI CV Assistant."
```

## 1.4 – Valider UX
```
/run-agent-task ux-designer *validate-ux-design "Validate UX design files against PRD.md."
```

---

# 🟧 FASE 2 – SOLUTIONING (Arkitektur, Stories, Testing)

## 2.1 – Arkitektur
```
/run-agent-task architect *create-architecture "Design full technical architecture for the AI CV Assistant."
```

## 2.2 – Epics & Stories
```
/run-agent-task pm *create-epics-and-stories "Generate epics and user stories based on PRD.md and architecture.md."
```

## 2.3 – Testdesign
```
/run-agent-task tea *test-design "Create a complete test plan for robustness, acceptance and integration."
```

## 2.4 – Gate Check
```
/run-agent-task architect *solutioning-gate-check "Verify readiness for implementation."
```

---

# 🟥 FASE 3 – IMPLEMENTASJON

## 3.1 – Sprint-planlegging
```
/run-agent-task sm *sprint-planning "Plan sprint 1 focusing on MVP: parsing, job ad analysis, semantic matching, gap table, cover letter generation."
```

---

## 3.2 – Epic nivå

### Lag teknisk epic-kontekst
```
/run-agent-task sm create-epic-tech-context "Create technical context for epic <EPIC_ID>."
```

### Valider epic-kontekst
```
/run-agent-task sm validate-epic-tech-context "Validate technical context for <EPIC_ID>."
```

---

## 3.3 – Story nivå

### Opprett story
```
/run-agent-task sm *create-story "Create story <STORY_KEY> with acceptance criteria."
```

### Valider story
```
/run-agent-task sm *validate-create-story "Validate <STORY_KEY>.md."
```

### Lag story-kontekst
```
/run-agent-task sm *create-story-context "Create context for <STORY_KEY>."
```

### Valider story-kontekst
```
/run-agent-task sm *validate-story-context "Validate <STORY_KEY>.context.xml."
```

### Klargjør for dev
```
/run-agent-task sm *story-ready-for-dev
```

---

## 3.4 – Utvikling og code review (loop)

### Utvikling
```
/run-agent-task dev *develop-story "Implement <STORY_KEY>."
```

### Code Review
```
/run-agent-task dev *code-review "Review implementation for <STORY_KEY>."
```

---

## 3.5 – Story ferdig + test

### Ferdigmelding
```
/run-agent-task dev *story-done "Mark <STORY_KEY> as done."
```

### Test review
```
/run-agent-task sm *test-review "Review tests for <STORY_KEY>."
```

---

## 3.6 – Epic Retrospective
```
/run-agent-task sm *epic-retrospective "Run a retrospective for epic <EPIC_ID>."
```

---

# 🟦 FASE 4 – DRIFT, LÆRING OG VIDEREUTVIKLING

## 4.1 – Post-release review
```
/run-agent-task pm *validate-prd "Review final implementation vs PRD and summarize unmet requirements."
```

## 4.2 – Definer KPI-er og målinger
```
/run-agent-task analyst *brainstorm "Define metrics for ATS improvement, satisfaction and performance."
```

## 4.3 – Logging og overvåkning
```
/run-agent-task architect *create-architecture "Extend architecture.md with logging, monitoring and error-handling strategy."
```

## 4.4 – Forbedrings-backlog (epics & stories)
```
/run-agent-task pm *create-epics-and-stories "Create a Phase 4 improvement backlog based on user feedback and operational insights."
```

## 4.5 – Ny testdesign basert på produksjon
```
/run-agent-task tea *test-design "Update and extend test strategy based on real usage patterns."
```

## 4.6 – Retrospektiv for hele MVP
```
/run-agent-task sm *epic-retrospective "Full MVP retrospective: what worked, what didn't, improvements for next iteration."
```

## 4.7 – Brukerdokumentasjon
```
/run-agent-task analyst *product-brief "Create a user-facing guide explaining how to use the AI CV Assistant."
```

---

# ✔️ Hele BMAD-prosessen (Fase 0–4) er nå dokumentert som en komplett referansefil.
