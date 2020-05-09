# DSND--Project--Charity-ML
This is the first project of the Data Science Nanodegree Program.


## Project Overview
CharityML is a fictious charity organization that provides financial support for people learning machine learning. In an effort to improve donor outreach, I build an algorithm that best identifies potential donors.  

My goal was to evaluate and optimize several different supervised learners to determine which algorithm will provide the highest donation yield. I choose to compare three different learners : a Naive Bayes learner, a Random Forest algorithm and a SVM model. The best models in terms of accuracy were the SVM model and the Random Forest. The latter appeared to be the best model because of a better computing efficiency.

## List of files
- finding_donors.ipynb : the jupyter notebook with all questions answered and all code cells executed and displaying output  
- finding_donors.html : the html export of the same file
- visuals.py : the python file for plotting the results

## Data used for the Project
The modified census dataset consists of approximately 32,000 data points, with each datapoint having 13 features. This dataset is a modified version of the dataset published in the paper "Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid", by Ron Kohavi.  

**Features :**  
- age : Age
- workclass : Working Class (Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked)
education_level : Level of Education (Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool)
- education-num : Number of educational years completed
- marital-status : Marital status (Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse)
- occupation : Work Occupation (Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces)
- relationship : Relationship Status (Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried)
- race : Race (White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black)
- sex : Sex (Female, Male)
- capital-gain : Monetary Capital Gains
- capital-loss : Monetary Capital Losses
- hours-per-week : Average Hours Per Week Worked
- native-country : Native Country (United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands)  

**Target :**
- income : Income Class (<=50K, >50K)
