#Imports
from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd


#load model and encoder
pipeline = joblib.load('./models_encoder/pipeline_rf.joblib')
encoder = joblib.load('./models_encoder/encoder.joblib')

#
app = FastAPI(
    title="Predicting if someone has Sepsis"
)

class SepsisFeatures(BaseModel):
    PRG : int
    PL : int
    PR : int
    SK : int
    TS : int
    M11 : float
    BD2 : float
    Age : int
    Insurance : int

#Endpoints
@app.get('/')
def Home():
    return "Sepsis Analysis"

@app.get('/info')
def appinfo():
    return "This is the info page"

@app.get('/info')
def appinfo():
    return "Sepsis Analysis API"

#post
# define a post request endpoint for making predictions based on the provided sepsis features
@app.post('/predict_sepsis')
def predict_sepsis(Sepsis_features: SepsisFeatures):
    df = pd.DataFrame([Sepsis_features.model_dump()])


    #perform prediction using the pre-trained pipeline
    prediction = pipeline.predict(df)

    #inversely transform the predicted value using the loaded encoder
    encoder_prediction=encoder.inverse_transform([prediction])[0]

    #return a dictionary with the predicted value
    return {'prediction' : encoder_prediction}

