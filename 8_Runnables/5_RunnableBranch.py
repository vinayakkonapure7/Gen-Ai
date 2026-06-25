from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda,RunnablePassthrough,RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template="write detailed report on {topic}",
    input_variables=["topic"]
)

prompt1=PromptTemplate(
    template="summrize the report on {text}",
    input_variables=["text"]
)

report_gen_chain=prompt | model | parser

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>200, RunnableSequence(prompt1, model, parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain, branch_chain)

result=final_chain.invoke({"topic": "Russia vs Ukrine"})

print(result)