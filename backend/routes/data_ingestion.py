from flask import Flask, request, jsonify
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENTIONS = {'csv', 'xlsx', 'json', 'xls'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS

@app.route('/upload_dataset', methods = ['POST'])
def upload_dataset():
    if 'file' not in request.files:
        return jsonify({"Error" : "no file in the request"}), 400
    
    file = request.files[file]

    if file.filename == '':
        return jsonify({"Error" : "No file exists"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(save_path)
            elif filename.endswith('.xlsx', 'xls'):
                df = pd.read_excel(save_path)
            elif filename.endswith('.json'):
                df = pd.read_json
            
            else:
                return jsonify({"error" : "unsupported format"}), 400
            
            return jsonify({"message": "File uploaded successfully", "data": df.head().to_dict()}), 201

        except Exception as e:
            return jsonify({"error": f"Error processing file: {str(e)}"}), 500
    else:
        return jsonify({"error": "File type not allowed"}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


    
