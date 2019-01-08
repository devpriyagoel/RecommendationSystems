# RecommendationSystems 
a series of different recommendation systems  
The dataset used can be downloaded from https://www.kaggle.com/rounakbanik/the-movies-dataset/version/7#movies_metadata.csv
Contents:
#Reco1.ipynb : jupyter notebook on which I prepared my 'cleaner' data_set ('metadata_exploded.csv') for my web app MovieRecommender. 
Each directory which follows contains web apps based on different recommendation systems
#1 - MovieRecommender
Its a flask-based web app which serves as a knowledge based recommender system which takes input from the user and accordingly give them results. It will ask the user for the genres, preferred range of duration and timeline of movies he/she is looking for.
Using the information collected, it will recommend movies to the user that have a high weighted rating (according to the IMDB formula) and that satisfy the preceding conditions.
