import streamlit as st
import requests
from PIL import Image
import io


# FastAPI endpoint
url = 'http://backend:8000/predict'  

st.title("Taylor Swift Eras Tour Pictures Classifier")
st.write("Upload an image and see which era it belongs to!")

# Image classification 
# Upload image file
uploaded_img = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_img is not None:
    # Display the uploaded image
    image = Image.open(uploaded_img)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Make prediction when 'Predict' button is clicked
    if st.button('Predict the image class', key="img"):
        with st.spinner("Classifying..."):
            # Prepare file for request
            bytes_data = uploaded_img.getvalue()
            files = {'file': (uploaded_img.name, io.BytesIO(bytes_data), uploaded_img.type)}
            
            # Send API request
            response = requests.post(url, files=files)

            if response.status_code == 200:
                # Display results
                result = response.json()
                predicted_class = result['predicted_class']
                confidence = result['confidence']
                st.write(f"**Prediction:** {predicted_class}")
                st.write(f"**Confidence:** {confidence:.2f}")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")

# Video classification experiment
uploaded_vid = st.file_uploader("Choose a video...", type=["mp4", "avi"])

if uploaded_vid is not None:
    # Display the uploaded video
    video_bytes = uploaded_vid.read()
    st.video(video_bytes)
    # Make prediction when 'Predict' button is clicked
    if st.button('Predict the video class', key="vid"):
        with st.spinner("Classifying..."):
        
            # Prepare file for request
            files = {'file': (uploaded_vid.name, io.BytesIO(video_bytes), uploaded_vid.type)}

            # Send API request
            response = requests.post(url, files=files)

            if response.status_code == 200:
                # Display results
                result = response.json()
                predicted_class = result['predicted_class']
                st.write(f"**Prediction:** {predicted_class}")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")