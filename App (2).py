

       import streamlit as st
from openai import OpenAI

# Page config
st.set_page_config(page_title="AI Prompt Generator", layout="wide")

st.title("🔥 AI Prompt Generator")
st.write("Generate AI responses using trendy prompts.")

# Get API key from secrets
api_key = st.secrets.get("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    st.warning("⚠️ Please add your OPENAI_API_KEY in Streamlit secrets.")
    client = None

# Prompt library
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

# Search
search = st.text_input("🔎 Search Prompt", "")

filtered_prompts = [
    p for p in prompt_library
    if search.lower() in p["title"].lower()
]

st.subheader("🔥 Trendy Prompts")

# Generate buttons
for prompt in filtered_prompts:
    st.markdown(f"### {prompt['title']}")
    st.write(prompt["content"])

    if st.button(f"Generate - {prompt['title']}"):
        if client:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt["content"]}
                ]
            )
            st.success("✅ AI Response:")
            st.write(response.choices[0].message.content)
        else:
            st.warning("Please configure your API key.")

# Custom Prompt Section
st.subheader("✍️ Create Your Own Prompt")

custom_prompt = st.text_area("Enter your prompt")

if st.button("Generate Custom Prompt"):
    if client and custom_prompt:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional AI prompt engineer."},
                {"role": "user", "content": custom_prompt}
            ],
            temperature=0.7
        )

        st.success("✅ AI Response:")
        st.write(response.choices[0].message.content)

    elif not custom_prompt:
        st.warning("Please enter a prompt.")
    else:
        st.warning("Please configure your API key.")


