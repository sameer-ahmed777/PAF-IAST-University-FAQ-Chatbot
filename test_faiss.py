import numpy as np
from faiss_manager import FAISSManager
# Create FAISS Manager
manager = FAISSManager()
# Generate dummy embeddings
embeddings = np.random.rand(
    10,
    384
).astype("float32")
# Add embeddings into FAISS
manager.add_embeddings(
    embeddings
)
# Generate query embedding
query = np.random.rand(
    1,
    384
).astype("float32")
# Search similar vectors
distances, indices = manager.search(
    query
)
print("Search Results:")
print(indices)
print("Distances:")
print(distances)