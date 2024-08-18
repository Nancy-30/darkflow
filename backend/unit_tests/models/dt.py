import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def decision_tree(df, target_column):
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    # Convert target to numerical values
    y = y.map({'MET': 1, 'NOT MET': 0})

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(max_depth=None, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return accuracy, report

df = pd.read_excel(r"C:\Users\ashis\Downloads\flipkart_delay_in_delivery_SOP2_1207_v2.xlsx")

accuracy, report = decision_tree(df, "result")
print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')
