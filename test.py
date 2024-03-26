import pickle
import pytest
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    return model

def preprocess(data):
    scaler = StandardScaler()
    X = scaler.fit_transform(data)
    return X

def test_predictions():
    #hard coding data for now
    age = 50
    sex = 0
    chest_pain = 2
    resting_bps = 140
    cholesterol = 195
    fasting_blood_sugar = 1
    resting_ecg = 0
    max_heart_rate = 122
    angina = 0
    oldpeak = 1
    st_slope = 2

    features = [[age, sex, chest_pain, resting_bps, cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate, angina, oldpeak, st_slope]]
    preprocessed_features =  preprocess(features)

    #loading the model
    model = load_model()
    predictions = model.predict(preprocessed_features)

    # Check if predictions are of the expected shape
    assert predictions.shape == (1, 1) 
    assert np.all(predictions >= 0) and np.all(predictions <= 1)  # Ensure predictions are probabilities
