# --- HOME PAGE ---

import streamlit as st

# Purpose/Aim Section
st.subheader("🌟 What is Envision?")
st.markdown("""
Envision is an **AI-powered application** specifically designed to assist visually impaired individuals. 
With cutting-edge technologies like **Generative AI**, it bridges the gap between challenges and accessibility, empowering individuals to lead more independent lives 💡. 
""")

# Did You Know Section
with st.expander("**DID YOU KNOW?**"):
    st.markdown("""
    <div style="
        border: 2px solid #333; 
        background-color: #a8dddf; 
        padding: 15px; 
        border-radius: 10px; 
        padding: 10px; 
        font-size: 14px; 
        color: #000;
    ">
        Over <b>2.2 Billion People Worldwide</b> have a vision impairment or blindness, according to the <b>World Health Organization (WHO)</b>. 
        Many of these impairments can be addressed with accessible technologies like Envision!
    </div>
    """, unsafe_allow_html=True)

st.markdown("")

# Key Features Section
st.subheader("🔑 Key Features")
st.markdown("""
- **🖼️ Real-Time Scene Understanding**: Generate detailed textual descriptions of images to help users understand the scene effectively.
- **🗣️ Text-to-Speech Conversion**: Convert generated description into audible speech for seamless content accessibility.
- **🛠️ Personalized Assistance**: Provide guidance for specific tasks such as recognizing items, reading labels, or identifying objects in the environment.
""")

st.markdown("")
st.markdown("")

# How to Use Section
st.markdown("""
<div style="
    border: 2px solid #ccc; 
    border-radius: 15px; 
    background-color: #f9f9f9; 
    padding: 20px; 
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    font-size: 16px; 
    line-height: 1.8; 
    color: #333;
">
    <h2 style="color: teal; text-align: center;">❓How to Use</h2>
    <ol style="margin-left: 20px;">
        <li><b>Navigation:</b> Use the navigation bar on the left to explore the app:</li>
        <ul style="margin-left: 20px; list-style-type: disc;">
            <li>🏠 <b>Home Page:</b> Provides a detailed overview of the application.</li>
            <li><b>Features Section:</b>
                <ul style="margin-left: 20px; list-style-type: circle;">
                    <li>🔍 <b>Describe Image:</b> Upload an image to receive a written scene description and audio narration.</li>
                    <li>🚶 <b>Task Assistance:</b> Upload an image to receive tailored assistance based on the visual content.</li>
                </ul>
            </li>
        </ul>
        <li><b>Analyze Images:</b> Select a feature, upload an image, and click the Analyze Image button. The app will process the image and generate results, including <b>written descriptions</b> 📝 and <b>text-to-speech outputs</b> 🔊.</li>
        <li><b>Accessibility:</b> The audio output ensures seamless interaction for users with visual impairments.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown("")

st.markdown("""
<div style=" border: 2px dashed #ccc; margin: 20px 0; width: 100%;"></div>""", unsafe_allow_html=True)

st.markdown("")

# Disclaimer Section
st.subheader("⚠️ Disclaimer")
st.markdown("""
Envision is a **prototype** designed to assist visually impaired individuals. While it strives to provide accurate and helpful outputs, it may not always be error-free or fully comprehensive. 
Users are advised to use the application as a supplementary tool, exercising discretion for critical decisions.
""")

st.markdown("")

# Contact Information Section
st.subheader("☎️ Contact Information")
st.markdown("""
For inquiries, suggestions, or support, please reach out to me at:
- **Email**: [maniyarhuda26@gmail.com](mailto:maniyarhuda26@gmail.com)
- **LinkedIn**: [HudaManiyar](https://www.linkedin.com/in/hudamaniyar/)  
- **GitHub**: [HudaManiyar](https://github.com/HudaManiyar)
            
**Developed by**: Huda Maniyar   
""")