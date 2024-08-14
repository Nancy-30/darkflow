from models.regression import xgbr, linear, rfr, dt
from models.classification import xgbcl, knn, logistic, rfc

# ANSI color code for blue text
BLUE = '\033[94m'
RESET = '\033[0m'

def print_blue(message):
    print(f"{BLUE}{message}{RESET}")

def getBestRegressionModel(processed_df, target_column):
    print_blue("Evaluating regression models...")
    
    # Evaluate each model
    xgbr_mse, _ = xgbr.xgboost_regression(processed_df, target_column)
    print_blue(f"XGBR MSE: {xgbr_mse}")
    
    linear_mse, _ = linear.linear_regression(processed_df, target_column)
    print_blue(f"Linear Regression MSE: {linear_mse}")
    
    rfr_mse, _ = rfr.randomforest_regression(processed_df, target_column)
    print_blue(f"Random Forest Regression MSE: {rfr_mse}")
    
    dt_mse, _ = dt.decision_tree(processed_df, target_column)
    print_blue(f"Decision Tree MSE: {dt_mse}")
    
    # Determine the best model
    mse_scores = [xgbr_mse, linear_mse, rfr_mse, dt_mse]
    best_model_score = min(mse_scores)
    print_blue(f"Best MSE: {best_model_score}")

    if best_model_score == xgbr_mse:
        return "XGBR"
    elif best_model_score == linear_mse:
        return "Linear"
    elif best_model_score == rfr_mse:
        return "RFR"
    elif best_model_score == dt_mse:
        return "DT"
    else:
        return "Error"

def getBestClassificationModel(processed_df, target_column):
    print_blue("Evaluating classification models...")
    
    # Evaluate each model
    xgbcl_acc, _ = xgbcl.xgboost_classifier(processed_df, target_column)
    print_blue(f"XGBCL Accuracy: {xgbcl_acc}")
    
    knn_acc, _ = knn.k_nearest_neighbors(processed_df, target_column)
    print_blue(f"KNN Accuracy: {knn_acc}")
    
    logistic_acc, _ = logistic.logistic_regression(processed_df, target_column)
    print_blue(f"Logistic Regression Accuracy: {logistic_acc}")
    
    rfc_acc, _ = rfc.random_forest_classifier(processed_df, target_column)
    print_blue(f"RFC Accuracy: {rfc_acc}")
    
    # Determine the best model
    acc_scores = [xgbcl_acc, knn_acc, logistic_acc, rfc_acc]
    best_model_score = max(acc_scores)
    print_blue(f"Best Accuracy: {best_model_score}")

    if best_model_score == xgbcl_acc:
        return "XGBCL"
    elif best_model_score == knn_acc:
        return "KNN"
    elif best_model_score == logistic_acc:
        return "Logistic"
    elif best_model_score == rfc_acc:
        return "RFC"
    else:
        return "Error"
