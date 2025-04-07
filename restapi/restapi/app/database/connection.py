from pymongo import MongoClient
from flask import current_app

def get_db_connection():
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['MONGO_DB']]
    return db