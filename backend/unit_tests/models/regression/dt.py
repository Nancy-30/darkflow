import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

import numpy as np
import mlflow
import mlflow.sklearn

import numpy as np


def decision_tree(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    # # Convert target to numerical values
    # y = y.map({'MET': 1, 'NOT MET': 0})

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(max_depth=None, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    experiment_name = "Regression"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run() as run:
        mlflow.set_tag("mlflow.runName", "Decision Tree")
        random_state = 60
        mlflow.log_param("random_state", random_state)

        mlflow.log_metric("accuracy", accuracy)

        with open("classification_report.txt", "w") as f:
            f.write(report)

        mlflow.log_artifact("classification_report.txt")
        mlflow.sklearn.log_model(model, "Decision Tree")

        print(accuracy)

    return accuracy, report


np.random.seed(0)

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

accuracy, report = decision_tree(data, "Target")
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
