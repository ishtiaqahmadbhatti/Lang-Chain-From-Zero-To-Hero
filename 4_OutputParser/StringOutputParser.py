from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['HF_HOME'] = r'D:\huggingface_cache\Qwen3-0.6B'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="write detailed pragraph about {topic} .",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="write 5 line summary of given text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

response = chain.invoke({'topic': 'artificial intelligence'})

print(response)