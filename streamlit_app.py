import streamlit as st
from transformers import pipeline
 
st.title("🎈 My new app") 
st.write(  
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.title("Text To Audio App")
# إعداد الـ pipeline
pipe = pipeline("text-to-speech", model="suno/bark-small", device="cpu")

# واجهة Streamlit
col = st.columns(2)

with col[0]: 
    input_text = st.text_area("Enter Your Text")
    btn = st.button("Text To Audio")
    if btn and input_text.strip() != "":
        with st.spinner("قاعدين نحضرو في الصوت..."):
            output = pipe(input_text)
            audio_bytes = output["audio"]
            sampling_rate = output["sampling_rate"]
            st.audio(audio_bytes, format="audio/wav", sample_rate=sampling_rate)
    elif btn:
        st.warning("رجاءً أدخل نص!")

 
