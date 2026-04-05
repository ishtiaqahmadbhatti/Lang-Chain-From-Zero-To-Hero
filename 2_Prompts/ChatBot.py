from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os

os.environ['HF_HOME'] = 'D:\huggingface_cache\Qwen3-0.6B'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)
chat_history = [
    SystemMessage(content="You are a helpful assistant that provides information about the latest research papers in AI.")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat...")
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"ChatBot: {response.content}")

print("Chat session ended.")
print("Chat history:", chat_history)