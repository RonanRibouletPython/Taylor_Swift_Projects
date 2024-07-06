
# The Eras Tour Image/Video classification (Taylor's version)

![image](https://github.com/RonanRibouletPython/Taylor_Swift_Projects/assets/164629492/2250debd-c805-43d7-a47e-90d73d7b2055)

This github repository hosts a computer vision Taylor Swift's themed image/video classification project.\
This project is inspired by the love of my girlfriend for this amazing artist.\
When I went to Taylor's concert in Lyon back in march I had the idea to create a machine learning application to classify the pictures that all her loving fans take during her show.  

## Roadmap

The project has had a lot of iterations since its debut (album) in June 2024\
This roadmap will retrace every steps of the project:

- The first model created was capable of binary classification between the Speak Now and the Fearless eras of the Tour. The dataset only had 100 pictures per classes. The model was created from scratch with a very solid CNN architecture composed of SeparableConv2D layers which are more parameter efficient than basic Conv2D layers. The macro F1-score was good (about 90% on the test dataset) but the project of classifying the 10 eras was not fulfilled

- The second model could classify the 10 eras of the tour but since the model was written from scratch the macro F1-score sinked down to 80%. This was notably  due to class imbalance between the different eras

- The third model could handle class imbalance with inverse frequency class weights that is well explained in the Medium article (https://medium.com/@ravi.abhinav4/improving-class-imbalance-with-class-weights-in-machine-learning-af072fdd4aa4#:~:text=Using%20Class%20Weights%20to%20Address%20Class%20Imbalance,-Class%20weights%20offer&text=The%20idea%20is%20to%20assign,make%20better%20predictions%20for%20it). This model was the first model which was not written from scratch but was a fine-tuning of the famous VGG-16 model (Its macro F1-score at most reached 91%)

-  The fourth model 

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



