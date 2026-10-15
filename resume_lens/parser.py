from io import BytesIO
from pypdf import PdfReader


def extract_pdf_text(file_obj: BytesIO) -> str:
    """Extract selectable text from a PDF file-like object."""
    reader = PdfReader(file_obj)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages).strip()
