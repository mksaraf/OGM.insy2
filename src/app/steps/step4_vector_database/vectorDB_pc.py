from steps.step0_environment.key import getPineconeKey
from pinecone import Pinecone

# Connect to Vector-DB Pinecone
def connectToPinecone():
    pc=Pinecone(api_key=getPineconeKey())
    return pc