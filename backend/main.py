from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set Flask configuration variables
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['MONGO_DB_NAME'] = 'user_data'

from routes.data_ingestion import data_ingestion_bp

# Register Blueprints
app.register_blueprint(data_ingestion_bp)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
