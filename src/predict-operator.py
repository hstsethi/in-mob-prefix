import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 
import joblib
import os

def checkSeriesInDatabase(series_to_predict: str, database_filename):
    data = pd.read_csv(database_filename)
    answer = data.loc[data["series"] == series_to_predict]["operator"]
    if answer.empty:
        return None
    else:
        return answer

def trainSaveModel(model_name, database_filename):
    data = pd.read_csv(database_filename)
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(data["series"].values.reshape(-1,1), data["operator"].values.reshape(-1,1)) # Pass a numpy array here directly so this method doesn't have to be called again and again.
    knn = KNeighborsClassifier() 
    knn.fit(X_train, y_train)
    train_pred = knn.predict(X_train)
    test_pred = knn.predict(X_test)
    train_acc = accuracy_score(train_pred, y_train)
    test_acc = accuracy_score(test_pred, y_test)
    print("Training accuracy:", train_acc, "\n", "Testing accuracy:,", test_acc)
    joblib.dump(knn, model_name)

def predictUsingSavedModel(model_to_load, series_to_predict):
    model = joblib.load(model_to_load)
    series_to_predict_array = np.array(int(series_to_predict)).reshape(-1,1) # predict() method takes an integer array
    predicted_operator = model.predict(series_to_predict_array)
    return predicted_operator

def main():
    # Implement Arg Parsing
    database_filename = "../data/9xxx-in-mob-prefix.csv"
    model_to_load = "../models/9xxx-knn.bin"
    series_to_predict = "9001"
    operator = checkSeriesInDatabase(series_to_predict, database_filename)
    if operator is not None:
        print("Operator Found in Database")
        print(operator) # Print on a seperate line so it's easier to grep
        return 0
    if os.path.exists(model_to_load):
        predicted_operator = predictUsingSavedModel(model_to_load, series_to_predict)
        print("Predicted Operator:", predicted_operator)
    else:
        print(model_to_load, "Doesn't exist. Training")
        trainSaveModel(model_to_load, database_filename)

main() 

