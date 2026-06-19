# VisitBrief AI Architecture

```text
+--------------------------------------------------+
|                VisitBrief AI Workspace           |
|                 (Streamlit UI)                   |
+--------------------------------------------------+
                        |
                        v
+--------------------------------------------------+
|                 Persona Layer                    |
|--------------------------------------------------|
| Caseworker | Supervisor | Intake Specialist      |
+--------------------------------------------------+
                        |
                        v
+--------------------------------------------------+
|                 Safety Layer                     |
|--------------------------------------------------|
| Refusal Logic                                    |
| Decision Prevention                              |
| Scope Enforcement                                |
+--------------------------------------------------+
                        |
                        v
+--------------------------------------------------+
|               Retrieval Layer                    |
|--------------------------------------------------|
| Synthetic Case Records                           |
| Context Assembly                                 |
| Record Selection                                 |
+--------------------------------------------------+
                        |
                        v
+--------------------------------------------------+
|                  AI Layer                        |
|--------------------------------------------------|
| OpenAI GPT-4o-mini                               |
| Grounded Response Generation                     |
+--------------------------------------------------+
                        |
                        v
+--------------------------------------------------+
|                Citation Layer                    |
|--------------------------------------------------|
| Source Attribution                               |
| Traceability                                     |
+--------------------------------------------------+
                        |
                        v
+--------------------------------------------------+
|              Evaluation Layer                    |
|--------------------------------------------------|
| Retrieval Tests                                  |
| Refusal Tests                                    |
| Guardrail Validation                             |
+--------------------------------------------------+
```

## Request Flow

User Question
↓
Safety Check
↓
Retrieve Relevant Records
↓
Build Context
↓
OpenAI Response Generation
↓
Attach Citations
↓
Return Answer

## Design Principles

- Human-in-the-loop
- Source grounded
- Citation driven
- No case decisions
- No legal determinations
- No risk scoring
- Preparation support only