import requests
import os
from PIL import Image

# Replace with your FastAPI endpoint
API_ENDPOINT = "http://localhost:8000/predict"

def send_image_to_api(image_path):
  """
  Sends an image to a FastAPI endpoint for prediction.

  Args:
    image_path: The path to the image file.

  Returns:
    The response from the API, containing the predicted label and confidence.
  """

  # Open the image file in binary read mode
  with open(image_path, 'rb') as image_file:
    image_data = image_file.read()

  # Send the image to the API
  files = {'file': ('image.jpg', image_data, 'image/jpeg')}  # Adjust file type if needed
  response = requests.post(API_ENDPOINT, files=files)

  # Process the response
  if response.status_code == 200:
    response_data = response.json()
    predicted_class = response_data['predicted_class']
    confidence = response_data['confidence']
    print(f"Predicted class: {predicted_class}, Confidence: {confidence}")
  else:
    print(f"Error: {response.status_code}")

# Example usage:
image_path = "../images/taylor_swift_1546367814.jpeg"
send_image_to_api(image_path)