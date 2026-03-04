import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Prompt Generator", layout="wide")

st.title("🔥 AI Prompt Generator")
st.write("Generate AI responses using trendy prompts.")



if api_key:
    client = OpenAI(api_key=api_key)

prompt_library = [
    {"title": "Instagram Caption Generator",
     "content": "Write a trendy Instagram caption with emojis about travel."},

    {"title": "Resume Improvement",
     "content": "Improve this resume summary to make it more professional:"},

    {"title": "Startup Idea Generator",
     "content": "Generate a unique AI-based startup idea in India."},

    {"title": "Coding Helper",
     "content": "Explain this Python code step by step:"},

    {"title": "Islamic Reminder",
     "content": "Write a short Islamic motivational reminder."}
]

search = st.text_input("🔎 Search Prompt")

filtered_prompts = [
    p for p in prompt_library
    if search.lower() in p["title"].lower()
]

st.subheader("🔥 Trendy Prompts")

for prompt in filtered_prompts:
    st.markdown(f"### {prompt['title']}")
    st.write(prompt["content"])

    if st.button(f"Generate - {prompt['title']}"):
        if api_key:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt["content"]}
                ]
            )
            st.success("✅ AI Response:")
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please enter your API key first.")

st.subheader("✍️ Create Your Own Prompt")

custom_prompt = st.text_area("Enter your prompt")

if st.button("Generate Custom Prompt"):
    if user_input:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional AI prompt engineer."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )

        st.success(response.choices[0].message.content)

    else:
        st.warning("Please enter a prompt.")
        st.write(response.choices[0].message.content)
    else:

        st.warning("Enter API key and prompt.")
