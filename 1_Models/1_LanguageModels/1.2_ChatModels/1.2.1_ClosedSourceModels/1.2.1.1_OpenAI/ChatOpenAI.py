# Import necessary libraries
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a ChatOpenAI instance
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Invoke the model with a prompt
response = model.invoke("What is the capital of India?")

# Print the response content
print(response.content)