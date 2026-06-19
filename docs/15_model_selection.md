# VisitBrief AI — Model and Vendor Selection Memo

## Document Information

**Project:** VisitBrief AI
**Document:** Model and Vendor Selection Memo
**Version:** 1.0
**Status:** Design Phase

---

# Purpose

This document explains the reasoning behind model selection for VisitBrief AI.

The objective is to identify a model that supports retrieval-based summarization and question answering while maintaining responsible AI boundaries.

---

# Business Need

VisitBrief AI requires a model capable of:

* Summarizing synthetic records
* Answering factual questions
* Following instructions reliably
* Supporting refusal behavior
* Operating on retrieved context
* Generating professional responses

The product does not require:

* Autonomous actions
* Agentic behavior
* Coding assistance
* Tool orchestration
* Complex reasoning beyond the workflow

---

# Evaluation Criteria

Models were evaluated using the following criteria:

| Criteria               | Importance |
| ---------------------- | ---------- |
| Instruction following  | High       |
| Grounded summarization | High       |
| Refusal behavior       | High       |
| Cost                   | Medium     |
| Latency                | Medium     |
| Ease of integration    | High       |
| Documentation quality  | Medium     |
| Developer experience   | Medium     |

---

# Candidate Approaches

## Option 1 — Traditional Search Only

Description:

Use search and filtering without AI.

Advantages:

* Low cost
* Predictable behavior
* Simple implementation

Disadvantages:

* No summarization
* No synthesis
* Limited natural-language interaction

Decision:

Not selected as primary solution.

Useful baseline comparison.

---

## Option 2 — Retrieval + LLM

Description:

Retrieve relevant records and provide them to an LLM.

Advantages:

* Supports grounded responses
* Supports summarization
* Supports citations
* Easier to explain
* Lower hallucination risk than relying on model memory

Disadvantages:

* Additional implementation complexity
* Requires retrieval evaluation

Decision:

Selected.

---

## Option 3 — Fine-Tuned Model

Description:

Train or fine-tune a custom model.

Advantages:

* Domain specialization

Disadvantages:

* Higher cost
* More complexity
* Additional governance concerns
* Limited value for MVP

Decision:

Not selected.

---

# Candidate Vendors

## OpenAI

Potential Models:

* GPT-5 family
* GPT-4 family

Advantages:

* Strong instruction following
* Large ecosystem
* Strong documentation
* Easy integration

Challenges:

* API costs
* Vendor dependency

---

## Anthropic

Potential Models:

* Claude family

Advantages:

* Strong long-context performance
* Reliable instruction following
* Good summarization quality

Challenges:

* Vendor dependency
* API costs

---

## Open-Source Models

Examples:

* Llama
* Mistral
* Qwen

Advantages:

* Greater control
* Lower long-term vendor dependency

Challenges:

* Hosting complexity
* Infrastructure requirements
* Additional operational burden

---

# Selected MVP Approach

Recommendation:

Retrieval-Augmented Generation (RAG)

Architecture:

Selected Case
↓
Retrieve Records
↓
Provide Context
↓
LLM Response
↓
Citations

Reasoning:

The workflow requires grounded answers rather than model memory.

Retrieval reduces hallucination risk and improves explainability.

---

# Why Not Fine-Tuning?

The project objective is preparation support rather than domain specialization.

The primary challenge is information retrieval and synthesis.

Fine-tuning does not solve retrieval, citation, or traceability requirements.

A retrieval-based approach provides more value for the MVP.

---

# Cost Considerations

The project budget target is less than $50.

Implications:

* Use API calls efficiently.
* Keep context sizes reasonable.
* Avoid unnecessary model usage.
* Support future provider flexibility.

---

# Latency Considerations

Target response time:

Less than 10 seconds.

Preferred:

Less than 5 seconds.

The selected architecture should balance answer quality with responsiveness.

---

# Vendor Independence Principle

The architecture should be designed so that the application can switch between providers with minimal changes.

This reduces long-term dependency on a single vendor.

---

# Model Selection Decision

Use a retrieval-based architecture with a commercial LLM provider for the MVP.

The retrieval layer remains the source of truth.

The language model acts as a summarization and question-answering layer rather than a decision-making system.

This approach best aligns with the project's goals of transparency, explainability, and responsible AI operation.
