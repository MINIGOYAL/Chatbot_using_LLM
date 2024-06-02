import requests
import streamlit as st

def get_ollama_response(endpoint, input_text):
    response = requests.post(
        f"http://localhost:8000/{endpoint}/invoke",
        json={'input': {'topic': input_text}}
    )
    return response.json()['output']

# Streamlit framework
st.title('Langchain Demo With LLAMA2 API')

# Input for essay
input_text_essay = st.text_input("Write an essay on")
if input_text_essay:
    essay_response = get_ollama_response("essay", input_text_essay)
    st.write(essay_response)

# Input for poem
input_text_poem = st.text_input("Write a poem on")
if input_text_poem:
    poem_response = get_ollama_response("poem", input_text_poem)
    st.write(poem_response)
