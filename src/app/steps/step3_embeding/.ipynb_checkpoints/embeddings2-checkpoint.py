from langchain_openai import OpenAIEmbeddings

# Create the Embedding model
'''
generate vector embeddings for text inputs to represent text data as numerical vectors,
'''
embeddings = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)
