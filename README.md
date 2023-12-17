## End to End Machine Learning Project

# Math Score Prediction Application

![Application Preview](end2end.PNG)

## Overview 🚀

This application is designed to predict math scores based on various input features. It utilizes machine learning models to provide accurate predictions and facilitate data-driven decision-making.

## Features

- **Data Ingestion:** Ingest the data .
- **Data Preprocessing:** Clean and preprocess input data for optimal model training.
- **Machine Learning Models:** Implement various regression models for predicting math scores.
- **Docker Integration:** Containerize the application for easy deployment and scalability.
- **Azure Deployment:** Deploy the application on Azure using App Service Linux plans.

## Requirements

- Python 3.x
- Docker
- Azure Account (for deployment)

## Getting Started 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/AdnaneAbou/MathScore-MLapp.git


2. Change directory to MathScore-MLapp:
    
   ```bash
   cd MathScore-MLapp
     
3. Install the necessary packages :

   ```bash
   pip install -r requirements.txt


4. Perform Data Ingestion Processing and Model Training :

    ```bash
     python src\components\data_ingestion.py
   
5. Run the Application :

    ```bash
     python app.py


## Build Docker Image and run Containers 

1. Build docker Image from Dockerfile :
   
   ```bash
     docker -t build MathScore-MLapp .
  
2. Run Docker Container :
   ```bash
     docker run -p 5000:5000 MathScore-MLapp

3. Use an existing Image from Dockerhub :
    ```bash
     docker pull adnaneabou/ml-app:latest
    
4. Run container :
   ```bash
     docker run -p 5000:5000 adnaneabou/ml-app:latest



## Azure Deployment

Deployment on azure using Container Registry 

1. Create a Container Registry in Azure
2. Create a Web App in Azure
3. Build docker Image for the Container Registry

   ```bash
   docker build -t container-registry-username/imagename:latest .

 4. Connect to the Container Registry
     ```bash
     docker login  container-registry-username

5. Push the Image to the Container Registry
   ```bash
      docker build  container-registry-username/imagename:latest 



# Project Conclusion 📊

## Summary

The Math Score Prediction Application has successfully concluded its journey, achieving significant milestones in the realms of machine learning, deployment, and community engagement.

### Key Achievements

1. **Machine Learning Models:** Implemented and trained a variety of regression models, showcasing robust performance in predicting math scores.

2. **Docker Integration:** Successfully integrated Docker, ensuring portability and scalability of the application across diverse environments.

3. **Azure Deployment:** Deployed the application on Azure using App Service Linux plans, making the math score prediction accessible to a wider audience.


## Thank You 🙌



 


