import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

def k_nearest_neighbors(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = KNeighborsClassifier(n_neighbors=4)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return accuracy, report

acc, _ = k_nearest_neighbors(pd.DataFrame({
    "A": [1, 2, 3, 4, 5],
    "B": [6, 7, 8, 9, 10],
    "C": [11, 12, 13, 14, 15],
    "D": [16, 17, 18, 19, 20],
    "E": [21, 22, 23, 24, 25],
    "F": [26, 27, 28, 29, 30],
    "G": [31, 32, 33, 34, 35],
    "H": [36, 37, 38, 39, 40],
    "I": [41, 42, 43, 44, 45],
    "J": [46, 47, 48, 49, 50],
    "Target": [1, 0, 1, 0, 1]
}), "Target")

print(acc)