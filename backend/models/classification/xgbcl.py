import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

import numpy as np
import mlflow
import mlflow.sklearn


def xgboost_classifier(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # y = y.map({'MET': 1, 'NOT MET': 0})

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    clf = XGBClassifier(
        use_label_encoder=False, eval_metric="mlogloss", random_state=42
    )
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    experiment_name = "Classification"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        mlflow.set_tag("mlflow.runName", "XGBoost Classifier")

        eval_metric = "mlogloss"
        random_state = 42

        mlflow.log_param("eval_metric", eval_metric)
        mlflow.log_param("random_state", random_state)

        mlflow.log_metric("accuracy", accuracy)

        with open("classification_report.txt", "w") as f:
            f.write(report)

        mlflow.log_artifact("classification_report.txt")

        mlflow.sklearn.log_model(clf, "XGBCL")

    return accuracy, report
