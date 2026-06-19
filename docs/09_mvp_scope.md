# VisitBrief AI — MVP Scope

## Document Information

**Project:** VisitBrief AI
**Document:** MVP Scope
**Version:** 1.0
**Status:** Definition Phase

---

# Purpose

This document defines what VisitBrief AI will include in the first MVP and what is intentionally excluded.

The goal is to build a narrow, safe, testable product that demonstrates AI Product Management thinking without overbuilding.

---

# MVP Goal

Build a live, synthetic-data AI preparation assistant that helps a caseworker prepare for a home visit by summarizing selected case records, answering factual case-specific questions, citing source notes, and flagging missing or conflicting information.

The MVP is designed for portfolio demonstration and product learning.

It is not designed for real agency deployment.

---

# In Scope

## 1. Synthetic Case Library

The MVP will include 3–5 synthetic case packets.

Each case packet may include:

* Intake summary
* Contact notes
* Visit notes
* Service-plan excerpt
* Task or deadline note
* School, medical, or provider note where appropriate

All records must be clearly labeled:

**SYNTHETIC DATA — FOR PORTFOLIO DEMO ONLY.**

---

## 2. Case Selection

Users can select one synthetic case from the sidebar.

The system must load only the selected case records.

---

## 3. Visit Brief Generation

Users can generate a structured visit-preparation brief.

The brief should include:

* Case background
* Recent updates
* Relevant concerns mentioned in records
* Upcoming deadlines or tasks
* Open follow-up items
* Missing information
* Conflicting information
* Source citations

---

## 4. Case-Specific Q&A

Users can ask factual questions about the selected synthetic case.

Examples:

* What was the last contact note?
* Are there upcoming deadlines?
* What concerns were mentioned?
* What documents appear to be missing?
* What follow-up items are open?

---

## 5. Citations

Factual answers should include citations in this format:

[Source: Case A - Contact Note 2 - 2026-04-08]

---

## 6. Refusal Behavior

The assistant must refuse unsupported or out-of-scope requests.

Unsupported answer refusal:

"I do not have enough verified information in the selected synthetic case records to answer that."

Decision/recommendation refusal:

"I cannot make or recommend case decisions. Please review the source records and consult the appropriate caseworker or supervisor."

---

## 7. Missing and Conflicting Information Flags

The system should identify when records contain missing, incomplete, unverified, or conflicting information.

---

## 8. Public Demo Disclaimers

The app must clearly state:

* It uses synthetic data only.
* It is for portfolio demonstration only.
* It is not affiliated with any employer or agency.
* It is not production-ready for real case use.
* It supports preparation only.
* It does not replace professional judgment.

---

# Out of Scope

The MVP will not include:

* Real client data
* Real child welfare data
* Employer or agency data
* Real agency integrations
* Risk scoring
* Placement recommendations
* Safety recommendations
* Eligibility determinations
* Legal recommendations
* Service-plan recommendations
* Predictive modeling
* Automated decisions
* Production authentication
* Role-based access control
* Audit logs
* Enterprise compliance workflows
* Real-time agency system integration

---

# Scope Rationale

The MVP is intentionally narrow because the workflow is high risk.

The product should first prove that it can safely support preparation using synthetic data before considering broader or more sensitive use cases.

A narrow scope allows the project to demonstrate:

* Responsible AI thinking
* Case-isolated retrieval
* Citation quality
* Refusal behavior
* Missing-information handling
* Conflict detection
* Human-in-the-loop boundaries

---

# MVP Success Criteria

The MVP is successful if:

1. A user can select a synthetic case.
2. A user can generate a visit-preparation brief.
3. A user can ask factual questions about the selected case.
4. The assistant cites source records.
5. The assistant refuses unsupported answers.
6. The assistant refuses decision or recommendation requests.
7. The assistant does not retrieve from unrelated cases.
8. The app can run locally.
9. The app can be hosted live.
10. The project can be explained clearly in an AI PM interview.

---

# Product Decision

Proceed with a narrow preparation-support MVP using synthetic data.

Do not expand into decision automation, real data, or production agency workflows.
