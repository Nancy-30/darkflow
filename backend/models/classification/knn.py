import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import mlflow
import mlflow.sklearn


def k_nearest_neighbors(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    clf = KNeighborsClassifier(n_neighbors=4)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # ml flow
    experiment_name = "Classification"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        
        mlflow.set_tag("mlflow.runName", "KNN Model")

        n_neighbors = 3
        mlflow.log_param("n_neighbors", n_neighbors)

        mlflow.log_metric("accuracy", accuracy)

        with open("classification_report.txt", "w") as f:
            f.write(report)

        mlflow.log_artifact("classification_report.txt")

        mlflow.sklearn.log_model(clf, "KNN_Classification")

        print(accuracy)

    return accuracy, report, clf