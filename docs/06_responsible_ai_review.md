# VisitBrief AI — Responsible AI Review

## Document Information

**Project:** VisitBrief AI
**Document:** Responsible AI Review
**Version:** 1.0
**Status:** Discovery Phase

---

# Purpose

This document identifies potential risks associated with using AI in a home-visit preparation workflow and defines safeguards to reduce those risks.

VisitBrief AI is intentionally designed as a preparation-support tool rather than a decision-support system.

The goal is to improve information access while preserving human accountability and professional judgment.

---

# Project Positioning

VisitBrief AI is:

* A portfolio case study
* A production-minded AI MVP
* Built using synthetic data
* Intended for demonstration and learning purposes

VisitBrief AI is not:

* A production child welfare system
* A decision-support system
* A risk assessment tool
* A recommendation engine
* A replacement for professional judgment

---

# Responsible AI Principles

The product should follow the following principles:

## Transparency

Users should understand:

* Where information came from
* Which records were used
* What information is missing
* What information is uncertain

The system should never present unsupported conclusions as facts.

---

## Human Accountability

The system may support preparation.

The system may not make decisions.

Humans remain responsible for:

* Interpretation
* Professional judgment
* Case decisions
* Escalations
* Approvals

---

## Traceability

Factual claims should include citations whenever possible.

Example:

[Source: Case A - Contact Note 2 - 2026-04-08]

Users should be able to verify information against source records.

---

## Reliability

The system should answer only from approved case records.

If evidence does not exist, the system should state that information is unavailable.

The system should avoid guessing.

---

# Risk Assessment

## Risk 1 — Hallucinated Information

Description:

The AI may generate information not present in the source records.

Potential Impact:

* Incorrect preparation
* Reduced trust
* Misunderstanding of case details

Mitigation:

* Retrieval-based architecture
* Source citations
* Unsupported-answer refusal behavior

---

## Risk 2 — Unsupported Recommendations

Description:

The AI may recommend actions that are not supported by records.

Potential Impact:

* Inappropriate influence on professional decisions

Mitigation:

* Recommendation refusal policy
* Explicit system instructions
* Human review requirement

---

## Risk 3 — Cross-Case Information Leakage

Description:

Information from one case could appear in another case response.

Potential Impact:

* Privacy violations
* Loss of trust
* Compliance concerns

Mitigation:

* Selected-case-only retrieval
* Strict retrieval boundaries
* Evaluation testing

---

## Risk 4 — Overreliance on AI

Description:

Users may trust AI output without reviewing records.

Potential Impact:

* Missed context
* Incorrect assumptions
* Reduced professional diligence

Mitigation:

* Source citations
* Human review messaging
* Explicit preparation-only positioning

---

## Risk 5 — Missing Information Misinterpretation

Description:

Users may assume information exists when it is actually missing.

Potential Impact:

* Incomplete preparation

Mitigation:

* Missing-information flags
* Transparency messaging
* Source traceability

---

## Risk 6 — Conflicting Information Overlooked

Description:

Important contradictions may be missed.

Potential Impact:

* Incorrect understanding of case history

Mitigation:

* Conflict-detection logic
* Review prompts
* Human verification requirement

---

# Prohibited System Behaviors

VisitBrief AI must not:

* Determine risk levels
* Recommend placements
* Recommend interventions
* Determine eligibility
* Predict outcomes
* Provide legal advice
* Generate service plans
* Replace professional judgment

---

# Required Refusal Behavior

If evidence is unavailable:

The system should respond:

"I do not have enough verified information in the selected synthetic case records to answer that."

---

If the user requests a recommendation or decision:

The system should respond:

"I cannot make or recommend case decisions. Please review the source records and consult the appropriate caseworker or supervisor."

---

# Human-in-the-Loop Requirement

Decision-critical information must be reviewed by a qualified professional.

The assistant may help users understand information.

The assistant may not determine outcomes.

---

# Evaluation Requirements

Responsible AI evaluation should test:

* Hallucination prevention
* Citation accuracy
* Missing-information handling
* Conflict detection
* Cross-case retrieval prevention
* Recommendation refusal behavior
* Decision refusal behavior

---

# Responsible AI Decision

VisitBrief AI should proceed only as a narrowly scoped preparation assistant.

The system should prioritize transparency, traceability, and human oversight over automation.

Any future production deployment would require additional governance, privacy review, compliance review, security review, and stakeholder approval.
