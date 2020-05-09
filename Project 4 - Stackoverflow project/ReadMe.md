# Stackoverflow survey 2019

The goal of this project is to study the 2019 Stackoverflow survey and to look into what factors are important when we speak about Career satisfaction according to this survey. I wanted to answer the following questions :
1. what factors are relevant to determining the career satisfaction
2. how does this satisfaction change when we get older
3. is the career satisfaction deeply related to the compensation


## Files description
- Stackoverflow survey 2019.ipynb : jupyter notebook where I made the study
- Stackoverflow survey 2019.html : same notebook in a html form
- survey_results_schema.csv : the questions asked in the survey
- ReadMe.md

I could not load the data of the survey because the file was too heavy for github. However one can find them on the following website : https://insights.stackoverflow.com/survey/


## Methodology and results
I chose amongst 3 models the one which fitted best the dataset when it was about modeling the career satisfaction. It was a bagging classifier - even though its f1 score was 0.58. I could then extract the features and their importances in the model.  

So the most important feature for the career satisfaction is the job satisfaction - which is logical after all. The other factors are less significant and I could not pick one which would be more important than the others. However it appeared that they mainly concerned the work environment - such as the tools used at work or the challenges face at work.

Concerning the satisfaction compared to the age of the population, I saw that the career satisfaction did not vary much except for retired people - who can appreciate their entire career without being biased by the present situation. Still we could see that the proportion of very satisfied decreases slightly between the ages of 30 and 50, and increases after 50 year old. It might be that the older we become the more we can appreciate our career. But these numbers are to be taken with caution because I did not have a huge population with an age.

Finaly I could see that the more satisfied you are the better your compensation tends to be. But once again one should be careful because not every body did give his compensation and because there might be other factors explaining the bigger compensation - such as the number of working hours - so it might be interesting to dive deeper into the subject. The difference exists but it is not so big that we can conclude easily. What could still be said is that if money does not make happiness, it certainly helps.

The results can also be found on the following website : https://medium.com/@pierre_henin/stackoverflow-survey-2019-what-makes-a-developers-career-satisfactory-c36e969a3eb4


## Aknowledgement
The data were provided by Stackoverflow.
