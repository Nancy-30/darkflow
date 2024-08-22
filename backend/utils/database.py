from pymongo import MongoClient
from flask import current_app

def get_mongo_client():
    """Create and return a MongoDB client."""
    mongo_uri = current_app.config['MONGO_URI']
    return MongoClient(mongo_uri)

def get_database():
    """Get the database instance."""
    client = get_mongo_client()
    db_name = current_app.config.get('MONGO_DB_NAME', 'user_data')
    return client[db_name]

def get_collection(collection_name='datasets'):
    """Get a collection from the database."""
    db = get_database()
    return db[collection_name]

def insert_document(collection_name, document):
    """Insert a document into the specified MongoDB collection."""
    collection = get_collection(collection_name)
    result = collection.insert_one(document)
    return result.inserted_id

def get_document(collection_name, query):
    """Get a document from the specified MongoDB collection."""
    collection = get_collection(collection_name)
    return collection.find_one(query)