from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model=ChatOpenAI()
chathistory=[] #saving all chathistory it acts as memory and with this it has knowledge about past chat also
while True:
    user_input=input("You: ")
    chathistory.append(user_input)
    if user_input == "exit":
        break
    else:
        result=model.invoke(chathistory)
        chathistory.append(result.content)
        print("AI: ",result.content)

print("chathistory",chathistory)

#print(model.model_name) #gpt-3.5-turbo
