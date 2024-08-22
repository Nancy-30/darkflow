import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import numpy as np
import mlflow
import mlflow.sklearn


def logistic_regression(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = LogisticRegression(max_iter=1000, random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    experiment_name = "Classification"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        max_iter = 1000
        random_state = 42

        mlflow.log_param("max_iter", max_iter)
        mlflow.log_param("random_state", random_state)

        mlflow.log_metric("accuracy", accuracy)

        with open("classification_report.txt", "w") as f:
            f.write(report)
        
        mlflow.log_artifact("classification_report.txt")

        mlflow.sklearn.log_model(clf, "Logistic")

    return accuracy, report


np.random.seed(0)

# Create a larger dataset
data = pd.DataFrame(
    {
        "A": np.random.randint(1, 100, size=100),
        "B": np.random.randint(1, 100, size=100),
        "C": np.random.randint(1, 100, size=100),
        "D": np.random.randint(1, 100, size=100),
        "E": np.random.randint(1, 100, size=100),
        "F": np.random.randint(1, 100, size=100),
        "G": np.random.randint(1, 100, size=100),
        "H": np.random.randint(1, 100, size=100),
        "I": np.random.randint(1, 100, size=100),
        "J": np.random.randint(1, 100, size=100),
        "Target": np.random.choice([0, 1], size=100),  # Binary target variable
    }
)

acc, report = logistic_regression(data, "Target")
print(acc)
print(report)