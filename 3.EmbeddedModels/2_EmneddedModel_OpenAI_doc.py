from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)
documents=["mumbai is captial of maharashtra ","dehil is captial of india","kolkata is captial of westbengal"]

result=embedding.embed_documents(documents)

print(str(result))