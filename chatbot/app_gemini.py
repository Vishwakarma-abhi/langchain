# In this Episode, we will be building a chatbot using LangChain and Gemini model.
#  The chatbot will be able to answer questions based on a given context.

import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# 1. Load the GOOGLE_API_KEY from the .env file
load_dotenv()

# 2. Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest", temperature=0.7, max_output_tokens=256)

# 3. Create a Prompt Template 
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert data science tutor."),
    ("user", "Explain the concept of {topic} in simple terms.")
    ])

# StreamLit Framework to create a simple web interface for the chatbot

st.title("LangChain Chatbot with Gemini Model")
input_text = st.text_input("Ask a question about data science:")


# Output parser to format the response
output_parser = StrOutputParser()



# 4. Chain the Prompt Template with the LLM together using the Lanchain Expression Language (LCEL)
chain =  prompt | llm | output_parser

if input_text:
    response = chain.invoke({"topic": input_text})
    st.write(response)
