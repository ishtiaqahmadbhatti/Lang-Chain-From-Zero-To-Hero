from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('human', "What is {topic}?")
])

prompt = chat_template.invoke(
    {
        "domain":"Cricket",
        "topic":"T20 World Cup"
    }
)

print("Generated Prompt:")
print(prompt)