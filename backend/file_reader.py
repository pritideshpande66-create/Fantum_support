from PyPDF2 import PdfReader
from docx import Document

def read_file(path):
    # PDF reading
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return " ".join(page.extract_text() or "" for page in reader.pages)

    # DOCX reading
    if path.endswith(".docx"):
        doc = Document(path)
        return " ".join(p.text for p in doc.paragraphs)

    return ""


