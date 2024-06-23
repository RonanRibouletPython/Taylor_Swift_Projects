
# Project Title

This project is a very simple binary classification of images from Taylor Swift the Eras Tour.\
Two types of images can be upload to the web app created.\
The images will be classified being either to the Fearless or the Speak Now Era of the tour.\

## Project update

The project has been updatet for a Multiclass-Classification problem with most of the Eras of the very famous Taylor's Eras World Tour


## Roadmap

- The binary classification app deployed will be changed to a multiclass classification to match all the eras of the tour: DONE

- The accuracy of 94% in the test dataset can be improved via other Deep Learning techniques -> Fine-tuning of the VGG16 model training with the imagenet dataset + new very solid CNN architecture with SeparableConv2D layers which are more parameter efficient than basic Conv2D layers + Dataset imbalance gestion with inverse frequency class weights 

- The design of the web application can be drastically improved


## Deployment

To deploy this project you have to download or run your Docker application\

As soon as Docker runs on your device:

1. Build the Docker Image:

```bash
  docker-compose build
```
2. Run the Docker container

```bash
  docker-compose up -d
```

3. Access the application
\
Open your web browser and go to:

```bash
  http://localhost:8000/static/index.html
```