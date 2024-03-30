import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    return model    

def preprocess(data):
    scaler = StandardScaler()
    X = scaler.fit_transform(data)
    return X

def predict():
    #Predict will take data input from user to do predictions
    
    age = int(input("Enter age: "))
    sex = int(input("Enter sex (0 for female, 1 for male): "))
    chest_pain = int(input("Enter chest pain type (0-3): "))
    resting_bps = int(input("Enter resting blood pressure: "))
    cholesterol = int(input("Enter cholesterol level: "))
    fasting_blood_sugar = int(input("Enter fasting blood sugar (0 for <= 120 mg/dl, 1 for > 120 mg/dl): "))
    resting_ecg = int(input("Enter resting electrocardiographic results (0-2): "))
    max_heart_rate = int(input("Enter maximum heart rate achieved: "))
    angina = int(input("Enter presence of exercise induced angina (0 for No, 1 for Yes): "))
    oldpeak = float(input("Enter ST depression induced by exercise relative to rest: "))
    st_slope = float(input("Enter slope of the peak exercise ST segment (0-2): "))

    features = [[age, sex, chest_pain, resting_bps, cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate, angina, oldpeak, st_slope]]
    preprocessed_features =  preprocess(features)

    #loading the model
    model = load_model()
    predictions = model.predict(preprocessed_features)
    print(f"Prediction Probability: {predictions[0][0]}")
    # Set a threshold value
    threshold = 0.5

    # Map the model output to either 0 or 1 based on the threshold
    result = 1 if predictions[0][0] >= threshold else 0
    if result == 1:
        print("You have a heart disease")
    else:
        print("You do not have a heart disease")   
    

predict()
