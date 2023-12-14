
from fastapi import FastAPI
#import uvicorn
from pymongo import MongoClient
from entities.entities import *
import requests
import joblib
import numpy as np


app = FastAPI()

#mongo client init
client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection

#iris scale and model pkl files
irstd= joblib.load("./ml/iris-scale.pkl")
irmodel= joblib.load("./ml/iris-classif-lr.pkl")

#diabetes scale and model pkl files
std= joblib.load("./ml/diabete-scale.pkl")
model= joblib.load("./ml/diabete-classif-lr.pkl")

#databases links
dico= {"diabete": "https://github.com/plotly/datasets/blob/master/diabetes.csv", "iris": "https://github.com/plotly/datasets/blob/master/iris.csv"}

#introduction page
@app.get("/") 
async def read_root():
    return {"message": "This is the backend of mlops project."}

#allow to read either iris or diabetes databases
@app.get("/{db}") 
async def read_table(db:str):
    if db not in ["iris", "diabete"]:
        return {"error": "Data unknown (must be iris either diabete)"}
    res= requests.get(dico[db])
    data= res.json()["payload"]["blob"]["csv"]
    return {db: data}


#iris prediction thanks to form
@app.post("/predict/iris")
async def prediction(iris:Iris):
    dt= [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width ]
    #let's apply standard scaling
    test= irstd.transform([dt])
    #lets do the prediction
    pred= irmodel.predict(test)
    #proba
    proba= irmodel.predict_proba(test)[0].max()
    return {"prediction": pred[0], "proba": proba}


#iris prediction thanks to array of element
@app.post("/predict/all/iris")
async def prediction2(data: DataFrame):
    #let's apply standard scaling
    array= data.data
    test= irstd.transform(array)
    #lets do the prediction
    pred= irmodel.predict(test)
    #proba
    proba= np.amax(irmodel.predict_proba(test), axis = 1)
    return {"prediction": pred.tolist(), "proba": proba.tolist()}



#diabetes prediction thanks to form
@app.post("/predict/diabete")
async def prediction3(diabete:Diabete):
    dt1= [diabete.Pregnancies, diabete.Glucose, diabete.BloodPressure, diabete.SkinThickness, diabete.Insulin, diabete.BMI, diabete.DiabetesPedigreeFunction, diabete.Age ]
    #let's apply standard scaling
    test1= std.transform([dt1])
    #lets do the prediction
    pred1= model.predict(test1)
    #proba
    proba1= model.predict_proba(test1)[0].max()
    return {"prediction": pred1[0], "proba": proba1}


#diabetes prediction thanks to array of element
@app.post("/predict/all/diabete")
async def prediction4(data: DataFrame):
    #let's apply standard scaling
    array= data.data
    test= std.transform(array)
    #lets do the prediction
    pred= model.predict(test)
    #proba
    proba= np.amax(model.predict_proba(test), axis = 1)
    return {"prediction": pred.tolist(), "proba": proba.tolist()}


if __name__ == '__main__':
    app.run(debug=True)