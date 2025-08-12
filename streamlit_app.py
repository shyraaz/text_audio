import streamlit as st
from transformers import pipeline 
import io
import soundfile as sf
import numpy as np

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
            audio_array = output["audio"]
            sampling_rate = output["sampling_rate"]
    
            # Ensure audio_array is a NumPy array with dtype float32
            audio_array = np.array(audio_array, dtype=np.float32)
    
            # Convert to WAV bytes with explicit subtype
            wav_io = io.BytesIO()
            sf.write(wav_io, audio_array, sampling_rate, format="WAV", subtype="PCM_16")
            wav_io.seek(0)
    
            st.audio(wav_io, format="audio/wav", sample_rate=sampling_rate)


 
