import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Open AI client
if not OPENAI_API_KEY:
    st.error("Open AI API key not found. Please check your .env file.", icon="🔐")
    st.stop()

client = OpenAI(api_key=OPENAI_API_KEY)

# Custom styling
st.markdown(
    """
    <style>
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .user-message {
        background-color: #DCF8C6;
        text-align: right;
    }
    .assistant-message {
        background-color: #E6F3FF;
        text-align: left;
    }
    .stButton > button {
        background-color: #1E90FF;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and introduction
st.markdown("<h1 style='text-align: center; color: #2E2E2E;'>Portfolio Assistant Chatbot</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center;'>
    Hi! I'm a chatbot built by Idowu Adamo, a Data Scientist and ML Engineer. 
    Ask me about Idowu's skills, projects, or anything related to Data Science and Machine Learning!
    </p>
    """,
    unsafe_allow_html=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm here to tell you about Idowu Adamo's work. Want to know about his projects like the Meeting Minutes Generator, E-commerce Price Comparison System, or his skills in Data Science?"
        }
    ]

# Display chat history
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.markdown(f"<div class='stChatMessage user-message'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='stChatMessage assistant-message'>{message['content']}</div>", unsafe_allow_html=True)

# Chat input
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:", placeholder="Type your question here...", key="chat_input")
    submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Prepare context for Open AI
        system_prompt = """
        You are a friendly and professional chatbot created by Idowu Adamo, a Data Scientist and ML Engineer with 3 years of experience. Your role is to showcase Idowu's portfolio and answer questions about his skills, projects, and background. Here’s some info to guide your responses:

        - **Background**: Idowu has a Diploma in Data Science from AltSchool Africa, is a self-taught programmer, and excels as a team-player and problem-solver.
        - **Skills**: Proficient in Python, SQL, MySQL, Matplotlib, Seaborn, Plotly, Tableau, PowerBI, Logistic Regression, Random Forest, XGBoost, Neural Networks, GPT, BERT, Transformers, Streamlit, Selenium, BeautifulSoup, Pandas, Scikit-learn, Gradio.
        - **Projects**:
          - **Meeting Minutes Generator**: A Generative AI app using Python, GPT-4, Llama, and Gradio to create meeting summaries and action items from audio, reducing summary time by ~60%. Hosted on Hugging Face: https://idowenst-meeting-minutes-generator.hf.space.
          - **E-commerce Price Comparison and Product Recommendation System**: An AI platform built with Python, Streamlit, Selenium, BeautifulSoup, and Pandas to help Nigerians find quality deals, saving ~20% on purchases. GitHub: https://github.com/IdowuAdamo/Neural-Drip.
          - **Customer Segmentation and Targeted Marketing**: A model using Python, Scikit-learn, Pandas, and Matplotlib to classify retail customers, improving purchase rates by 15%. GitHub: https://github.com/IdowuAdamo/RFM-Customer-Segmentation.
        - **Experience**: 3 years in Data Science and Machine Learning, building models, visualizations, and interactive apps.
        - **Tone**: Be approachable, professional, and enthusiastic. Share brief project details and direct users to the Projects page or contact form for more info.
        - **Limits**: If the question is unrelated to Idowu’s portfolio (e.g., general trivia), gently redirect to his skills or suggest contacting him.

        If the user asks to contact Idowu, suggest: "I’d love to connect you with Idowu! Please use the contact form in the 'About Me' section to reach out."
        """
        messages = [
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ]

        try:
            # Call Open AI API
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            assistant_reply = response.choices[0].message.content.strip()
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

            # Rerun to update chat display
            st.rerun()

        except Exception as e:
            st.error(f"Error generating response: {str(e)}", icon="🚫")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ by Idowu Adamo | Powered by Open AI</p>",
    unsafe_allow_html=True
)