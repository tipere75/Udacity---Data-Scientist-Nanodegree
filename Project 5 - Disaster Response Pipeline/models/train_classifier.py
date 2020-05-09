import sys
import re
import pandas as pd
import pickle
import nltk
nltk.download(["punkt", "wordnet", "stopwords"])

from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#regex to recognize urls
url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'



def load_data(database_filepath):
    """
    Load the database obtained from pocess_data.py
    Input :
        database_filepath
    Output : 
        - X : messages (features)
        - y categories (target)
    """
    #load the database
    engine = create_engine("sqlite:///" + database_filepath)
    df = pd.read_sql_table(database_filepath, con=engine)
    
    #split it into features and target
    X = df["message"]
    y = df.iloc[:,4:]
    
    #add the "genre" variable as a dummy variable to Y
    y_add = pd.get_dummies(df["genre"])
    y = pd.concat([y, y_add], axis=1)
    
    #extract the category names
    category_names = list(df.columns[4:])
    
    return X, y, category_names



def tokenize(text):
    """
    Tokenize function to process the data
    Input : 
        original text
    Output :
        normalized, tokenized and lemmatized text without stopwords
    """
    #normalize text : convert to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    
    #tokenize text
    words = word_tokenize(text)
    
    #remove stop words
    words = [word for word in words if word not in stopwords.words("english")]
    
    #lemmatize
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(w) for w in words]
    
    return clean_tokens



def build_model():
    """
    Build a ML pipeline with tfidf, random forrest and gridsearch
    Input : 
        None
    Output :
        ML_model
    """
    #define the pipeline
    pipeline = Pipeline([
            ("vect", CountVectorizer(tokenizer=tokenize)),
            ("tfidf", TfidfTransformer()),
            ("clf", MultiOutputClassifier(RandomForestClassifier()))
            ])
    
    #define the parameters to tune
    parameters = {
        "clf__estimator__max_depth": [10, 20, None],
        "clf__estimator__min_samples_leaf": [1, 5, 10],
        "clf__estimator__min_samples_split": [2, 5,]
    }
    
    #define the model with gridsearch
    ML_model = GridSearchCV(pipeline, parameters)
    
    return ML_model
    


def evaluate_model(model, X_test, Y_test, category_names):
    """
    Train and evaluate the model
    Input :
        - model to use
        - features of the test set
        - target of the test set to compare with the predictions
        - category names
    Output : for each category and agregated
        - category
        - precision
        - recall
        - f_beta_score
    """
    #predictions
    y_pred = model.predict(X_test)
    
    #accuracy of each category
    ncol = 0
    for category in category_names:
        acc_score = accuracy_score(Y_test[category], y_pred[:, ncol])
        ncol += 1
        print("Category : {0} \n Accuracy score : {1}".format(category, acc_score))
        
    

def save_model(model, model_filepath):
    """
    Save the model as a pickle file
    Input : 
        - model
        - pickle file path
    Output :
        pickle file
    """
    pickle.dump(model, open(model_filepath, "wb"))



def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print("Loading data...\n    DATABASE: {}".format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print("Building model...")
        model = build_model()
        
        print("Training model...")
        model.fit(X_train, Y_train)
        
        print("Evaluating model...")
        evaluate_model(model, X_test, Y_test, category_names)

        print("Saving model...\n    MODEL: {}".format(model_filepath))
        save_model(model, model_filepath)

        print("Trained model saved!")

    else:
        print("Please provide the filepath of the disaster messages database "\
              "as the first argument and the filepath of the pickle file to "\
              "save the model to as the second argument. \n\nExample: python "\
              "train_classifier.py ../data/DisasterResponse.db classifier.pkl")


if __name__ == "__main__":
    main()