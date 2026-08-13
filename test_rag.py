from rag_pipeline import RAGPipeline
rag = RAGPipeline()
answer = rag.ask_question(
    "What is attendance policy?"
)
print("\nAnswer:\n")
print(answer)