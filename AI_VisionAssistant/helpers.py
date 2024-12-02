# --- HELPERS ---

import streamlit as st
from PIL import Image  # For image processing
import base64 
import io 
import re

# HELPER FUNCTIONS


# Function to encode image to Base64
def encode_image_to_base64(image):
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    return base64.b64encode(image_bytes.getvalue()).decode("utf-8")


# Function to handle image upload
def upload_image():
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        try:
            image = Image.open(uploaded_file)
            st.columns(3)[1].image(image, caption="Uploaded Image", width=500)
            #st.image(image, caption="Uploaded Image", width = 500)
            #st.image(image, caption="Uploaded Image", use_container_width=True)
            image_base64 = encode_image_to_base64(image)
            return image_base64
        except Exception as e:
            st.error(f"Error uploading image: {str(e)}")
            return None
    return None


# Function to Clean Text for Audio Generation
def clean_text(text):
    # Remove Markdown/HTML formatting
    cleaned_text = re.sub(r'\*\*|__|<[^>]+>', '', text)  # Remove bold (**), italics (__), and HTML tags
    return cleaned_text.strip()