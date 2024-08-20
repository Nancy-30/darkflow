import pandas as pd

def detect_problem(df, target_column):
    target_data = df[target_column]

    if pd.api.types.is_numeric_dtype(target_data):
        unique_values = target_data.unique()

        if unique_values <= 10:
            return "Classification"
        else:
            return "Regression"
    else:
        return "Classification"