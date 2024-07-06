
# The Eras Tour Image/Video classification (Taylor's version)

![Alt text](https://i.pinimg.com/736x/5d/07/d1/5d07d10b59ff9f4616fc87b86ee0b3d9.jpg)


This github repository hosts a computer vision Taylor Swift's themed image/video classification project.\
This project is inspired by the love of my girlfriend for this amazing artist.\
When I went to Taylor's concert in Lyon back in march I had the idea to create a machine learning application to classify the pictures that all her loving fans take during her show.  

# Built with

<p align="center">
  <a href="https://www.python.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python" width="40" height="40"/> 
  </a>   
  <a href="https://www.tensorflow.org/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="TensorFlow" width="40" height="40"/> 
  </a>   
  <a href="https://keras.io/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/keras/keras-original.svg" alt="Keras" width="40" height="40"/> 
  </a>   
  <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" alt="FastAPI" width="40" height="40"/> 
  </a>   
  <a href="https://streamlit.io/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/streamlit/streamlit-original.svg" alt="Streamlit" width="40" height="40"/> 
  </a>   
  <a href="https://opencv.org/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="OpenCV" width="40" height="40"/> 
  </a>   
  <a href="https://albumentations.ai/" target="_blank" rel="noreferrer">
    <img src="https://repository-images.githubusercontent.com/136265021/094cf680-b83f-11e9-9512-e4b538ed8e4d" alt="Albumentations" width="40" height="40"/> 
  </a>   
  <a href="https://www.docker.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="Docker" width="40" height="40"/> 
  </a> 
</p>

# Roadmap

The project has had a lot of iterations since its debut (album) in March 2024\
This roadmap will retrace every steps of the project:

- The first model created was capable of binary classification between the Speak Now and the Fearless eras of the Tour. The dataset only had 100 pictures per classes. The model was created from scratch with a very solid CNN architecture composed of SeparableConv2D layers which are more parameter efficient than basic Conv2D layers. The macro F1-score was good (about 90% on the test dataset) but the project of classifying the 10 eras was not fulfilled

- The second model could classify the 10 eras of the tour but since the model was written from scratch the macro F1-score sinked down to 80%. This was notably  due to class imbalance between the different eras

- The third model could handle class imbalance with inverse frequency class weights that is well explained in this Medium article (https://medium.com/@ravi.abhinav4/improving-class-imbalance-with-class-weights-in-machine-learning-af072fdd4aa4#:~:text=Using%20Class%20Weights%20to%20Address%20Class%20Imbalance,-Class%20weights%20offer&text=The%20idea%20is%20to%20assign,make%20better%20predictions%20for%20it). This model was the first model which was not written from scratch but was the fine-tuning of the famous VGG-16 model (Its macro F1-score at most reached 91%).

-  The fourth model was a fine-tuning of the better model RESNET-50 with a better built dataset composed of screenshots of The Eras Tour Movie, screenshots of public recordings of concerts in different locations and other public images of the concerts. The dataset contains roughly 2000 pictures. The models' F1-Score achieved 93% but there were issues during inferences with generalization of what the model learned.

- That is why the fifth and last model to date was built. The dataset has been augmented with the Albumentations framework which tripled the pictures it contains. More augmentation could be performed to the dataset but since I just have a CPU to train the model I could'nt have a bigger dataset. The model EfficientNetV2S has been fine-tuned and achieved an F1-Score of 95% for 8 hours of training.
- In most deep learning project the problem is the opacity of what the models learn. But in Computer Vision projects we can use something that is called GradCam that basically displays what the model is focusing on when it makes a decision. It creates a heatmap highlighting the areas of the image that were most important for the model's prediction. This function has been added to the project and allowed me to understand better what patterns the model had trouble focusing on.

- An idea of using the best model to classify videos of the concerts has emerged while I worked on the project. The approach is quite simple, instead of creating a brand new model using other technics to classify videos, we could simply take screenshots of the videos and classify every one of them. For each screenshots we can add the confidence of the classifiation of every classes and simply output the class with the greater confidence. This technique is clever but the inference time is multiplied by the number of screenshots that is classified.

# Web application

## Backend

The REST API where inference of the model prediction takes place has been written with FastAPI framework. The API has two endpoints:

### `/ping` (GET)

- Health check endpoint.
- **Response:** Returns "Hello World" if the API is running.

### `/predict` (POST)

- Predicts the Taylor Swift era from an uploaded image or video.
- **Request:**
    - `file`: The image or video file to classify (multipart/form-data).
- **Response (Image):**
    ```json
    {
        "predicted_class": "Era Name",
        "confidence": 0.85 
    }
    ```
- **Response (Video):**
    ```json
    {
        "predicted_class": "Era Name"
    }
    ```

  ## Frontend
The frontend of the web application has been written with Streamlit framework. This is a user-friendly web interface is built to interact with the API.

Image/Video Upload: Easily upload images or videos.
Real-time Predictions: View results instantly, including predicted era and confidence level (for images).

# Further experiments and improvements
- The design of the web application can be improved by using Figma to create a better layout of the Streamlit website
- Train the EfficientNetV2S or other models with a GPU on a cloud platform such as AWS or GCP with a bigger and better dataset
- Create a lighter version of the model (with TF-Lite) to be used in a React based website my partners are creating
- Deployment of the web application on a cloud platform or a platform like Heroku 

# Local deployment

If you want to have fun with the model you can use the following steps

## Requirements:
- Download Docker Desktop with this URL (https://www.docker.com/products/docker-desktop/) and install it on your device
- Download and install Git with this URL (https://git-scm.com/downloads) to be able to clone this repository

## Clone the repository

 1. Create a directory where to put the repository and perform the following command on a terminal

 ```bash
  git clone https://github.com/RonanRibouletPython/Taylor_Swift_Projects.git
```

## Run the Docker container locally 

Change directory to where you cloned the repository and do the following steps

1. Launch Docker Desktop

2. Build the Docker Image with the following command in your terminal:

```bash
  docker-compose build
```
3. Run the Docker container with the following command in your terminal:

```bash
  docker-compose up -d
```
## Use the application

1. Access the application
\
Open your web browser and go to the following address:

```bash
  http://localhost:8501/
```



