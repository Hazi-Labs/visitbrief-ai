PROHIBITED_TERMS = [
    "should",
    "recommend",
    "best course",
    "remove",
    "placement",
    "escalate",
    "legal",
    "eligible",
    "risk score",
    "decision",
    "what action",
    "what should happen",
    "intervention",
    "service plan recommendation",
]


DECISION_REFUSAL = (
    "I cannot make or recommend case decisions. Please review the source records "
    "and consult the appropriate caseworker or supervisor."
)


UNSUPPORTED_REFUSAL = (
    "I do not have enough verified information in the selected synthetic case records to answer that."
)


def is_prohibited_question(question: str) -> bool:
    question_lower = question.lower().strip()
    return any(term in question_lower for term in PROHIBITED_TERMS)


def get_decision_refusal() -> str:
    return DECISION_REFUSAL


def get_unsupported_refusal() -> str:
    return UNSUPPORTED_REFUSAL