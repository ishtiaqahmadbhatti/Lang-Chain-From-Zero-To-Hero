from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os

os.environ['HF_HOME'] = 'D:\huggingface_cache\Qwen3-0.6B'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You are a helpful assistant that provides information about the latest research papers in AI."),
    HumanMessage(content="What is SQL?"),
]

response = model.invoke(messages)

messages.append(AIMessage(content=response.content))

print("Chat history:", messages)