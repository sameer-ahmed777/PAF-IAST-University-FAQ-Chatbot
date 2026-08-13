from ingest import PDFProcessor
from chunker import TextChunker
from embeddings import EmbeddingModel
from faiss_manager import FAISSManager
pdf_path = (
    "data/raw/PAF_IAST_University_Rules_Handbook_Sample.pdf"
)
# Extract text
text = PDFProcessor.extract_text(
    pdf_path
)
# Create chunks
chunks = TextChunker.chunk_text(
    text
)
print(
    f"Total Chunks: {len(chunks)}"
)
# Generate embeddings
embedding_model = EmbeddingModel()
embeddings = embedding_model.encode(
    chunks
)
print(
    f"Embeddings Shape: {embeddings.shape}"
)
# Create FAISS Index
manager = FAISSManager()
manager.add_embeddings(
    embeddings
)
print(
    "FAISS Index Created Successfully!"
)