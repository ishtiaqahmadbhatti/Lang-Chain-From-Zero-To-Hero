from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

prompt1 = PromptTemplate(
    template="write details about {topic}?",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="please summarize in  5 line about \n{text}?",
    input_variables=["text"],
)
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({'topic': 'LangChain'})

print("Response:")
print(response)