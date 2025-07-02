# app.py
import streamlit as st
from PIL import Image
from ocr_core import extract_text

st.set_page_config(page_title="OCR App", layout="centered")
st.title("📄 OCR Image to Text")

uploaded = st.file_uploader("Image ya PDF upload karein", type=["png", "jpg", "jpeg", "pdf"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image")

    st.subheader("Extracted Text:")
    text = extract_text(img)
    st.code(text)

    st.download_button("Download Text", text.encode(), file_name="output.txt")