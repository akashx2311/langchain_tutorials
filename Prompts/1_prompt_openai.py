from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model='openai/gpt-oss-120b')


st.header("Research Tool")
usr_input =  st.text_input("Enter your prompt")
result = model.invoke(usr_input)
if st.button('Summarize'):
    st.write(result.content)

