from app.utils.db import get_db
from bson.objectid import ObjectId

def create_category(data):
    db = get_db()
    result = db.categories.insert_one(data)
    return {"id": str(result.inserted_id)}

def get_all_categories():
    db = get_db()
    categories = list(db.categories.find())
    for cat in categories:
        cat["_id"] = str(cat["_id"])
    return {"categories": categories}

def get_enabled_categories():
    db = get_db()
    categories = list(db.categories.find({"status": True}))
    for cat in categories:
        cat["_id"] = str(cat["_id"])
    return {"categories": categories}

def update_category(id, data):
    db = get_db()
    db.categories.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"message": "Category updated successfully."}

def delete_category(id):
    db = get_db()
    db.categories.delete_one({"_id": ObjectId(id)})
    return {"message": "Category deleted successfully."}
