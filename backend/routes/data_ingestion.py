from flask import Blueprint, request, jsonify, current_app
import pandas as pd
import os
from werkzeug.utils import secure_filename
from .database import insert_document
from utils.data_preprocessing import data_preprocessing
from utils.detect_problem import detect_problem

data_ingestion_bp = Blueprint('data_ingestion', __name__)

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'json', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@data_ingestion_bp.route('/upload_dataset', methods=['POST'])
def upload_dataset():
    print("yaha")
    if 'file' not in request.files:
        return jsonify({"Error": "No file in the request"}), 400
    
    file = request.files['file']


    if file.filename == '':
        return jsonify({"Error": "No file exists"}), 400
   
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(save_path)
            elif filename.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(save_path)
            elif filename.endswith('.json'):
                df = pd.read_json(save_path)
            else:
                return jsonify({"error": "Unsupported format"}), 400
            
            # removing primary column from the dataset
            index = request.form.get('index', None)
            target = request.form.get('target', None)

            # Detect type of problem
            problem = detect_problem(df.copy(), target)
            
            # apply data preprocessing on the dataset
            preprocessed_df = data_preprocessing(df.copy(), {index, target})
            
            original_dataset_info = {
                "filename": filename,
                "original_data": df.to_dict(orient='records'),
                "index": index,
                "target": target
            }

            original_insert_id = insert_document('original_datasets', original_dataset_info)

            preprocessed_dataset_info = {
                "filename": filename,
                "preprocessed_data": preprocessed_df.to_dict(orient='records'),
                "index": index,
                "target": target,
                "original_dataset_id": original_insert_id
            }

            preprocessed_insert_id = insert_document('preprocessed_datasets', preprocessed_dataset_info)


            return jsonify({
                "message": "File uploaded successfully",
                "problem-category": problem,
                "original_data_preview": df.head().to_dict(),
                "preprocessed_data_preview": preprocessed_df.head().to_dict(),
                "original_insert_id": str(original_insert_id),
                "preprocessed_insert_id": str(preprocessed_insert_id)
            }), 201

        except Exception as e:
            return jsonify({"error": f"Error processing file: {str(e)}"}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400
