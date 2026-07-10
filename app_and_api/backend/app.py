from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# langserve will be used to create the APIs
from langserve import add_routes
import uvicorn
import os 
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)

gemini_llm = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")
ollama_llm = OllamaLLM(model="qwen2.5:0.5b")

# Add the Routes


prompt1 = ChatPromptTemplate.from_template(
    "Write me an Poem about {topic} around 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me an Poem about {topic} around 100 words"
)


add_routes(
    app,
    prompt1|gemini_llm,
    path="/essay"
)

add_routes(
    app,
    prompt2|ollama_llm,
    path="/poem"
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=9000)