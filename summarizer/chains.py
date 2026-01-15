from langchain.chains import LLMChain
from summarizer.llm import get_llm
from summarizer.prompts import SUMMARY_PROMPT

def summarize_text(text: str) -> str:
    llm = get_llm()

    chain = LLMChain(
        llm=llm,
        prompt=SUMMARY_PROMPT,
    )

    result = chain.invoke({"text": text})
    return result["text"]
