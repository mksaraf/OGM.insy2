from langchain.chat_models import ChatOpenAI
from steps.step0_environment.key import getOpenAiKey

model='gpt-3.5-turbo'
temperature=0.0

# Create llm
def llmModel(model, temperature):
    llm = ChatOpenAI(
        openai_api_key=getOpenAiKey(),
        model_name=model,
        temperature=temperature
    )
    return llm








