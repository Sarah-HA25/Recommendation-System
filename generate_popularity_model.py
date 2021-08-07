import pandas as pd
import popularity_recommender
import pickle
import sklearn

orders_list=pd.read_csv("data/orders_items.csv")
products=pd.read_csv("data/products.csv")


from sklearn.model_selection import train_test_split
orders_train, orders_test = train_test_split(orders_list, test_size = 0.10, random_state=0)

pr=popularity_recommender.Popularity_Recommender()

pr.create(orders_train,products)
#products.head()
filename = 'popularity_recommender.sav'
pickle.dump(pr, open(filename, 'wb'))
 

product_id=123456
loaded_model = pickle.load(open(filename, 'rb'))
	
print(loaded_model.recommend(product_id))
