"""

This module checks initializing pinecone , checking existing index, if not present then create it

"""
from pinecone import Pinecone,ServerlessSpec
from pinecone.exceptions import PineconeApiException

def CheckAndCreateIndex(index_name, pc):
    try:
        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=1536,
                metric='euclidean',
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-west-2'
                )
            )
            response = {"message": f"Index: {index_name} created successfully"}
            return response  
        
        else:
            response = {"message": f"Index: {index_name} already exists"}
    except PineconeApiException as e:
            print(f"Error: {e}")
    finally:
            print("Always ececuted")
            return response






