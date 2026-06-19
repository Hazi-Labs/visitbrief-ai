import streamlit as st

from src.data_loader import list_cases, load_case_documents
from src.retrieval import generate_structured_visit_brief, answer_from_records
from src.evaluation import run_evaluation


st.set_page_config(
    page_title="VisitBrief AI",
    page_icon="🗂️",
    layout="wide"
)


case_metadata = {
    "case_a": {
        "family": "Synthetic Family A",
        "focus": "School attendance and caregiver contact",
        "status": "Active",
        "priority": "Medium",
        "next_action": "School follow-up",
        "next_date": "2026-04-22",
        "review_due": "2026-04-25",
        "progress": 68,
        "open_tasks": 4,
    },
    "case_b": {
        "family": "Synthetic Family B",
        "focus": "Housing stability and provider coordination",
        "status": "Active",
        "priority": "Medium-High",
        "next_action": "Residence verification",
        "next_date": "2026-05-22",
        "review_due": "2026-05-27",
        "progress": 52,
        "open_tasks": 5,
    },
    "case_c": {
        "family": "Synthetic Family C",
        "focus": "Appointment follow-up and provider communication",
        "status": "Active",
        "priority": "Medium",
        "next_action": "Provider record review",
        "next_date": "2026-06-22",
        "review_due": "2026-06-28",
        "progress": 61,
        "open_tasks": 4,
    },
}


timeline_data = {
    "case_a": [
        ("2026-04-02", "Intake summary created", "intake_summary.md"),
        ("2026-04-05", "Initial caregiver contact attempted", "contact_note_1.md"),
        ("2026-04-08", "Caregiver returned call and agreed to home visit", "contact_note_2.md"),
        ("2026-04-10", "School provider note confirmed attendance concerns", "provider_note.md"),
        ("2026-04-15", "Home visit completed", "visit_note_1.md"),
        ("2026-04-16", "Service plan and deadline notes updated", "service_plan_excerpt.md / task_deadline_note.md"),
        ("2026-04-22", "School follow-up target date", "task_deadline_note.md"),
        ("2026-04-25", "Supervisory review due", "task_deadline_note.md"),
    ],
    "case_b": [
        ("2026-05-01", "Intake summary created for housing instability concerns", "intake_summary.md"),
        ("2026-05-04", "Phone number found no longer in service", "contact_note_1.md"),
        ("2026-05-09", "Caregiver provided new phone number and temporary residence information", "contact_note_2.md"),
        ("2026-05-12", "Provider noted difficulty maintaining contact", "provider_note.md"),
        ("2026-05-15", "Home visit completed at temporary residence", "visit_note_1.md"),
        ("2026-05-16", "Housing stabilization follow-up documented", "service_plan_excerpt.md / task_deadline_note.md"),
        ("2026-05-22", "Residence verification target date", "task_deadline_note.md"),
        ("2026-05-27", "Supervisory review scheduled", "task_deadline_note.md"),
    ],
    "case_c": [
        ("2026-06-01", "Intake summary created for missed appointment concerns", "intake_summary.md"),
        ("2026-06-04", "Initial caregiver contact attempted", "contact_note_1.md"),
        ("2026-06-08", "Caregiver reported transportation issues", "contact_note_2.md"),
        ("2026-06-10", "Provider note documented missed and completed appointments", "provider_note.md"),
        ("2026-06-14", "Home visit completed", "visit_note_1.md"),
        ("2026-06-15", "Service plan and deadline notes updated", "service_plan_excerpt.md / task_deadline_note.md"),
        ("2026-06-22", "Appointment attendance confirmation target date", "task_deadline_note.md"),
        ("2026-06-28", "Supervisory review scheduled", "task_deadline_note.md"),
    ],
}


st.sidebar.title("VisitBrief AI")
st.sidebar.caption("Fictional GovTech caseworker workspace")

persona = st.sidebar.selectbox(
    "View as",
    ["Caseworker View", "Supervisor View", "Intake Specialist View"]
)

cases = list_cases()
if not cases:
    st.error("No synthetic cases found. Check data/synthetic_cases.")
    st.stop()

selected_case = st.sidebar.selectbox("Assigned case", cases)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Case Records",
        "Timeline",
        "Tasks",
        "Calendar",
        "VisitBrief AI",
        "Evaluation",
    ]
)

st.sidebar.divider()
st.sidebar.caption("VisitBrief AI • Case Preparation Workspace")

