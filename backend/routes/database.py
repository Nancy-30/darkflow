from pymongo import MongoClient
from flask import current_app
from flask import Blueprint, jsonify

database_bp = Blueprint('database', __name__)

def get_mongo_client():
    mongo_uri = current_app.config['MONGO_URI']
    return MongoClient(mongo_uri)

def get_database():
    client = get_mongo_client()
    db_name = current_app.config.get('MONGO_DB_NAME')
    return client[db_name]

