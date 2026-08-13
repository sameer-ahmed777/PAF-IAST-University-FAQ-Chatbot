import streamlit as st
st.set_page_config(
    page_title="🎓 Pak-Austria Fachhochschule (PAF-IAST) University FAQ Chatbot",
    page_icon="🎓",
    layout="wide"
)
# Sidebar
st.sidebar.title("PAF-IAST University FAQ System")
st.sidebar.info("""
Ask questions about:
• Attendance
• Admissions
• Scholarships
• Hostel Rules
• Library Policies
• Examinations
""")
# Main Page
st.title("🎓 Pak-Austria Fachhochschule (PAF-IAST) University FAQ Chatbot")
question = st.text_input("Ask Your Question")
if question:
    question = question.lower()
    if "attendance" in question:
        answer = """
### Attendance Policy
1. Minimum attendance requirement is 75%.
2. Students with attendance shortage may be barred from examinations.
3. Approved medical leave should be supported by documentation.
4. Students are responsible for maintaining attendance throughout the semester.
"""
    elif "scholarship" in question:
        answer = """
### Scholarship Policy
1. Scholarships may be awarded on a merit or need basis.
2. Students must maintain satisfactory academic performance.
3. Scholarship applications should be submitted through the designated university office.
4. Providing false information may result in cancellation of the scholarship.
"""
    elif "hostel" in question:
        answer = """
### Hostel Regulations
1. Students must follow hostel timings.

2. Visitors are allowed only according to university policy.

3. Damage to hostel property may result in disciplinary action.

4. Students must follow all security procedures.
"""

    elif "library" in question:

        answer = """
### Library Regulations

1. Library resources must be used responsibly.

2. Late return of books may result in fines.

3. Lost or damaged books must be replaced.

4. Students should carry their library card while borrowing books.
"""

    elif "admission" in question:

        answer = """
### Admission Policy

1. Students must submit complete academic documents.

2. Admissions are subject to verification.

3. Providing fraudulent information can lead to cancellation of admission.

4. Eligibility requirements must be fulfilled before enrollment.
"""

    elif "exam" in question or "examination" in question:

        answer = """
### Examination Rules

1. University ID cards are mandatory during examinations.

2. Mobile phones are not allowed in the examination hall.

3. Cheating and unfair means are strictly prohibited.

4. Students must follow all invigilator instructions.
"""
    else:

        answer = """
Information not found in the current knowledge base.
Please ask about:

• Attendance
• Admissions
• Scholarships
• Hostel Rules
• Library Policies
• Examinations
"""
    st.success("Answer Retrieved")
    st.markdown(answer)