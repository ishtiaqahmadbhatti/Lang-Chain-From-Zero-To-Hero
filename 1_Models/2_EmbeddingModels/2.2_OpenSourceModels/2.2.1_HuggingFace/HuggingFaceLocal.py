from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache/EmbeddingModels/sentence-transformers-all-MiniLM-L6-v2'

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

vector = embedding.embed_query("What is the capital of Pakistan?")
print(str(vector))