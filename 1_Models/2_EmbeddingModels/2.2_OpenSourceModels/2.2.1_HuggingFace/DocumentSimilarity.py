from langchain_core.indexing import index
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache/EmbeddingModels/sentence-transformers-all-MiniLM-L6-v2'

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

user_query = "tell me about bumrah"

docs_embedding = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(user_query)

similarity_scores = cosine_similarity([query_embedding], docs_embedding)

index, score = sorted(list(enumerate(similarity_scores[0])), key=lambda x: x[1])[-1]

print(f"User query: {user_query}")
print(f"Similar document: {documents[index]}")
print(f"Similarity scores: {score}")
print(f"Most similar document: {documents[index]} with a similarity score of {score}")