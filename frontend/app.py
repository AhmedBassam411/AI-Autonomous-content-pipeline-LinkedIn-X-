import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/generate-content"


st.set_page_config(page_title="Autonomous Content Pipeline")

st.title("Autonomous Content Pipeline")

st.write("Generate blogs and social media content using AI agents.")


with st.form("content_form"):

    topic = st.text_input("Topic")

    audience = st.text_input("Target Audience")

    platform = st.selectbox(
        "Choose Platform",
        ["linkedin", "twitter"]
    )

    submit = st.form_submit_button("Generate Content")


if submit:

    payload = {
        "topic": topic,
        "audience": audience,
        "platform": platform
    }

    with st.spinner("Generating content..."):

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.subheader("Generated Social Post")
            st.markdown(result["post"])

        else:
            st.error("Failed to generate content")