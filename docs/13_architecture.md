# VisitBrief AI — System Architecture

## Document Information

**Project:** VisitBrief AI
**Document:** System Architecture
**Version:** 1.0
**Status:** Design Phase

---

# Purpose

This document describes the high-level architecture of VisitBrief AI.

The architecture is intentionally simple, explainable, and appropriate for a portfolio MVP.

The goal is to demonstrate responsible AI design principles rather than production-scale infrastructure.

---

# Architecture Overview

VisitBrief AI follows a retrieval-based architecture.

The system retrieves information from the selected synthetic case and uses that information to generate grounded responses.

The system does not rely on model memory or external knowledge for case-specific answers.

---

# High-Level Architecture

User
↓
Streamlit Application
↓
Case Selection Layer
↓
Retrieval Layer
↓
Safety Layer
↓
LLM Layer
↓
Response Generation
↓
Citation Layer
↓
User

---

# Component Descriptions

## User Interface Layer

Technology:

* Streamlit

Responsibilities:

* Display disclaimers
* Allow case selection
* Generate visit briefs
* Accept user questions
* Display citations
* Display refusal messages

---

## Synthetic Case Repository

Technology:

* Local markdown files

Responsibilities:

* Store synthetic records
* Organize records by case
* Provide source material for retrieval

Example Structure:

data/
synthetic_cases/
case_a/
case_b/
case_c/

---

## Case Selection Layer

Responsibilities:

* Identify active case
* Restrict retrieval scope
* Prevent cross-case retrieval

Importance:

This layer is critical for preventing information leakage.

---

## Retrieval Layer

Responsibilities:

* Read case records
* Identify relevant content
* Retrieve supporting evidence

Purpose:

Provide context for the language model.

The retrieval layer acts as the source of truth.

---

## Safety Layer

Responsibilities:

* Detect prohibited requests
* Detect recommendation requests
* Detect decision requests
* Trigger refusal behavior

Examples:

* "Should this child be removed?"
* "What action should the worker take?"

These requests should be refused.

---

## Language Model Layer

Potential Providers:

* OpenAI
* Anthropic
* Alternative compatible models

Responsibilities:

* Summarization
* Question answering
* Missing-information analysis
* Conflict analysis

The model should operate only on retrieved context.

---

## Citation Layer

Responsibilities:

* Attach source references
* Preserve traceability
* Support verification

Example:

[Source: Case A - Contact Note 2 - 2026-04-08]

---

# Architecture Principles

## Principle 1

Selected-case-only retrieval.

No cross-case retrieval.

---

## Principle 2

Grounded answers only.

No unsupported conclusions.

---

## Principle 3

Human accountability.

Humans make decisions.

AI provides preparation support.

---

## Principle 4

Source traceability.

Users should be able to verify information.

---

## Principle 5

Safety before automation.

The system should refuse unsafe requests rather than provide potentially harmful answers.

---

# Production Expansion Considerations

If expanded into a real system, additional components would likely include:

* Authentication
* Role-based access control
* Audit logging
* Encryption
* Monitoring
* Compliance controls
* Human review workflows
* Prompt version control
* Evaluation pipelines

These components are intentionally excluded from the MVP.

---

# Architecture Decision

Use a simple retrieval-based architecture with selected-case isolation, safety guardrails, citation support, and human-in-the-loop boundaries.
