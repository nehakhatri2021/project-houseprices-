import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('assignment2.pkl','rb')) 

@app.route('/')           # url with run with"/""
def home():
  
    return render_template("index.html")   #will make the func return to html page
  
@app.route('/predict',methods=['GET'])   #url will look for "/predict" to run
def predict():
    
    
    '''
    For rendering results on HTML GUI
    
    '''
    sqft = float(request.args.get('sqft'))
    
    prediction = model.predict([[sqft]])
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted price for given sqft is : {}'.format(prediction))

if __name__ == "__main__":
  app.run(debug=True)
