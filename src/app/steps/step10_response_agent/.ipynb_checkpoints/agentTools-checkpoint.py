from langchain.agents import Tool
from steps.step9_retrieval.retrievalQA import retrievalQA


def agentTools(retrieval_qa):
    tools = [Tool(
            name='Knowledge Base',
            func=retrieval_qa.invoke,
            description=(
                'use this tool when answering general knowledge queries to get '
                'more information about the topic'
            ))]
    return tools

# # Call the function and assign the returned value to a variable
# agent_tools = agentTools(retrieval_qa)