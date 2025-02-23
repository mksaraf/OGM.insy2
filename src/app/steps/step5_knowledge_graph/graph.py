import streamlit as st

# tag::graph[]
from langchain_community.graphs import Neo4jGraph

graph = Neo4jGraph(
    url=st.secrets["NEO4J_URI"],
    username=st.secrets["NEO4J_USERNAME"],
    password=st.secrets["NEO4J_PASSWORD"],
)
#end::graph[]

# import streamlit as st
# from langchain_community.graphs import Neo4jGraph

# def graph():
#     # Create a Neo4jGraph instance
#     kgraph = Neo4jGraph(
#         url=st.secrets["NEO4J_URI"],
#         username=st.secrets["NEO4J_USERNAME"],
#         password=st.secrets["NEO4J_PASSWORD"],
#     )
#     return kgraph

# # Test the graph function
# kgraph = graph()

# # Check if the kgraph object is not None
# if kgraph is not None:
#     print("Neo4jGraph instance created successfully")
# else:
#     print("Failed to create Neo4jGraph instance")

# # You can also test the connection to the Neo4j database
# try:
#     kgraph.run("MATCH (n) RETURN n LIMIT 10")
#     print("Connection to Neo4j database successful")
# except Exception as e:
#     print(f"Error connecting to Neo4j database: {e}")