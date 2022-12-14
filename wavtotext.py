import streamlit as st
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import wave

import speech_recognition as sr
r = sr.Recognizer()

wav_file = st.file_uploader("Upload wav",type = ["wav"])

sentences = []   

try:
    sound_file = AudioSegment.from_wav(wav_file)
    audio_chunks = split_on_silence(sound_file, min_silence_len=500, silence_thresh=-40 )
    list_chuncks = []
    for i, chunk in enumerate(audio_chunks):
     out_file = "chunk{0}.wav".format(i)
     chunk.export(out_file, format="wav")
     list_chuncks.append(out_file)
    for wave_sentence_name in list_chuncks: 
     with sr.AudioFile(wave_sentence_name) as source:
      audio = r.listen(source)
     try:
      s = r.recognize_google(audio)
      sentences.append(s)
     except Exception as e:
      st.write("Exception: "+str(e))
    
    st.write(sentences)

except Exception as e:
    st.write("Please upload wav file")  
