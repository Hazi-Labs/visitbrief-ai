# VisitBrief AI — AI Opportunity Assessment

## Document Information

**Project:** VisitBrief AI
**Document:** AI Opportunity Assessment
**Version:** 1.0
**Status:** Discovery Phase

---

# Purpose

This document evaluates where artificial intelligence may provide meaningful value within the home-visit preparation workflow.

The goal is to identify opportunities where AI can improve efficiency, understanding, and information accessibility while avoiding areas that require human judgment.

---

# Core Question

Before introducing AI, the product team should ask:

"Can this problem be solved with search, workflow improvements, or traditional software?"

AI should only be introduced when it provides meaningful additional value.

---

# Workflow Evaluation

| Workflow Activity                | Traditional Software | AI Value    | Recommendation          |
| -------------------------------- | -------------------- | ----------- | ----------------------- |
| Locate records                   | Strong               | Low         | Use traditional search  |
| Filter documents                 | Strong               | Low         | Use traditional filters |
| Review lengthy notes             | Limited              | High        | AI candidate            |
| Summarize history                | Limited              | High        | AI candidate            |
| Explain recent changes           | Limited              | High        | AI candidate            |
| Identify missing information     | Moderate             | Medium-High | AI candidate            |
| Identify conflicting information | Moderate             | Medium-High | AI candidate            |
| Answer factual questions         | Limited              | High        | AI candidate            |
| Make decisions                   | Not applicable       | Unsafe      | Human only              |

---

# High-Value AI Opportunities

## Opportunity 1 — Visit Brief Generation

The system can generate a concise preparation summary from approved records.

Potential value:

* Faster preparation
* Improved consistency
* Reduced manual review effort

---

## Opportunity 2 — Case-Specific Question Answering

The system can answer factual questions grounded in selected records.

Examples:

* What was the most recent contact note?
* What deadlines are upcoming?
* What concerns were documented?

Potential value:

* Faster information retrieval
* Natural-language access to records

---

## Opportunity 3 — Missing Information Detection

The system can identify information that appears incomplete or unverified.

Potential value:

* Improved preparation quality
* Reduced oversight risk

---

## Opportunity 4 — Conflict Detection

The system can identify records that appear inconsistent.

Potential value:

* Easier verification
* Improved awareness before visits

---

# Low-Value AI Opportunities

The following activities are unlikely to require advanced AI:

* Opening records
* Searching by keyword
* Filtering by date
* Sorting documents
* Basic navigation

These activities can often be handled through traditional software.

---

# Prohibited AI Activities

The system should not:

* Determine risk levels
* Recommend placements
* Recommend interventions
* Determine eligibility
* Provide legal advice
* Approve service plans
* Predict case outcomes
* Replace professional judgment

---

# Human-in-the-Loop Requirement

The AI assistant may support understanding.

The AI assistant may not determine outcomes.

Humans remain responsible for:

* Interpretation
* Judgment
* Decisions
* Escalation
* Approval

---

# Key Discovery Insight

The primary opportunity is not document search.

The primary opportunity is reducing the effort required to synthesize information across multiple records while maintaining transparency and human accountability.

AI should therefore focus on preparation support rather than decision support.

---

# Recommendation

Proceed with a narrowly scoped AI MVP focused on:

* Summarization
* Information retrieval
* Missing-information identification
* Conflict detection
* Source traceability

Avoid decision automation and recommendation generation entirely.
