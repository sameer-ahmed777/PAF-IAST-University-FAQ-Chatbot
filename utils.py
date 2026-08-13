import streamlit as st

st.set_page_config(
    page_title="RAG University FAQ Chatbot",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 RAG University FAQ Chatbot")

st.markdown("""
Welcome to the University FAQ Chatbot.

You can ask questions about:

- Admissions
- Attendance
- Examinations
- Scholarships
- Hostel Rules
- Library Policies
- Academic Regulations
""")
question = st.text_input(
    "Ask Your Question"
)
if question:
    st.success("Question Received Successfully")
    st.write(f"You Asked: {question}")