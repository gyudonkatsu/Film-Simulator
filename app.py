import streamlit as st
from PIL import Image, ImageEnhance

def kodak_style(img):
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(1.5)

st.title("🎞️ Film Simulator Test")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Original")
    
    if st.button("Apply Kodak Filter"):
        filtered = kodak_style(img)
        st.image(filtered, caption="Kodak Style")
