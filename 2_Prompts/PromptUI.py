from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import load_prompt
import streamlit as st
import os

os.environ['HF_HOME'] = 'D:\huggingface_cache\Qwen3-0.6B'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation',
)
model = ChatHuggingFace(llm=llm)

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

prompt = load_prompt("research_paper_explanation_template.json")


if st.button("Generate Explanation"):
    chain = prompt | model

    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    st.subheader("Generated Explanation")
    st.write(response.content)