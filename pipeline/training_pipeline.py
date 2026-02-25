import pandas as pd
import joblib
import os
import yaml
from pipeline.config import CONFIG_PATH
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(X,Y):
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)
    test_size_param = config["model"]["test_size"]
    random_state_param = config["model"]["random_state"]
    models_path = config["models"]["path"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = test_size_param, stratify=Y, random_state=random_state_param)
    model = LogisticRegression()
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_train)
    accuracy = accuracy_score(Y_pred, Y_train)
    print("Predictions accuracy for training: " + accuracy)   
    Y_test_ped = model.predict(X_test)
    accuracy_test = accuracy_score(Y_test_ped, Y_test)
    print("Predictions accuracy for testing: " + accuracy_test)
    joblib.dump(model, models_path)
    print("Model saved successfully!")

