from fastapi import FastAPI
from pydantic import BaseModel
import json
import pickle

app = FastAPI()

#define request schema
class inputData(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

#load model
model = pickle.load(open('diabetes_model.sav','rb'))

@app.get('/')
def hello():
    return {"message":"Hello world"}

#predict diabetes route
@app.post('/predict-diabetes')
def predictDiabetes(reqLoad: inputData):
    inputData = reqLoad.json()
    inputDataDict = json.loads(inputData)
    preg = inputDataDict['Pregnancies']
    glu = inputDataDict['Glucose']
    bp = inputDataDict['BloodPressure']
    skin = inputDataDict['SkinThickness']
    insulin = inputDataDict['Insulin']
    bmi = inputDataDict['BMI']
    dpf = inputDataDict['DiabetesPedigreeFunction']
    age = inputDataDict['Age']

    inputList = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = model.predict([inputList])

    if prediction ==0:
        return {"message":"patient is not diabetic"}
    else:
        return {"message":"patient is diabetic"}

