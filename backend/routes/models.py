from flask import Flask, request, jsonify, Blueprint
from models.classification import xgbcl, knn, logistic, rfc
from models.regression import xgbr, linear, rfr, dt
from utils.best_model import getBestRegressionModel, getBestClassificationModel
import pandas as pd
from utils.detect_problem import detect_problem

model_bp = Blueprint('model', __name__)

@model_bp.route('/get_models', methods=['GET'])
def get_models():
    return jsonify({"message": "Get models"})

@model_bp.route('/train_model', methods=['POST'])
def train_best_model():
    # Read the uploaded file into a DataFrame
    file = request.files.get('processed_df')
    if not file:
        return jsonify({"message": "No file uploaded"}), 400

    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)
        elif file.filename.endswith('.json'):
            df = pd.read_json(file)
        else:
            return jsonify({"message": "Unsupported file format"}), 400
        
        # Clean column names
        df.columns = [col.strip().replace(' ', '_').replace('[', '').replace(']', '').replace('<', '').replace('>', '') for col in df.columns]
        
    except Exception as e:
        return jsonify({"message": f"Error reading file: {str(e)}"}), 400

    target_column = request.form.get('target_column')
    if not target_column:
        return jsonify({"message": "No target column provided"}), 400

    model_type = detect_problem(df, target_column)
    
    if model_type == "Regression":
        best_model, metrics = getBestRegressionModel(df, target_column)
    elif model_type == "Classification":
        best_model, metrics = getBestClassificationModel(df, target_column)
    else:
        return jsonify({"message": "Invalid model type"}), 400

    return jsonify({"best_model": best_model, "metrics": metrics})
