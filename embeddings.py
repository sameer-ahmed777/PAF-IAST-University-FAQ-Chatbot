import numpy as np
class EmbeddingModel:
    def encode(self, texts):
        embeddings = []
        for text in texts:
            embeddings.append(
                np.random.rand(384)
            )
        return np.array(embeddings)
if __name__ == "__main__":
    model = EmbeddingModel()
    result = model.encode(
        ["Attendance must be 75 percent"]
    )
    print(result.shape)