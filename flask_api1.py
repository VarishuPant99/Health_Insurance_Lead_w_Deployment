# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:40:43 2021

@author: Varishu
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger      #Front end U.I.
from flasgger import Swagger  #API that automatically creates front end

#Initialize Flask
app=Flask(__name__)
Swagger(app)

#Read Model
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

#App route creates a Webpage
@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict():
    
    #Description for U.I.
    
    #Type is class(num,str,etc)
    #Required: Is parameter req or not
    #Responses:If status is 200,show description
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number      
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    #Getting Variables from URL
    #Eg-
    #http://127.0.0.1:5000/predict?variance=0&skewness=-3&curtosis=-2&entropy=1
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    kurtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    pred=classifier.predict([[variance,skewness,kurtosis,entropy]])
    return "The predicted value is"+str(pred)
   
@app.route('/predict_file',methods=["POST"])
def predict_file():
    #Make sure there's one indentation before U.I. part
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    
    #Reading variables from test file and predicting
    df_test=pd.read_csv(request.files.get("file"))
    pred=classifier.predict(df_test)
    return "The predicted value is"+str(list(pred))
    #Go to http://127.0.0.1:5000/apidocs/

if __name__=='__main__':
    app.run()