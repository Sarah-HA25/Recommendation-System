from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)
import pdb
import pickle 
import pandas as pd 
print("Load recommender")
start_time = time.time()
print("Recommenderr is successfully loaded")
print(time.time() - start_time, "seconds")


def load_model(path):
	product_id=123456
	loaded_model = pickle.load(open(path, 'rb'))
	return loaded_model.recommend(product_id)
	
def recommend_item(i):
	products = pd.read_csv('data/products.csv')
	products = products.drop(['title','created_at','published_at'], axis = 1)
	products.rename(columns = {'id':'product_id'}, inplace = True)
	products['product_id'] = products['product_id'].astype(str)
	#products = pd.read_pickle('/Users/patriciaporal/Downloads/archive/products')
	with open('collaborative/correlation_matrix','rb') as f: correlation_matrix = pickle.load(f)
	with open('collaborative/transposed_item','rb') as f: transposed_item = pickle.load(f)
	item=[]
	product_id = list(transposed_item.index)
	product_ID = product_id.index(i)
	correlation_product_ID = correlation_matrix[product_ID]
	Recommend = list(transposed_item.index[correlation_product_ID > 0.90])
	Recommend.remove(i)
	a = Recommend[0:3]
	for i in range(len(a)):
		item.append(products.loc[products['product_id'] == a[i]])
	return pd.concat(item).to_string(index=False)

@app.route("/", methods = ["POST", "GET"])
def index_page(text = ""):
	if request.method == "GET":
		return render_template('index.html')
		
@app.route("/result", methods = ["POST", "GET"])
def result_page():
	try:
		model_result=""
		col_model_result=""	
		selected_model = request.form["model_type"]
		selected_item = request.form["product_type_id"]
		if selected_model =="BaseLine":
			model_result = load_model('models/popularity_recommender.sav')
		else:
			col_model_result = recommend_item(selected_item)
		return render_template('result.html', model_result=model_result, col_model_result=col_model_result)
	except:
		return render_template("error.html")
	

if __name__ == "__main__":
	app.run(host = '0.0.0.0', port = 88, debug = True)
	#app.run(host='127.0.0.1', threaded=True)
