from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

chat_history = []

while True:
    usr_input = input('User: ')
    chat_history.append(usr_input)
    if usr_input != 'EXIT':
        result = model.invoke(chat_history)
        chat_history.append(result.content)
        print("AI: ", result.content)
        
    else:
        break

print(chat_history)    
    