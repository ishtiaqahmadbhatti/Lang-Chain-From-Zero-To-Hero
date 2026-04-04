# Import necessary libraries
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an OpenAIEmbeddings instance
embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

# Generate embeddings for a text
vector = embedding.embed_query("What is the capital of India?")

# Print the generated embeddings
print(str(vector))