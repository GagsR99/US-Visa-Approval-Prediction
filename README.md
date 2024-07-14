# US-Visa-Approval-Prediction

## Git Commands

```bash
git add .

git commit -m "Updated"

git push origin main
 
```

## How to run?

```bash
conda create -n visa python=3.8 -y
```

```bash
conda activate visa
```

```bash
pip install -r requirements
```

```bash
python app.py
```

## Workflow

1. constant
2. config_entity
3. artifact_entity
4. component
5. pipeline
6. app.py / demo.py

## Export the environment variables
```bash

export MONGODB_URL="mongodb+srv://rasinenigagan:<password>@cluster0.5o80sus.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment
```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

## 3. Create ECR repo to store/save docker image
```bash
- Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject
```

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:
```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

## 6. Configure EC2 as self-hosted runner:
```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

## 7. Setup github secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO

# Workflow
## 1. Data Ingestion
Description: This is the initial step where raw data is collected from various sources. This can include databases, CSV files, APIs, web scraping, or other data streams. The goal is to gather all relevant data required for the project.

Tasks Involved:

Connecting to data sources
Extracting data
Loading data into a storage system (e.g., a data lake or a database)

## 2. Data Validation
Description: After data ingestion, it's crucial to ensure the quality and integrity of the data. Data validation involves checking for errors, inconsistencies, and completeness of the data. This step ensures that the data meets the required standards before any processing begins.

Tasks Involved:

Checking for missing or null values
Ensuring data types are correct
Validating data ranges and constraints
Removing duplicates
Handling outliers and anomalies

## 3. Data Transformation
Description: This step involves transforming the raw data into a format suitable for analysis and modeling. Data transformation includes cleaning, normalizing, aggregating, and enriching the data.

Tasks Involved:

Data cleaning (e.g., handling missing values, correcting errors)
Feature engineering (e.g., creating new features from existing ones)
Data normalization and scaling
Data encoding (e.g., converting categorical data to numerical)
Aggregating data (e.g., summarizing data over a period)

## 4. Model Training
Description: In this step, the transformed data is used to train machine learning models. The goal is to create a model that can learn patterns from the data and make accurate predictions.

Tasks Involved:

Splitting the data into training and testing sets
Selecting appropriate machine learning algorithms
Training the model using the training data
Tuning hyperparameters to optimize model performance

## 5. Model Evaluation
Description: Once the model is trained, it's important to evaluate its performance using the testing set. Model evaluation helps to understand how well the model generalizes to new, unseen data.

Tasks Involved:

Assessing model performance using metrics such as accuracy, precision, recall, F1 score, etc.
Performing cross-validation to ensure model robustness
Analyzing confusion matrix and ROC curves
Identifying overfitting or underfitting issues

## 6. Model Deployment (Pusher Model)
Description: The final step is deploying the trained and evaluated model into a production environment where it can be used to make predictions on new data. This step involves setting up the necessary infrastructure to serve the model and integrating it with existing systems.

Tasks Involved:

Saving the trained model (e.g., serialization)
Setting up a model serving environment (e.g., REST API, microservices)
Integrating the model with front-end applications or other systems
Monitoring the model in production to ensure it performs as expected
Updating the model periodically based on new data and feedback