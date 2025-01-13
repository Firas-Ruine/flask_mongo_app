from bson import ObjectId
from app.utils.db import get_db

def create_subscriber(data):
    db = get_db()
    subscriber_id = db.subscribers.insert_one(data).inserted_id
    return {"id": str(subscriber_id)}

def get_all_subscribers(search_query=""):
    db = get_db()

    query = {}
    if search_query:
        query = {
            "$or": [
                {"first_name": {"$regex": search_query, "$options": "i"}},
                {"last_name": {"$regex": search_query, "$options": "i"}},
                {"email": {"$regex": search_query, "$options": "i"}},
                {"address": {"$regex": search_query, "$options": "i"}},
            ]
        }

    subscribers = list(db.subscribers.find(query))
    for sub in subscribers:
        sub["_id"] = str(sub["_id"])  # Convert ObjectId to string

    return {"subscribers": subscribers}

def update_subscriber(subscriber_id, data):
    db = get_db()
    result = db.subscribers.update_one(
        {"_id": ObjectId(subscriber_id)}, {"$set": data}
    )
    return {"modified_count": result.modified_count}

def delete_subscriber(subscriber_id):
    db = get_db()
    result = db.subscribers.delete_one({"_id": ObjectId(subscriber_id)})
    return {"deleted_count": result.deleted_count}
