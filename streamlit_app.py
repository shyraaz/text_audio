import streamlit as st
from transformers import pipeline 
import io
import soundfile as sf
import numpy as np

import streamlit as st
from transformers import pipeline

# عنوان التطبيق
st.title("sentiment analysis")

# إعداد الـ pipelines
sentiment_pipe = pipeline("sentiment-analysis")
tts_pipe = pipeline("text-to-speech", model="suno/bark-small", device="cpu")

# إدخال النص
user_text = st.text_input("أدخل النص هنا:")

# زر التنفيذ
if st.button("حلل النص و اسمع الصوت"):
    # تحليل المشاعر
    sentiment_result = sentiment_pipe(user_text)
    st.write("نتيجة تحليل المشاعر:")
    st.write(sentiment_result)
    
    # تحويل النص إلى صوت
    audio_result = tts_pipe(user_text)
    st.audio(audio_result["audio"], format="audio/wav")

 
