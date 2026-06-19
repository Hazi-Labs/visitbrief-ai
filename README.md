# VisitBrief AI

## Executive Summary

VisitBrief AI is a fictional GovTech AI assistant designed to support caseworker home-visit preparation using synthetic case records.

The project was built as an AI Product Management case study to demonstrate how an AI Product Manager can design, evaluate, and deploy a responsible AI assistant for a high-risk government workflow.

Rather than focusing solely on model integration, the project emphasizes workflow design, safety guardrails, source traceability, evaluation, human oversight, and product thinking.

All data used in the project is synthetic and created for demonstration purposes.

---

## Problem Statement

Caseworkers often review information across multiple documents before conducting a home visit.

Preparation may require reviewing:

* Intake summaries
* Contact notes
* Provider records
* Visit notes
* Service plans
* Deadlines and follow-up actions

This process can be time-consuming and may increase the risk of missing relevant information.

The challenge is not making decisions for caseworkers.

The challenge is helping them prepare efficiently while maintaining human oversight and accountability.

---

## Solution Overview

VisitBrief AI provides a workspace where users can:

* Review synthetic case records
* Generate visit-preparation briefs
* Ask factual questions about selected records
* Review case timelines
* Track tasks and deadlines
* Evaluate AI guardrail behavior

The assistant is intentionally limited to preparation support and source review.

The system does not make recommendations, decisions, risk scores, legal judgments, eligibility determinations, or service-plan recommendations.

---

## Product Goals

### Primary Goal

Reduce preparation effort required to review case information before a visit.

### Secondary Goals

* Improve information accessibility
* Surface missing or conflicting information
* Improve source traceability
* Demonstrate responsible AI design patterns

---

## Key Features

### Workspace Dashboard

* Case overview
* Preparation readiness indicators
* Open task tracking
* Upcoming deadlines

### Case Records

* Review synthetic source records
* Navigate individual case documents
* View record content directly

### Timeline View

* Chronological case activity history
* Intake, contacts, visits, provider updates, and reviews

### Tasks & Follow-Ups

* Open activities
* Review reminders
* Visit preparation checklist

### Calendar

* Upcoming actions
* Review deadlines
* Scheduled preparation work

### VisitBrief AI

* OpenAI-powered assistant
* Conversation history
* Case-specific question answering
* Visit brief generation
* Citation-based responses

### Evaluation

* Retrieval testing
* Refusal testing
* Baseline AI quality validation

---

## Responsible AI Design

VisitBrief AI intentionally includes several safety controls.

### Human-in-the-Loop Design

The assistant supports preparation only.

Final decisions remain with human professionals.

### Refusal Behavior

The system refuses requests involving:

* Case decisions
* Service recommendations
* Placement decisions
* Risk scoring
* Legal conclusions
* Eligibility determinations

### Source Grounding

Responses are generated using selected case records.

### Missing Information Handling

When information is unavailable, the assistant explicitly states that insufficient verified information exists.

### Evaluation Framework

Baseline tests validate:

* Follow-up retrieval
* Deadline retrieval
* Missing-information handling
* Conflict identification
* Refusal behavior

---

## AI Architecture

```text
User
  ↓
VisitBrief AI Workspace
  ↓
Safety Layer
  ↓
Retrieval Layer
  ↓
OpenAI Integration
  ↓
Citation Layer
  ↓
Response
```

### Components

#### UI Layer

* Streamlit

#### Safety Layer

* Request filtering
* Decision-refusal behavior

#### Retrieval Layer

* Case-record retrieval
* Context assembly

#### AI Layer

* OpenAI GPT integration
* Grounded response generation

#### Citation Layer

* Source traceability
* Document attribution

#### Evaluation Layer

* Baseline validation tests

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI

* OpenAI API

### Configuration

* python-dotenv

### Data

* Synthetic markdown case records

---

## Project Structure

```text
VisitBrief-AI
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── .streamlit
│   └── config.toml
│
├── data
│   └── synthetic_cases
│
├── docs
│
└── src
    ├── ai_client.py
    ├── citation_utils.py
    ├── data_loader.py
    ├── evaluation.py
    ├── retrieval.py
    └── safety.py
```

---

## Running Locally

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Enhancements

Potential future enhancements include:

* Multi-case retrieval
* Enhanced citation linking
* Document upload workflows
* Evaluation dashboards
* Caseworker feedback loops
* Role-based permissions
* Analytics and adoption tracking

---

## Product Management Takeaways

This project demonstrates how an AI Product Manager can move from:

1. Problem definition
2. Workflow design
3. User requirements
4. Synthetic data creation
5. Responsible AI guardrails
6. Retrieval architecture
7. LLM integration
8. Evaluation design
9. Deployment readiness

The focus of the project is not simply building an AI assistant.

The focus is demonstrating how responsible AI systems can be designed for high-risk workflows while maintaining transparency, traceability, and human oversight.
