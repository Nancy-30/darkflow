from flask import Flask, request, jsonify, Blueprint, current_app
from models.classification import xgbcl, knn, logistic, rfc
from models.regression import xgbr, linear, rfr, dt
from utils.best_model import getBestRegressionModel, getBestClassificationModel
import pandas as pd

model_bp = Blueprint('model', __name__)

# ANSI color code for blue text
BLUE = '\033[94m'
RESET = '\033[0m'

def print_blue(message):
    print(f"{BLUE}{message}{RESET}")

@model_bp.route('/get_models', methods=['GET'])
def get_models():
    return jsonify({"message": "Get models"})

@model_bp.route('/choose_model', methods=['POST'])
def choose_model():
    model_type = request.json.get('model_type')
    if model_type in ["regression", "classification"]:
        current_app.config['model_type'] = model_type
        print_blue(f"Model type chosen: {model_type}")
        return jsonify({"model_type": model_type})
    else:
        print_blue(f"Invalid model type: {model_type}")
        return jsonify({"message": "Invalid model type"}), 400
    
@model_bp.route('/train_model', methods=['POST'])
def train_best_model():
    # Read the uploaded Excel file into a DataFrame
    file = request.files.get('processed_df')
    if not file:
        print_blue("No file uploaded.")
        return jsonify({"message": "No file uploaded"}), 400

    try:
        # Use read_excel for Excel files
        df = pd.read_excel(file)
        
        # Clean and debug column names
        df.columns = [col.strip().replace(' ', '_').replace('[', '').replace(']', '').replace('<', '').replace('>', '') for col in df.columns]
        print_blue(f"Cleaned column names: {df.columns.tolist()}")
        
    except Exception as e:
        print_blue(f"Error reading file: {str(e)}")
        return jsonify({"message": f"Error reading file: {str(e)}"}), 400

    target_column = request.form.get('target_column')
    if not target_column:
        print_blue("No target column provided.")
        return jsonify({"message": "No target column provided"}), 400

    model_type = current_app.config.get('model_type')
    print_blue(f"Model type from config: {model_type}")
    
    if model_type == "regression":
        print_blue("Training regression model.")
        best_model = getBestRegressionModel(df, target_column)
    elif model_type == "classification":
        print_blue("Training classification model.")
        best_model = getBestClassificationModel(df, target_column)
    else:
        print_blue(f"Invalid model type: {model_type}")
        return jsonify({"message": "Invalid model type"}), 400

    return jsonify({"best_model": best_model})
