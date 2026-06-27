from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

loader=PyPDFLoader("007_Practical Machine Learning copy.pdf")

docs=loader.load()

parser=StrOutputParser()

prompt=PromptTemplate(
    template="write summery of the following topic \n {topic}",
    input_variables=["topic"]
)

chain= prompt | model | parser

result=chain.invoke({"topic":docs[0].page_content})
print(result)

# print(docs[1].page_content)
# print(docs[2].metadata)