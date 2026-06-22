from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import json

load_dotenv()

model=ChatOpenAI()

#chat templete
chat_templete=ChatPromptTemplate([
        ("system",
     """You are a customer support agent.

     Always use the information available in chat history.
     Do not ask for information already present in chat history.
     """),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human","{query}")
])

# load chat history

#with txt
chat_history=[]
with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())

#with json

# chat_history=[]
# with open("chat_history.json") as f:
#     data=json.load(f)

# for msg in data:
#     if msg["role"]== "human":
#         chat_history.append(HumanMessage(content=msg["content"]))
#     else:
#         chat_history.append(AIMessage(content=msg["content"]))
# # print(chat_history)


# create prompt
prompt=chat_templete.invoke({"chat_history":chat_history,"query":"what is my refund status"})

result=model.invoke(prompt)
print(result.content)