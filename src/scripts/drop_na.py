import pandas as pd


def drop_null_cols(filename):
    data = pd.read_csv(filename)
    data.info()
    data.dropna(thresh=2, inplace=True)
    data.to_csv(filename, index=False)
    data.info()


def main():
    filename = "9xxx-in-mob-prefix.csv"
    drop_null_cols(filename)


main()
