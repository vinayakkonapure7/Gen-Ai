from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template="write joke about {topic}",
    input_variables=["topic"]
)

prompt1=PromptTemplate(
    template="explain the follwing joke {text}"
)

chain=RunnableSequence(prompt, model, parser, prompt1, model, parser)

result=chain.invoke({"topic":"water"})

print(result)
print(chain.get_graph().print_ascii())