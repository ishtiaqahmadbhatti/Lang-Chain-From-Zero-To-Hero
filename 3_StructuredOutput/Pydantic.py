from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

class Review(BaseModel):
    key_themes:list[str] = Field(..., description="The key themes of the review, such as plot, acting, cinematography, etc.")
    summary: str = Field(..., description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neu"] = Field(..., description="The sentiment of the review which can be positive (pos), negative (neg), or neutral (neu)")
    name: Optional[str] = Field(default=None, description="The name of the reviewer if available, otherwise None")

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
structured_model = model.with_structured_output(Review)

review = "The movie was fantastic! The plot was engaging and the acting was top-notch. by Ishtiaq Ahmad Bhatti"
response = structured_model.invoke(review)
print("Structured Output:",response)
print(type(response))
print("Key Themes:", response.key_themes)
print("Summary:", response.summary)
print("Sentiment:", response.sentiment)
print("Name:", response.name)