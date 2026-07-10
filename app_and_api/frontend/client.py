# Web App / Mobile App API Client

import streamlit as st
import requests

def get_gemini_response(input_text: str):
    response = requests.post(
        "http://localhost:9000/essay/invoke",
        json={"input": {"topic": input_text}}
    )

    return response.json()['output']['content'][0]["text"]



def get_ollama_response(input_text: str):
    response = requests.post(
        "http://localhost:9000/poem/invoke",
        json={"input": {"topic": input_text}}
    )
    # Always Check what is the response structure of the LLM Model then only return the Response
    return response.json()['output']


st.title("Langchain Demo With Gemini and LLAMA2 API")
gemini_text= st.text_input("Write an Essay on ")
ollama_text = st.text_input("Write a poem on")

if gemini_text:
    st.write(get_gemini_response(gemini_text))

if ollama_text:
    st.write(get_ollama_response(ollama_text))