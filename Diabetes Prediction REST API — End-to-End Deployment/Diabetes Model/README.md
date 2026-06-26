# Diabetes Prediction Model

An end-to-end machine learning project for predicting diabetes using the **PIMA Indians Diabetes Dataset**. The project includes data exploration, preprocessing, model training with Logistic Regression, and deployment via a Flask API.

## Project Structure

```
Diabetes Model/
├── Diabetes model deployment.ipynb   # Jupyter notebook with full pipeline
├── diabetes.csv                       # PIMA Indians Diabetes Dataset
├── README.md                          # Project documentation
└── Server/
    ├── server.py                      # Flask API for serving predictions
    ├── test.py                        # Test script for the API
    ├── requirments.txt                # Python dependencies
    ├── diabetes_model.pkl             # Trained Logistic Regression model
    └── scaler_model.pkl               # Fitted StandardScaler
```

## Dataset

The dataset contains 768 records with the following features:

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skin fold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body mass index (weight in kg/(height in m)^2) |
| DiabetesPedigreeFunction | Diabetes pedigree function (genetic risk score) |
| Age | Age (years) |
| Outcome | Target variable (1 = diabetic, 0 = non-diabetic) |

## Model Pipeline

1. **Data Exploration** - Check for duplicates, missing values, skewness, and summary statistics
2. **Preprocessing** - Replace impossible zero values in medical features with NaN and impute using median
3. **Feature Scaling** - Standardize features using `StandardScaler`
4. **Model Training** - Train a `LogisticRegression` classifier
5. **Evaluation** - Achieves ~80% training accuracy and ~71% test accuracy
6. **Serialization** - Save model and scaler as pickle files for deployment

## Flask API

The `Server/server.py` file provides a REST API:

- `GET /` - Health check endpoint
- `POST /predict` - Accepts JSON with patient data and returns prediction

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
  }'
```

### Example Response

```json
{"prediction": "Diabetes"}
```

## Setup & Usage

1. Install dependencies:
   ```bash
   pip install -r Server/requirments.txt
   ```

2. Run the API server:
   ```bash
   python Server/server.py
   ```

3. Test with sample data:
   ```bash
   python Server/test.py
   ```

## Dependencies

- Flask 3.1.0
- NumPy 2.2.1
- Pandas 2.2.3
- scikit-learn 1.6.0
