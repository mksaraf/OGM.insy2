from langchain.chains import RetrievalQA


# Create Retrieval QA
def retrievalQA(chainType,vectorstore,llm):
    retrieval_qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type=chainType,
        retriever=vectorstore.as_retriever()
    )
    return retrieval_qa

