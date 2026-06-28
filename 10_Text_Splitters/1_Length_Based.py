from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader("007_Practical Machine Learning copy.pdf")

docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separator=""
) 

result=splitter.split_documents(docs)

print(result[6].page_content)