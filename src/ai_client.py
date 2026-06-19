import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or api_key.strip() == "":
        return None

    return OpenAI(api_key=api_key)


def is_ai_available():
    return get_openai_client() is not None


def build_case_context(documents):
    context = ""

    for doc in documents:
        context += f"\n\n--- FILE: {doc['filename']} ---\n"
        context += doc["content"]

    return context


def generate_case_response(question, documents):
    client = get_openai_client()

    if client is None:
        return None

    context = build_case_context(documents)

    system_prompt = """
You are VisitBrief AI, a preparation-support assistant for a fictional GovTech caseworker workspace.

Rules:
- Use only the selected-case context provided.
- Do not use outside knowledge.
- Do not make case decisions.
- Do not recommend actions, interventions, placements, eligibility outcomes, legal actions, or service plans.
- Do not generate risk scores.
- If the selected case context does not contain enough evidence, say:
  "I do not have enough verified information in the selected synthetic case records to answer that."
- Use neutral, professional language.
- Every factual claim must include a source citation using the source notes in the records.
- The assistant supports preparation only and does not replace professional judgment.
"""

    user_prompt = f"""
Selected Case Records:
{context}

User Question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
        )

        return response.choices[0].message.content

    except Exception as error:
        return f"AI Error: {error}"