from flask import Flask, request, jsonify, Blueprint, current_app
from models.classification import xgbcl, knn, logistic, rfc
from models.regression import xgbr, linear, rfr, dt
import pandas as pd

model_bp = Blueprint('model', __name__)

@model_bp.route('/get_models', methods=['GET'])
def get_models():
    return jsonify({"message": "Get models"})

@model_bp.route('/choose_model', methods=['POST'])
def choose_model():
    model_type = request.json['model_type']
    model_name = request.json['model_name']
    current_app.config['model_type'] = model_type
    current_app.config['model_name'] = model_name

    df = pd.DataFrame()

    if model_type == "regression":
        print("here1")
        if model_name == "xgbr":
            print("here2")
            return xgbr.xgboost_regression(df, "")
    return jsonify({"model_type": model_type, "model_name": model_name})
