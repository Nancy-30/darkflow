from models.regression import xgbr, linear, rfr, dt
from models.classification import xgbcl, knn, logistic, rfc

# ANSI color code for blue text
BLUE = '\033[94m'
RESET = '\033[0m'

def print_blue(message):
    print(f"{BLUE}{message}{RESET}")

def getBestRegressionModel(processed_df, target_column):
    # Evaluate each model
    xgbr_mse, _ = xgbr.xgboost_regression(processed_df, target_column)
    linear_mse, _ = linear.linear_regression(processed_df, target_column)
    rfr_mse, _ = rfr.randomforest_regression(processed_df, target_column)
    dt_mse, _ = dt.decision_tree(processed_df, target_column)
    
    # Determine the best model
    mse_scores = {
        "XGBR": xgbr_mse,
        "Linear": linear_mse,
        "RFR": rfr_mse,
        "DT": dt_mse
    }
    best_model = min(mse_scores, key=mse_scores.get)
    best_model_score = mse_scores[best_model]

    # Return the best model and metrics
    return best_model, mse_scores

def getBestClassificationModel(processed_df, target_column):
    # Evaluate each model
    xgbcl_acc, _ = xgbcl.xgboost_classifier(processed_df, target_column)
    knn_acc, _ = knn.k_nearest_neighbors(processed_df, target_column)
    logistic_acc, _ = logistic.logistic_regression(processed_df, target_column)
    rfc_acc, _ = rfc.random_forest_classifier(processed_df, target_column)
    
    # Determine the best model
    acc_scores = {
        "XGBCL": xgbcl_acc,
        "KNN": knn_acc,
        "Logistic": logistic_acc,
        "RFC": rfc_acc
    }
    best_model = max(acc_scores, key=acc_scores.get)
    best_model_score = acc_scores[best_model]

    # Return the best model and metrics
    return best_model, acc_scores
