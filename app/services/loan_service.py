from app.utils.db import get_db
from bson.objectid import ObjectId

def get_all_loans(search_query=""):
    db = get_db()

    # Build query for search
    query = {}
    if search_query:
        query = {
            "$or": [
                {"subscriber_name": {"$regex": search_query, "$options": "i"}},
                {"document_title": {"$regex": search_query, "$options": "i"}},
                {"status": {"$regex": search_query, "$options": "i"}},
            ]
        }

    loans = list(db.loans.find(query))
    for loan in loans:
        loan["_id"] = str(loan["_id"])  # Convert ObjectId to string
    return {"loans": loans}

def create_loan(data):
    db = get_db()

    # Insert loan into the collection
    result = db.loans.insert_one(data)
    return {"id": str(result.inserted_id)}

def update_loan(id, data):
    db = get_db()

    # Update the loan
    db.loans.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"message": "Loan updated successfully."}

def delete_loan(id):
    db = get_db()

    # Delete the loan
    db.loans.delete_one({"_id": ObjectId(id)})
    return {"message": "Loan deleted successfully."}
