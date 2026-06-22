from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chat_templete=ChatPromptTemplate([
    ("system","You are a helpfull {domian} expert"),
    ("human","explain in simple terms, what is {topic}")
])

prompt=chat_templete.invoke({"domian":"cricket","topic":"LBW"})

# result=model.invoke(prompt)
# print(result.content)
print(chat_templete)