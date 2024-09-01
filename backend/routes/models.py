from flask import Flask, request, jsonify, Blueprint
from models.classification import xgbcl, knn, logistic, rfc
from models.regression import xgbr, linear, rfr, dt
from utils.best_model import getBestRegressionModel, getBestClassificationModel
import pandas as pd
from utils.detect_problem import detect_problem
from bson import ObjectId
from utils.database import get_document

model_bp = Blueprint('model', __name__)

@model_bp.route('/get_models', methods=['GET'])
def get_models():
    return jsonify({"message": "Get models"})

@model_bp.route('/train_model', methods=['POST'])
def train_best_model():
    # Get the dataset_id from the request
    dataset_id = request.form.get('dataset_id')
    if not dataset_id:
        return jsonify({"message": "No dataset ID provided"}), 400

    try:
        # Convert the string ID to an ObjectId and fetch the document from MongoDB
        dataset_object_id = ObjectId(dataset_id)
        dataset_info = get_document('original_datasets', {"_id": dataset_object_id})
        
        if not dataset_info:
            return jsonify({"message": "Dataset not found"}), 404
        

        # Load the dataset from the data saved in the document
        df = pd.DataFrame(dataset_info['original_data'])
        
        # Clean column names (if needed)
        df.columns = [col.strip().replace(' ', '_').replace('[', '').replace(']', '').replace('<', '').replace('>', '') for col in df.columns]
        
    except Exception as e:
        return jsonify({"message": f"Error loading dataset: {str(e)}"}), 400

    target_column = dataset_info.get('target')
    if not target_column:
        return jsonify({"message": "Target column not found in dataset information"}), 400

    model_type = detect_problem(df, target_column)
    
    if model_type == "Regression":
        best_model, metrics = getBestRegressionModel(df, target_column)
    elif model_type == "Classification":
        best_model, metrics = getBestClassificationModel(df, target_column)
    else:
        return jsonify({"message": "Invalid model type"}), 400

    return jsonify({"best_model": best_model, "metrics": metrics})
