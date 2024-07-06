from fastapi import FastAPI, UploadFile, File
import uvicorn 
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

from fastapi.staticfiles import StaticFiles
from backend.utils import capture_random_frames, delete_files_in_directory, count_files_in_directory

# Load the tensorflow model
PROD_MODEL_PATH = "best_model_weighted_RESNET50_getty_aug.keras"

PROD_MODEL = tf.keras.models.load_model(PROD_MODEL_PATH)

CLASS_NAMES = ["1989", "Acoustic", "Fearless", "Folkmore", "Lover", "Midnights", "Red", "Reputation", "Speak Now", "TTPD"]

app = FastAPI()

app.mount("/static", StaticFiles(directory="C:/Users/Ronan/Documents/ML/Taylor_Swift_Projects/CNN/static"), name="static")

@app.get("/ping")
async def read_root():
    return "Hello World"

def read_file_as_img(data)-> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))

    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    temp_video_path = f"temp_{file.filename}"
    with open(temp_video_path, "wb") as buffer:
        buffer.write(await file.read())

    output_folder = "screenshots"
    num_captures = 10  # Capture a number of screenshots

    capture_random_frames(temp_video_path, output_folder, num_captures)

    # Remove the temporary video file
    os.remove(temp_video_path)

    predicted_classes = {
    "1989": 0.0,
    "Acoustic": 0.0,
    "Fearless": 0.0,
    "Folkmore": 0.0,
    "Lover": 0.0,
    "Midnights": 0.0,
    "Red": 0.0,
    "Reputation": 0.0,
    "Speak Now": 0.0,
    "TTPD": 0.0
}
    
    num_imgs = count_files_in_directory(output_folder)

    for i in range(0, num_imgs): 

        img_path = f"screenshots/{i}.jpg"

        with open(img_path, 'rb') as img_file:
            # Read the binary data
            img_data = img_file.read()

            img = read_file_as_img(img_data)

        img = tf.image.resize(img, [384, 384])
        img_batch = np.expand_dims(img, 0)
        predictions = PROD_MODEL.predict(img_batch)

        # Update the accumulated predictions
        predicted_classes["1989"] += predictions[0][0]
        predicted_classes["Acoustic"] += predictions[0][1]
        predicted_classes["Fearless"] += predictions[0][2]
        predicted_classes["Folkmore"] += predictions[0][3]
        predicted_classes["Lover"] += predictions[0][4]
        predicted_classes["Midnights"] += predictions[0][5]
        predicted_classes["Red"] += predictions[0][6]
        predicted_classes["Reputation"] += predictions[0][7]
        predicted_classes["Speak Now"] += predictions[0][8]
        predicted_classes["TTPD"] += predictions[0][9]

    predicted_class = max(predicted_classes, key=predicted_classes.get)

    # Delete the screenshots after prediction
    directory_to_clean = output_folder
    delete_files_in_directory(directory_to_clean)

    return{
        "predicted_class": predicted_class
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)