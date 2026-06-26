import streamlit as st
import base64

def set_background(image_file):

    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    page_bg_img = f"""
    <style>

    /* Main Background */

    .stApp {{
        background:
            linear-gradient(
                rgba(0,0,0,0.65),
                rgba(0,0,0,0.65)
            ),
            url("data:image/jpg;base64,{encoded}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Sidebar */

    [data-testid="stSidebar"] {{
        background: linear-gradient(
            180deg,
            #131921 0%,
            #232F3E 50%,
            #37475A 100%
        );

        border-right: 2px solid #FF9900;

        box-shadow:
            0 0 20px rgba(255,153,0,0.4);
    }}

    /* Sidebar Text */

    [data-testid="stSidebar"] * {{
        color: white !important;
    }}

    /* Sidebar Headers */

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        color: #FF9900 !important;
        font-weight: bold;
    }}

    /* Sidebar Info Box */

    [data-testid="stSidebar"] .stAlert {{
        border-radius: 15px;
        border: 1px solid #FF9900;
        background: rgba(255,153,0,0.08);
    }}

    /* Metric Cards */

    div[data-testid="metric-container"] {{
        background-color: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,153,0,0.25);
        padding: 15px;
        border-radius: 15px;
        box-shadow:
            0px 4px 15px rgba(0,0,0,0.3);
    }}

    /* DataFrames */

    .stDataFrame {{
        border-radius: 15px;
        overflow: hidden;
    }}

    /* Charts */

    .js-plotly-plot {{
        border: 1px solid rgba(255,153,0,0.25);
        border-radius: 15px;
        padding: 10px;
        background: rgba(255,255,255,0.02);
    }}

    /* Scrollbar */

    ::-webkit-scrollbar {{
        width: 8px;
    }}

    ::-webkit-scrollbar-track {{
        background: #111;
    }}

    ::-webkit-scrollbar-thumb {{
        background: #FF9900;
        border-radius: 10px;
    }}

    ::-webkit-scrollbar-thumb:hover {{
        background: #E68A00;
    }}

    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)