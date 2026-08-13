from embeddings import EmbeddingModel
from faiss_manager import FAISSManager
import numpy as np
class SearchEngine:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.manager = FAISSManager()
        sample_embeddings = np.random.rand(
            6,
            384
        ).astype("float32")
        self.manager.add_embeddings(
            sample_embeddings
        )
    def search(self, question):
        query_embedding = (
            self.embedding_model.encode(
                [question]
            )
        )
        distances, indices = (
            self.manager.search(
                query_embedding
            )
        )
        return indices