# Sparkify
The goal of this project is to predict a churn rate for a fictional music streaming service (Sparkify) using the spark environment. I want to identify the clients who might leave the service before they do so they can hypothetically receive discounts and incentives to stay.


## Library used
The following was used for the environment setup :  
- PySpark SQL  
- PySpark ML  


## Folder and files description
- Sparkify.ipynb : jupyter notebook where the exploratory analysis and the selection of the model were done  
- Sparkify.html : the same notebook in a html version  
- Sparkify full dataset.ipynb : jupyter notebook where I implemented the selected model on the full dataset on AWS  
- Sparkify full dataset.html : the same notebook in a html version  
- ReadMe.md  

The file mini_sparkify_event_data.json - which contained the dataset used throughout this project - could not be uploaded to Github because of its size.


## Feature engineering, results, and improvements
I chose to keep a few features available :  
- number of days since registration  
- number of days as a paid user  
- number of days as a free user  
- gender  
- level  
- total length of music played per user  
- events which seemed related to the churn rate in our exploratory analysis : bascialy when the user had an interaction with his service  

I fitted a logistic regression, a random forest classifier, and a gradient boosting classifier to see which one would give better results.  
Since the dataset used for choosing the model was small, I used F1 score as the metric to optimize.  
I used cross validation to optimize the different parameters of the models.  

The random forrest classifier was the model with the highest F1 score - 0.78. It is the model I used on the full dataset in AWS.

I also posted my study on Medium : https://medium.com/@pierre_henin/customer-churning-how-to-identify-them-in-order-to-keep-them-be8e9d8c541e


## Acknowledgement
Starter code and data were provided by Udacity.
