from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template="genrate tweet about following {topic}",
    input_variables=["topic"]
)

prompt1=PromptTemplate(
    template="genrate linkedin post about following {topic}",
    input_variables=["topic"]
)

parallel_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt, model, parser),
    "linkedin":RunnableSequence(prompt1, model, parser)
})

result=parallel_chain.invoke({"topic":"AI"})

print(result)

print(result["tweet"])
print(result["linkedin"])

print(parallel_chain.get_graph().print_ascii())


