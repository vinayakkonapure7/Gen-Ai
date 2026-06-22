from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini")

parser=JsonOutputParser()

templete=PromptTemplate(
    template="give me facts about {topic} \n {formate_instruction}",
    input_variables=['topic'],
    partial_variables={"formate_instruction":parser.get_format_instructions()}
)

# method 1

# prompt=templete.format({'topic':"black hole"})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

# print(final_result)
# # print(prompt)

# method 2

chain=templete | model | parser
result1=chain.invoke({'topic':"black hole"})
print(result1)
