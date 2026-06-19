def get_source_note(content: str, filename: str) -> str:
    for line in content.splitlines():
        if line.strip().startswith("[Source:"):
            return f"{line.strip()} | File: {filename}"
    return f"[Source: Selected synthetic case record | File: {filename}]"


def format_citation(doc: dict) -> str:
    return get_source_note(doc["content"], doc["filename"])