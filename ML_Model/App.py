from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import joblib
app=Flask(__name__)

ml_f=open("linear_reg.pkl","rb")
ml_model=joblib.load(ml_f)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method=='POST':
        try:
            NewYork=float(request.form['NewYork'])
            Florida=float(request.form['Florida'])
            California=float(request.form['California'])
            RnDSpend=float(request.form['RnDSpend'])
            AdminSpend=float(request.form['AdminSpend'])
            MrktngSpend=float(request.form['MrktngSpend'])
            pred_args=[RnDSpend,AdminSpend,MrktngSpend,California,Florida,NewYork]

            pred_args_arr=np.array(pred_args)
            pred_args_arr=pred_args_arr.reshape(1,-1)

            model_predict=ml_model.predict(pred_args_arr)
            model_predict=round(float(model_predict),2)
        except valueError:
            return "Check the values again"

    return render_template('home.html',prediction=model_predict)

if __name__ =="__main__":
    app.run()