documents = load_case_documents(selected_case)
meta = case_metadata[selected_case]
case_name = selected_case.replace("_", " ").title()

page_context = (
    f"Current page: {page}. Selected case: {case_name}. "
    f"Family: {meta['family']}. Focus: {meta['focus']}. "
    f"Status: {meta['status']}. Priority: {meta['priority']}. "
    f"Next action: {meta['next_action']} due {meta['next_date']}. "
    f"Supervisory review due {meta['review_due']}."
)

st.title("VisitBrief AI Workspace")
st.write("Fictional GovTech caseworker workspace for visit preparation.")

st.info(
    "Synthetic data only. This tool supports preparation and source review only. "
    "It does not make case decisions or recommendations."
)

st.write(f"**Persona:** {persona} | **Selected Case:** {case_name}")


def render_small_assistant():
    st.subheader("VisitBrief AI")
    st.caption("Ask about the selected case.")

    question = st.text_area(
        "Question",
        placeholder="Example: What follow-up items are open?",
        key=f"side_question_{page}",
        height=100
    )

    if st.button("Ask", key=f"side_ask_{page}", use_container_width=True):
        if question.strip():
            st.session_state["side_answer"] = answer_from_records(question, documents, page_context)
        else:
            st.session_state["side_answer"] = "Enter a question first."

    if st.button("Generate Visit Brief", key=f"side_brief_{page}", use_container_width=True):
        st.session_state["side_answer"] = generate_structured_visit_brief(documents)

    if st.session_state.get("side_answer"):
        st.markdown(st.session_state["side_answer"])


