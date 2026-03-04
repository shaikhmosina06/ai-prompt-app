import streamlit as st
import requests

st.set_page_config(page_title="AI Prompt Generator", layout="wide")

st.title("🔥 AI Prompt Generator (Free Version)")
st.write("Powered by Hugging Face 🤗")

api_key = st.secrets.get("HUGGINGFACE_API_KEY")

if not api_key:
    st.error("Please add HUGGINGFACE_API_KEY in Streamlit secrets.")
    st.stop()

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {api_key}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

prompt = st.text_area("Enter your prompt")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            output = query({
                "inputs": prompt
            })

        if isinstance(output, list):
            st.success(output[0]["generated_text"])
        else:
            st.error("Error generating response.")
    else:
        st.warning("Please enter a prompt.")



