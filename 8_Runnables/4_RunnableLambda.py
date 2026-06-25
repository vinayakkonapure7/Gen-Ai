from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnableSequence,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI()

parser=StrOutputParser()

def word_count(text):
    return len(text.split())

prompt=PromptTemplate(
    template="write joke about {topic}",
    input_variables=["topic"]
)

joke_gen_chain=RunnableSequence(prompt, model, parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "count":RunnableLambda(word_count) 
})


parallel_chain2=RunnableParallel({
    "joke":RunnablePassthrough(),
    "count":RunnableLambda(lambda x: len(x.split())) 
})

final_chain=RunnableSequence(joke_gen_chain, parallel_chain)

result=final_chain.invoke({"topic":"water"})

final_result=""" {} \n word count - {}""".format(result["joke"],result["count"])

print(final_result)
print(final_chain.get_graph().print_ascii())