
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Whenever we want to do third party integration we need import from Lanchain Community
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

llm = OllamaLLM(model="qwen2.5:0.5b")

# 3. Create a Prompt Template 
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert data science tutor."),
    ("user", "Explain the concept of {topic} in simple terms.")
    ])

# StreamLit Framework to create a simple web interface for the chatbot

st.title("LangChain Chatbot with Ollama Qwen Model")
input_text = st.text_input("Ask a question about data science:")


# Output parser to format the response
output_parser = StrOutputParser()



# 4. Chain the Prompt Template with the LLM together using the Lanchain Expression Language (LCEL)
chain =  prompt | llm | output_parser

if input_text:
    response = chain.invoke({"topic": input_text})
    st.write(response)
