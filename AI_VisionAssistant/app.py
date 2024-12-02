# Name: Huda Maniyar

# INSTRUCTIONS
# 1. Download and SetUP (requirements.txt)
# 2. Acquire Google API Key (save it to secrets.toml)
# 3. Run the Streamlit Application (streamlit run app.py)

# --- MAIN ---

import streamlit as st


# Set Page Configurations
st.set_page_config(layout="wide", page_title="Envision: AI Visual Assist", initial_sidebar_state="expanded") 

# Title
st.markdown("<h1 style='font-size: 65px; text-align: center;'><span style='color: teal;'>Envision:</span> AI Visual Assist</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='font-size: 18px; text-align: center;'>Empowering visually impaired individuals through AI-driven solutions</h3>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #ccc;'/>", unsafe_allow_html=True)

# Logo
st.logo("assets/envision_logo.png")

# Page Footer
st.markdown("""
    <div style="position: fixed; bottom: 0; width: 100%; background-color: #2c3e50; color: white; padding: 3px 10px; font-size: 10px; display: flex; align-items: center;">
        <p style="margin: 0;"><strong>Envision</strong> | Created by Huda Maniyar | Powered by Google Gen AI and Streamlit</p>
    </div>
""", unsafe_allow_html=True)

# Page Setup
home_page = st.Page(
    page = "views/home.py",
    title = "HOME PAGE",
    icon = ":material/home:", 
    default = True
)

describe_page = st.Page(
    page = "views/features/describe.py",
    title = "DESCRIBE IMAGE",
    icon = ":material/search:"
)

task_page = st.Page(
    page = "views/features/task.py",
    title = "TASK ASSISTANCE",
    icon = ":material/blind:"
)

# Navigation Setup
pg = st.navigation(
    {
    "Info": [home_page],
    "Features": [describe_page, task_page], 
    }
)

pg.run() # Run Navigation








