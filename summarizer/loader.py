from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os

def load_pdf(file) -> str:
    """
    Takes an uploaded PDF file and returns extracted text
    """

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    documents = loader.load()

    # Clean up temp file
    os.remove(tmp_path)

    # Combine all pages into one string
    full_text = "\n".join(doc.page_content for doc in documents)
    return full_text
