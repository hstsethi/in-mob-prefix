import os
import argparse

from train_save import train_save_model
from check_series_db import check_series_in_database
from predict_saved_model import predict_using_saved_model


def main():

    parser = argparse.ArgumentParser(
        description="Script to predict/lookup operator name based on series. Part of in-mob-prefix project by HstSethi <hstsethi@outlook.com>"
    )
    parser.add_argument("database", help=".csv database to use")
    parser.add_argument(
        "series",
        help="Series to predict. Must be a positive 4 digit integer between 6-9",
    )
    parser.add_argument("model", help="Model to load")
    args = parser.parse_args()
    database_filename = args.database
    model_to_load = args.model
    series_to_predict = args.series
    if not series_to_predict.isnumeric() and not len(series_to_predict) == 4:
        raise (
            ValueError(
                "Series must be an integer and have exactly 4 digits ranging from 6-9"
            )
        )
    operator = check_series_in_database(series_to_predict, database_filename)
    if operator is not None:
        print(
            "Operator Found in Database:\n", operator
        )  # Print on a seperate line so it's easier to grep
    elif os.path.exists(model_to_load):
        predicted_operator = predict_using_saved_model(model_to_load, series_to_predict)
        print("Predicted Operator:\n", predicted_operator)
    else:
        print(f"Error: {model_to_load} Does not exist. Starting model training")
        train_save_model(model_to_load, database_filename)
        predict_using_saved_model(model_to_load, series_to_predict)


main()
