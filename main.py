import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os


st.set_page_config(page_title="Main Page", layout="wide")


@st.cache_data
def get_img_as_base64(file_path: str) -> str | None:
    """Cache the image as base64 to avoid repeated encoding."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

background_path = r"background/8.jpg"
backgr = get_img_as_base64(background_path)

if backgr:
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{backgr}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stSidebar"] {{ display: none; }}

    .fade-in {{
        animation: fadeIn 1s ease-in-out;
        font-size: 20px;
        line-height: 1.6;
    }}

    .menu-container {{
        text-align: center;
        margin-top: -400px;
        margin-left: auto;
        margin-right: auto;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(15px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="menu-container">', unsafe_allow_html=True)

selected = option_menu(
    menu_title="Main Menu",
    options=["Main", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    orientation="horizontal",
    default_index=0
)

st.markdown('</div>', unsafe_allow_html=True)

def switch_page(selection: str):
    if selection == "Projects":
        st.switch_page("pages/proj.py")
    elif selection == "Contact":
        st.switch_page("pages/contact.py")

switch_page(selected)

st.markdown("""
<div class="fade-in">
    <h1>Welcome to My Portfolio</h1>
    <h2>I'm Ntando Nkuna</h2>
    <h3>Data Engineering & Analytics Specialist</h3>
</div>

<div class="fade-in">
## Skills I Offer:

- **Extract & Integrate Data:** Collect data from multiple sources, ensuring all information is available for analysis.  
- **Prepare Data for Analysis:** Clean, validate, and transform raw data into structured, usable formats for analytics and downstream applications.  
- **Design & Maintain Data Pipelines:** Build scalable, efficient ETL pipelines that move data seamlessly from source to destination.  
- **Manage Data Infrastructure:** Set up and maintain the systems and architecture for data collection, processing, and storage.  
- **Enable Actionable Insights:** Provide clean, reliable data that empowers organizations to make informed, data-driven decisions.  

## Tools & Technologies I Use:

- **Programming Languages:** Python, SQL  
- **Data Processing Frameworks:** Apache Spark, Pandas  
- **Databases:** PostgreSQL, MongoDB  
- **Cloud Platforms:** AWS, GCP  
- **Data Visualization:** Tableau, Power BI  
</div>
""", unsafe_allow_html=True)


