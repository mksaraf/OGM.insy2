import streamlit as st

# tag::llm[]
# Create the LLM
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model=st.secrets["OPENAI_MODEL"],
)
# end::llm[]

# tag::embedding[]
# Create the Embedding model
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)
# end::embedding[]


# # Initialize llm for OpenAI model
# import streamlit as st
# from langchain_openai import ChatOpenAI

# def llmModel():
#     '''
#     The llm object is now an instance of the LLM, 
#     which can be used to generate text or respond to user input.
#     '''
#     llm = ChatOpenAI(
#         openai_api_key=st.secrets["OPENAI_API_KEY"],
#         model=st.secrets["OPENAI_MODEL2"],
#     )
#     return llm
