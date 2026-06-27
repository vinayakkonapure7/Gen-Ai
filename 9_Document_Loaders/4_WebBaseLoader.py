from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

url="https://www.croma.com/apple-macbook-pro-14-2-inch-m5-16gb-1tb-macos-space-black-/p/318768?srsltid=AfmBOorxKe15khLvmYiZsRlhsRid4dPma4Scws1RfpsIQzbpZEaBxW4c6jE"

loader=WebBaseLoader(url)

docs=loader.load()

prompt=PromptTemplate(
    template="answer the following Question \n {question} from the following text {text}",
    input_variables=["question",'text']
)

chain=prompt | model | parser 
result=chain.invoke({"question":"what is product name","text":docs[0].page_content})

print(result)
# print(docs[0].page_content)
# print(len(docs))