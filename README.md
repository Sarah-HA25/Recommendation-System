# Recommendation-System-
An online clothing store aims to increase the average bill per customer, proposed the solution as a recommender system which suggests a set of other products for customers, we tested two models and prepared a demo using Flask. 

# Data:
We used the data of an online clothing store 
https://www.kaggle.com/ruichenyang/ecommerce-clothing-store

# Models:
We tested two models :
Baseline: Popularity based product recommendation(Recommend top Purchased Items)
Collaborative Filtering: Singular Value Decomposition (SVD) based Recommender System


# Code Structure:
-data_exploration.ipynb : a jupyter notebook to explore data and make some statistics 
-generate_popularity_model.py : where we create popularity model, popularity_recommender.py is used inside it 
-collaborative folder : Which contains all notebooks and files to generate collaborative model 
-models folder : which contains the two saved generated models (i.e collaborative + popularity)
-static folder: which contains the css of the demo pages 
-templates folder : it contains our html pages 
-data folder : it contains the link of our data, in addition to two csv files (orders_items + products' specification) 
-demo_screenshots folder: contains screenshots from demo 


# Environment : 
We used google colab for data exploration,AS for model building python 3.7.5, the backend was written by Flask (Python) and the frontend using Bootstrap.

# To test the program just run this:
python main.py
