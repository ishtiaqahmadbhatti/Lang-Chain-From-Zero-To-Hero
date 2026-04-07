from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

os.environ['HF_HOME'] = r'D:\huggingface_cache\Qwen3-0.6B'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write details about {topic}?",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="please summarize in  5 line about \n{text}?",
    input_variables=["text"],
)

Chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

response = Chain.invoke({"topic": "Python programming language"})

print(response)