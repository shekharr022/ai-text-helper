import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Text Helper")
choice = st.radio("Choose Action", ["Summarize", "Rewrite"])
text = st.text_area("Enter your text here:")

if st.button("Generate"):
    if text.strip():
        prompt = f"{choice} the following text:\n{text}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.write(response.choices[0].message["content"])
    else:
        st.warning("Please enter some text.")
