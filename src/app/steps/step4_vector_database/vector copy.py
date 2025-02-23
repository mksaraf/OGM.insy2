import streamlit as st
from steps.step7_llm_model.llm import llm, embeddings
from steps.step5_knowledge_graph.graph import graph

# tag::import_vector[]
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
# end::import_vector[]
# tag::import_chain[]
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
# end::import_chain[]

# tag::import_chat_prompt[]
from langchain_core.prompts import ChatPromptTemplate
# end::import_chat_prompt[]

# Define multiple Neo4jVector instances for different indexes
neo4jvector_moviePlots = Neo4jVector.from_existing_index(
    embeddings,                              
    graph=graph,                             
    index_name="moviePlots",                 
    node_label="Movie",                      
    text_node_property="plot",               
    embedding_node_property="plotEmbedding", 
    retrieval_query="""
RETURN
    node.plot AS text,
    score,
    {
        title: node.title,
        directors: [ (person)-[:DIRECTED]->(node) | person.name ],
        actors: [ (person)-[r:ACTED_IN]->(node) | [person.name, r.role] ],
        tmdbId: node.tmdbId,
        source: 'https://www.themoviedb.org/movie/'+ node.tmdbId
    } AS metadata
"""
)

neo4jvector_reviews = Neo4jVector.from_existing_index(
    embeddings,                              
    graph=graph,                             
    index_name="movieReviews",               
    node_label="Review",                     
    text_node_property="reviewText",         
    embedding_node_property="reviewEmbedding", 
    retrieval_query="""
RETURN
    node.reviewText AS text,
    score,
    {
        reviewer: node.reviewer,
        rating: node.rating,
        movieTitle: node.movieTitle,
        source: node.sourceUrl
    } AS metadata
"""
)

# Create retrievers for each index
retriever_moviePlots = neo4jvector_moviePlots.as_retriever()
retriever_reviews = neo4jvector_reviews.as_retriever()

# Combine the retrievers by defining a function that queries both and merges the results
class CombinedRetriever:
    def __init__(self, retrievers):
        self.retrievers = retrievers
    
    def get_relevant_documents(self, query):
        results = []
        for retriever in self.retrievers:
            results.extend(retriever.get_relevant_documents(query))
        return results

combined_retriever = CombinedRetriever([retriever_moviePlots, retriever_reviews])

# Define the prompt template
instructions = (
    "Use the given context to answer the question."
    "If you don't know the answer, say you don't know."
    "Context: {context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", instructions),
        ("human", "{input}"),
    ]
)

# Define the chain with the combined retriever
question_answer_chain = create_stuff_documents_chain(llm, prompt)
plot_retriever = create_retrieval_chain(
    combined_retriever, 
    question_answer_chain
)

# Function to get movie plot and additional information
def get_movie_plot(input):
    return plot_retriever.invoke({"input": input})
