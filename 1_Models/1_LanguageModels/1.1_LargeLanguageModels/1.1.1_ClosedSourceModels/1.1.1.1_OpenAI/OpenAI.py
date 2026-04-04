# Import necessary libraries
from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI LLM with the desired model
model = OpenAI(model='gpt-3.5-turbo-instruct')

# Invoke the Model with a prompt
result = model.invoke("What is the capital of India")

# Print the result
print(result)