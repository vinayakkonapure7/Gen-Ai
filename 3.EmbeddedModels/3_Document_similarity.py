from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-small",dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query="tell me about virat kohli"

doc_embedding=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

scores=cosine_similarity([query_embedding],doc_embedding)[0] #here comes in list of list so just select innerlist[0]
index, score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1] #(Doc Index, Similarity Score) [0,0.63905739] sort by score high score at last[-1]
print(query)
print(documents[index])
print("cosine_similarity is : ",score)