from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib


def train_save_model(model_name, database_filename):
    """Train modes for specified prefix using GradientBoostingClassifier classifier and save them"""
    data = pd.read_csv(database_filename)
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(
        data["series"].values.reshape(-1, 1), data["operator"].values.reshape(-1, 1)
    )  # Pass a numpy array here directly so this method doesn't have to be called again and again.
    gbc = GradientBoostingClassifier(n_estimators=75, max_depth=2, random_state=42)
    gbc.fit(X_train, y_train.ravel())
    train_pred = gbc.predict(X_train)
    test_pred = gbc.predict(X_test)
    train_acc = accuracy_score(train_pred, y_train)
    test_acc = accuracy_score(test_pred, y_test)
    print("Training accuracy:", train_acc, "\n", "Testing accuracy:,", test_acc)
    joblib.dump(gbc, model_name)
    print(f"Saved {model_name} to disk")
