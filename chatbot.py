"""
University Chatbot Module
"""
class UniversityChatbot:
    def generate_response(
        self,
        question: str,
        context: str
    ) -> str:

        return f"""
Question:
{question}
Answer:
{context}
"""
if __name__ == "__main__":
    chatbot = UniversityChatbot()
    response = chatbot.generate_response(
        "What is the attendance requirement?",
        "Students must maintain 75% attendance."
    )
    print(response)