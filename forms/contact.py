import streamlit as st
import re
import pandas as pd
from datetime import datetime

def is_valid_email(email):
    """Validate email format using regex."""
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_pattern, email))

def sanitize_input(text):
    """Basic input sanitization to prevent injection attacks."""
    harmful_chars = r"[<>{}\[\];]"
    return re.sub(harmful_chars, "", text.strip())

def log_submission(name, email, message):
    """Log form submission to a CSV file."""
    log = {
        "timestamp": datetime.now(),
        "name": name,
        "email": email,
        "message": message
    }
    df = pd.DataFrame([log])
    # Append to CSV; create header only if file doesn't exist
    df.to_csv("contact_logs.csv", mode="a", index=False, header=not pd.io.common.file_exists("contact_logs.csv"))

def contact_form():
    """Render and handle the contact form."""
    # Custom styling for form inputs and button
    st.markdown(
        """
        <style>
        .stTextInput > div > input, .stTextArea > div > textarea {
            border-radius: 8px;
            border: 1px solid #1E90FF;
            padding: 10px;
        }
        .stButton > button {
            background-color: #1E90FF;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Rate limiting with session state
    if "submit_count" not in st.session_state:
        st.session_state.submit_count = 0

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name", placeholder="Enter your full name", key="name")
        email = st.text_input("Email", placeholder="Enter your email address", key="email")
        message = st.text_area("Message", placeholder="Write your message here...", key="message", height=150)
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            # Rate limiting check
            if st.session_state.submit_count >= 3:
                st.error("Too many submissions. Please try again later.", icon="⏳")
                return
            st.session_state.submit_count += 1

            # Sanitize inputs
            name = sanitize_input(name)
            email = sanitize_input(email)
            message = sanitize_input(message)

            # Validation checks
            if not name:
                st.error("Please enter your name", icon="🧑")
                return

            if not email:
                st.error("Please enter your email", icon="📧")
                return

            if not is_valid_email(email):
                st.error("Please enter a valid email address", icon="📧")
                return

            if not message:
                st.error("Please enter your message", icon="📝")
                return

            try:
                # Save to CSV
                log_submission(name, email, message)
                st.success("Message sent successfully! I'll get back to you soon.", icon="🚀")

            except Exception as e:
                st.error(f"Failed to save message: {str(e)}", icon="🚫")
                return

# Optional: Email sending function (uncomment and configure if needed)
"""
def send_email(name, email, message):
    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(f"From: {name}\nEmail: {email}\nMessage: {message}")
    msg["Subject"] = "Contact Form Submission"
    msg["From"] = "your_email@gmail.com"  # Replace with your email
    msg["To"] = "your_email@gmail.com"    # Replace with your email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_app_password")  # Use App Password
        server.send_message(msg)

# To use email instead of CSV, call send_email(name, email, message) in the try block
# and add 'smtplib' to requirements.txt.
"""

# For local testing
if __name__ == "__main__":
    st.set_page_config(page_title="Contact Form Test")
    contact_form()