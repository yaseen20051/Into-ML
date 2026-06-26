#!pip install requests==2.32.3

import requests 

url = "http://127.0.0.1:5000/predict"

data = {
    "Pregnancies" : 6, 
    "Glucose": 148, 
    "BloodPressure": 72, 
    "SkinThickness": 35, 
    "Insulin": 0, 
    "BMI": 33.6 , 
    "DiabetesPedigreeFunction": 0.627, 
    "Age": 50
}

responce = requests.post(url,json=data)
print(responce.json())