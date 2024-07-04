import streamlit as st
import requests
from PIL import Image
import io

# FastAPI endpoint
url = 'http://backend:8000/predict'  

st.title("Taylor Swift Eras Tour Pictures Classifier")
st.write("Upload an image and see which era it belongs to!")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Make prediction when 'Predict' button is clicked
    if st.button('Predict'):
        with st.spinner("Classifying..."):
            # Prepare file for request
            bytes_data = uploaded_file.getvalue()
            files = {'file': (uploaded_file.name, io.BytesIO(bytes_data), uploaded_file.type)}
            
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