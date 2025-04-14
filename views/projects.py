import streamlit as st

# Custom styling
st.markdown(
    """
    <style>
    .project-card {
        border: 1px solid #1E90FF;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #F9F9F9;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stButton > button {
        background-color: #1E90FF;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        margin: 5px;
    }
    .stExpander {
        background-color: #E6F3FF;
        border-radius: 8px;
    }
    .placeholder-image {
        text-align: center;
        color: #666;
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and introduction
st.markdown("<h1 style='text-align: center; color: #2E2E2E;'>My Projects</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center;'>
    Explore my Data Science and Machine Learning projects showcasing expertise in Generative AI, recommendation systems, and customer analytics. 
    Want to discuss a project? Visit the <a href='/About_Me'>About Me</a> section to get in touch!
    </p>
    """,
    unsafe_allow_html=True
)

# Analytics for page views
if "project_views" not in st.session_state:
    st.session_state.project_views = 0
st.session_state.project_views += 1

# Projects list
projects = [
    {
        "title": "Meeting Minutes Generator",
        "description": "Built a Generative AI application to generate meeting minutes, summaries, and action items from audio recordings.",
        "technologies": "Python, GPT-4, Llama, Gradio",
        "results": "Reduced meeting summary time by approximately 60% for users.",
        "links": [
            {"label": "Hugging Face Space", "url": "https://idowenst-meeting-minutes-generator.hf.space/?logs=container&__theme=system"}
        ]
    },
    {
        "title": "E-commerce Price Comparison and Product Recommendation System",
        "description": "Developed an AI-powered platform to help Nigerians find the best deals without compromising quality, enabling smarter shopping.",
        "technologies": "Python, Streamlit, Selenium, BeautifulSoup, Pandas",
        "results": "Helped users save an estimated 20% on purchases by recommending budget-friendly, high-quality products.",
        "links": [
            {"label": "GitHub Repository", "url": "https://github.com/IdowuAdamo/Neural-Drip"}
        ]
    },
    {
        "title": "Customer Segmentation and Targeted Marketing",
        "description": "Created a model to classify retail customers into distinct groups for targeted marketing campaigns.",
        "technologies": "Python, Scikit-learn, Pandas, Matplotlib",
        "results": "Improved customer purchase rates by 15% through personalized campaigns.",
        "links": [
            {"label": "GitHub Repository", "url": "https://github.com/IdowuAdamo/RFM-Customer-Segmentation/tree/main"}
        ]
    }
]

# Display projects in cards
for project in projects:
    with st.container():
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1], gap="medium")
        
        with col1:
            st.markdown(f"### {project['title']}")
            st.write(project['description'])
            
            with st.expander("View Details"):
                st.markdown(
                    f"""
                    - **Technologies**: {project['technologies']}
                    - **Results**: {project['results']}
                    """
                )
                for link in project['links']:
                    st.markdown(f"[{link['label']}]({link['url']})")

        with col2:
            # Placeholder for project image/screenshot
            st.markdown("<p class='placeholder-image'>[Project screenshot placeholder]</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# Back to top button
if st.button("⬆ Back to Top", key="back_to_top"):
    st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ using Streamlit | © 2025 Idowu Adamo</p>",
    unsafe_allow_html=True
) 