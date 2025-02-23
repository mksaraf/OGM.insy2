
"""

Purpose: To run the virtual agent Insy using streamlit app
Created By: Geetika Manish Saraf
Created On: July 24 2024
Version: 1
How to run locally: 
Come to the path OGM.insy/src/app/ 
the command is  streamlit run mainagent_streamlit_FreezeCode.py
Example:
(.venv) geetikasaraf@geetikas-mbp OGM.Thesis.Geetika % streamlit run mainagent_streamlit_FreezeCode.py
How to run on web: The Insy application was successfully deployed on https://ogminsy.streamlit.app

"""

# Import library
from steps.step0_environment.key import getOpenAiKey, getPineconeKey
from steps.step1_data_loading.dataSources import checkDataSource, dataLoad
from steps.step2_data_chunking.chunking import chunking
from steps.step3_embeding.embeddings import embedding
from steps.step4_vector_database.Index import CheckAndCreateIndex
from steps.step4_vector_database.createVectorstore import CallVectorStore
from steps.step4_vector_database.uploadVectorsToIndex import UploadVectorsToIndex
from steps.step4_vector_database.vectorDB_pc import connectToPinecone
from steps.step6_prompt_eng.prompt import prompt
from steps.step7_llm_model.llm_models import llmModel
from steps.step8_memory.memory import addMemory
from steps.step8_memory.memory import conversationalMemory
from steps.step9_retrieval.qa import qa
#from steps.step9_retrieval.crc import crChain
from steps.step9_retrieval.retrievalAugQAChain import raQaChain
from steps.step10_response_agent.agentTools import agentTools
from steps.step10_response_agent.agentIntialization import intializeAgent
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import warnings
warnings.filterwarnings('ignore')

# Arguments
openAiKey=getOpenAiKey()
model='gpt-3.5-turbo'
temperature=0.0
chainType="stuff"
index_name='life-insurance-index1'

import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from openai import OpenAI


pc=connectToPinecone()
index = pc.Index(index_name)
pc_vectorstore = CallVectorStore(index)
Client=OpenAI(api_key=openAiKey)

# Set up Langchain models
model_name = st.selectbox("Select an LLM model", ["gpt-4o", "gpt-4", "gpt-3.5-turbo"])
llm_model = llmModel(model_name, temperature)
qa2 = qa(chainType,pc_vectorstore,llm_model)
tools=agentTools(qa2)
memory=conversationalMemory()
agent=intializeAgent(tools,llm_model,memory)

st.title("INSY: A Life Insurance Virtual Agent")
st.write(
    """
This application was developed by Geetika Saraf. Insy offers a chat experience based on a knowledge base, allowing you to ask questions and receive relevant information regarding Life Insurance.

"""
)

# st.info(
#     """
# **The template has the following parts**
# 1. A prompt template providing the instructions to ChatGPT.
# 2. Uploading PDFs and creating a vectordb using OpenAI embeddings.
# 3. Searching the vectordb for parts of the PDF that semantically match the question.
# 4. Calling ChatGPT with the extra PDF context and the user question.
# """
# )

# Define vector store
st.session_state["vectordb"] = pc_vectorstore

# Define prompt tempate
prompt_template = """
    You are financial expert that combines your knowledge about life insurance and data in vector db.
"""
# Define prompt
prompt = st.session_state.get("prompt", [{"role": "system", "content": "none"}])

for message in prompt:
    if message["role"]!= "system":
           with st.chat_message(message["role"]):
                st.write(message["content"])

# User input: question
question = st.chat_input("Hi I am Insy! How can I help you?")
if question:
    vectordb = st.session_state.get("vectordb", None)
    if not vectordb:
        st.error("You need to provide a PDF")
        st.stop()

    search_results = vectordb.similarity_search(question, k=5)
    pdf_extract = "\n ".join([result.page_content for result in search_results])

    prompt[0] = {
        "role": "system",
        "content": prompt_template.format(pdf_extract=pdf_extract),
    }

    prompt.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        botmsg = st.empty()  

    # response = []
    #response = agent(search_results, prompt)
    response = list(agent(search_results, prompt).values())
    result = ""
    for chunk in Client.chat.completions.create(
        model="gpt-3.5-turbo", messages=prompt, stream=True
    ):
        text = chunk.choices[0].delta.content
        if text is not None:
            response.append(text)
            result = "".join(response).strip()

            botmsg.write(result)

    prompt.append({"role": "assistant", "content": result})

    st.session_state["prompt"] = prompt

if __name__ == "__main__":
    st.write("App is running")




