# --- TASK PAGE ---

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
st.subheader("Task Assistance")
st.markdown("<p style='font-size: 16px; text-align: left;'>Get real-time, AI-powered guidance for navigating spaces, identifying objects, and completing daily tasks, designed to empower visually impaired individuals with safety and ease.</p>", unsafe_allow_html=True)

# Function to "OFFER PERSONALISED TASK ASSISTANCE"
def task_assistance(uploaded_image):

    # AI Prompts
    system_prompt = (
        "system",
        """
            You are an AI assistant specifically designed to help visually impaired individuals by analyzing uploaded images and providing them with actionable guidance. Ensure responses are detailed, easy to understand, and tailored to the user's needs; and should include: 
            1. Item Identification (Names, Types, Key Features; Relative Positions) 
            2. Label Reading and Text Recognition (Warnings, Instructions, or Important Markings) 
            3. Navigation Safety (Guide through space, Highlight key landmarks/obstacles/hazards)
            4. Guidance for Daily Tasks (Step-by-Step Instructions, Suggest Safety Precautions, Highlight Important Object Location) 
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
    
        assistance = task_assistance(image)
        
        if assistance:
            st.markdown("""
                <div style="border: 3px solid #333; border-radius: 10px; padding: 20px; background-color: #f9f9f9; box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.1);">
                    <h3 style="text-align: center; color: teal;">📝 Assistance</h3>
                    <p style="font-size: 16px; color: #333;">{}</p>
                </div>
                """.format(assistance), unsafe_allow_html=True)
            
            # Generate Audio
            if "generated_text" in st.session_state and st.session_state["generated_text"].strip():
                read_text()
                st.success("Task Assistance and Audio Generated Successfully!")