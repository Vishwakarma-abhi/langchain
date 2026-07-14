import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time


load_dotenv()


if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")

    st.session_state.docs = st.session_state.loader.load()

    st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)


    st.session_state.final_documents= st.session_state.text_splitter.split_documents(
        st.session_state.docs[:50]
    )

    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)


st.title("ChatGroq Demo")
llm = ChatGroq(model="llama-3.3-70b-versatile")

prompt = ChatPromptTemplate.from_template(
    """
Answer the Questions based on the provided COntent only .
Please provide the most accurate response baesd on the contxext and based on the quesition
<content>
{context}
Questions: {input}
"""
)

document_chain = create_stuff_documents_chain(llm,prompt)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever,document_chain)

prompt = st.text_input("Input Your Prompt Here")

if prompt:
    start = time.process_time()
    response = retrieval_chain.invoke({"input": prompt})
    print("Resppnse time :",time.process_time()-start)
    st.write(response['answer'])

    # with streamlit expander
    with st.expander("Document Similarity Search"):
        # find the relevant chunks
        for i , doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("------------------------------------------")
            