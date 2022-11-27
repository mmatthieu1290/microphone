import streamlit as st

import speech_recognition as sr

def user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit= 30)
        try:
            text = r.recognize_google(audio)
            return text
        except Exception as e:
            return e

if st.button("Start recording"):  
    sentence = user_input()
    st.write(sentence)           