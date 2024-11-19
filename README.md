
# Multifunctional Speech and Text Application  

### 🚀 Live Demo on Hugging Face: [Click Here](https://huggingface.co/spaces/Vivek6041/Speech_Text_Processor)

---

## Table of Contents  
1. [About the Project](#about-the-project)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Technologies Used](#technologies-used)  
6. [Live Demo](#live-demo)  

---

## About the Project  
This is a **Multifunctional Speech and Text Application** built using Streamlit. It combines several powerful features like:
- Converting Speech to Text
- Generating Speech from Text
- Translating Text between languages  

This tool is perfect for language learning, accessibility, or just having fun experimenting with text and speech conversions!

---

## Features  
1. **Speech-to-Text**:
   - Upload an audio file (`.wav`, `.mp3`, `.ogg`) and convert it into text using `SpeechRecognition`.
  
2. **Text-to-Speech**:
   - Enter text and convert it to speech using `gTTS` (Google Text-to-Speech). Supports multiple languages.

3. **Text Translation**:
   - Translate input text into another language using `deep-translator`. Supports translation to/from English, French, Spanish, Hindi, and German.

---

## Installation  

To set up and run the project locally, follow these steps:  

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vivekd16/Speech_Text_Processor.git
   cd Speech_Text_Processor

2. **Install Dependencies**:  
   Make sure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt

3. **Run the Application**:  
   Launch the Streamlit app locally:  
   ```bash
   streamlit run app.py

4. **Access the App**:  
   Open your web browser and navigate to:  
   ```bash
   http://localhost:8501


5. **Explore the Features**:  
- **Speech-to-Text**: Upload an audio file and convert it into text.  
- **Text-to-Speech**: Enter text and listen to it in the selected language.  
- **Text Translation**: Translate text into multiple supported languages.  

6. **Stop the Application**:  
   To stop the Streamlit server, go back to the terminal and press:  
   ```bash
   Ctrl + C

---

## Usage  

1. **Select a Feature**:  
   Use the sidebar to choose one of the three features:  
   - **Speech-to-Text**: Upload an audio file in `.wav`, `.mp3`, or `.ogg` format to convert it into text.  
   - **Text-to-Speech**: Enter text and convert it into speech. You can download the audio or listen to it directly.  
   - **Text Translation**: Input text and select the target language to translate into.  

2. **Interact with Results**:  
   - For Speech-to-Text, view the transcribed text in the app.  
   - For Text-to-Speech, listen to the generated speech or save the audio file.  
   - For Text Translation, copy or use the translated text directly.  

3. **Real-Time Processing**:  
   All features are designed for immediate interaction, making it user-friendly and efficient.

---

## Technologies Used  

This project leverages the following technologies:  

- **[Streamlit](https://streamlit.io/)**: Framework for building interactive web applications.  
- **[gTTS](https://pypi.org/project/gTTS/)**: Library for generating speech from text.  
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)**: For converting speech to text from uploaded audio files.  
- **[Deep-Translator](https://pypi.org/project/deep-translator/)**: For translating text between languages.  
- **[PyDub](https://pypi.org/project/pydub/)**: For handling audio file formats and conversions.  

---

## Live Demo  

Experience the application live on Hugging Face Spaces:  

👉 **[Multifunctional Speech and Text Application](https://huggingface.co/spaces/Vivek6041/Speech_Text_Processor)**  

Simply navigate to the link, and start using the app without any installation!  

Let me know if you need further updates! 😊


