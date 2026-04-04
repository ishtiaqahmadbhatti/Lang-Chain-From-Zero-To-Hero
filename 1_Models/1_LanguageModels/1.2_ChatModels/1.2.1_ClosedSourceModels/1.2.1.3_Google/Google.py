from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
response = model.invoke("What is the difference between and purpose of langchain, langgraph, langsmith and deepagent?")
print(response.content)