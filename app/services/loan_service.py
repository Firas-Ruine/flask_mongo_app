from app.utils.db import get_db
from bson.objectid import ObjectId

def get_all_loans(search=""):
    db = get_db()

    pipeline = [
        {
            "$addFields": {
                "subscriber_id": {"$toObjectId": "$subscriber_id"},
                "document_id": {"$toObjectId": "$document_id"},
            }
        },
        {
            "$lookup": {
                "from": "subscribers",
                "localField": "subscriber_id",
                "foreignField": "_id",
                "as": "subscriber",
            }
        },
        {
            "$lookup": {
                "from": "documents",
                "localField": "document_id",
                "foreignField": "_id",
                "as": "document",
            }
        },
        {"$unwind": "$subscriber"},
        {"$unwind": "$document"},
        {
            "$match": {
                "$or": [
                    {"subscriber.first_name": {"$regex": search, "$options": "i"}},
                    {"subscriber.last_name": {"$regex": search, "$options": "i"}},
                    {"document.title": {"$regex": search, "$options": "i"}},
                    {"status": {"$regex": search, "$options": "i"}},
                ]
            }
        },
        {
            "$project": {
                "_id": {"$toString": "$_id"},  # Convert ObjectId to string
                "subscriber_name": {
                    "$concat": ["$subscriber.first_name", " ", "$subscriber.last_name"]
                },
                "document_title": "$document.title",
                "status": 1,
            }
        },
    ]

    loans = list(db.loans.aggregate(pipeline))
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
