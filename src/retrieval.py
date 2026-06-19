from src.safety import (
    is_prohibited_question,
    get_decision_refusal,
    get_unsupported_refusal,
)

from src.citation_utils import format_citation
from src.ai_client import is_ai_available, generate_case_response


def extract_section(content, section_title):
    lines = content.splitlines()
    captured = []
    capture = False

    for line in lines:
        stripped = line.strip()

        if stripped.lower().startswith(section_title.lower()):
            capture = True
            continue

        if capture:
            if stripped == "":
                continue

            if stripped.endswith(":") and not stripped.startswith("-"):
                break

            if stripped.startswith("-"):
                captured.append(stripped)

    return captured


def find_documents_with_phrase(documents, phrases):
    matches = []

    for doc in documents:
        text = doc["content"].lower()
        if any(phrase.lower() in text for phrase in phrases):
            matches.append(doc)

    return matches


def generate_structured_visit_brief(documents):
    concerns = []
    followups = []
    missing_info = []
    conflicts = []
    deadlines = []

    for doc in documents:
        content = doc["content"]
        citation = format_citation(doc)

        for item in extract_section(content, "Relevant Concerns Mentioned"):
            concerns.append((item, citation))

        for item in extract_section(content, "Open Follow-Up"):
            followups.append((item, citation))

        for item in extract_section(content, "Upcoming Tasks"):
            followups.append((item, citation))

        for item in extract_section(content, "Missing or Unverified Information"):
            missing_info.append((item, citation))

        if "Potential Conflict:" in content:
            conflicts.append((doc["filename"], citation))

        if "Deadline:" in content:
            for line in content.splitlines():
                if "supervisory review" in line.lower() or "due" in line.lower():
                    deadlines.append((line.strip(), citation))

    brief = "## Home Visit Preparation Brief\n\n"
    brief += "Generated from the selected synthetic case records only.\n\n"

    brief += "### Relevant Concerns Mentioned\n"
    if concerns:
        for item, citation in concerns:
            brief += f"- {item}\n  - {citation}\n"
    else:
        brief += "- No documented concerns found.\n"
    brief += "\n"

    brief += "### Open Follow-Up Items\n"
    if followups:
        for item, citation in followups:
            brief += f"- {item}\n  - {citation}\n"
    else:
        brief += "- No open follow-up items found.\n"
    brief += "\n"

    brief += "### Missing or Unverified Information\n"
    if missing_info:
        for item, citation in missing_info:
            brief += f"- {item}\n  - {citation}\n"
    else:
        brief += "- No missing or unverified information found.\n"
    brief += "\n"

    brief += "### Potential Conflicting Information\n"
    if conflicts:
        for filename, citation in conflicts:
            brief += f"- Potential conflict documented in `{filename}`.\n  - {citation}\n"
    else:
        brief += "- No potential conflicts found.\n"
    brief += "\n"

    brief += "### Upcoming Deadlines\n"
    if deadlines:
        for item, citation in deadlines:
            brief += f"- {item}\n  - {citation}\n"
    else:
        brief += "- No upcoming deadlines found.\n"
    brief += "\n"

    brief += "### Human Review Notice\n"
    brief += (
        "This brief supports preparation only. It does not make recommendations, "
        "risk scores, legal judgments, placement decisions, or service-plan decisions."
    )

    return brief


def deterministic_answer(question, documents, page_context):
    q = question.lower().strip()

    if "summarize this page" in q or "current page" in q:
        return page_context

    if "deadline" in q or "due" in q or "review" in q:
        matches = find_documents_with_phrase(documents, ["deadline", "supervisory review", "upcoming tasks"])
    elif "contact" in q or "phone" in q:
        matches = find_documents_with_phrase(documents, ["contact note", "phone", "call", "voicemail"])
    elif "missing" in q or "unverified" in q or "confirm" in q:
        matches = find_documents_with_phrase(documents, ["missing or unverified information", "unverified", "confirm"])
    elif "conflict" in q or "inconsistent" in q:
        matches = find_documents_with_phrase(documents, ["potential conflict", "conflict"])
    elif "concern" in q:
        matches = find_documents_with_phrase(documents, ["relevant concerns mentioned", "concerns"])
    elif "visit" in q:
        matches = find_documents_with_phrase(documents, ["visit note", "home visit"])
    elif "follow" in q or "task" in q:
        matches = find_documents_with_phrase(documents, ["open follow-up", "upcoming tasks"])
    elif "background" in q or "summary" in q:
        matches = documents[:3]
    else:
        matches = []

    if not matches:
        return get_unsupported_refusal()

    response = "### Answer\n\nBased on the selected case records:\n\n"

    for doc in matches[:3]:
        response += f"**Source Record: {doc['filename']}**\n\n"
        response += doc["content"][:900].strip()
        response += "\n\n"
        response += f"**Citation:** {format_citation(doc)}\n\n---\n\n"

    return response


def answer_from_records(question, documents, page_context):
    if is_prohibited_question(question):
        return get_decision_refusal()

    if is_ai_available():
        ai_answer = generate_case_response(question, documents)

        if ai_answer and not ai_answer.startswith("AI Error:"):
            return ai_answer

    return deterministic_answer(question, documents, page_context)