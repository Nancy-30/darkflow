import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

import numpy as np
import mlflow
import mlflow.sklearn


def randomforest_regression(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, max_depth=None, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    experiment_name = "Regression"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        mlflow.set_tag("mlflow.runName", "Random Forest Regression")
        random_state = 42
        n_estimators = 100
        mlflow.log_param("random_state", random_state)
        mlflow.log_param("n_estimators", n_estimators)

        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)

        # mlflow.log_artifact("classification_report.txt")
        mlflow.sklearn.log_model(model, "Random Forest")

    return mse, r2
