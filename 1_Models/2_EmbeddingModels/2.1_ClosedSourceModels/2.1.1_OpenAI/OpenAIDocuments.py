# Import necessary libraries
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an OpenAIEmbeddings instance
embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents = [
    "What is the capital of India?",
    "What is the capital of France?",
    "What is the capital of Germany?"
]

# Generate embeddings for all documents
vectors = embedding.embed_documents(documents)

# Print the generated embeddings
print(str(vectors))