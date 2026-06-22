from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
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

prompt1=template1.invoke({"topic":"black hole"})

result=model.invoke(prompt1)

prompt2=template2.invoke({"text":result.content})

result1=model.invoke(prompt2)


print(result1.content)