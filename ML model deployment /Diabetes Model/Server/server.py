import pickle 
import numpy 
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

with open("diabetes_model.pkl","rb") as model_file :
    model  = pickle.load(model_file)
with open("scaler_model.pkl","rb") as scaler_file:
    scaler = pickle.load(scaler_file)


@app.route("/")
def home():
    return "Diabetes Prediction App is running"

@app.route("/predict",methods=["POST"]) ## end point
def predict():
    try:
        # get the JSON data from the api request
        data = request.get_json()

        input_data = pd.DataFrame([data])
        # check if input is provided
        if not data:
            return jsonify({"error": "Input data not provided"}) ,400
        
        # validate input columns
        required_columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin"	, "BMI", "DiabetesPedigreeFunction", "Age"]

        if not all(col in input_data.columns for col in required_columns):
            return jsonify({"error": f"Required Columns missing. Required columns: {required_columns}"}) ,400
        
        ## scale the data  
        scaled_data = scaler.transform(input_data)  ## we don't need to put it in a list since it is a dataframe

        # make prediction 
        prediction = model.predict(scaled_data)

        # responce 
        responce = {
            "prediction":"Diabetes" if prediction[0] == 1 else "No Diabetes" 
        }

        return jsonify (responce)

    except Exception as e:
        return jsonify({"error":str(e)}),500
if __name__=="__main__":
    app.run(debug=True)
        