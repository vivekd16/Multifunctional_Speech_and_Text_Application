import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import os

# Streamlit App Title and Description
st.title("Multifunctional Speech and Text Application")
st.markdown("""
A versatile application for Speech-to-Text, Text-to-Speech, and Text Translation.  
Experience seamless speech and text conversions with language translation support!  
""")

# --- Sidebar for Navigation ---
st.sidebar.title("Choose a Feature:")
feature = st.sidebar.radio(
    "Select an option:", 
    ["Speech-to-Text", "Text-to-Speech", "Text Translation"]
)

# --- Feature 1: Speech-to-Text ---
if feature == "Speech-to-Text":
    st.header("Speech-to-Text")
    st.markdown("Upload an audio file to convert speech into text.")
    
    # File upload for audio
    audio_file = st.file_uploader("Upload an audio file (WAV format preferred):", type=["wav", "mp3", "ogg"])
    
    if audio_file:
        # Save uploaded file temporarily
        with open("uploaded_audio.wav", "wb") as f:
            f.write(audio_file.read())
        
        try:
            # Convert audio to text
            recognizer = sr.Recognizer()
            with sr.AudioFile("uploaded_audio.wav") as source:
                audio_data = recognizer.record(source)
                text_output = recognizer.recognize_google(audio_data)
                st.success("Conversion Successful!")
                st.text_area("Converted Text:", text_output, height=150)
        except Exception as e:
            st.error(f"Speech-to-Text Conversion Error: {e}")
        finally:
            os.remove("uploaded_audio.wav")  # Clean up the temporary file

# --- Feature 2: Text-to-Speech ---
elif feature == "Text-to-Speech":
    st.header("Text-to-Speech")
    st.markdown("Enter text to convert into speech.")
    
    # User input for text
    text_input = st.text_area("Enter text for speech synthesis:", placeholder="Type something here...")
    
    # Language selection
    language = st.selectbox(
        "Select Language:",
        options=["en", "fr", "es", "hi", "de"],
        format_func=lambda x: {
            "en": "English",
            "fr": "French",
            "es": "Spanish",
            "hi": "Hindi",
            "de": "German",
        }.get(x, x)
    )
    
    if st.button("Convert to Speech"):
        if text_input.strip():
            try:
                # Generate speech using gTTS
                tts = gTTS(text=text_input, lang=language)
                tts.save("output_audio.mp3")
                st.success("Speech synthesis successful!")
                st.audio("output_audio.mp3", format="audio/mp3")
            except Exception as e:
                st.error(f"Text-to-Speech Conversion Error: {e}")
        else:
            st.warning("Please enter some text for conversion.")

# --- Feature 3: Text Translation ---
elif feature == "Text Translation":
    st.header("Text Translation")
    st.markdown("Translate text into another language.")
    
    # User input for text
    text_to_translate = st.text_area("Enter text to translate:", placeholder="Type text here...")
    
    # Target language selection
    target_language = st.selectbox(
        "Select Target Language:",
        options=["en", "fr", "es", "hi", "de"],
        format_func=lambda x: {
            "en": "English",
            "fr": "French",
            "es": "Spanish",
            "hi": "Hindi",
            "de": "German",
        }.get(x, x)
    )
    
    if st.button("Translate Text"):
        if text_to_translate.strip() and target_language:
            try:
                # Translate text
                translation = GoogleTranslator(source="auto", target=target_language).translate(text_to_translate)
                st.success("Translation Successful!")
                st.text_area("Translated Text:", translation, height=150)
            except Exception as e:
                st.error(f"Translation Error: {e}")
        else:
            st.warning("Please enter text and select a target language!")

# --- Footer ---
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit, gTTS, and Deep-Translator.")
