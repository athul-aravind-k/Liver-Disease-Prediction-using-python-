# -*- coding: utf-8 -*-
"""
@author: Athul Aravind
"""

import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle


app = Flask(__name__)
model = pickle.load(open('liverdml.pkl','rb'))


@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    age=request.form.get("age")
    Total_Bilirubin=request.form.get("TotalBilrubin")
    Direct_Bilirubin=request.form.get("DirectBilirubin")
    Alkaline_Phosphotase=request.form.get("AlkalinePhosphotase")
    Alamine_Aminotransferase=request.form.get("AlamineAminotransferase")
    Aspartate_Aminotransferase=request.form.get("AspartateAminotransferase")
    Total_Protiens=request.form.get("TotalProtiens")
    Albumin=request.form.get("Albumin1")
    Albumin_and_Globulin_Ratio=request.form.get("AlbuminandGlobulinRatio")
    gnd=request.form.get("gender")
    Gender_Female=0
    Gender_Male=0
    if gnd=="male":
       Gender_Female=0
       Gender_Male=1
    elif gnd=="female":
        Gender_Female=1
        Gender_Male=0
    input=([[int(age),float(Total_Bilirubin),float(Direct_Bilirubin),float(Alkaline_Phosphotase),float(Alamine_Aminotransferase),float(Aspartate_Aminotransferase),float(Total_Protiens),float(Albumin),float(Albumin_and_Globulin_Ratio),int(Gender_Female),int(Gender_Male)]])
    prediction = model.predict(input)
    #return render_template('home.html', prediction_text='Prediction Success {}'.format(prediction))
    if prediction==0:
            return render_template('home.html',prediction_text='You Have No Liver Disease')
    elif prediction==1:
            return render_template('home.html',prediction_text='You Have Liver Disease')
    

if __name__ == '__main__':
    app.run(debug=True)
