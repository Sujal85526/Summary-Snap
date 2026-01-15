from langchain.prompts import PromptTemplate

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["text"],
    template=(
        "You are an expert summarizer.\n"
        "Summarize the following text in clear, concise language:\n\n"
        "{text}"
    ),
)
