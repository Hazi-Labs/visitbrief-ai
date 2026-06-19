# VisitBrief AI — Risk Register

## Document Information

**Project:** VisitBrief AI
**Document:** Risk Register
**Version:** 1.0
**Status:** Discovery Phase

---

# Purpose

This document identifies key product, technical, operational, and AI-related risks associated with VisitBrief AI.

The objective is to proactively identify potential failure modes and define mitigation strategies before implementation.

---

# Risk Scoring Method

Likelihood:

* Low
* Medium
* High

Impact:

* Low
* Medium
* High

Priority is determined using a combination of likelihood and impact.

---

# Risk Register

| ID  | Risk                                 | Likelihood | Impact | Priority |
| --- | ------------------------------------ | ---------- | ------ | -------- |
| R1  | Hallucinated information             | Medium     | High   | High     |
| R2  | Cross-case information leakage       | Low        | High   | High     |
| R3  | Unsupported recommendations          | Medium     | High   | High     |
| R4  | Missing information not identified   | Medium     | Medium | Medium   |
| R5  | Conflicting information not surfaced | Medium     | Medium | Medium   |
| R6  | User overreliance on AI              | Medium     | High   | High     |
| R7  | Poor citation quality                | Medium     | Medium | Medium   |
| R8  | Retrieval failure                    | Medium     | Medium | Medium   |
| R9  | Low user trust                       | Medium     | High   | High     |
| R10 | Poor adoption                        | Medium     | Medium | Medium   |

---

# Detailed Risk Analysis

## R1 — Hallucinated Information

Description:

The AI generates information not supported by source records.

Potential Impact:

* Incorrect preparation
* Reduced trust
* Misinformed users

Mitigation:

* Retrieval-based architecture
* Citation requirements
* Evaluation testing
* Refusal behavior

---

## R2 — Cross-Case Information Leakage

Description:

Information from one case appears in another case response.

Potential Impact:

* Privacy violation
* Compliance concerns
* Loss of trust

Mitigation:

* Selected-case-only retrieval
* Retrieval testing
* Case-isolation controls

Success Criteria:

0 cross-case retrieval incidents.

---

## R3 — Unsupported Recommendations

Description:

The assistant recommends actions or decisions.

Potential Impact:

* Improper influence on professional judgment

Mitigation:

* Safety guardrails
* Prompt controls
* Refusal policies
* Human review requirements

---

## R4 — Missing Information Not Identified

Description:

The assistant fails to recognize gaps in available records.

Potential Impact:

* Incomplete preparation

Mitigation:

* Missing-information review logic
* Evaluation testing

---

## R5 — Conflicting Information Not Surfaced

Description:

Contradictory records are not highlighted.

Potential Impact:

* Incorrect understanding of case history

Mitigation:

* Conflict detection rules
* Review prompts
* Evaluation testing

---

## R6 — User Overreliance on AI

Description:

Users rely on summaries without reviewing source material.

Potential Impact:

* Reduced diligence
* Missed context

Mitigation:

* Citations
* Human-in-the-loop messaging
* Transparency notices

---

## R7 — Poor Citation Quality

Description:

Answers contain incomplete or incorrect citations.

Potential Impact:

* Reduced trust
* Verification difficulties

Mitigation:

* Citation testing
* Standardized source formatting

---

## R8 — Retrieval Failure

Description:

Relevant records are not retrieved.

Potential Impact:

* Incomplete answers
* Missing context

Mitigation:

* Retrieval evaluation
* Test datasets
* Quality monitoring

---

## R9 — Low User Trust

Description:

Users do not trust outputs.

Potential Impact:

* Low adoption
* Limited product value

Mitigation:

* Transparency
* Citations
* Clear limitations
* Consistent behavior

---

## R10 — Poor Adoption

Description:

Users do not integrate the tool into their workflow.

Potential Impact:

* Reduced business value

Mitigation:

* Workflow alignment
* User testing
* Simplicity
* Fast response times

---

# Highest-Priority Risks

The highest-priority risks for VisitBrief AI are:

1. Cross-case information leakage
2. Hallucinated information
3. Unsupported recommendations
4. User overreliance on AI

These risks should receive the greatest attention during design, implementation, and evaluation.

---

# Risk Management Philosophy

The product should prioritize safety, transparency, and reliability over automation.

When uncertainty exists, the system should favor caution and explicit human review.