if page == "VisitBrief AI":
    st.header("VisitBrief AI Assistant")
    st.write("Ask factual questions about the selected case or generate a visit-preparation brief.")

    chat_key = f"chat_history_{selected_case}"

    if chat_key not in st.session_state:
        st.session_state[chat_key] = []

    full_question = st.text_area(
        "Ask a factual question",
        placeholder="Example: Are there upcoming deadlines?",
        height=130,
        key="full_ai_question"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ask Assistant", key="full_ask", use_container_width=True):
            if full_question.strip():
                answer = answer_from_records(full_question, documents, page_context)
                st.session_state[chat_key].append({"role": "user", "content": full_question})
                st.session_state[chat_key].append({"role": "assistant", "content": answer})
            else:
                st.warning("Enter a question first.")

    with col2:
        if st.button("Generate Visit Brief", key="full_brief", use_container_width=True):
            brief = generate_structured_visit_brief(documents)
            st.session_state[chat_key].append({"role": "user", "content": "Generate Visit Brief"})
            st.session_state[chat_key].append({"role": "assistant", "content": brief})

    with col3:
        if st.button("Clear Chat", key="clear_chat", use_container_width=True):
            st.session_state[chat_key] = []
            st.rerun()

    st.divider()

    if st.session_state[chat_key]:
        st.subheader("Conversation")
        for message in st.session_state[chat_key]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    else:
        st.caption("No conversation yet. Ask a question or generate a visit brief.")

    st.divider()
    st.subheader("Suggested Questions")
    st.write("- Summarize this page")
    st.write("- What follow-up items are open?")
    st.write("- Are there upcoming deadlines?")
    st.write("- Are there any conflicts?")
    st.write("- What information is missing or unverified?")
    st.write("- Should services be escalated?")

else:
    main_col, ai_col = st.columns([2.4, 1])

    with main_col:
        if page == "Dashboard":
            st.header(f"{case_name}: {meta['family']}")

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Status", meta["status"])
            m2.metric("Priority", meta["priority"])
            m3.metric("Open Tasks", meta["open_tasks"])
            m4.metric("Source Records", len(documents))

            st.subheader("Case Focus")
            st.write(meta["focus"])

            st.subheader("Preparation Progress")
            st.progress(meta["progress"] / 100)
            st.caption(f"{meta['progress']}% preparation checklist reviewed")

            st.subheader("Upcoming Work")
            st.write(f"**Next Action:** {meta['next_action']}")
            st.write(f"**Target Date:** {meta['next_date']}")
            st.write(f"**Supervisory Review Due:** {meta['review_due']}")

            st.subheader("Worker Summary")
            w1, w2, w3, w4 = st.columns(4)
            w1.metric("Assigned Cases", "8")
            w2.metric("Due This Week", "3")
            w3.metric("Needs Review", "2")
            w4.metric("Completed Visits", "14")

            if persona == "Supervisor View":
                st.subheader("Supervisor Review Queue")
                st.dataframe(
                    [
                        {"Case": "Case A", "Focus": "School attendance", "Review Due": "2026-04-25", "Status": "Needs source review"},
                        {"Case": "Case B", "Focus": "Housing stability", "Review Due": "2026-05-27", "Status": "Missing verification"},
                        {"Case": "Case C", "Focus": "Provider follow-up", "Review Due": "2026-06-28", "Status": "Timeline conflict"},
                    ],
                    use_container_width=True
                )

            if persona == "Intake Specialist View":
                st.subheader("Intake Verification Queue")
                st.dataframe(
                    [
                        {"Case": "Case A", "Missing Item": "Caregiver contact verification", "Status": "Open"},
                        {"Case": "Case B", "Missing Item": "Current residence", "Status": "Open"},
                        {"Case": "Case C", "Missing Item": "Complete provider attendance history", "Status": "Open"},
                    ],
                    use_container_width=True
                )

        elif page == "Case Records":
            st.header("Case Records")
            st.write("Select and review source records for the selected case.")

            selected_file = st.selectbox(
                "Source record",
                [doc["filename"] for doc in documents],
                key="case_record_selector"
            )

            selected_doc = next(doc for doc in documents if doc["filename"] == selected_file)

            st.subheader(selected_file)
            st.text_area(
                "Record content",
                selected_doc["content"],
                height=550,
                key=f"record_content_{selected_file}"
            )

        elif page == "Timeline":
            st.header("Case Timeline")
            st.write("Chronological view of selected case activity.")

            for date, event, source in timeline_data[selected_case]:
                st.subheader(date)
                st.write(event)
                st.caption(f"Source: {source}")
                st.divider()

        elif page == "Tasks":
            st.header("Tasks & Follow-Ups")

            task_rows = [
                {"Task": meta["next_action"], "Due": meta["next_date"], "Owner": persona.replace(" View", ""), "Status": "Open"},
                {"Task": "Review missing or unverified information", "Due": meta["review_due"], "Owner": persona.replace(" View", ""), "Status": "Open"},
                {"Task": "Review source records before visit", "Due": meta["next_date"], "Owner": persona.replace(" View", ""), "Status": "In Progress"},
                {"Task": "Prepare unresolved items for supervisory review", "Due": meta["review_due"], "Owner": "Supervisor", "Status": "Open"},
            ]

            st.dataframe(task_rows, use_container_width=True)

            st.subheader("Preparation Checklist")
            st.checkbox("Review intake summary", key="check_1")
            st.checkbox("Review recent contact notes", key="check_2")
            st.checkbox("Review provider/service notes", key="check_3")
            st.checkbox("Confirm deadlines", key="check_4")
            st.checkbox("Check missing or conflicting information", key="check_5")

        elif page == "Calendar":
            st.header("Calendar")

            st.subheader(meta["next_date"])
            st.write(f"**{meta['next_action']}**")
            st.write(f"Case: {case_name}")
            st.write("Type: Follow-up")

            st.divider()

            st.subheader(meta["review_due"])
            st.write("**Supervisory Review Due**")
            st.write(f"Case: {case_name}")
            st.write("Type: Review")

            st.divider()

            st.subheader(meta["next_date"])
            st.write("**Review Source Records**")
            st.write(f"Case: {case_name}")
            st.write("Type: Preparation")

        elif page == "Evaluation":
            st.header("Evaluation")
            st.write("Run baseline tests for factual retrieval and refusal behavior.")

            if st.button("Run Evaluation", use_container_width=True):
                results = run_evaluation(answer_from_records, documents, page_context)

                passed_count = sum(1 for result in results if result["passed"])
                total_count = len(results)

                st.metric("Tests Passed", f"{passed_count}/{total_count}")

                st.dataframe(
                    [
                        {
                            "Question": result["question"],
                            "Expected Signal": result["expected"],
                            "Passed": "✅" if result["passed"] else "❌",
                        }
                        for result in results
                    ],
                    use_container_width=True
                )

                if passed_count == total_count:
                    st.success("All baseline evaluation tests passed.")
                else:
                    st.warning("Some evaluation tests failed. Review retrieval and response behavior.")

    with ai_col:
        render_small_assistant()