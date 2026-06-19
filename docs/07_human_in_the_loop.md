# VisitBrief AI — Human-in-the-Loop Design

## Document Information

**Project:** VisitBrief AI
**Document:** Human-in-the-Loop Design
**Version:** 1.0
**Status:** Discovery Phase

---

# Purpose

This document defines how humans and AI interact within VisitBrief AI.

The objective is to ensure that AI supports professional workflows without replacing professional judgment.

---

# Core Principle

VisitBrief AI is a preparation assistant.

The AI may help users:

* Find information
* Summarize information
* Organize information
* Surface missing information
* Surface conflicting information

The AI may not:

* Make decisions
* Approve actions
* Recommend actions
* Determine outcomes

---

# Decision Ownership

All decisions remain the responsibility of qualified professionals.

Examples include:

* Safety decisions
* Placement decisions
* Eligibility decisions
* Legal decisions
* Service-plan decisions
* Escalation decisions

The system must never imply that it has authority to make these decisions.

---

# Human + AI Workflow

## Step 1

Human selects a case.

AI loads only approved records for that case.

---

## Step 2

Human requests a visit brief.

AI summarizes available records.

---

## Step 3

Human reviews the summary.

AI provides citations.

---

## Step 4

Human asks questions.

AI answers only from approved records.

---

## Step 5

Human reviews cited records when necessary.

---

## Step 6

Human applies professional judgment.

The AI does not participate in the decision.

---

# Escalation Conditions

The system should encourage human review when:

* Information is missing
* Information is conflicting
* Information is incomplete
* Information is decision-critical
* Information is sensitive

---

# AI Responsibilities

The AI is responsible for:

* Retrieval
* Summarization
* Citation
* Transparency
* Refusal behavior

---

# Human Responsibilities

Humans remain responsible for:

* Interpretation
* Verification
* Decision-making
* Approval
* Escalation
* Accountability

---

# Human Override Principle

Humans should always be able to:

* Review source records
* Ignore AI outputs
* Correct errors
* Reach different conclusions

The AI must never be treated as the final authority.

---

# Design Philosophy

The purpose of VisitBrief AI is not to automate judgment.

The purpose of VisitBrief AI is to reduce information retrieval and preparation effort while keeping accountability with humans.

The system should make professionals more informed, not less responsible.

---

# Human-in-the-Loop Decision

VisitBrief AI should operate as a preparation-support assistant with clear human ownership of all decisions and outcomes.
