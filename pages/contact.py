import streamlit as st
from streamlit_option_menu import option_menu
import base64
import time

st.set_page_config(page_title="Contact Page", layout="wide")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

backgr = get_img_as_base64(r"background/6.jpeg")


page_back = f"""
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
"""
st.markdown(page_back, unsafe_allow_html=True)

selected = option_menu(
    menu_title="Main Menu",
    options=["Main", "Projects", "Contact"],
    icons=["house", "book", "envelope"],
    orientation="horizontal",
    default_index=2
)

if selected == "Main":

    st.switch_page("main.py")

elif selected == "Projects":

    st.switch_page("pages/proj.py")

st.markdown(
    """
    <div class="fade-in" style="text-align: center; margin-top: 150px;">
        <h1>Contact Me Page</h1>
        <h2>Phone Number : +27687603568</h2>
        <h2>You can reach me at: ntandodataanalysis2099@gmail.com</h2>
        <h2>
            LinkedIn: 
            <a href="https://www.linkedin.com/in/ntando-nkuna-abb20a35b/" target="_blank">
                Visit My LinkedIn Profile
            </a>
        </h2>
    </div>
    """,
    unsafe_allow_html=True

)
