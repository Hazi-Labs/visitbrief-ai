# VisitBrief AI — Product Requirements

## Document Information

**Project:** VisitBrief AI
**Document:** Product Requirements
**Version:** 1.0
**Status:** Definition Phase

---

# Purpose

This document defines the functional, AI, and non-functional requirements for VisitBrief AI.

These requirements establish the minimum capabilities required for the MVP.

---

# Product Objective

Enable a caseworker to prepare for a home visit more efficiently by generating grounded summaries and answering factual questions from selected synthetic case records.

The system supports preparation only and does not replace professional judgment.

---

# Functional Requirements

## FR-1 Case Selection

The user shall be able to select a synthetic case from the application interface.

Acceptance Criteria:

* Available cases are visible.
* User can switch between cases.
* Only one case is active at a time.

---

## FR-2 Selected-Case Retrieval

The system shall retrieve information only from the selected synthetic case.

Acceptance Criteria:

* Retrieval remains limited to the selected case.
* No information from unrelated cases appears in responses.

---

## FR-3 Visit Brief Generation

The system shall generate a structured visit-preparation summary.

The summary shall include:

* Case background
* Recent updates
* Relevant concerns
* Open follow-up items
* Upcoming tasks
* Deadlines
* Missing information
* Conflicting information
* Citations

Acceptance Criteria:

* Summary generates successfully.
* Citations are included.
* Information is grounded in source records.

---

## FR-4 Case-Specific Question Answering

The user shall be able to ask factual questions about the selected case.

Examples:

* What was the last contact note?
* What deadlines are upcoming?
* What concerns were mentioned?

Acceptance Criteria:

* Answers are grounded in selected records.
* Answers include citations when applicable.

---

## FR-5 Missing Information Detection

The system shall identify missing, incomplete, or unverified information when present.

Acceptance Criteria:

* Missing information is surfaced clearly.
* Users can trace findings to source records.

---

## FR-6 Conflict Detection

The system shall identify potentially conflicting information across records.

Acceptance Criteria:

* Conflicts are surfaced.
* Source records are cited.

---

## FR-7 Citation Support

The system shall provide source references for factual claims.

Citation format:

[Source: Case A - Contact Note 2 - 2026-04-08]

Acceptance Criteria:

* Citations appear consistently.
* Citations reference the correct source record.

---

## FR-8 Unsupported Answer Refusal

The system shall refuse unsupported questions.

Required Response:

"I do not have enough verified information in the selected synthetic case records to answer that."

Acceptance Criteria:

* Unsupported answers are refused.
* The system does not invent information.

---

## FR-9 Decision Refusal

The system shall refuse decision-making or recommendation requests.

Required Response:

"I cannot make or recommend case decisions. Please review the source records and consult the appropriate caseworker or supervisor."

Acceptance Criteria:

* Decision requests are refused.
* Recommendations are not generated.

---

## FR-10 Disclaimer Visibility

The application shall display clear disclaimers.

Acceptance Criteria:

Users can see:

* Synthetic data notice
* Portfolio demo notice
* Human-review notice
* Non-production notice

---

# AI Requirements

## AIR-1 Grounded Responses

The AI shall answer only from retrieved case records.

---

## AIR-2 No Hallucination Goal

The AI should avoid generating unsupported information.

---

## AIR-3 Case Isolation

The AI shall remain restricted to the selected case.

---

## AIR-4 Citation Support

The AI shall support traceable answers.

---

## AIR-5 Missing Information Handling

The AI shall identify when evidence appears incomplete.

---

## AIR-6 Conflict Detection

The AI shall identify when records appear inconsistent.

---

## AIR-7 Recommendation Refusal

The AI shall not provide recommendations.

---

## AIR-8 Human Oversight

The AI shall support preparation but not decision-making.

---

# Non-Functional Requirements

## NFR-1 Local Execution

The application shall run locally on a personal computer.

---

## NFR-2 Live Hosting

The application shall support public hosting for portfolio demonstration.

---

## NFR-3 Explainability

Outputs should be understandable and traceable.

---

## NFR-4 Response Time

Standard requests should complete within a reasonable time.

Target:

Less than 10 seconds.

---

## NFR-5 Security

API keys shall not be hardcoded.

Secrets shall be stored using environment variables or secure configuration methods.

---

## NFR-6 Maintainability

Project structure should be understandable to future reviewers.

---

## NFR-7 Portfolio Readability

The repository should be understandable to recruiters, hiring managers, and AI PM interviewers.

---

# Future Production Requirements (Out of MVP Scope)

If VisitBrief AI were expanded into a real production system, additional requirements would likely include:

* Authentication
* Role-based access control
* Audit logs
* Encryption
* Data retention controls
* Compliance reviews
* Security testing
* Accessibility reviews
* Monitoring
* Incident response
* Governance workflows

These items are intentionally excluded from the MVP.

---

# Requirements Decision

Proceed with a preparation-support AI assistant focused on retrieval, summarization, citations, and responsible AI guardrails.
