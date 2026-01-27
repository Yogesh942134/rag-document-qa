from PyPDF2 import PdfReader

def extract_text(file):
    text = ""

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    else:
        text = file.file.read().decode("utf-8")

    return text.strip()
