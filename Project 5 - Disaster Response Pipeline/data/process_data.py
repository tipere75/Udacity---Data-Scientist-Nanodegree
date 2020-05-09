import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    Import the messages and the categories and merge it together
    Input : 
        - message_filepath
        - category_file path
    Output :
        Dataframe df with the messages and the categories value associated
    """
    #import message data
    messages = pd.read_csv(messages_filepath)
    
    #import categories of messages
    categories = pd.read_csv(categories_filepath)
    
    #merge the 2 datasets
    df = messages.merge(categories, left_on="id", right_on="id")
    
    return df



def clean_data(df):
    """
    Clean the data : split categories into separate columns, convert category values to just numbers 0 or 1 and remove duplicates row
    Input : 
        the dataframe with messages and categories column
    Output : 
        the cleaned dataframe
    """
    #split categories into separate columns
    categories = df["categories"].str.split(";", expand=True)
    row = categories.iloc[0]
    category_colnames = list(map(lambda x: x[:(len(x)-2)], row))
    categories.columns = category_colnames
    
    #convert category values to just numbers 0 or 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1:]    
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    #replace categories column in df with new category columns
    df.drop("categories", axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)
    
    #remove duplicates
    df.drop_duplicates(inplace=True)
    
    return df



def save_data(df, database_filename):
    """
    Save the cleaned dataframe into a SQL database
    Input :
        - cleaned dataframe
        - path to the SQL database
    Output :
        a SQLite database
    """
    engine = create_engine("sqlite:///" + database_filename)
    df.to_sql(database_filename, engine, index=False)
    


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print("Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}"
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print("Cleaning data...")
        df = clean_data(df)
        
        print("Saving data...\n    DATABASE: {}".format(database_filepath))
        save_data(df, database_filepath)
        
        print("Cleaned data saved to database!")
        
        print(df.head())
    
    else:
        print("Please provide the filepaths of the messages and categories "\
              "datasets as the first and second argument respectively, as "\
              "well as the filepath of the database to save the cleaned data "\
              "to as the third argument. \n\nExample: python process_data.py "\
              "disaster_messages.csv disaster_categories.csv "\
              "DisasterResponse.db")


if __name__ == "__main__":
    main()