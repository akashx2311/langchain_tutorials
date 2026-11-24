from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

chat_history = []

chat_history.append(SystemMessage(content="You are a helpful AI assistant"))

while True:
    usr_input = input('User: ')
    chat_history.append(HumanMessage(content=usr_input))
    if usr_input != 'EXIT':
        result = model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print("AI: ", result.content)
        
    else:
        break

print(chat_history)  