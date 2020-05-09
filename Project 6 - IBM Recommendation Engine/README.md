# Recommendation Engine with IBM
The goal of this project is to build an recommendation engine for the IBM data science online community. The engin is based on user behavior and articles data to surface content most likely to be relevant to a user.

## Folder and files description
In the folder data are stored two files :
- articles_community.csv : list of the articles and some informations such a the full name and the content
- user-item-interactions.csv : list of every entry on an article made by a user

The file located at the root are the following :
- Recommendations_with_IBM.ipynb :  jupyter notebook where the recommendation engine was developped
- Recommendations_with_IBM.html : same file in a HTML format
- README.md : readme
- project-tests.py, top_10.p, top_20.p, top_5.p, user_item_matrix.p : files for checking some development along the process

## Summmary
The following tasks have been performed during the project :
- Exploratory data analysis
- Rank based recommendations : To get started I first find the most popular articles based on the number of interactions users had with theses articles. This part is for making recommendations to new users - given that they didn't have any interaction with any article so we don't know much about their preferences
- User-user based collaborative filtering : for a given user, I look for users that are similar in terme of the items they have interacted with so that I could recommend the same items
- Content-based recommendation engine : using NLP techniques, I base my recommendations on the similarity between the title of each article.
- Matrix factorization : I finaly used a machine learning approach to make recommendations. Using the decomposition of the user-item interactions matrix, I was able to predict with more or less accuracy which articles an individual might interact with

## Licensing, authors and aknowledgements
The starter code were given by Udacity and the data were provided by IBM Watson
