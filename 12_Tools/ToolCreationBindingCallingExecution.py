from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv

load_dotenv()

# tool create
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

# print(multiply.invoke({'a':3, 'b':4}))

# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

# tool binding
llm  = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

# response = llm.invoke('hi')

# print(response)

llm_with_tools = llm.bind_tools([multiply])

# response  = llm_with_tools.invoke('Hi how are you')

# print(response)

query = HumanMessage('can you multiply 3 with 1000')

messages = [query]

# print(messages)

result = llm_with_tools.invoke(messages)

messages.append(result)

# print(messages)

tool_result = multiply.invoke(result.tool_calls[0])

# print(tool_result)

messages.append(tool_result)

# print(messages)

final_response = llm_with_tools.invoke(messages).content

print(final_response)