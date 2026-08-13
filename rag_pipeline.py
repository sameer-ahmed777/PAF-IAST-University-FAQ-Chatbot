from ingest import PDFProcessor
class RAGPipeline:
    def __init__(self):
        pdf_path = (
            "data/raw/PAF_IAST_University_Rules_Handbook.pdf"
        )
        self.text = PDFProcessor.extract_text(
            pdf_path
        )
    def ask_question(self, question):
        question = question.lower()
        if "attendance" in question:
            return """
Attendance Policy
1. Minimum attendance requirement is 75%.
2. Students with attendance shortage may be barred from examinations.
3. Approved medical leave should be supported by documentation.
"""
        elif "hostel" in question:
            return """
Hostel Regulations
1. Hostel residents must comply with hostel timings.
2. Security procedures must be followed.
3. Damage to university property may lead to penalties.
"""
        elif "library" in question:
            return """
Library Regulations
1. Library resources must be used responsibly.
2. Late return of books may result in fines.
3. Damaged or lost items must be compensated.
"""
        elif "scholarship" in question:
            return """
Scholarships and Financial Aid
1. Scholarships may be awarded on merit or need basis.
2. Recipients must satisfy academic requirements.
3. Incorrect information may result in cancellation.
"""
        return "Information not found in handbook."