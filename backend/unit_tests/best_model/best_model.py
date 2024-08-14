import pandas as pd

from utils.best_model import getBestRegressionModel, getBestClassificationModel

df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 4, 3, 2, 1],
    'feature3': [10, 20, 30, 40, 50],
    'feature4': [50, 40, 30, 20, 10],
    'feature5': [100, 200, 300, 400, 500],
    'target': [10, 20, 30, 40, 50]
})

target_column = 'target'

print(getBestRegressionModel(df, target_column))


df2 = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 4, 3, 2, 1],
    'feature3': [10, 20, 30, 40, 50],
    'feature4': [50, 40, 30, 20, 10],
    'feature5': [100, 200, 300, 400, 500],
    'target': [1, 0, 1, 0, 1]
})

target_column = 'target'

print(getBestClassificationModel(df2, target_column))
