from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model=OpenAIEmbeddings()

splitter=SemanticChunker(
    model,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

text="""
Ketchup was originally sold as medicine in the 1830s, far before it became a staple condiment. Meanwhile, in astronomy, it takes sunlight exactly 8.3 minutes to reach Earth. Back on land, the iconic Statue of Liberty requires an extensive exterior paint job every few years due to environmental wear.

The world's largest desert is actually Antarctica, which qualifies due to its incredibly low annual precipitation. In a completely different realm, the first computer mouse was constructed out of wood by Douglas Engelbart in 1964. Far away from technology, a single healthy honeybee colony can produce up to 100 kilograms of honey in just one season.
"""

result=splitter.split_text(text)

print(len(result))
print(result[0])