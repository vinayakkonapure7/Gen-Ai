from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

template=PromptTemplate(
    template="genreate a detailed report on {topic}",
    input_variables=["topic"]
)

template1=PromptTemplate(
    template="genrate a 5 pointer summary from the following text \n {text}",
    input_variables=["text"]
)

parser=StrOutputParser()

chains=template | model | parser | template1 | model | parser

result = chains.invoke({"topic":"tenis"})
print(result)