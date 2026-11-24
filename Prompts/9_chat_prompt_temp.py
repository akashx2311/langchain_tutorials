from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')


prompt_template = ChatPromptTemplate([
    ('system','You are helpful {domain} expert'),
    ( 'human', 'Explain the term {topic}')
    # SystemMessage(content='You are helpful {domain} expert'),
    # HumanMessage(content = 'Explain the term {topic}')
])

template = prompt_template.invoke({'domain':'cricket','topic':'wide ball'})

result = model.invoke(template)

print(result.content)