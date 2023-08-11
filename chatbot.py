import streamlit as st
import openai

# Initialize the GPT-4 API client with the secret key
openai.api_key = st.secrets["openai"]["gpt4_api_key"]

def get_gpt4_response(prompt):
    response = openai.Completion.create(engine="GPT-4", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

st.title("My GPT-4 Chatbot")

user_input = st.text_input("Ask me anything!")
if user_input:
    response = get_gpt4_response(user_input)
    st.write(f'Chatbot: {response}')
