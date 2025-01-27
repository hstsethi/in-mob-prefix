import pandas as pd


def check_series_in_database(series_to_predict: str, database_filename):
    """
    Checks if the input series is a row in dataset and returns the operator column of that row.

    Returns:
    result_operator: Scalar Numpy array of the looked up operator value, if found.

    """

    data = pd.read_csv(database_filename)
    result_operator = data.loc[data["series"] == series_to_predict][
        "operator"
    ].values  # Return a scalar instead of dataframe for performance and easier debugging.
    if not result_operator.size == 0:
        return result_operator
