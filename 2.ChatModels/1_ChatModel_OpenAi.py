from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=10)

result=model.invoke("write poem on cricket")

print(result.content) # without .content it shows metadata also like how amny token used etc.. 