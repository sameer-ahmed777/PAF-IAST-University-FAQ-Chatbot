from chunker import TextChunker

sample_text = (
    "Attendance must be 75 percent. " * 50
)

chunks = TextChunker.chunk_text(
    sample_text
)

print("Total Chunks:", len(chunks))