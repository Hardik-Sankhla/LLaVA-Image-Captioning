# frontend/app.py

import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/caption/"

st.title("🖼️ Image Caption Generator (LLaVA)")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        files = {"file": uploaded_file.getvalue()}
        try:
            response = requests.post(BACKEND_URL, files=files)
            response.raise_for_status()
            caption = response.json().get("caption", "No caption generated.")
            st.success(f"📝 Caption: {caption}")
        except Exception as e:
            st.error(f"Error: {e}")
