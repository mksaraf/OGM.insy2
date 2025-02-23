"""

This module defines how to get open AI Key

"""
import os
import openai
from dotenv import load_dotenv, find_dotenv

def getOpenAiKey():
    _ = load_dotenv(find_dotenv()) # read local .env file
    openai.api_key = os.environ['OPENAI_API_KEY']
    return openai.api_key
    
def getPineconeKey():
    _ = load_dotenv(find_dotenv()) # read local .env file
    pinecone_api_key = os.environ['PINECONE_API_KEY']
    return pinecone_api_key

# openai_key = getOpenAiKey()
# pinecone_key = getPineconeKey()
# print(openai_key)
# print(pinecone_key)