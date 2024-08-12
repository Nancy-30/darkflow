from flask import Flask, request, jsonify, Blueprint, current_app

model_bp = Blueprint('model', __name__)

@model_bp.route('/get_models', methods=['GET'])
def get_models():
    return jsonify({"message": "Get models"})

