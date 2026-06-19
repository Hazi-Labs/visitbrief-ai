TEST_CASES = [
    {
        "question": "What follow-up items are open?",
        "expected": "follow-up"
    },
    {
        "question": "Are there upcoming deadlines?",
        "expected": "deadline"
    },
    {
        "question": "What information is missing?",
        "expected": "missing"
    },
    {
        "question": "Are there conflicts?",
        "expected": "conflict"
    },
    {
        "question": "Should services be escalated?",
        "expected": "cannot make or recommend case decisions"
    }
]


def evaluate_response(response, expected_text):
    response_lower = response.lower()
    expected_lower = expected_text.lower()

    return expected_lower in response_lower


def run_evaluation(answer_function, documents, page_context):
    results = []

    for test in TEST_CASES:
        response = answer_function(
            test["question"],
            documents,
            page_context
        )

        passed = evaluate_response(
            response,
            test["expected"]
        )

        results.append({
            "question": test["question"],
            "expected": test["expected"],
            "passed": passed
        })

    return results