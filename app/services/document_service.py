from app.utils.db import get_db
from bson.objectid import ObjectId

def get_all_documents(search_query=""):
    db = get_db()

    # Build query for search
    query = {}
    if search_query:
        query = {
            "$or": [
                {"title": {"$regex": search_query, "$options": "i"}},
                {"author": {"$regex": search_query, "$options": "i"}},
                {"category": {"$regex": search_query, "$options": "i"}},
            ]
        }

    documents = list(db.documents.find(query))
    for doc in documents:
        doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return {"documents": documents}

def create_document(data):
    db = get_db()

    # Insert document into the collection
    result = db.documents.insert_one(data)
    return {"id": str(result.inserted_id)}

def update_document(id, data):
    db = get_db()

    # Update the document
    db.documents.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"message": "Document updated successfully."}

def delete_document(id):
    db = get_db()

    # Delete the document
    db.documents.delete_one({"_id": ObjectId(id)})
    return {"message": "Document deleted successfully."}
