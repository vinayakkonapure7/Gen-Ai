from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableSequence
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


joke_gen_chain=RunnableSequence(prompt, model, parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt1, model, parser)
})

final_chain=RunnableSequence(joke_gen_chain, parallel_chain)

result=final_chain.invoke({"topic":"water"})

print(result)

print(final_chain.get_graph().print_ascii())
