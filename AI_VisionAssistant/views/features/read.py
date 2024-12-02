# --- READ ---

import streamlit as st
from gtts import gTTS # For Text to Speech
import io 
from helpers import clean_text


# Function to "CONVERT TEXT TO SPEECH"
def read_text():
    try:
        # Check if Text is Available in Session State
        if "generated_text" not in st.session_state or not st.session_state["generated_text"].strip():
            st.warning("No text available to read. Please analyze an image first.")
            return

        text_to_read = st.session_state["generated_text"]
        text_to_read = clean_text(text_to_read)

        # Convert Text to Speech using gTTS
        tts = gTTS(text=text_to_read, lang='en-uk')
        audio_output = io.BytesIO()  
        tts.write_to_fp(audio_output)  # Write audio data to buffer
        audio_output.seek(0)  

        # Display the Generated Audio
        st.markdown("### 🎧 Generated Audio:")
        st.audio(audio_output, format="audio/mp3")

    except Exception as e:
        st.error(f"Error generating audio: {str(e)}")