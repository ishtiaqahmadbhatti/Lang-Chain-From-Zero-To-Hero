from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

# Json Schema
JsonSchema = {
    "title": "Review",
    "description": "A review of a movie",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "The key themes of the review, such as plot, acting, cinematography, etc."
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg", "neu"],
            "description": "The sentiment of the review which can be positive (pos), negative (neg), or neutral (neu)"
        },
        "name": {
            "type": ["string", "null"],
            "description": "The name of the reviewer if available, otherwise None"
        }
    },
}
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
structured_model = model.with_structured_output(JsonSchema)

review = "The movie was fantastic! The plot was engaging and the acting was top-notch. by Ishtiaq Ahmad Bhatti"
response = structured_model.invoke(review)
print("Structured Output:",response)
print(type(response))
