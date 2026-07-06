from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    pass
    try:
        reader = PdfReader(pdf_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        return f"Error reading PDF: {e}"