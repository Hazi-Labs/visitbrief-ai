# VisitBrief AI Case Study

## Executive Summary

VisitBrief AI is an AI-powered case preparation assistant designed to help caseworkers prepare for client visits by reviewing records, identifying follow-up items, surfacing deadlines, and generating preparation briefs.

The project was created as an AI Product Management portfolio case study demonstrating product discovery, workflow design, responsible AI practices, retrieval-based AI architecture, evaluation planning, and deployment.

The solution uses synthetic case data and is intended solely as a preparation support tool. Human review remains required for all decisions.

---

# Problem

Caseworkers often spend significant time reviewing scattered notes, intake records, provider updates, service plans, and previous visit documentation before conducting a visit.

Common challenges include:

* Information spread across multiple records
* Missed follow-up items
* Difficulty identifying conflicting information
* Limited preparation time
* Lack of summarized visit context

Preparation work can become inconsistent depending on experience level and workload.

---

# Users

## Primary User

Caseworker

Responsibilities:

* Prepare for client visits
* Review historical records
* Track follow-up items
* Coordinate with providers
* Document findings

## Secondary User

Supervisor

Responsibilities:

* Review cases
* Monitor workload
* Identify preparation gaps
* Support quality assurance

---

# Opportunity

Provide an AI-assisted preparation workspace capable of:

* Reviewing source records
* Generating visit briefs
* Highlighting deadlines
* Identifying missing information
* Supporting preparation workflows

while maintaining transparency, traceability, and human oversight.

---

# Solution

VisitBrief AI combines:

* Synthetic case records
* Retrieval-based AI assistance
* Structured preparation workflows
* Source record review
* Visit brief generation
* Responsible AI guardrails

The system does not make decisions and does not replace professional judgment.

---

# Product Features

## Dashboard

Provides:

* Case status
* Priority
* Open tasks
* Record counts
* Preparation progress

## Case Records

Allows users to:

* Review source documents
* Explore historical records
* Understand case context

## Tasks

Displays:

* Follow-up activities
* Ownership
* Due dates
* Preparation checklist items

## Calendar

Provides:

* Upcoming deadlines
* Scheduled preparation activities
* Visit planning visibility

## VisitBrief AI Assistant

Supports:

* Question answering
* Brief generation
* Record summarization
* Context exploration

---

# Architecture

User Interface

↓

Streamlit Application

↓

Retrieval Layer

↓

Synthetic Case Documents

↓

OpenAI Model

↓

Response Generation

↓

Human Review

---

# Responsible AI Design

The system follows several guardrails:

* Human review required
* No autonomous decisions
* Synthetic data only
* Transparent source usage
* Limited scope assistance
* Retrieval-first design

---

# Evaluation Approach

Evaluation focused on:

* Answer relevance
* Source grounding
* Brief usefulness
* Hallucination reduction
* Workflow alignment

The project includes:

* Evaluation plan
* Evaluation dataset
* Test results template

for ongoing measurement.

---

# Success Metrics

Primary Metric:

Preparation time reduction

Supporting Metrics:

* Brief generation usage
* Question answering usefulness
* Missing information identification
* User satisfaction

Guardrail Metrics:

* Unsupported answer rate
* Citation coverage
* Safety violations

---

# Results

The project successfully demonstrates:

* AI product discovery
* Workflow design
* Responsible AI implementation
* Retrieval-based architecture
* Evaluation planning
* Production deployment

The application was deployed publicly through Streamlit Cloud and integrated with OpenAI.

---

# Lessons Learned

Key lessons included:

* Retrieval improves transparency
* Guardrails are essential
* Workflow context matters more than model size
* Evaluation should be planned early
* Product value comes from workflow integration rather than AI alone

---

# Future Roadmap

Potential future enhancements:

* Citation-level retrieval
* Advanced analytics
* Multi-case prioritization
* Workflow recommendations
* Supervisor review automation
* Enterprise case-management integrations

---

# Final Product Decision

VisitBrief AI should assist preparation, improve awareness, and support human workers without replacing professional judgment.
