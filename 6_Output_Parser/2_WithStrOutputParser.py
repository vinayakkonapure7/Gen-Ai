from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

# prompt 1 Detailed report
template1=PromptTemplate(
    template="write detailed report on {topic}",
    input_variables=["topic"]         
    )

# prompt 2 summery

template2=PromptTemplate(
    template="write 5 line summery on the following text. \n {text} ",
    input_variables=["text"]
)

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

result=chain.invoke({"topic":"black hole"})

print(result)   