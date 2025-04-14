import streamlit as st

# Centralized page configuration
st.set_page_config(
    page_title="Idowu Adamo's Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling for sidebar and nav
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #F9F9F9;
    }
    .stButton > button {
        background-color: #1E90FF;
        color: white;
        border-radius: 8px;
    }
    a {
        color: #1E90FF;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define pages with error handling
try:
    about_page = st.Page(
        "./views/about_me.py",
        title="About Me",
        icon="👩‍💻",
        default=True
    )
except Exception as e:
    st.error(f"Failed to load About Me page: {e}")

try:
    projects_page = st.Page(
        "./views/projects.py",
        title="Projects",
        icon="🚀"
    )
except Exception as e:
    st.error(f"Failed to load Projects page: {e}")

try:
    chatbot_page = st.Page(
        "./views/chatbot.py",
        title="Portfolio Assistant",
        icon="💬"
    )
except Exception as e:
    st.error(f"Failed to load Chatbot page: {e}")

# Navigation setup
page = st.navigation(
    {
        "Info": [about_page],
        "Work": [projects_page, chatbot_page],
    }
)

# Sidebar content
# st.logo("./assets/id-noble_logo.png")
st.sidebar.markdown(
    """
    <p style='text-align: center; font-size: 1.2em;'>
        Idowu Adamo's Portfolio
    </p>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    Made with ❤️ by [Idowu Adamo](https://github.com/IdowuAdamo)  
    Connect: [LinkedIn](https://www.linkedin.com/in/adamoidowu/) | [Email](mailto:idowuadamo2904@gmail.com) | [X](https://x.com/IdowuAdamo)
    """,
    unsafe_allow_html=True
)

# Run navigation
page.run()