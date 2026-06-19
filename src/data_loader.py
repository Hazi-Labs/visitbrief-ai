from pathlib import Path


DATA_DIR = Path("data/synthetic_cases")


def list_cases():
    """Return available synthetic case folder names."""
    if not DATA_DIR.exists():
        return []

    return sorted([
        folder.name
        for folder in DATA_DIR.iterdir()
        if folder.is_dir()
    ])


def load_case_documents(case_id):
    """Load all markdown documents for one selected case only."""
    case_path = DATA_DIR / case_id

    if not case_path.exists():
        return []

    documents = []

    for file_path in sorted(case_path.glob("*.md")):
        documents.append({
            "filename": file_path.name,
            "content": file_path.read_text(encoding="utf-8")
        })

    return documents