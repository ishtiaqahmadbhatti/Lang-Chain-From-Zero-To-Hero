from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
import os
os.environ['HF_HOME'] = r'D:\huggingface_cache\Qwen3-0.6B'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="write notes about this: \n{text}?",
    input_variables=["text"],
)

prompt2 = PromptTemplate(
    template="please give 5 questions and answers about this: \n{text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="please give the notes -> {notes} and questions and answers -> {quiz}?",
    input_variables=["notes", "quiz"],
)

parallel_chain = RunnableParallel(
{
    "notes": RunnableSequence(prompt1 | model | parser),
    "quiz": RunnableSequence(prompt2 | model | parser),
}
)

merge_chain = RunnableSequence(prompt3 , model , parser)

final_chain = RunnableSequence(parallel_chain | merge_chain)

my_text = """
1.4. Support Vector Machines
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""
response = final_chain.invoke({'text': my_text})

print("Response:")
print(response)

final_chain.get_graph().print_ascii()