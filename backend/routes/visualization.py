import os
import io
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, request, jsonify, Blueprint, send_file
from utils.visualize_dataset import scatter_plot
from utils.database import get_document
from bson import ObjectId
import seaborn as sns

visualization_bp = Blueprint('visualization', __name__)

@visualization_bp.route('/scatter_plot', methods=['POST'])
def scatter_plot_route():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({"error": "Missing ID in request"}), 400

    try:
        objectId = ObjectId(id)
    except Exception as e:
        return jsonify({"error": f"Invalid ObjectId: {str(e)}"}), 400

    # Fetch the document from MongoDB using the object ID
    result = get_document('original_datasets', {'_id': objectId})

    if result is None:
        return jsonify({"error": "Document not found"}), 404

    # Extract data and metadata from the MongoDB document
    data = result.get('original_data')
    
    if not data:
        return jsonify({"error": "No data found in document"}), 400
    
    df = pd.DataFrame(data)

    # Automatically determine columns for the scatter plot
    columns = df.columns
    if len(columns) < 3:
        return jsonify({"error": "Insufficient columns for scatter plot"}), 400

    x_col = columns[2]  # First column for x-axis
    y_col = columns[1]  # Second column for y-axis
    hue_col = columns[0]  # Third column for hue

    # Generate the scatter plot
    buf = io.BytesIO()
    plt.figure()
    scatter_plot(df, x_col, y_col, hue_col, 'Scatter Plot')
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

@visualization_bp.route('/line_plot', methods=['POST'])
def line_plot_route():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({"error": "Missing ID in request"}), 400

    try:
        objectId = ObjectId(id)
    except Exception as e:
        return jsonify({"error": f"Invalid ObjectId: {str(e)}"}), 400

    # Fetch the document from MongoDB using the object ID
    result = get_document('original_datasets', {'_id': objectId})

    if result is None:
        return jsonify({"error": "Document not found"}), 404

    # Extract data and metadata from the MongoDB document
    data = result.get('original_data')
    
    if not data:
        return jsonify({"error": "No data found in document"}), 400
    
    df = pd.DataFrame(data)

    # Automatically determine columns for the line plot
    columns = df.columns
    if len(columns) < 2:
        return jsonify({"error": "Insufficient columns for line plot"}), 400

    x_col = columns[0]

    # Generate the line plot
    buf = io.BytesIO()
    plt.figure()
    plt.plot(df[x_col])
    plt.title('Line Plot')
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

@visualization_bp.route('/bar_plot', methods=['POST'])
def bar_plot_route():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({"error": "Missing ID in request"}), 400

    try:
        objectId = ObjectId(id)
    except Exception as e:
        return jsonify({"error": f"Invalid ObjectId: {str(e)}"}), 400

    # Fetch the document from MongoDB using the object ID
    result = get_document('original_datasets', {'_id': objectId})

    if result is None:
        return jsonify({"error": "Document not found"}), 404

    # Extract data and metadata from the MongoDB document
    data = result.get('original_data')
    
    if not data:
        return jsonify({"error": "No data found in document"}), 400
    
    df = pd.DataFrame(data)

    # Automatically determine columns for the bar plot
    columns = df.columns
    if len(columns) < 2:
        return jsonify({"error": "Insufficient columns for bar plot"}), 400

    x_col = columns[0]
    y_col = columns[1]

    # Generate the bar plot
    buf = io.BytesIO()
    plt.figure()
    plt.bar(df[x_col], df[y_col])
    plt.title('Bar Plot')
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

@visualization_bp.route('/box_plot', methods=['POST'])
def box_plot_route():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({"error": "Missing ID in request"}), 400

    try:
        objectId = ObjectId(id)
    except Exception as e:
        return jsonify({"error": f"Invalid ObjectId: {str(e)}"}), 400

    # Fetch the document from MongoDB using the object ID
    result = get_document('original_datasets', {'_id': objectId})

    if result is None:
        return jsonify({"error": "Document not found"}), 404

    # Extract data and metadata from the MongoDB document
    data = result.get('original_data')
    
    if not data:
        return jsonify({"error": "No data found in document"}), 400
    
    df = pd.DataFrame(data)

    # Automatically determine columns for the box plot
    columns = df.columns
    if len(columns) < 2:
        return jsonify({"error": "Insufficient columns for box plot"}), 400

    x_col = columns[0]
    y_col = columns[1]

    # Generate the box plot
    buf = io.BytesIO()
    plt.figure()
    plt.boxplot(df[y_col])
    plt.title('Box Plot')
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

@visualization_bp.route('/violin_plot', methods=['POST'])
def violin_plot_route():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({"error": "Missing ID in request"}), 400

    try:
        objectId = ObjectId(id)
    except Exception as e:
        return jsonify({"error": f"Invalid ObjectId: {str(e)}"}), 400

    # Fetch the document from MongoDB using the object ID
    result = get_document('original_datasets', {'_id': objectId})

    if result is None:
        return jsonify({"error": "Document not found"}), 404

    # Extract data and metadata from the MongoDB document
    data = result.get('original_data')
    
    if not data:
        return jsonify({"error": "No data found in document"}), 400
    
    df = pd.DataFrame(data)

    # Automatically determine columns for the violin plot
    columns = df.columns
    if len(columns) < 2:
        return jsonify({"error": "Insufficient columns for violin plot"}), 400

    x_col = columns[0]
    y_col = columns[1]

    # Generate the violin plot
    buf = io.BytesIO()
    plt.figure()
    sns.violinplot(data=df, x=x_col, y=y_col)
    plt.title('Violin Plot')
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

@visualization_bp.route('/heatmap', methods=['POST'])
def heatmap_route():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({"error": "Missing ID in request"}), 400

    try:
        objectId = ObjectId(id)
    except Exception as e:
        return jsonify({"error": f"Invalid ObjectId: {str(e)}"}), 400

    # Fetch the document from MongoDB using the object ID
    result = get_document('original_datasets', {'_id': objectId})

    if result is None:
        return jsonify({"error": "Document not found"}), 404

    # Extract data and metadata from the MongoDB document
    data = result.get('original_data')
    
    if not data:
        return jsonify({"error": "No data found in document"}), 400
    
    df = pd.DataFrame(data)

    # Generate the heatmap
    buf = io.BytesIO()
    plt.figure()
    sns.heatmap(df.corr(), annot=True)
    plt.title('Heatmap')
    plt.savefig(buf, format='png')
    buf.seek(0)

    return send_file(buf, mimetype='image/png')