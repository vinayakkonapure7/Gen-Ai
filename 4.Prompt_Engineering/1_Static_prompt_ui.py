from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model=ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=30)

st.header("Reasearch Tool")
user_input= st.text_input("enter your prompt")

if st.button("summarize"):
    result=model.invoke(user_input)
    st.write(result.content)

# streamlit run /Users/vinayak/LangChain/4.Prompt_Engineering/prompt_ui.py
# control +c stop