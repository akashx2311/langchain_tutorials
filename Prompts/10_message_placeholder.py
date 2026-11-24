from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

# chat template

chat_template = ChatPromptTemplate([
    ('system','you are helful customer assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
    ])

# load chat history

chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
model = ChatGroq(model = 'openai/gpt-oss-120b')
    

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is the my case?' })

# print(prompt)

result = model.invoke(prompt)

print(result.content)

