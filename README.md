# Recommendation-System
An online clothing store aims to increase the average bill per customer, we proposed the solution as a recommender system which suggests a set of related products for customers, we tested two models and prepared a demo using Flask. 

# Data:
We used the data of an online clothing store 
https://www.kaggle.com/ruichenyang/ecommerce-clothing-store

# Models:
We tested two models :
* Baseline: Popularity based recommendation (recommend top purchased items)
* Collaborative Filtering: Singular Value Decomposition (SVD) based Recommendation


# Code Structure:
- data_exploration.ipynb : a jupyter notebook to explore data and make some statistics 
- generate_popularity_model.py : where we create popularity model, popularity_recommender.py is used inside it 
- collaborative folder : which contains all notebooks and files to generate collaborative model 
- models folder : which contains the two saved generated models (i.e collaborative + popularity)
- static folder: which contains the css of the demo pages 
- templates folder : it contains our html pages 
- data folder : it contains the link of our data, in addition to two csv files (orders_items + products' specification) 
- demo_screenshots folder: contains screenshots from demo 


# Environment : 
We used google colab for data exploration,as for model building python 3.7.5, the backend was written with Flask (Python) and the frontend using Bootstrap.

# To test the program just run this:
python main.py

# Demo Sample 
![img](https://github.com/Sarah-HA25/Recommendation-System-/blob/main/demo_screenshots/demo1.PNG)
After hitting submit, it shows the recommendations according to the selected model 
![img](https://github.com/Sarah-HA25/Recommendation-System-/blob/main/demo_screenshots/result1.PNG)
There is also an error page, in case of undefined product 
![img](https://github.com/Sarah-HA25/Recommendation-System-/blob/main/demo_screenshots/result3.PNG)

