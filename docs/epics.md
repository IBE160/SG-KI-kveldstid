## Epic 1: Core Profile Management
    2 Goal: Enable users to input and manage their CV data for job application purposes.
    3 
    4 ### Story 1.1: Upload CV (Text-only)
    5 As a job seeker,
    6 I want to upload my CV as a text-only document,
    7 So that the system can parse my skills and experience for job matching.
    8 
    9 **Acceptance Criteria:**
   10 **Given** I am on the profile creation page
   11 **When** I upload a .txt or .pdf (parsed as text) file
   12 **Then** The system extracts key information like name, contact, work experience, education, and skills.
   13 **And** I receive a confirmation that my CV has been processed.
   14 
   15 **Prerequisites:** None
   16 **Technical Notes:** Focus on simple text parsing, not complex layout analysis.
   17 
   18 ### Story 1.2: Manually Edit Profile
   19 As a job seeker,
   20 I want to manually edit my parsed CV information,
   21 So that I can correct any parsing errors or add missing details.
   22 
   23 **Acceptance Criteria:**
   24 **Given** My CV has been parsed
   25 **When** I navigate to the profile editing interface
   26 **Then** I can see and modify extracted fields (e.g., job titles, dates, descriptions, skills).
   27 **And** The changes are saved to my profile.
   28 
   29 **Prerequisites:** Story 1.1
   30 
   31 ## Epic 2: Job Matching & Analysis
   32 Goal: Provide users with relevant job opportunities and analyze their fit.
   33 
   34 ### Story 2.1: Input Job Advertisement
   35 As a job seeker,
   36 I want to input a job advertisement (text),
   37 So that the system can analyze its requirements against my profile.
   38 
   39 **Acceptance Criteria:**
   40 **Given** I am on the job matching page
   41 **When** I paste a job description text into the input field
   42 **Then** The system processes the text to identify required skills, experience, and keywords.
   43 **And** I receive a confirmation that the job ad has been analyzed.
   44
   45 **Prerequisites:** Story 1.1, Story 1.2
   46
   47 ### Story 2.2: Semantic Matching of CV to Job Ad
   48 As a job seeker,
   49 I want the system to semantically match my CV against a job advertisement,
   50 So that I can see how well my skills and experience align with the job requirements.
   51
   52 **Acceptance Criteria:**
   53 **Given** I have an uploaded CV and an analyzed job advertisement
   54 **When** I request a match analysis
   55 **Then** The system provides a score or percentage indicating my compatibility.
   56 **And** It highlights areas of strong match and potential gaps.
   57
   58 **Prerequisites:** Story 1.1, Story 1.2, Story 2.1
   59
   60 ### Story 2.3: Basic Gap Table
   61 As a job seeker,
   62 I want to view a basic table of skill gaps between my CV and a job ad,
   63 So that I can easily identify what I'm missing for a specific role.
   64
   65 **Acceptance Criteria:**
   66 **Given** I have a semantic match analysis completed
   67 **When** I view the match results
   68 **Then** A table displays required skills from the job ad that are missing or weak in my CV.
   69 **And** The table is clear and easy to understand.
   70
   71 **Prerequisites:** Story 2.2
   72
   73 ## Epic 3: Application Assistance
   74 Goal: Assist users in generating tailored application materials.
   75
   76 ### Story 3.1: Simple Cover Letter Generation View
   77 As a job seeker,
   78 I want to generate a simple draft cover letter based on my CV and a job ad,
   79 So that I have a starting point for my application.
   80
   81 **Acceptance Criteria:**
   82 **Given** I have an uploaded CV and an analyzed job advertisement
   83 **When** I select to generate a cover letter
   84 **Then** The system produces a draft cover letter incorporating elements from my CV and addressing the job requirements.
   85 **And** I can copy or save the generated text.
   86
   87 **Prerequisites:** Story 1.1, Story 2.1, Story 2.2
