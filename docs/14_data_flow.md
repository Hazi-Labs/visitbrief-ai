# VisitBrief AI — Data Flow

## Document Information

**Project:** VisitBrief AI
**Document:** Data Flow
**Version:** 1.0
**Status:** Design Phase

---

# Purpose

This document describes how information moves through VisitBrief AI from user request to final response.

The objective is to provide transparency, support explainability, and reduce AI-related risks.

---

# Data Flow Overview

User
↓
Select Case
↓
Load Selected Case Records
↓
Retrieve Relevant Content
↓
Safety Validation
↓
Construct Prompt
↓
LLM Processing
↓
Citation Attachment
↓
Display Response

---

# Visit Brief Flow

## Step 1 — Case Selection

The user selects a synthetic case.

Example:

Case A

The system records the active case.

---

## Step 2 — Record Loading

The application loads records associated with the selected case.

Examples:

* Intake Summary
* Contact Notes
* Visit Notes
* Provider Notes
* Task Notes

No other cases are loaded.

---

## Step 3 — Retrieval

Relevant records are retrieved.

For a visit brief, all selected-case records may be considered.

The retrieval layer becomes the source of truth for the response.

---

## Step 4 — Safety Validation

The request is checked for prohibited behavior.

Examples:

* Recommendation requests
* Decision requests
* Risk scoring requests

If detected:

Refusal behavior is triggered.

---

## Step 5 — Prompt Construction

Retrieved records are assembled into structured context.

The prompt includes:

* Retrieved records
* Safety instructions
* Citation requirements
* Human-review requirements

---

## Step 6 — Language Model Processing

The language model receives:

* User request
* Retrieved context
* System instructions

The model generates:

* Summary
* Answer
* Missing-information observations
* Conflict observations

---

## Step 7 — Citation Generation

Supporting source references are attached.

Example:

[Source: Case A - Contact Note 2 - 2026-04-08]

The user can trace information back to source records.

---

## Step 8 — Response Display

The application displays:

* Generated response
* Citations
* Safety messaging
* Disclaimers

---

# Question Answering Flow

## User Question

Example:

"What was the last contact note?"

---

## Retrieval

Relevant records are retrieved from the selected case.

---

## Safety Check

The system determines whether the question is allowed.

If allowed:

Continue.

If prohibited:

Refuse.

---

## Answer Generation

The model answers using retrieved content only.

---

## Citation Attachment

Supporting citations are attached.

---

## Display

The final answer is shown to the user.

---

# Refusal Flow

## Example Request

"What action should the worker take?"

---

## Safety Layer

The request is classified as decision-oriented.

---

## Refusal Trigger

The system returns:

"I cannot make or recommend case decisions. Please review the source records and consult the appropriate caseworker or supervisor."

---

## Response Display

No recommendation is generated.

---

# Missing Information Flow

## Retrieval

Records are reviewed.

---

## Analysis

The model identifies information that appears incomplete or unverified.

---

## Output

Missing-information flags are included in the response.

---

# Conflict Detection Flow

## Retrieval

Multiple records are reviewed.

---

## Comparison

Records are compared for inconsistencies.

---

## Output

Potential conflicts are surfaced.

Sources are cited.

---

# Data Isolation Principle

VisitBrief AI follows strict case isolation.

Rules:

* One active case at a time
* One retrieval scope at a time
* No unrelated-case retrieval
* No cross-case answer generation

This principle is critical for trust and privacy.

---

# Data Flow Decision

All responses should originate from retrieved content associated with the selected synthetic case.

The system should prioritize transparency, traceability, and case isolation over automation.
