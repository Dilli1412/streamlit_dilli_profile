import streamlit as st
from streamlit_option_menu import option_menu
import urllib.parse

# Page configuration
st.set_page_config(page_title="K. DilliBabu - Professional Profile", layout="wide")

# Custom CSS for a more professional look
st.markdown("""
<style>
    .main {
        padding: 2rem 3rem;
    }
    h1, h2, h3 {
        color: #1E3A8A;
    }
    .stButton>button {
        background-color: #1E3A8A;
        color: white;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #F3F4F6;
    }
    .reportview-container .main .block-container {
        max-width: 1200px;
    }
    .stExpander {
        background-color: #F3F4F6;
        border: 1px solid #E5E7EB;
        border-radius: 0.375rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Navigation bar
selected = option_menu(
    menu_title=None,
    options=["Professional Summary", "Experience", "Skills & Projects", "Contact"],
    icons=["person-badge", "briefcase", "code-slash", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#F3F4F6"},
        "icon": {"color": "#1E3A8A", "font-size": "16px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#EEF2FF"},
        "nav-link-selected": {"background-color": "#1E3A8A", "color": "white"},
    }
)

# Professional Summary section
if selected == "Professional Summary":
    st.title("K. DilliBabu")
    st.subheader("ERP Functional Consultant")
    
    st.markdown("""
    Versatile ERP professional with over 8 years of experience in Project Management, 
    Business System Analysis, and ERP Implementation. Specialized in ERPNext and various 
    other ERP systems. Proven track record in delivering high-value solutions, leading 
    cross-functional teams, and optimizing business processes across diverse industries.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Core Competencies")
        competencies = [
            "ERPNext Implementation",
            "ERP Functional Consulting",
            "Business Process Optimization",
            "Project Management",
            "Client Relationship Management",
            "In-house Development"
        ]
        for comp in competencies:
            st.markdown(f"- {comp}")
    
    with col2:
        st.subheader("Education")
        st.markdown("**Master of Computer Applications**")
        st.markdown("SRM University, 2023 - Present")
        st.markdown("**B.E. Computer Science**")
        st.markdown("Anna University, Apollo Engineering College, 2010 - 2014")

# Experience section
elif selected == "Experience":
    st.title("Professional Experience")
    
    st.subheader("ERP Functional Consultant")
    st.markdown("**DTECH Information Technology & Outsourcing Private LTD, Coimbatore | September 2024 - Present**")
    st.markdown("""
    - Provide comprehensive ERP solutions, specializing in ERPNext implementation and customization
    - Lead in-house development initiatives to tailor ERP systems to client-specific requirements
    - Conduct thorough business process analysis to optimize ERP configurations and enhance operational efficiency
    - Collaborate with cross-functional teams to ensure seamless integration of ERP solutions across various departments
    """)
    
    st.subheader("Senior Executive - Implementation and Subject Matter Expert")
    st.markdown("**Intech Creative Services | October 2023 - August 2024**")
    st.markdown("""
    - Led a team of 20 professionals in Searates ERP By DP World Implementation and support
    - Drove successful ERP implementations, conducted comprehensive customer training programs, and performed rigorous quality assurance testing
    - Spearheaded pre-sales initiatives and strategically enhanced product features based on localization requirements
    """)
    
    st.subheader("Team Lead - Implementation and Business Consultant")
    st.markdown("**Newage Software And Solutions | April 2021 - September 2023**")
    st.markdown("""
    - Orchestrated ERP module implementations for new accounts and managed change request processes
    - Developed detailed Business Requirement Documents (BRDs) and facilitated seamless communication between stakeholders
    - Provided expert consultation to clients, translating complex business needs into actionable technical solutions
    """)

# Skills & Projects section
elif selected == "Skills & Projects":
    st.title("Skills & Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Technical Skills")
        skills = [
            "ERPNext",
            "ERP Systems (Searates, Newage)",
            "Business Process Modeling",
            "Data Analysis & Visualization",
            "SQL & Database Management",
            "Python Programming",
            "Agile Methodologies"
        ]
        for skill in skills:
            st.markdown(f"- {skill}")
    
    with col2:
        st.subheader("Soft Skills")
        soft_skills = [
            "ERP Functional Consulting",
            "Leadership & Team Management",
            "Client Communication",
            "Problem-Solving",
            "Adaptability",
            "Continuous Learning"
        ]
        for skill in soft_skills:
            st.markdown(f"- {skill}")
    
    st.subheader("Key Projects")
    projects = [
        {
            "name": "ERPNext Implementation for Manufacturing Firm",
            "description": "Led the end-to-end implementation of ERPNext for a mid-sized manufacturing company, resulting in a 40% improvement in inventory management and a 25% reduction in production lead times.",
        },
        {
            "name": "Custom ERP Module Development",
            "description": "Spearheaded the development of custom ERP modules for specific client needs, including a specialized quality control system that increased product consistency by 30%.",
        },
        {
            "name": "Searates ERP Global Implementation",
            "description": "Managed the implementation of Searates ERP for multiple international clients in the logistics sector, resulting in a 30% increase in operational efficiency and improved global shipment tracking capabilities.",
        },
    ]
    
    for project in projects:
        with st.expander(project["name"]):
            st.write(project["description"])

# Contact section
elif selected == "Contact":
    st.title("Contact Information")
    st.markdown("I welcome opportunities for collaboration and professional engagements.")
    
    st.subheader("Direct Contact")
    st.markdown("**Email:** dillibehappy@gmail.com")
    #st.markdown("**Phone:** +91 9597 242 884")
    st.markdown("**LinkedIn:** [linkedin.com/in/dilli](https://www.linkedin.com/in/dilli)")

    # Add any additional contact information or message you'd like to display
    st.markdown("""
    Feel free to reach out to me via email or LinkedIn for any professional inquiries, 
    collaboration opportunities, or if you have any questions about my work in ERP implementation 
    and functional consulting.
    
    I'm always open to discussing new projects, sharing insights about ERP systems, 
    or exploring how we can work together to optimize business processes through effective 
    ERP solutions.
    """)

    # You can add a call-to-action button for LinkedIn
    if st.button("Connect on LinkedIn"):
        st.markdown("[Click here to view my LinkedIn profile](https://www.linkedin.com/in/dilli)")