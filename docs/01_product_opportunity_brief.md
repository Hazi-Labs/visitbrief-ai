# VisitBrief AI — Product Opportunity Brief

## Document Information

**Project:** VisitBrief AI
**Author:** Hazi Ali Pattan
**Type:** Product Opportunity Brief
**Version:** 1.0
**Status:** Discovery Phase

---

# Executive Summary

VisitBrief AI is a production-minded AI MVP and portfolio case study designed to explore how artificial intelligence can support home-visit preparation workflows in a high-risk GovTech environment.

The project uses only synthetic records and does not represent a real agency system, employer initiative, or production deployment.

The objective is to investigate whether AI can help caseworkers prepare for home visits more efficiently and consistently by summarizing approved records, surfacing relevant context, identifying missing or conflicting information, and answering factual questions while maintaining clear human oversight and responsible AI boundaries.

The system is intentionally designed as a preparation assistant rather than a decision-support or recommendation engine.

---

# Problem Statement

Caseworkers preparing for home visits often need to review information spread across multiple records, including intake summaries, contact notes, visit notes, service-plan updates, provider communications, and administrative tasks.

Important information may be distributed across lengthy documentation, requiring significant manual review before each visit.

This creates several challenges:

* Preparation may be time-consuming.
* Important context may be overlooked.
* Information may be duplicated across records.
* Missing or conflicting information may be difficult to identify.
* Visit readiness may vary between workers.
* Administrative review may reduce time available for direct client support.

The goal is not to automate professional judgment but to reduce the burden of locating and organizing information before a visit.

---

# Why This Problem Matters

Public-sector caseworkers frequently manage complex workloads and large volumes of documentation.

When preparation requires significant manual effort, workers spend less time on activities that directly support individuals and families.

If AI can safely assist with information retrieval and summarization, workers may be able to spend more time exercising professional judgment rather than searching through records.

Because this is a high-risk domain, any AI involvement must prioritize transparency, traceability, human oversight, and safety.

---

# Target User

## Primary User

Caseworker preparing for an assigned home visit.

Primary responsibilities:

* Review case history.
* Understand recent developments.
* Identify follow-up items.
* Confirm deadlines.
* Prepare for client interaction.
* Escalate concerns when necessary.

## Secondary Stakeholders

### Supervisor

Responsible for oversight, coaching, review, and approval.

### Agency Leadership

Interested in consistency, efficiency, and operational outcomes.

### Compliance and Privacy Teams

Responsible for ensuring policy adherence and safe AI usage.

### Technology Teams

Responsible for system deployment, security, and maintenance.

---

# Current Workflow (Hypothesis)

Prior to a home visit, a caseworker may:

1. Open the assigned case.
2. Review intake documentation.
3. Read recent contact notes.
4. Review previous visit notes.
5. Review service-plan updates.
6. Check provider communications.
7. Identify deadlines and tasks.
8. Identify missing information.
9. Prepare discussion topics.
10. Conduct the visit.

This workflow may require navigating multiple documents and manually assembling context from various sources.

---

# User Pain Points

| Pain Point                             | Impact                       |
| -------------------------------------- | ---------------------------- |
| Information spread across many records | Increased review time        |
| Long documentation histories           | Context difficult to locate  |
| Missing information not obvious        | Additional manual effort     |
| Conflicting information across records | Reduced confidence           |
| Limited preparation time               | Variable visit readiness     |
| Administrative burden                  | Less time for direct support |

These pain points are hypotheses and should be validated through user research in a real-world environment.

---

# Opportunity Hypothesis

If AI can retrieve information only from approved case records and generate grounded summaries with citations, then caseworkers may be able to prepare for visits more efficiently and consistently.

The opportunity is not decision automation.

The opportunity is information organization and retrieval.

Potential value areas include:

* Faster preparation.
* Better visibility into relevant history.
* Improved source traceability.
* Easier identification of missing information.
* Reduced information-search burden.

---

# Why AI?

Traditional search tools require users to know what they are looking for.

Large language models may provide additional value by:

* Summarizing lengthy records.
* Synthesizing information across notes.
* Answering natural-language questions.
* Explaining what information is missing.
* Highlighting conflicting information.
* Providing source citations.

However, AI introduces new risks that require guardrails and human oversight.

---

# Responsible AI Position

VisitBrief AI is intentionally limited.

The system should:

* Support preparation.
* Provide citations.
* Surface missing information.
* Surface conflicting information.
* Refuse unsupported answers.
* Stay within selected case records.

The system should not:

* Make case decisions.
* Recommend placements.
* Recommend interventions.
* Score risk.
* Predict outcomes.
* Provide legal guidance.
* Replace professional judgment.

---

# Human-in-the-Loop Principle

The AI assistant serves as a preparation aid.

All decisions remain the responsibility of qualified professionals.

When information is incomplete, conflicting, sensitive, or decision-critical, users must review original source records and follow organizational procedures.

The assistant may support understanding but must not determine outcomes.

---

# Success Metrics

## Primary Success Metric

Reduce average visit-preparation time by at least 20% during task-based testing compared with manual review workflows.

## Supporting Metrics

* Percentage of users able to complete preparation tasks successfully.
* User-reported preparation confidence.
* User-reported reduction in administrative burden.
* User-reported usefulness of generated visit briefs.

---

# Guardrail Metrics

The assistant should:

* Cite supporting records for factual claims.
* Remain within the selected case.
* Refuse unsupported questions.
* Refuse decision-making requests.
* Avoid hallucinated information.
* Flag missing information.
* Flag conflicting information.

Target evaluation goals:

* ≥90% citation-supported factual claims.
* 0 cross-case retrieval incidents.
* 100% refusal of prohibited recommendation requests during testing.

---

# MVP Recommendation

Build a narrow AI-assisted preparation workflow using synthetic records.

The MVP should include:

* Synthetic case library.
* Case selection.
* Visit brief generation.
* Case-specific factual Q&A.
* Citations.
* Missing-information flags.
* Conflict detection.
* Refusal behavior.

The MVP should not include:

* Real agency data.
* Real client data.
* Risk scoring.
* Predictive models.
* Eligibility determinations.
* Recommendation generation.
* Real system integrations.

---

# Key Assumption

The core assumption behind VisitBrief AI is:

"Caseworkers spend meaningful time locating and synthesizing information before home visits, and an AI assistant that provides grounded summaries with citations can reduce preparation effort without replacing professional judgment."

The remainder of the project will evaluate this assumption through product design, responsible AI review, implementation, and testing.
