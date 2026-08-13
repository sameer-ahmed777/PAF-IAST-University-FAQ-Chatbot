from search_engine import SearchEngine

engine = SearchEngine()

result = engine.search(
    "What is attendance policy?"
)
print(
    "Retrieved Chunks:",
    result
)
