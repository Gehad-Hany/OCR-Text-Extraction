import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# Initialize EasyOCR reader
reader = easyocr.Reader(["en"])  
# Streamlit app title and description
st.title("OCR Text Extraction App 📝")
st.write("Upload an image containing numbers, and the model will extract them!")

# File uploader to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open and display the image with a smaller size
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=400)  
    
    # Convert image to NumPy array
    image_np = np.array(image)
    
    # Perform OCR
    st.write("Extracting numbers... Please wait!")
    results = reader.readtext(image_np, detail=0)  
    
    # Display extracted text
    extracted_text = " ".join(results)
    
    st.subheader("Extracted Text:")
    st.code(extracted_text, language="text")  
    
    # Download button
    st.download_button("Download Text", extracted_text, file_name="extracted_text.txt")
