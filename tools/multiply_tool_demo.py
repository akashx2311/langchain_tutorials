from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq

load_dotenv()


@tool
def multiply(a: int, b: int) -> int:
  """This is tool for the multiplication"""
  return a * b


model = ChatGroq(model="openai/gpt-oss-120b")
model_with_tools = model.bind_tools([multiply])

# 1. Start the conversation history
messages = [HumanMessage("what is the multiplication of 2 and 3")]

# 2. First LLM call: LLM decides to use the tool
ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)  # Add the LLM's tool-call request to history

# 3. Execute the tool(s) requested by the LLM
for tool_call in ai_msg.tool_calls:
  # Calling .invoke() on the @tool with the entire tool_call dict
  # automatically returns a properly formatted ToolMessage!
  tool_msg = multiply.invoke(tool_call)
  messages.append(tool_msg)

# 4. Second LLM call: LLM reads the ToolMessage and writes the final output
final_response = model_with_tools.invoke(messages)
print(final_response.content)