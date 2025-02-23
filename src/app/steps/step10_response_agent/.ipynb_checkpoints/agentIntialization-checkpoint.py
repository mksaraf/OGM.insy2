from langchain.agents import initialize_agent

def intializeAgent(tools,llm,memory):
    agent = initialize_agent(
        agent='chat-conversational-react-description',
        tools=agent_tools,
        llm=llm,
        verbose=True,
        max_iterations=10,
        early_stopping_method='generate',
        memory=memory
    )
    return agent