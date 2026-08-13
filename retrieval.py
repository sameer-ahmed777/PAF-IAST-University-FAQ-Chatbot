"""
Retrieval Module
----------------
Handles retrieval of relevant information
from the FAISS vector database.
"""
import numpy as np
class Retriever:

    def search(
        self,
        query_embedding,
        document_embeddings
    ):
        """
        Find the most relevant document chunk.
        """
        similarities = np.dot(
            document_embeddings,
            query_embedding
        )
        best_match = np.argmax(
            similarities
        )
        return best_match
if __name__ == "__main__":
    retriever = Retriever()
    query_embedding = np.array(
        [1, 2, 3]
    )
    document_embeddings = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [0, 1, 1]
    ])
    result = retriever.search(
        query_embedding,
        document_embeddings
    )
    print(
        f"Best Match Index: {result}"
    )