import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

loader=TextLoader("linearRegression.txt", encoding= "utf-8")

docs=loader.load()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template="write summery of the following topic \n {topic}",
    input_variables=["topic"]
)

chain= prompt | model | parser

result=chain.invoke({"topic":docs[0].page_content})

print(result)