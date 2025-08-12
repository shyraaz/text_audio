import streamlit as st
from transformers import pipeline

# عنوان التطبيق
st.title("sentiment analysis")

# إعداد الـ pipeline
sentiment_pipe = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# إدخال النص
user_text = st.text_input("أدخل النص هنا:")

# زر التنفيذ
if st.button("حلل النص"):
    # تحليل المشاعر
    sentiment_result = sentiment_pipe(user_text)
    st.write("نتيجة تحليل المشاعر:")
    st.write(sentiment_result)
