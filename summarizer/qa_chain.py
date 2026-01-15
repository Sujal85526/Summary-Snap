from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from summarizer.llm import get_llm

def get_qa_chain(vectordb):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
    )

    return ConversationalRetrievalChain.from_llm(
        llm=get_llm(),
        retriever=vectordb.as_retriever(),
        memory=memory,
        return_source_documents=True,
    )
