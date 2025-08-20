from streamlit_option_menu import option_menu
import streamlit as st
import base64
import fitz
from PIL import Image
import io

st.set_page_config(page_title="Projects Page", layout="wide")


def get_img_as_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

backgr = get_img_as_base64(r"background/7.png")

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
    default_index=1
)

if selected == "Main":
    st.switch_page("main.py")
elif selected == "Contact":
    st.switch_page("pages/contact.py")


def display_project():
    st.markdown(
        "<h1 style='text-align: center; width: 100%;'>Project: Cafe Sales Data Cleaning & Exploration</h1>",
        unsafe_allow_html=True
    )
    
    st.image(r"background/Issue Log.png", use_container_width=True)

    pdf_path = r"Dirty_Cafe_Sales_Project_Description.pdf"
    doc = fitz.open(pdf_path)

    st.markdown("<h2 style='text-align: center;'>Project Description PDF</h2>", unsafe_allow_html=True)

    with st.expander("View PDF Pages"):  
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            st.image(img, use_container_width=True)


    with open(r"cafe_Eda.ipynb", "rb") as f:
        st.download_button(
            label="Download Project Notebook Here",
            data=f,
            file_name="cafe_Eda.ipynb",
            mime="application/octet-stream"
        )

# Call the function

display_project()
