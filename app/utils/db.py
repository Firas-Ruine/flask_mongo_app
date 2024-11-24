from pymongo import MongoClient
import os

client = None

def get_db():
    """
    Get a MongoDB database instance.
    """
    global client
    if not client:
        client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    db_name = os.getenv("DB_NAME", "flask_db")
    return client[db_name]

def reconnect_db():
    """
    Reconnect to the MongoDB instance.
    """
    global client
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
