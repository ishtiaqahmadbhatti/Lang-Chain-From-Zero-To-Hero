from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

prompt = PromptTemplate(
    template="write details about {topic}?",
    input_variables=["topic"],
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'topic': 'LangChain'})

print("Response:")
print(response)