from langchain_community.embeddings import OpenAIEmbeddings
from steps.step0_environment.key import getOpenAiKey


# Initialize the instance of open AI Embedding class
def embedding():
    embeddings=OpenAIEmbeddings(openai_api_type=getOpenAiKey())
    return embeddings