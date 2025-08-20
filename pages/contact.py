import streamlit as st
from streamlit_option_menu import option_menu
import base64
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Contact Page", layout="wide")

# ------------------ BACKGROUND IMAGE ------------------
@st.cache_data
def get_img_as_base64(file_path: str) -> str | None:
    """Return base64 string of an image if it exists."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

background_path = r"background/6.jpeg"
backgr = get_img_as_base64(background_path)

if backgr:
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpeg;base64,{backgr}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stSidebar"] {{ display: none; }}

    .fade-in {{
        animation: fadeIn 0.6s ease-in-out;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    """, unsafe_allow_html=True)

# ------------------ MENU ------------------
selected = option_menu(
    menu_title="Main Menu",
    options=["Main", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    orientation="horizontal",
    default_index=2
)

# ------------------ PAGE SWITCH ------------------
if selected == "Main":
    st.switch_page("main.py")
elif selected == "Projects":
    st.switch_page("pages/proj.py")

# ------------------ CONTACT CONTENT ------------------
st.markdown("""
<div class="fade-in" style="text-align: center; margin-top: 150px;">
    <h1>Contact Me</h1>
    <h2>Phone Number: +27 68 760 3568</h2>
    <h2>Email: <a href="mailto:ntandodataanalysis2099@gmail.com">
        ntandodataanalysis2099@gmail.com
    </a></h2>
    <h2>
        LinkedIn: 
        <a href="https://www.linkedin.com/in/ntando-nkuna-abb20a35b/" target="_blank">
            Visit My LinkedIn Profile
        </a>
    </h2>
</div>
""", unsafe_allow_html=True)
