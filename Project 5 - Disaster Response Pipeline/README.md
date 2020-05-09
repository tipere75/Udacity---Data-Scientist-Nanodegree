# Disaster Response Pipeline Project

The goal if this project is to build an API that classifies messages that people sent during disasters thanks to a machine learning pipeline.


## Folder and files description
There are three main folders :
1. app
    - templates : templates for the API
    - run.py : to launch the API
2. data
    - disaster_messages.csv : the messages used for training the ML pipeline
    - disaster_categries.csv : the category of each message
    - process_data.py : ETL pipeline to read, clean and save data into a SQLite database
    - DisasterResponse.db : the SQLite database containing the messages and their category
3. models
    - train_classifier.py : ML pipeline to trian and export a classifier
    - classifier.pkl : trained model used in the API


## Instructions
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


## Licensing, authors and acknowledgements
The starter code were given by Udacity and the data were provided by FigureEight.
