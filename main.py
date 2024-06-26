import streamlit as st
from audio_recorder_streamlit import audio_recorder
from openai import OpenAI 
import os

# Set API key
API_KEY = "YOUR_API_KEY"
os.environ["API_KEY"] = API_KEY

def transcribe_text_to_voice(audio_location):
    client = OpenAI(api_key=API_KEY)  
    audio_file = open(audio_location, "rb")
    transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcript.text

def chat_completion_call(text):
    client = OpenAI(api_key=API_KEY)  
    messages = [{"role": "user", "content": text}]
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106", messages=messages)
    return response.choices[0].message.content

def text_to_speech_ai(speech_file_path, api_response):
    client = OpenAI(api_key=API_KEY)  
    response = client.audio.speech.create(model="tts-1", voice="nova", input=api_response)
    response.stream_to_file(speech_file_path)

st.title("Voice Assistant")

"""
Hi just click on the voice recorder and let me know how I can help you today?
"""
"""
Made by Chaitanya N
"""

audio_bytes = audio_recorder()
if audio_bytes:
    
    audio_location = "audio_file.wav"
    with open(audio_location, "wb") as f:
        f.write(audio_bytes)

    
    text = transcribe_text_to_voice(audio_location)
    st.write(text)

   
    api_response = chat_completion_call(text)
    st.write(api_response)

    speech_file_path = 'audio_response.mp3'
    text_to_speech_ai(speech_file_path, api_response)
    st.audio(speech_file_path)
