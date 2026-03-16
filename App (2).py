import streamlit as st
import requests

st.set_page_config(page_title="AI Prompt Generator", layout="wide")

st.title("🔥 AI Prompt Generator")
st.write("Powered by Hugging Face 🤗")

api_key = st.secrets.get("HUGGINGFACE_API_KEY")

if not api_key:
    st.error("Please add HUGGINGFACE_API_KEY in Streamlit secrets.") 
    st.stop()

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {api_key}"
}

def query(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# -------------------------
# 🌟 Popular Prompts Section
# -------------------------

st.subheader("🌟 Popular Prompts")

popular_prompts = [
    "Write a trendy Instagram caption about Goa trip.",
    "Generate a unique AI startup idea in India.",
    "Write a short Islamic motivational reminder.",
    "Improve this resume summary professionally.",
    "Explain Python loops in simple language."
]

selected_prompt = st.selectbox("Choose a popular prompt:", popular_prompts)

if st.button("Generate Popular Prompt"):
    with st.spinner("Generating response..."):
        result = query(selected_prompt)

    if isinstance(result, list) and "generated_text" in result[0]:
        st.success("✅ AI Response:")
        st.write(result[0]["generated_text"])
    else:
        st.error("Model is loading or rate limit exceeded. Try again in 20 seconds.")

# -------------------------
# ✍️ Custom Prompt Section
# -------------------------

st.subheader("✍️ Create Your Own Prompt")

custom_prompt = st.text_area("Enter your custom prompt")

if st.button("Generate Custom Prompt"):
    if custom_prompt:
        with st.spinner("Generating response..."):
            result = query(custom_prompt)

        if isinstance(result, list) and "generated_text" in result[0]:
            st.success("✅ AI Response:")
            st.write(result[0]["generated_text"])
        else:
            st.error("Model is loading or rate limit exceeded. Try again.")
    else:
        st.warning("Please enter a prompt.")



