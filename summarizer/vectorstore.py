from langchain_community.vectorstores import Chroma
from summarizer.embeddings import get_embeddings
from summarizer.splitter import split_text
from langchain.docstore.document import Document

def build_vectorstore(text: str):
    chunks = split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=get_embeddings(),
    )
    return vectordb
