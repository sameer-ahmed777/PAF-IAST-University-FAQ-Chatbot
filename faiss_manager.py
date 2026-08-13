import faiss
import numpy as np


class FAISSManager:

    def __init__(self, dimension=384):

        self.index = faiss.IndexFlatL2(
            dimension
        )

    def add_embeddings(
        self,
        embeddings
    ):
        self.index.add(
            embeddings.astype("float32")
        )
    def search(
        self,
        query_embedding,
        top_k=3
    ):
        distances, indices = (
            self.index.search(
                query_embedding.astype(
                    "float32"
                ),
                top_k
            )
        )
        return distances, indices