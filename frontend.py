import streamlit as st
import requests
import json

# Replace this with your API Gateway endpoint URL
API_URL = "https://rghc2hszub.execute-api.us-east-1.amazonaws.com/dev/blog-generation"

st.set_page_config(page_title="AI Blog Generator", page_icon="📝", layout="centered")

st.title("📝 AI Blog Generator")
st.write("Generate blogs using your AWS Bedrock Lambda function.")

# Blog topic input
blog_topic = st.text_input("Enter Blog Topic", placeholder="e.g., Benefits of learning AI in 2025")

if st.button("Generate Blog"):
    if not blog_topic.strip():
        st.error("Please enter a blog topic before generating.")
    else:
        with st.spinner("Generating blog... ⏳"):
            try:
                # Send request to Lambda API
                payload = {"blog_topic": blog_topic}
                headers = {"Content-Type": "application/json"}
                response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

                if response.status_code == 200:
                    resp_json = response.json()

                    blog_text = resp_json.get("blog", "")
                    if blog_text:
                        st.success("✅ Blog Generated Successfully!")
                        st.text_area("Generated Blog", blog_text, height=400)
                    else:
                        st.warning("API call succeeded but no blog content was returned.")
                        st.json(resp_json)  # Debugging
                else:
                    st.error(f"API call failed. Status code: {response.status_code}")
                    st.text(response.text)

            except Exception as e:
                st.error(f"Error while calling API: {e}")
