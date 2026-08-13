"""
Text Chunking Module
"""
class TextChunker:
    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 500
    ):
        chunks = []
        for i in range(
            0,
            len(text),
            chunk_size
        ):
            chunks.append(
                text[i:i + chunk_size]
            )
        return chunks
        from src.chunker import TextChunker
sample_text = (
    "Attendance must be 75 percent. " * 50
)
chunks = TextChunker.chunk_text(
    sample_text
)
print("Total Chunks:", len(chunks))