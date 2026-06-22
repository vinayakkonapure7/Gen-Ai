from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableLambda
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal["positive","negative"] = Field(description="The sentiment of the feedback")

parser1=PydanticOutputParser(pydantic_object=Feedback)

prompt=PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative. \n {format_instructions}\n feedback: {feedback}",
    input_variables=["feedback"],
    partial_variables={"format_instructions":parser1.get_format_instructions()}
)

classifer_chain=prompt | model | parser1 
# print(classifer_chain.invoke({"feedback": "This is a worst smartphone"}))

prompt1=PromptTemplate(
    template="Write an appreciative thank you response to this positive feedback:\n{feedback}",
    input_variables=["feedback"]
)

prompt2=PromptTemplate(
    template="Write an apologetic  response to this negative feedback:\n{feedback}",
    input_variables=["feedback"]
)

conditional_chain=RunnableBranch(
    (lambda x: x.sentiment == "positive" , prompt1 | model | parser),
    (lambda x:x.sentiment == "negative", prompt2 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment.")
)

chain = classifer_chain | conditional_chain

result=chain.invoke({"feedback": "This is a worst smartphone"})
print(result)

chain.get_graph().print_ascii()