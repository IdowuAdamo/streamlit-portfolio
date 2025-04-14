import streamlit as st
try:
    from forms.contact import contact_form
except ImportError:
    st.error("Contact form module not found. Please check the file path.")

# Contact form dialog
@st.dialog("Contact Me")
def show_contact_form():
    try:
        contact_form()
    except Exception as e:
        st.error(f"Error loading contact form: {e}")

# Title with custom styling
st.markdown("<h1 style='text-align: center; color: #2E2E2E;'>About Me</h1>", unsafe_allow_html=True)

# Experience and Qualification Section
st.markdown("## Experience and Qualifications")
st.markdown("---")

col1, col2 = st.columns([1, 2], gap="medium", vertical_alignment="center")

with col1:
    # Commented out image section
    st.markdown("<p style='text-align: center;'>[Profile photo placeholder]</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h2 style='color: #1E90FF;'>Idowu Adamo</h2>", unsafe_allow_html=True)
    st.markdown("**Data Scientist | ML Engineer**")
    if st.button("📬 Contact Me", key="contact_button"):
        show_contact_form()
    st.markdown(
        """
        - 🕒 3 years of experience in Data Science and Machine Learning
        - 🎓 Diploma in Data Science from AltSchool Africa
        - 💻 Self-taught programmer
        - 🤝 Excellent team-player and problem-solver
        """
    )

# Skills Section with Tabs
st.markdown("## Skills")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Programming", "Data Visualization & Tools", "Modeling & LLM"])

with tab1:
    st.markdown(
        """
        - 🐍 **Python**: Advanced scripting, automation, and ML pipelines
        - 🗄️ **SQL**: Query optimization and database management
        - 🌐 **MySQL**: Relational database design and querying
        """
    )

with tab2:
    st.markdown(
        """
        - 📊 **Matplotlib & Seaborn**: Custom visualizations
        - ✨ **Plotly**: Interactive dashboards
        - 📈 **Tableau & PowerBI**: Business intelligence dashboards
        """
    )

with tab3:
    st.markdown(
        """
        - 🤖 **Logistic Regression, Random Forest, XGBoost**: Predictive modeling
        - 🧠 **Neural Networks**: Deep learning frameworks (TensorFlow, PyTorch)
        - 📚 **LLM**: GPT, BERT, Transformers for NLP tasks
        """
    )

# Skill Proficiency Bar
#st.markdown("### Skill Proficiency")
#skills = {
    #"Python": 90,
    #"SQL": 85,
    #"Data Visualization": 80,
    #"Machine Learning": 95,
    #"LLM": 90
#}
#for skill, proficiency in skills.items():
    #st.write(f"{skill}:")
    #st.progress(proficiency)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ using Streamlit | © 2025 Idowu Adamo</p>",
    unsafe_allow_html=True
)