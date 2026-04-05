from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
import json

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

# Define the expected output structure
class Personality(BaseModel):
    name: str = Field(description="Name of the personality")
    age: int = Field(description="Age of the personality")
    profession: str = Field(description="Profession of the personality")

class PersonalitiesList(BaseModel):
    personalities: List[Personality] = Field(description="List of famous personalities")

parser = PydanticOutputParser(pydantic_object=PersonalitiesList)

template = PromptTemplate(
    template="write five name, age and profession of famous personalities in Pakistan \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt = template.format()
response = model.invoke(prompt)

# Handle response content - could be string or list
response_text = response.content
if isinstance(response_text, list):
    response_text = ''.join([item.get('text', '') if isinstance(item, dict) else str(item) for item in response_text])

parsed_response = parser.parse(response_text)

print("Parsed Response:")
print(json.dumps(parsed_response if isinstance(parsed_response, dict) else parsed_response.model_dump(), indent=2))