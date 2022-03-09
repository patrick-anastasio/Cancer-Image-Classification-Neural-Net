# Acute Lymphoblastic Leukemia (ALL) Diagnosis Using Neural Networks

[A Guide to Leukemia](https://www.healthline.com/health/leukemia)

[Chilhood Cancer Statistics](https://www.acco.org/childhood-cancer-statistics/)

[Childhood Leukemia Statistics](https://www.acco.org/childhood-leukemias/)

[Survival Rates and Outlook for Acute Lymphocytic Leukemia (ALL)](https://www.healthline.com/health/acute-lymphocytic-leukemia-survival-rate-outlook)

>### *Dance like no one is watching*     
>### *Live like you are dying*           
>### *Regret the things you've done, not what you didn't do*

![Spirits UP](data/happy_young_girl_with_cancer-1200x628-facebook-1200x628.jpeg) 

## Business Understanding:

>### Cancer is the leading disease-related cause of death in children aged 5 to 14, and leukemia is the most prevalent form of cancer in children. 75% will be diagnosed with Acute Lymphoblastic Leukemia (ALL). [Childhood Leukemia Statistics](https://www.acco.org/childhood-leukemias/)

>### Survival rate is directly correlated with how early it is caught. If we can catch the leukemia early enough, we can save many more lives. 

>### I seek to create a method to accurately diagnose leukemia by taking pictures of white blood cells and predicting if they are normal or cancerous. A Machine Learning model that can accurately identify leukemia cells will enhance the medical profession’s ability to diagnosis at an early stage. Humans are prone to error so a model that can accurately predict will help with that human error.

## Data Understanding

> ### Leukemia manifests itself in immature white blood cells called blasts. The data for this project consists of images of white blood cells that have been analyzed under a microscope and labeled as normal or cancerous.
>### The dataset comes from the [Cancer Imaging Archive](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=52758223)    
>>#### To download this, you will need to use the data sharing browser extension [IBM Aspera Connect](https://www.ibm.com/aspera/connect/). 
>>>When you download the data it will automatically walk you through the process, it is simple and painless.

### The data for this project was acquired in three parts:

> #### 1) A training set separated into 3 directories, each with separate class labeled directories
> #### 2) A validation set with all images in the same directory and a CSV file with filenames and class labels
> #### 3) A test set with no class labels

- #### We will combine all the data of the training and validation sets into labeled directories and split the whole into training, validation, and test sets for use in this project.
> The code steps that follow below will set this up, creating all necessary directories from the downloaded file . Just create a fodrop the downloaded file into a 

- #### We will re-name the provided test set and to "unlabeled_images" and reserve it for demonstration purposes, as there is no way of knowing if the predicitions are correct and how a particular model is performing with it.

```
Our Class indeces will be:
{'Normal': 0, 'ALL': 1}
```

## The Methods

- Preprocessing the data using TensorFlow, organizing the directories and generating the images and labels

- Splitting the data between training, validation and holdout testing sets.

- Balancing the dataset and randomly augmenting images using rotation, horizontal and vertical flipping, and brightness adjustments for optimal robust model training.

- Iterating through various Neural Network models to maximize prediction Recall. We will used techniques like regularizers and dropping out layers to avoid overfitting.

## Results

- Our final model was a Convolutional Neural Network. We used images generated with the listed data augmentation techniques. We had three (3) hidden Convolutional layers using 32, 64, and 128 nodes respectively. We finished with a flattening layer, and two dense layers with 64 and 128 nodes respectively. We used the "relu" activation function throughout and the "sigmoid" function on our output layer.










