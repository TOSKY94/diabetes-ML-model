import requests
import json


url = 'http://127.0.0.1:8000/predict-diabetes'

data1 = {
  "Pregnancies": 1,
  "Glucose": 85,
  "BloodPressure": 66,
  "SkinThickness": 29,
  "Insulin": 0,
  "BMI": 26.6,
  "DiabetesPedigreeFunction": 0.351,
  "Age": 31
}

data2 = {
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}

input_json = json.dumps(data1)

response = requests.post(url, data=input_json)

print(response.text)
