# VisitBrief AI — Product Decision Log

## Document Information

**Project:** VisitBrief AI
**Document:** Product Decision Log
**Version:** 1.0
**Status:** Active

---

# Purpose

This document records major product decisions, alternatives considered, and rationale.

The goal is to preserve decision-making context and make tradeoffs transparent.

---

# Decision Log

---

## PD-001

### Decision

Build a home-visit preparation assistant rather than a general-purpose case-management assistant.

### Alternatives Considered

* Full case-management copilot
* General AI chatbot
* Workflow automation platform

### Rationale

Preparation support is narrower, safer, easier to evaluate, and more appropriate for a portfolio MVP.

### Tradeoff

Less functionality but lower risk.

---

## PD-002

### Decision

Use synthetic records only.

### Alternatives Considered

* Real case data
* Anonymized records
* Public records

### Rationale

Synthetic data eliminates privacy concerns and supports public portfolio sharing.

### Tradeoff

Less realism but significantly lower risk.

---

## PD-003

### Decision

Position the product as a preparation assistant.

### Alternatives Considered

* Decision-support tool
* Recommendation engine
* Risk-assessment assistant

### Rationale

Preparation support aligns with responsible AI principles and human accountability.

### Tradeoff

Reduced automation.

---

## PD-004

### Decision

Require source citations.

### Alternatives Considered

* Free-form summaries
* Confidence scores only

### Rationale

Users must be able to verify information.

### Tradeoff

Additional implementation complexity.

---

## PD-005

### Decision

Restrict retrieval to the selected case.

### Alternatives Considered

* Multi-case search
* Global retrieval

### Rationale

Prevents cross-case leakage and improves trust.

### Tradeoff

Less flexibility.

---

## PD-006

### Decision

Refuse recommendations and decisions.

### Alternatives Considered

* Recommendation generation
* Action suggestions

### Rationale

The workflow is high risk and requires professional judgment.

### Tradeoff

Reduced perceived AI capability.

---

## PD-007

### Decision

Flag missing information.

### Alternatives Considered

* Ignore missing information
* Return only available information

### Rationale

Awareness of missing information is valuable preparation context.

### Tradeoff

Additional evaluation requirements.

---

## PD-008

### Decision

Flag conflicting information.

### Alternatives Considered

* Present most recent information only

### Rationale

Transparency is preferable to hidden assumptions.

### Tradeoff

Additional complexity.

---

## PD-009

### Decision

Build a simple Streamlit MVP.

### Alternatives Considered

* Full web application
* Enterprise platform
* Mobile application

### Rationale

Streamlit enables rapid delivery and easy demonstration.

### Tradeoff

Limited production scalability.

---

## PD-010

### Decision

Optimize for explainability over sophistication.

### Alternatives Considered

* Advanced agent architecture
* Multi-agent workflow
* Autonomous actions

### Rationale

The project is intended to demonstrate AI PM thinking and responsible AI design.

### Tradeoff

Less technical complexity but stronger explainability.

---

# Decision-Making Principle

When tradeoffs exist, VisitBrief AI prioritizes:

1. Safety
2. Transparency
3. Human accountability
4. Explainability
5. User value
6. Automation

Automation should never take precedence over responsible AI operation.
