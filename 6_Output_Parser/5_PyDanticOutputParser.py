from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

class Person(BaseModel):

    name:str = Field(description="name of person")
    age:int = Field(gt=19, description="age of person")
    city:str =Field(description="the person city where lives")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="""
Generate realistic information for a person from {place}.

Include:
- name
- age (must be greater than 18)
- city
\n
{format_instructions}
""",
    input_variables=["place"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain=template | model | parser
result=chain.invoke({"place":"indian"})
print(result)
print(type)