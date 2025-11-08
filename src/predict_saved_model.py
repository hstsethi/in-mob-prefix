import joblib
import numpy as np


def predict_using_saved_model(model_to_load, series_to_predict):
    """Make predictions about operator using pretrained model"""
    model = joblib.load(model_to_load)
    series_to_predict_array = np.array(int(series_to_predict)).reshape(
        -1, 1
    )  # predict() method takes an array instead of a scalar
    predicted_operator = model.predict(series_to_predict_array)
    return predicted_operator
