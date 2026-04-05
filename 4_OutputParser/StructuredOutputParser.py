from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

parser = StructuredOutputParser.from_response_schemas(
    [
        ResponseSchema(name="name", description="Name of the person"),
        ResponseSchema(name="age", description="Age of the person"),
        ResponseSchema(name="profession", description="Profession of the person")
    ]
)

template = PromptTemplate(
    template="write five name, age and profession of famous personalities in this world \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt = template.format()

response = model.invoke(prompt)

structured_response = parser.parse(response.content)

print("Structured Response:", structured_response)


