# --- DESCRIBE PAGE ---

import streamlit as st
import time

from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from helpers import upload_image
from views.features.read import read_text

# Establishing Model Configurations
GEMINI_API_KEY = st.secrets["API_KEY"]
MODEL_NAME = "gemini-1.5-pro"

# Heading and Description
st.subheader("Describe Image")
st.markdown("<p style='font-size: 16px; text-align: left;'>Upload an image to let AI analyze and provide a detailed, easy-to-understand description, including scene overview, key objects, activities, and settings.</p>", unsafe_allow_html=True)

# Function to "DESCRIBE THE IMAGE"
def describe_image(uploaded_image):

    # AI Prompts
    system_prompt = (
        "system",
        """
        You are an AI assistant specifically designed for visually impaired individuals. Your task is as follows: 
        Analyze the uploaded image and provide clear, simple language and detailed description of it in paragraph form.
        The description should include information on Scene Overview, Key Objects, Human Activities, and Setting (Colors and Lighting).
        """
    )
    human_prompt = (
        "human",
        [
            {"type": "text", "text": "Please provide a detailed description of the uploaded image."},
            {"type": "image_url", "image_url": f"data:image/png;base64,{uploaded_image}"}
        ]
    )

    # Create LangChain Pipeline
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
    output_parser = StrOutputParser()
    chat_model = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=MODEL_NAME)
    pipeline = chat_prompt | chat_model | output_parser

    try:
        description = pipeline.invoke({"input": "Analyze the scene.", "image_data": uploaded_image})
        if description:
            st.session_state["generated_text"] = description  # Save to session state
            return description
    except Exception as e:
        st.error(f"Error analyzing image: {str(e)}")
        return None


# MAIN EXECUTION FLOW

image = upload_image()
if image and st.button("Analyze Image"):
    
    progress_bar = st.progress(0) # Initialize Progress Bar
    
    # Generate Image Description and Audio
    with st.spinner("Analyzing the Image and Generating Audio ... "):
        for i in range(100):
            time.sleep(0.05)  # Simulate Processing Delay
            progress_bar.progress(i + 1)  # Update Progress Bar from 1% to 100%
    
        description = describe_image(image)
        
        if description:
            if description:
                st.markdown("""
                <div style="border: 3px solid #333; border-radius: 10px; padding: 20px; background-color: #f9f9f9; box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.1);">
                    <h3 style="text-align: center; color: teal;">📝 Description</h3>
                    <p style="font-size: 16px; color: #333;">{}</p>
                </div>
                """.format(description), unsafe_allow_html=True)
            
            # Generate Audio
            if "generated_text" in st.session_state and st.session_state["generated_text"].strip():
                read_text()
                st.success("Image Description and Audio Generated Successfully!")
            
           

