from langchain_community.embeddings import OpenAIEmbeddings
from steps.step0_environment.key import getOpenAiKey

# Initialize the instance of open AI Embedding class
def embedding():
    embeddings=OpenAIEmbeddings(openai_api_type=getOpenAiKey())
    return embeddings


def get_embedding(llm, text):
    response = llm.embeddings.create(
            input=chunk.page_content,
            model="text-embedding-ada-002"
        )
    return response.data[0].embedding

# Create embedding for KG
import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

def create_embedding(text):
        load_dotenv()
        llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = llm.embeddings.create(
            input=text,
            model="text-embedding-ada-002"
        )
        return response.data[0].embedding


# from langchain_community.embeddings import OpenAIEmbeddings
# from steps.step0_environment.key import getOpenAiKey


# # Initialize the instance of open AI Embedding class
# def embedding():
#     embeddings=OpenAIEmbeddings(openai_api_type=getOpenAiKey())
#     return embeddings

# import streamlit as st

# tag::llm[]
# Create the LLM

