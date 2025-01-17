from app.utils.db import get_db
from bson.objectid import ObjectId

from app.utils.db import get_db
from bson.objectid import ObjectId

def get_all_loans(search=""):
    db = get_db()

    pipeline = [
        # Convert subscriber_id and document_id to ObjectId
        {
            "$addFields": {
                "subscriber_id": {"$toObjectId": "$subscriber_id"},
                "document_id": {"$toObjectId": "$document_id"},
            }
        },
        # Lookup subscriber details
        {
            "$lookup": {
                "from": "subscribers",
                "localField": "subscriber_id",
                "foreignField": "_id",
                "as": "subscriber",
            }
        },
        # Lookup document details
        {
            "$lookup": {
                "from": "documents",
                "localField": "document_id",
                "foreignField": "_id",
                "as": "document",
            }
        },
        # Unwind the arrays to get single subscriber and document
        {"$unwind": "$subscriber"},
        {"$unwind": "$document"},
        # Optional search filtering
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
        # Select fields to project
        {
            "$project": {
                "_id": {"$toString": "$_id"},  # Convert ObjectId to string
                "subscriber_name": {
                    "$concat": ["$subscriber.first_name", " ", "$subscriber.last_name"]
                },
                "document_title": "$document.title",
                "status": 1,
                # Include dates and format them as strings
                "loan_date": {
                    "$dateToString": {"format": "%Y-%m-%d %H:%M:%S", "date": "$loan_date"}
                },
                "due_date": {
                    "$dateToString": {"format": "%Y-%m-%d %H:%M:%S", "date": "$due_date"}
                },
                "return_date": {
                    "$cond": {
                        "if": {"$not": ["$return_date"]},  # Check if return_date is null
                        "then": "N/A",  # Default value if null
                        "else": {
                            "$dateToString": {
                                "format": "%Y-%m-%d %H:%M:%S",
                                "date": "$return_date",
                            }
                        },
                    }
                },
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
