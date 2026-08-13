"""
PDF Ingestion Module
This module:
1. Reads PDF files
2. Extracts text
3. Displays extracted content
"""
from pathlib import Path
from pypdf import PdfReader
class PDFProcessor:
    """Handles PDF processing operations."""
    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """Extract text from a PDF file."""
        reader = PdfReader(pdf_path)
        extracted_text = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text.append(page_text)
        return "\n".join(extracted_text)
def main():
    pdf_path = (
        "data/raw/PAF_IAST_University_Rules_Handbook_Sample.pdf"
    )
    if not Path(pdf_path).exists():
        print("ERROR: PDF file not found.")
        return
    print("=" * 60)
    print("PDF FOUND SUCCESSFULLY")
    print("=" * 60)
    text = PDFProcessor.extract_text(pdf_path)
    print("\nExtracted Text Preview:\n")
    print(text[:1000])
if __name__ == "__main__":
    main()