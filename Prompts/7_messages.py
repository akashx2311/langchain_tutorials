from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

messages = [
      SystemMessage(content='You are a helpful assistant'),
      HumanMessage(content='What is the capital of india?')
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)


