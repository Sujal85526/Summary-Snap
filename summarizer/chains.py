from langchain.chains.summarize import load_summarize_chain
from summarizer.llm import get_llm
from summarizer.splitter import split_text
from langchain.docstore.document import Document

def summarize_text(text: str) -> str:
    llm = get_llm()

    chunks = split_text(text)

    docs = [Document(page_content=chunk) for chunk in chunks]

    chain = load_summarize_chain(
        llm=llm,
        chain_type="map_reduce",
    )

    result = chain.invoke(docs)
    return result["output_text"]
