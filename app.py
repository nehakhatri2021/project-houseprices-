import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('assisgnment2.pkl','rb')) 

@app.route('/')           # url with run with"/""
def home():
  
    return render_template("index.html")   #will make the func return to html page
  
@app.route('/predict',methods=['GET'])   #url will look for "/predict" to run
def predict():
    
    
    '''
    For rendering results on HTML GUI
    
    '''
    exp = float(request.args.get('exp'))
    
    prediction = model.predict([[exp]])
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted price for given sqft is : {}'.format(prediction))


app.run(debug=True)
