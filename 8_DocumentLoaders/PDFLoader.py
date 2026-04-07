from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('resume.pdf')

docs = loader.load()

print(len(docs))
print("***********************Start Page Content****************************")
print(docs[2].page_content)
print("***********************End Page Content****************************")
print("***********************Start Metadata****************************")
print(docs[2].metadata)
print("***********************End Metadata****************************")