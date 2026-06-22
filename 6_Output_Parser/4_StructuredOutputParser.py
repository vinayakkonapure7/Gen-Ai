# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain.output_parsers.structured import (
#     StructuredOutputParser,
#     ResponseSchema
# )
# from dotenv import load_dotenv

# load_dotenv()

# model=ChatOpenAI(model="gpt-4o-mini",max_completion_tokens=30)

# schema=[
#     ResponseSchema(name="fact1", description="fact 1 about the topic"),
#     ResponseSchema(name="fact2", description="fact 2 about the topic"),
#     ResponseSchema(name="fact3", description="fact 3 about the topic")
# ]

# parser=StructuredOutputParser.from_response_schema(schema)

# template=PromptTemplate(
#     template="give me 3 fact about {topic} \n {formate_instructions}",
#     input_variables=["topic"],
#     partial_variables={"formate_instructions":parser.get_format_instructions()}
# )

# chain= template | model | parser

# result=chain.invoke({"topic":"blackhole"})

# print(result)

# # import langchain_core.output_parsers as op

# # print(dir(op))
# #  note:StructuredOutputParser is not avaliable after version 1+ langchain