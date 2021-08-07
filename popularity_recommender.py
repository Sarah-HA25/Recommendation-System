import numpy
import pandas as pd

class Popularity_Recommender():

	def __init__(self):
		self.orders_list = None

		self.products = None

		self.product_popularity = None

		self.popularity_recommendataions = None

	def create(self,orders_list,products):

		self.orders_list = orders_list

		self.products = products

		
   
		products_types=products[["id","product_type"]]
		products_types=products_types.rename(columns={"id": "product_id", "product_type": "type"})



		#print(len(products.id.unique()))

		#print(len(orders_list.product_id.unique()))

		popularity_df = pd.DataFrame(orders_list, columns= ['id','product_id'])
		popular_ser= popularity_df.pivot_table(columns=['product_id'], aggfunc='size')
		popular_ser=popular_ser.sort_values(ascending=False)
		
		popular_products=popular_ser.to_frame()
		#inds=list(range(1,len(orders_list.product_id.unique())))
		#index_list= pd.Series(inds)
		popular_products=popular_products.reset_index()
		
		popular_products=popular_products.rename(columns={"product_id": "product_id", "0": "quantity"})
		#popular_products=popular_products.add_index([index_list])
		
		#print(popular_products.head(10))


		popular_items= pd.merge(popular_products, products_types, on='product_id')       
		#print (">>  Popular items in our store that you may like <<","\n" )
		recomended=(popular_items.head(10))
		#print (recomended)

		# The first 15 items are saved into the popularity_recommendataions and it is returned. 
		self.popularity_recommendataions = recomended


	# Method to user created recommendations
	def recommend(self,dummy):

		# Init the user_recommendataion var by popularity_recommendataions since the recommendations has been saved into this column.
		user_recommendataion = self.popularity_recommendataions[["product_id","type"]]
		user_recommendataion["product_id"]=user_recommendataion["product_id"].astype(str).str[:-2]
		user_recommendataion=user_recommendataion.rename(columns={"product_id": "Product ID", "type": "Type"})
		return user_recommendataion.to_string(index=False)