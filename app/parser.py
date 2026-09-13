import fitz


def extract_text_from_pdf(pdf_bytes: bytes) -> str:

    document = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text