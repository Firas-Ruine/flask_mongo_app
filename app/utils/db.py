from pymongo import MongoClient
import os

def get_db():
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    db = client[os.getenv("DB_NAME", "eshop")]
    return db
